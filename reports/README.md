# HTML Report Templates

This folder contains rendered sample HTML reports.
Source templates and shared CSS used by `scripts/generate_reports.py` are in `templates/reports/`.

## Leadership report pack

- `../templates/reports/weekly-status-email-template.html`
- `../templates/reports/portfolio-health-chat-template.html`
- `../templates/reports/executive-briefing-template.html`
- `../templates/reports/raid-digest-template.html`
- `../templates/reports/adr-log-template.html`
- `../templates/reports/daily-ops-pulse-template.html`
- `../templates/reports/dependency-critical-path-template.html`
- `../templates/reports/capacity-milestone-confidence-template.html`
- `../templates/reports/adoption-change-readout-template.html`
- `../templates/reports/executive-portfolio-radar-template.html`
- `../templates/reports/_theme.css`

These `*-template.html` files are Jinja templates and will show placeholders such as `{{ ... }}` and `{% ... %}` when opened directly.
Render them first with `python scripts/generate_reports.py`.

## Optional static examples

- `weekly-status-email-sample.html`
- `portfolio-health-chat-sample.html`
- `executive-briefing-sample.html`
- `raid-digest-sample.html`
- `adr-log-sample.html`
- `daily-ops-pulse-sample.html`
- `dependency-critical-path-review-sample.html`
- `capacity-milestone-confidence-sample.html`
- `adoption-change-readout-sample.html`
- `executive-portfolio-radar-sample.html`

## Notes

- Recommended workflow is Copilot prompt-first orchestration, then human review.
- CLI/script report generation remains an optional fallback path.
- Use `docs/report-generation.md` for setup and run instructions.
- Keep sensitive or confidential data out of externally shared reports.
- Maintain human-in-the-loop approval before sending.
