"""
Pulse Orchestrator — JSON validation utility.

Validates all data/*.json files against the field schemas expected by
scripts/generate_reports.py and the Jinja report templates.

Usage:
    python agents/pulse-orchestrator/validate.py
    python agents/pulse-orchestrator/validate.py --data-dir data/
    python agents/pulse-orchestrator/validate.py --file data/sample-weekly-status.json
"""

import argparse
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Field schema definitions
# Each entry: (field_path, required, description)
# field_path uses dot notation for nested keys, e.g. "capacity.planned"
# ---------------------------------------------------------------------------
SCHEMAS: dict[str, list[tuple[str, bool, str]]] = {
    "sample-weekly-status.json": [
        ("program", True, "Program name"),
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("owner", True, "Program TPM owner"),
        ("health", True, "Green | Amber | Red"),
        ("highlights", True, "List of highlight strings"),
        ("risks", True, "List of risk objects"),
        ("decisionsNeeded", True, "List of decision strings"),
        ("next7Days", True, "List of next-action strings"),
    ],
    "sample-portfolio-health.json": [
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("green", True, "Count of green programs"),
        ("amber", True, "Count of amber programs"),
        ("red", True, "Count of red programs"),
        ("total", True, "Total program count"),
        ("rows", True, "List of program row objects"),
        ("leadershipAsks", True, "List of leadership ask strings"),
    ],
    "sample-executive-briefing.json": [
        ("title", True, "Report title"),
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("owner", True, "Report owner"),
        ("topWin", True, "Top win narrative"),
        ("topRisk", True, "Top risk narrative"),
        ("decisionNeeded", True, "Key decision ask"),
        ("programSummary", True, "List of program summary objects"),
        ("asks", True, "List of executive ask strings"),
    ],
    "sample-raid-digest.json": [
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("entries", True, "List of RAID entry objects"),
    ],
    "sample-adr-log.json": [
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("decisions", True, "List of decision objects"),
    ],
    "sample-daily-ops-pulse.json": [
        ("date", True, "ISO date YYYY-MM-DD"),
        ("owner", True, "Portfolio TPM owner"),
        ("blockersOpen", True, "Count of open blockers"),
        ("criticalDue24h", True, "Count critical items due within 24 h"),
        ("topBlockers", True, "List of top blocker objects"),
        ("todayActions", True, "List of action strings"),
    ],
    "sample-dependency-critical-path.json": [
        ("weekEnding", True, "ISO date YYYY-MM-DD"),
        ("owner", True, "Cross-org TPM owner"),
        ("items", True, "List of dependency objects"),
    ],
    "sample-capacity-milestone-confidence.json": [
        ("month", True, "Month label e.g. July 2026"),
        ("owner", True, "Program operations TPM"),
        ("capacity", True, "Capacity object with planned/available/delta"),
        ("milestones", True, "List of milestone objects"),
        ("asks", True, "List of ask strings"),
    ],
    "sample-adoption-change-readout.json": [
        ("month", True, "Month label e.g. July 2026"),
        ("owner", True, "Change management TPM owner"),
        ("kpis", True, "KPI metrics object"),
        ("wins", True, "List of win strings"),
        ("nextActions", True, "List of next action strings"),
    ],
    "sample-executive-portfolio-radar.json": [
        ("author", True, "Report author"),
        ("weekOf", True, "Week label"),
        ("heroStats", True, "Hero stats object"),
        ("scorecards", True, "List of scorecard objects"),
        ("program", True, "Program cluster object"),
    ],
}

SCHEMA_ALIASES = {
    "weekly-status.json": "sample-weekly-status.json",
    "portfolio-health.json": "sample-portfolio-health.json",
    "executive-briefing.json": "sample-executive-briefing.json",
    "raid-digest.json": "sample-raid-digest.json",
    "adr-log.json": "sample-adr-log.json",
    "daily-ops-pulse.json": "sample-daily-ops-pulse.json",
    "dependency-critical-path.json": "sample-dependency-critical-path.json",
    "capacity-milestone-confidence.json": "sample-capacity-milestone-confidence.json",
    "adoption-change-readout.json": "sample-adoption-change-readout.json",
    "executive-portfolio-radar.json": "sample-executive-portfolio-radar.json",
}

# RAID entry required sub-fields
RAID_ENTRY_FIELDS = ["type", "title", "severity", "owner", "nextAction"]
# ADR decision required sub-fields
ADR_DECISION_FIELDS = ["id", "title", "status", "owner"]
# Portfolio row required sub-fields
PORTFOLIO_ROW_FIELDS = ["program", "health"]


def _get_nested(data: dict, path: str):
    """Return the value at dot-separated path, or raise KeyError."""
    parts = path.split(".")
    current = data
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]
    return current


def validate_file(path: Path, schema: list[tuple[str, bool, str]]) -> list[str]:
    """
    Validate a single JSON file against its schema.
    Returns a list of error/warning strings (empty = valid).
    """
    errors: list[str] = []

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        return [f"JSON parse error: {exc}"]

    for field_path, required, description in schema:
        try:
            value = _get_nested(data, field_path)
            # Basic type checks for list fields
            if description.startswith("List") and not isinstance(value, list):
                truncated = repr(value)[:60]
                errors.append(
                    f"  WARN  {field_path}: expected a list, got {type(value).__name__} ({truncated})"
                )
            elif isinstance(value, list) and len(value) == 0:
                errors.append(f"  WARN  {field_path}: list is empty (add at least one entry)")
        except KeyError:
            if required:
                errors.append(f"  MISSING  {field_path}: {description}")
            else:
                errors.append(f"  OPTIONAL {field_path}: {description} (not present)")

    # Deep validation for specific files
    filename = SCHEMA_ALIASES.get(path.name, path.name)
    if filename == "sample-raid-digest.json":
        entries = data.get("entries", [])
        for i, entry in enumerate(entries):
            for field in RAID_ENTRY_FIELDS:
                if field not in entry:
                    errors.append(f"  MISSING  entries[{i}].{field}")
    elif filename == "sample-adr-log.json":
        decisions = data.get("decisions", [])
        for i, decision in enumerate(decisions):
            for field in ADR_DECISION_FIELDS:
                if field not in decision:
                    errors.append(f"  MISSING  decisions[{i}].{field}")
    elif filename == "sample-portfolio-health.json":
        rows = data.get("rows", [])
        for i, row in enumerate(rows):
            for field in PORTFOLIO_ROW_FIELDS:
                if field not in row:
                    errors.append(f"  MISSING  rows[{i}].{field}")

    return errors


def run_validation(data_dir: Path, single_file: Path | None = None) -> int:
    """
    Run validation. Returns 0 if all files pass, 1 if any errors found.
    """
    exit_code = 0

    if single_file is not None:
        schema_name = SCHEMA_ALIASES.get(single_file.name, single_file.name)
        files_to_check = [(single_file, SCHEMAS.get(schema_name))]
    else:
        files_to_check = []
        for filename, schema in SCHEMAS.items():
            files_to_check.append((data_dir / filename, schema))

    for filepath, schema in files_to_check:
        if schema is None:
            print(f"[SKIP] {filepath.name} — no schema defined")
            continue
        if not filepath.exists():
            print(f"[MISSING FILE] {filepath} — file not found")
            exit_code = 1
            continue

        errors = validate_file(filepath, schema)
        if errors:
            print(f"[FAIL] {filepath.name}")
            for err in errors:
                print(err)
            exit_code = 1
        else:
            print(f"[OK]   {filepath.name}")

    return exit_code


def main():
    parser = argparse.ArgumentParser(
        description="Validate TPM data JSON files against expected schemas."
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Directory containing data JSON files (default: data/)",
    )
    parser.add_argument(
        "--file",
        default=None,
        help="Validate a single specific JSON file instead of all files",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    data_dir = repo_root / args.data_dir
    single_file = Path(args.file) if args.file else None
    if single_file and not single_file.is_absolute():
        single_file = repo_root / single_file

    print("Pulse Orchestrator — JSON Validation")
    print("=" * 40)

    exit_code = run_validation(data_dir, single_file)

    print("=" * 40)
    if exit_code == 0:
        print("All files valid. Safe to run report generation.")
    else:
        print("Validation issues found. Fix before running report generation.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
