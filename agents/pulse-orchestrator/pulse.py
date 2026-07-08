#!/usr/bin/env python3
"""
Pulse Orchestrator CLI — the TPM agent command-line interface.

Run common TPM workflows directly from the command line.

Usage:
    python agents/pulse-orchestrator/pulse.py <command> [options]

Commands:
    status      Show weekly status summary for a program
    portfolio   Show portfolio health summary
    adr         Generate a new ADR draft from template
    risks       Show open risks and blockers
    validate    Validate all data JSON files
    reports     Run the full HTML report generation pipeline

Examples:
    python agents/pulse-orchestrator/pulse.py status
    python agents/pulse-orchestrator/pulse.py portfolio
    python agents/pulse-orchestrator/pulse.py adr "Adopt shared API contract standard"
    python agents/pulse-orchestrator/pulse.py risks
    python agents/pulse-orchestrator/pulse.py validate
    python agents/pulse-orchestrator/pulse.py reports
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

# Locate repo root relative to this file
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = REPO_ROOT / "data"
TEMPLATES_DIR = REPO_ROOT / "templates"
SCRIPTS_DIR = REPO_ROOT / "scripts"
ADR_DRAFTS_DIR = DATA_DIR / "adrs"
TODAY = date.today().isoformat()

PROGRAM_FILE_MAP = {
    "weekly": "weekly-status.json",
    "executive": "executive-briefing.json",
    "raid": "raid-digest.json",
    "adr": "adr-log.json",
    "daily_ops": "daily-ops-pulse.json",
    "dependency": "dependency-critical-path.json",
    "capacity": "capacity-milestone-confidence.json",
    "adoption": "adoption-change-readout.json",
}

PORTFOLIO_FILE_MAP = {
    "portfolio": "portfolio-health.json",
    "executive": "executive-briefing.json",
    "executive_portfolio_radar": "executive-portfolio-radar.json",
}

SAMPLE_FILE_MAP = {
    "weekly": "sample-weekly-status.json",
    "portfolio": "sample-portfolio-health.json",
    "executive": "sample-executive-briefing.json",
    "raid": "sample-raid-digest.json",
    "adr": "sample-adr-log.json",
    "daily_ops": "sample-daily-ops-pulse.json",
    "dependency": "sample-dependency-critical-path.json",
    "capacity": "sample-capacity-milestone-confidence.json",
    "adoption": "sample-adoption-change-readout.json",
    "executive_portfolio_radar": "sample-executive-portfolio-radar.json",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _health_badge(health: str) -> str:
    badges = {"green": "✅ Green", "amber": "🟡 Amber", "red": "🔴 Red"}
    return badges.get(health.lower(), health)


def _severity_badge(severity: str) -> str:
    badges = {"high": "🔴 High", "medium": "🟡 Medium", "low": "🟢 Low"}
    return badges.get(severity.lower(), severity)


def slugify(text: str) -> str:
    """Convert a decision title to a URL-safe slug for use in ADR file names.

    Parameters:
        text: Human-readable decision title, e.g. "Adopt shared API contract standard".

    Returns:
        Lowercase hyphen-separated slug truncated to 60 characters so that the
        resulting ADR file name stays within typical filesystem path-length limits
        (e.g. ``ADR-2026-07-07-adopt-shared-api-contract-standard.md``).
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60]


def repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def resolve_input_path(mode: str, logical_name: str, program_slug: str | None = None) -> Path:
    if mode == "program" and program_slug and logical_name in PROGRAM_FILE_MAP:
        candidate = DATA_DIR / "programs" / program_slug / PROGRAM_FILE_MAP[logical_name]
        if candidate.exists():
            return candidate
    if mode == "portfolio" and logical_name in PORTFOLIO_FILE_MAP:
        candidate = DATA_DIR / "portfolio" / PORTFOLIO_FILE_MAP[logical_name]
        if candidate.exists():
            return candidate
    return DATA_DIR / SAMPLE_FILE_MAP[logical_name]


def resolve_data_path(explicit_path: str | None, default_path: Path) -> Path:
    if not explicit_path:
        return default_path
    path = Path(explicit_path)
    if path.is_absolute():
        return path
    repo_candidate = REPO_ROOT / path
    if repo_candidate.exists():
        return repo_candidate
    data_candidate = DATA_DIR / path
    return data_candidate


def default_output_dir(mode: str, program_slug: str | None = None) -> str | None:
    if mode == "program" and program_slug:
        return f"output/{program_slug}/{TODAY}"
    if mode == "portfolio":
        return f"output/portfolio/{TODAY}"
    return None


# ---------------------------------------------------------------------------
# status command
# ---------------------------------------------------------------------------

def cmd_status(args):
    default_path = resolve_input_path("program", "weekly", args.program_slug)
    path = resolve_data_path(args.json, default_path)
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    data = load_json(path)
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  Weekly Status — {data.get('program', 'Unknown Program')}")
    print(f"  Week ending   : {data.get('weekEnding', 'TBD')}")
    print(f"  Owner         : {data.get('owner', 'TBD')}")
    print(f"  Health        : {_health_badge(data.get('health', 'TBD'))}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    highlights = data.get("highlights", [])
    if highlights:
        print("\nHighlights:")
        for h in highlights:
            print(f"  • {h}")

    risks = data.get("risks", [])
    if risks:
        print("\nRisks:")
        for r in risks:
            # The schema defines risks as objects; guard against plain strings
            # in case a user populates the field with a simple list of strings.
            risk_text = r.get("risk", r) if isinstance(r, dict) else r
            owner = r.get("owner", "TBD") if isinstance(r, dict) else ""
            print(f"  ⚠  {risk_text}" + (f" ({owner})" if owner else ""))

    decisions = data.get("decisionsNeeded", [])
    if decisions:
        print("\nDecisions Needed:")
        for d in decisions:
            print(f"  ❓ {d}")

    next_actions = data.get("next7Days", [])
    if next_actions:
        print("\nNext 7 Days:")
        for a in next_actions:
            print(f"  → {a}")

    print()


# ---------------------------------------------------------------------------
# portfolio command
# ---------------------------------------------------------------------------

def cmd_portfolio(args):
    default_path = resolve_input_path("portfolio", "portfolio")
    path = resolve_data_path(args.json, default_path)
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    data = load_json(path)
    total = data.get("total", 0)
    green = data.get("green", 0)
    amber = data.get("amber", 0)
    red = data.get("red", 0)

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  Portfolio Health — Week ending {data.get('weekEnding', 'TBD')}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  Total programs : {total}")
    print(f"  ✅ Green       : {green}")
    print(f"  🟡 Amber       : {amber}")
    print(f"  🔴 Red         : {red}")

    rows = data.get("rows", [])
    if rows:
        print()
        print(f"  {'Program':<20} {'Health':<10} {'Decision?':<12} Risk")
        print(f"  {'-------':<20} {'------':<10} {'---------':<12} ----")
        for row in rows:
            print(
                f"  {row.get('program',''):<20} "
                f"{row.get('health',''):<10} "
                f"{row.get('decisionPending',''):<12} "
                f"{row.get('risk','')}"
            )

    asks = data.get("leadershipAsks", [])
    if asks:
        print("\nLeadership Asks:")
        for ask in asks:
            print(f"  ❗ {ask}")

    print()


# ---------------------------------------------------------------------------
# adr command
# ---------------------------------------------------------------------------

def cmd_adr(args):
    title = args.title
    today = date.today().isoformat()
    slug = slugify(title)
    adr_id = f"ADR-{today}-{slug}"

    # Load template
    template_path = TEMPLATES_DIR / "adr-template.md"
    if not template_path.exists():
        print(f"Error: ADR template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    template_text = template_path.read_text(encoding="utf-8")

    # Fill in known fields; leave unknowns as TBD per governance rules
    draft = template_text.replace("ADR-XXXX", adr_id)
    draft = draft.replace("[Decision Title]", title)
    draft = draft.replace(
        "Proposed | Accepted | Superseded",
        "Proposed"
    )
    if args.context:
        draft = draft.replace("What problem are we solving?", args.context)
    if args.program:
        draft = draft.replace("- Related program:", f"- Related program: {args.program}")

    # Save draft
    ADR_DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = ADR_DRAFTS_DIR / f"{adr_id}.md"
    output_path.write_text(draft, encoding="utf-8")

    print()
    print(f"ADR draft created: {output_path.relative_to(REPO_ROOT)}")
    print()
    print("Next steps (governance):")
    print("  1. Open the draft and fill in Context, Decision, Options, Rationale.")
    print("  2. Mark unknown owners and dates as TBD.")
    print("  3. Get approval before changing status from Proposed to Accepted.")
    print("  4. Add to data/sample-adr-log.json once approved.")
    print()


# ---------------------------------------------------------------------------
# risks command
# ---------------------------------------------------------------------------

def cmd_risks(args):
    default_path = resolve_input_path("program", "raid", args.program_slug)
    path = resolve_data_path(args.json, default_path)
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(1)

    data = load_json(path)
    entries = data.get("entries", [])

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  RAID Digest — Week ending {data.get('weekEnding', 'TBD')}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    type_order = ["Risk", "Issue", "Dependency", "Assumption"]
    for entry_type in type_order:
        typed = [e for e in entries if e.get("type", "") == entry_type]
        if not typed:
            continue
        label = "Dependencies" if entry_type == "Dependency" else f"{entry_type}s"
        print(f"\n{label}:")
        for e in typed:
            severity = _severity_badge(e.get("severity", ""))
            owner = e.get("owner", "TBD")
            action = e.get("nextAction", "TBD")
            print(f"  {severity}  {e.get('title', '')}")
            print(f"    Owner: {owner} | Next: {action}")

    print()


# ---------------------------------------------------------------------------
# validate command
# ---------------------------------------------------------------------------

def cmd_validate(args):
    validate_script = Path(__file__).resolve().parent / "validate.py"
    if args.data_dir:
        cmd = [sys.executable, str(validate_script), "--data-dir", args.data_dir]
        result = subprocess.run(cmd)
        sys.exit(result.returncode)

    files_to_validate: list[Path] = []
    if args.mode == "program":
        if not args.program_slug:
            print("Error: --program-slug is required when --mode program", file=sys.stderr)
            sys.exit(1)
        logical_names = ["weekly", "raid", "adr", "daily_ops", "dependency", "capacity", "adoption"]
        for logical_name in logical_names:
            candidate = resolve_input_path("program", logical_name, args.program_slug)
            if candidate.exists() and candidate not in files_to_validate:
                files_to_validate.append(candidate)
    elif args.mode == "portfolio":
        logical_names = ["portfolio", "executive", "executive_portfolio_radar"]
        for logical_name in logical_names:
            candidate = resolve_input_path("portfolio", logical_name)
            if candidate.exists() and candidate not in files_to_validate:
                files_to_validate.append(candidate)
    else:
        cmd = [sys.executable, str(validate_script)]
        result = subprocess.run(cmd)
        sys.exit(result.returncode)

    if not files_to_validate:
        print("Error: no input files found for validation in the selected mode", file=sys.stderr)
        sys.exit(1)

    exit_code = 0
    for file_path in files_to_validate:
        cmd = [sys.executable, str(validate_script), "--file", repo_relative(file_path)]
        result = subprocess.run(cmd, cwd=str(REPO_ROOT))
        if result.returncode != 0:
            exit_code = result.returncode
    sys.exit(exit_code)


# ---------------------------------------------------------------------------
# reports command
# ---------------------------------------------------------------------------

def cmd_reports(args):
    generate_script = SCRIPTS_DIR / "generate_reports.py"
    if not generate_script.exists():
        print(f"Error: {generate_script} not found.", file=sys.stderr)
        sys.exit(1)

    print("Running report generation…")
    cmd = [sys.executable, str(generate_script)]

    mode = args.mode
    program_slug = args.program_slug
    resolved_output_dir = args.output_dir or default_output_dir(mode, program_slug)
    if resolved_output_dir:
        cmd += ["--output-dir", resolved_output_dir]

    input_map = {
        "--weekly-json": resolve_input_path(mode if mode == "program" else "all", "weekly", program_slug),
        "--portfolio-json": resolve_input_path(mode, "portfolio", program_slug),
        "--executive-json": resolve_input_path(mode, "executive", program_slug),
        "--raid-json": resolve_input_path(mode if mode == "program" else "all", "raid", program_slug),
        "--adr-json": resolve_input_path(mode if mode == "program" else "all", "adr", program_slug),
        "--daily-ops-json": resolve_input_path(mode if mode == "program" else "all", "daily_ops", program_slug),
        "--dependency-json": resolve_input_path(mode if mode == "program" else "all", "dependency", program_slug),
        "--capacity-json": resolve_input_path(mode if mode == "program" else "all", "capacity", program_slug),
        "--adoption-json": resolve_input_path(mode if mode == "program" else "all", "adoption", program_slug),
        "--executive-portfolio-radar-json": resolve_input_path(mode, "executive_portfolio_radar", program_slug),
    }
    for flag, path in input_map.items():
        cmd += [flag, repo_relative(path)]

    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if result.returncode == 0:
        print()
        final_output = resolved_output_dir or "output/"
        print(f"Reports generated. Review outputs in {final_output} before sharing.")
        print("Human approval required before external distribution.")
    sys.exit(result.returncode)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="pulse",
        description="Pulse Orchestrator — TPM agent CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True

    # status
    p_status = subparsers.add_parser("status", help="Show weekly status summary")
    p_status.add_argument(
        "--json",
        default=None,
        metavar="FILE",
        help="Weekly status JSON file path (program-scoped or explicit override)",
    )
    p_status.add_argument("--program-slug", default=None, help="Program slug for program-scoped status")
    p_status.set_defaults(func=cmd_status)

    # portfolio
    p_portfolio = subparsers.add_parser("portfolio", help="Show portfolio health summary")
    p_portfolio.add_argument(
        "--json",
        default=None,
        metavar="FILE",
        help="Portfolio health JSON file path (portfolio-scoped or explicit override)",
    )
    p_portfolio.set_defaults(func=cmd_portfolio)

    # adr
    p_adr = subparsers.add_parser("adr", help="Generate a new ADR draft")
    p_adr.add_argument("title", help="Decision title (quoted string)")
    p_adr.add_argument("--program", default="", help="Related program name")
    p_adr.add_argument("--context", default="", help="Problem context (one sentence)")
    p_adr.set_defaults(func=cmd_adr)

    # risks
    p_risks = subparsers.add_parser("risks", help="Show open risks and blockers")
    p_risks.add_argument(
        "--json",
        default=None,
        metavar="FILE",
        help="RAID digest JSON file path (program-scoped or explicit override)",
    )
    p_risks.add_argument("--program-slug", default=None, help="Program slug for program-scoped RAID")
    p_risks.set_defaults(func=cmd_risks)

    # validate
    p_validate = subparsers.add_parser(
        "validate", help="Validate data JSON files against expected schemas"
    )
    p_validate.add_argument(
        "--data-dir",
        default=None,
        help="Override data directory path",
    )
    p_validate.add_argument(
        "--mode",
        choices=["all", "program", "portfolio"],
        default="all",
        help="Validation mode (default: all)",
    )
    p_validate.add_argument(
        "--program-slug",
        default=None,
        help="Program slug for program-scoped validation",
    )
    p_validate.set_defaults(func=cmd_validate)

    # reports
    p_reports = subparsers.add_parser("reports", help="Run HTML report generation")
    p_reports.add_argument(
        "--output-dir",
        default=None,
        help="Override output directory",
    )
    p_reports.add_argument(
        "--mode",
        choices=["all", "program", "portfolio"],
        default="all",
        help="Report generation mode (default: all)",
    )
    p_reports.add_argument(
        "--program-slug",
        default=None,
        help="Program slug for program-scoped report generation",
    )
    p_reports.set_defaults(func=cmd_reports)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
