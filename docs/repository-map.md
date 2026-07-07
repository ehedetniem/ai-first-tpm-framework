# Repository Map

## Top-level

- `README.md` - Overview and quickstart
- `CONTRIBUTING.md` - Contribution process
- `CODE_OF_CONDUCT.md` - Collaboration expectations
- `SECURITY.md` - Security reporting guidance
- `LICENSE` - MIT license

## Reporting stack

- `scripts/generate_reports.py` - Jinja-based HTML report generator
- `scripts/run_reports.ps1` - Windows runner for full report pack
- `scripts/run_reports.sh` - macOS/Linux runner for full report pack
- `templates/reports/` - Source report templates and shared CSS
- `data/` - JSON input data for each report
- `output/` - Generated HTML outputs
- `reports/` - Static sample HTML reports

## Framework content

- `lifecycle/` - Program phases and exit criteria
- `governance/` - Human-in-the-loop decision boundaries
- `templates/` - Reusable program artifacts
- `upskilling/` - PM-to-TPM adoption plan
- `automation/` - AI maturity progression
- `docs/` - Practical implementation and context

## Agent patterns

- `agents/pulse-orchestrator/` - Starter orchestration pattern included in this repo

Notes:
- There is no built-in `XPO` runtime agent in this repository.
- Teams can use templates and scripts directly, then add an orchestrator later if needed.
