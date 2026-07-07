# HTML Report Templates

This folder contains the leadership-themed report templates and supporting CSS used by `scripts/generate_reports.py`.

## Leadership report pack

- `weekly-status-email-template.html`
- `portfolio-health-chat-template.html`
- `executive-briefing-template.html`
- `raid-digest-template.html`
- `adr-log-template.html`
- `_theme.css`

These `*-template.html` files are Jinja templates and will show placeholders such as `{{ ... }}` and `{% ... %}` when opened directly.
Render them first with `python scripts/generate_reports.py`.

## Optional static examples

- `weekly-status-email-sample.html`
- `portfolio-health-chat-sample.html`
- `executive-briefing-sample.html`
- `raid-digest-sample.html`
- `adr-log-sample.html`

## Notes

- Use `docs/report-generation.md` for setup and run instructions.
- Keep sensitive or confidential data out of externally shared reports.
- Maintain human-in-the-loop approval before sending.
