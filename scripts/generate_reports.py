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
    adr_data = load_json(root / args.adr_json)

    env = Environment(
        loader=FileSystemLoader(str(root / "reports")),
        autoescape=select_autoescape(["html", "xml"]),
    )
    theme_css = (root / "reports" / "_theme.css").read_text(encoding="utf-8")

    weekly_template = env.get_template("weekly-status-email-template.html.j2")
    portfolio_template = env.get_template("portfolio-health-chat-template.html.j2")
    executive_template = env.get_template("executive-briefing-template.html.j2")
    raid_template = env.get_template("raid-digest-template.html.j2")
    adr_template = env.get_template("adr-log-template.html.j2")

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
