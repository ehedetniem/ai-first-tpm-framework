import argparse
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def prepare_adr_view_model(adr_data: dict):
    decisions = adr_data.get("decisions", [])
    summary = {
        "total": 0,
        "accepted": 0,
        "proposed": 0,
        "rejected": 0,
        "pending": 0,
        "completion": 0,
    }
    pending_items = []
    normalized = []

    for decision in decisions:
        status = str(decision.get("status", "")).strip().lower()
        status_class = "red"
        if status in {"accepted", "approved"}:
            summary["accepted"] += 1
            status_class = "green"
        elif status in {"proposed", "in review"}:
            summary["proposed"] += 1
            status_class = "amber"
        elif status in {"rejected", "superseded"}:
            summary["rejected"] += 1

        summary["total"] += 1
        approved_by = str(decision.get("approvedBy", "")).strip()
        approved_at = str(decision.get("approvedAt", "")).strip()
        if approved_by.lower() == "pending" or approved_at.lower() == "pending":
            summary["pending"] += 1
            pending_items.append(decision)

        normalized.append({**decision, "statusClass": status_class})

    if summary["total"] > 0:
        summary["completion"] = int(
            ((summary["total"] - summary["pending"]) * 100) / summary["total"]
        )

    return {
        **adr_data,
        "decisions": normalized,
        "pendingItems": pending_items,
        "summary": summary,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate TPM HTML reports from JSON inputs."
    )
    parser.add_argument(
        "--weekly-json",
        default="data/sample-weekly-status.json",
        help="Path to weekly status JSON input",
    )
    parser.add_argument(
        "--portfolio-json",
        default="data/sample-portfolio-health.json",
        help="Path to portfolio health JSON input",
    )
    parser.add_argument(
        "--executive-json",
        default="data/sample-executive-briefing.json",
        help="Path to executive briefing JSON input",
    )
    parser.add_argument(
        "--raid-json",
        default="data/sample-raid-digest.json",
        help="Path to RAID digest JSON input",
    )
    parser.add_argument(
        "--adr-json",
        default="data/sample-adr-log.json",
        help="Path to ADR log JSON input",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory for generated HTML files",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    weekly_data = load_json(root / args.weekly_json)
    portfolio_data = load_json(root / args.portfolio_json)
    executive_data = load_json(root / args.executive_json)
    raid_data = load_json(root / args.raid_json)
    adr_data = prepare_adr_view_model(load_json(root / args.adr_json))

    templates_dir = root / "templates" / "reports"
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    theme_css = (templates_dir / "_theme.css").read_text(encoding="utf-8")

    weekly_template = env.get_template("weekly-status-email-template.html")
    portfolio_template = env.get_template("portfolio-health-chat-template.html")
    executive_template = env.get_template("executive-briefing-template.html")
    raid_template = env.get_template("raid-digest-template.html")
    adr_template = env.get_template("adr-log-template.html")

    weekly_html = weekly_template.render(data=weekly_data, theme_css=theme_css)
    portfolio_html = portfolio_template.render(data=portfolio_data, theme_css=theme_css)
    executive_html = executive_template.render(data=executive_data, theme_css=theme_css)
    raid_html = raid_template.render(data=raid_data, theme_css=theme_css)
    adr_html = adr_template.render(data=adr_data, theme_css=theme_css)

    output_dir = root / args.output_dir
    write_text(output_dir / "weekly-status-email.html", weekly_html)
    write_text(output_dir / "portfolio-health-chat.html", portfolio_html)
    write_text(output_dir / "executive-briefing.html", executive_html)
    write_text(output_dir / "raid-digest.html", raid_html)
    write_text(output_dir / "adr-log.html", adr_html)

    print("Generated:")
    print(f"- {output_dir / 'weekly-status-email.html'}")
    print(f"- {output_dir / 'portfolio-health-chat.html'}")
    print(f"- {output_dir / 'executive-briefing.html'}")
    print(f"- {output_dir / 'raid-digest.html'}")
    print(f"- {output_dir / 'adr-log.html'}")


if __name__ == "__main__":
    main()
