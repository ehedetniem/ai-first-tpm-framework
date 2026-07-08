# Report Generation Guide

This repo includes a Python generator for a leadership-ready HTML reporting pack.

## Source-of-truth note

- In many TPM implementations, YAML is the operational source of truth and is refreshed by an external bridge from a work tracking system.
- This public repo focuses on the rendering layer: JSON inputs in `data/` to HTML outputs in `output/`.
- If your team uses YAML upstream, add a mapping/export step that writes the report JSON files before running the generator.

## Public data lanes

Use two separate data lanes:

1. Program-scoped inputs
- `data/programs/<program-slug>/...`

2. Portfolio-scoped inputs
- `data/portfolio/...`

Use separate output directories as well:

- `output/<program-slug>/YYYY-MM-DD/`
- `output/portfolio/YYYY-MM-DD/`

## Bridge handoff contract example (YAML -> JSON)

Use this as a lightweight contract between the bridge owner and report owner.

| YAML source path (example) | JSON target file | JSON field | Notes |
|---|---|---|---|
| `program.identity.name` | `data/sample-executive-portfolio-radar.json` | `program.name` | Preserve anonymization policy if required |
| `program.identity.owner` | `data/sample-executive-portfolio-radar.json` | `program.owner` | Use display name or alias agreed by leadership |
| `program.health.status` | `data/sample-executive-portfolio-radar.json` | `program.status` | Expected values align to visual badge classes |
| `program.health.last_updated` | `data/sample-executive-portfolio-radar.json` | `program.updated` | ISO date preferred (`YYYY-MM-DD`) |
| `program.milestones.completed` + `program.milestones.total` | `data/sample-executive-portfolio-radar.json` | `heroStats.milestonesDone` | Format as `X/Y` |
| `program.risks.high_count` | `data/sample-executive-portfolio-radar.json` | `heroStats.highRisks` | Numeric string accepted |
| `program.dependencies.blockers[]` | `data/sample-executive-portfolio-radar.json` | `program.risks[]` where `type=dep` | Flatten with owner + summary |
| `program.workstreams[]` | `data/sample-executive-portfolio-radar.json` | `program.workstreams[]` | Map status to `g/a/r/p` for color dot |
| `program.actions.next[]` | `data/sample-executive-portfolio-radar.json` | `program.actions[]` | Keep action text short and decision-oriented |

## Bridge output validation checklist

Before report generation, validate these checks:

1. Required files exist in `data/` for the reports you are generating.
2. JSON parses successfully (no trailing commas or malformed quotes).
3. Every array field expected by template loops is present (can be empty, but must exist).
4. Status values match expected display classes (for example `bdg-g`, `bdg-a`, `bdg-r`).
5. Date fields use one standard format across all files.
6. Any anonymized fields are consistently masked across all outputs.

Suggested Copilot prompt for validation:

- "Validate all report JSON files in `data/` against template usage in `templates/reports/`. List missing fields and fix them without changing schema intent."

## What it generates

- `output/weekly-status-email.html`
- `output/portfolio-health-chat.html`
- `output/executive-briefing.html`
- `output/raid-digest.html`
- `output/adr-log.html`
- `output/daily-ops-pulse.html`
- `output/dependency-critical-path-review.html`
- `output/capacity-milestone-confidence.html`
- `output/adoption-change-readout.html`
- `output/executive-portfolio-radar.html`

## Inputs

- `data/sample-weekly-status.json`
- `data/sample-portfolio-health.json`
- `data/sample-executive-briefing.json`
- `data/sample-raid-digest.json`
- `data/sample-adr-log.json`
- `data/sample-daily-ops-pulse.json`
- `data/sample-dependency-critical-path.json`
- `data/sample-capacity-milestone-confidence.json`
- `data/sample-adoption-change-readout.json`
- `data/sample-executive-portfolio-radar.json`

## Templates

- `templates/reports/weekly-status-email-template.html`
- `templates/reports/portfolio-health-chat-template.html`
- `templates/reports/executive-briefing-template.html`
- `templates/reports/raid-digest-template.html`
- `templates/reports/adr-log-template.html`
- `templates/reports/daily-ops-pulse-template.html`
- `templates/reports/dependency-critical-path-template.html`
- `templates/reports/capacity-milestone-confidence-template.html`
- `templates/reports/adoption-change-readout-template.html`
- `templates/reports/executive-portfolio-radar-template.html`
- `templates/reports/_theme.css`

## Copilot-first execution

Ask Copilot to:

1. Validate the structured inputs for the program or portfolio run
2. Run the repo's report generation workflow
3. Tell you where outputs were written
4. Summarize any missing fields, TBD owners, or validation gaps

Suggested Copilot prompt:

- "Validate the current inputs, run report generation, and tell me which output files were created."

## Implementation note

This repo includes scripts and runners behind the scenes, but TPMs should use Copilot Chat as the primary interaction layer.

## Workflow recommendation

1. Ask Copilot to update structured inputs from your weekly program data.
2. Ask Copilot to generate the HTML pack.
3. Review outputs with a human approver.
4. Publish to email/chat/executive review channels.
