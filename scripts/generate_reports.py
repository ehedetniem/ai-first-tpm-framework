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
        description="Generate sample TPM HTML reports from JSON input."
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
        "--output-dir",
        default="output",
        help="Output directory for generated HTML files",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    weekly_data = load_json(root / args.weekly_json)
    portfolio_data = load_json(root / args.portfolio_json)

    env = Environment(
        loader=FileSystemLoader(str(root / "reports")),
        autoescape=select_autoescape(["html", "xml"]),
    )

    weekly_template = env.get_template("weekly-status-email-template.html.j2")
    portfolio_template = env.get_template("portfolio-health-chat-template.html.j2")

    weekly_html = weekly_template.render(data=weekly_data)
    portfolio_html = portfolio_template.render(data=portfolio_data)

    output_dir = root / args.output_dir
    write_text(output_dir / "weekly-status-email.html", weekly_html)
    write_text(output_dir / "portfolio-health-chat.html", portfolio_html)

    print("Generated:")
    print(f"- {output_dir / 'weekly-status-email.html'}")
    print(f"- {output_dir / 'portfolio-health-chat.html'}")


if __name__ == "__main__":
    main()
