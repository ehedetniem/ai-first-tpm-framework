# Copilot Orchestrated Mode (No JSON Editing)

This is the recommended public-repo workflow for non-technical TPMs.

## Goal

Use one intake file and one Copilot prompt to:

1. Update report input JSON files
2. Validate schema and required fields
3. Run report generation
4. Summarize key deltas for review

## Step 1 - Fill intake

Copy or edit:

- `data/intake/weekly-intake-template.md`

Save as:

- `data/intake/weekly-intake-YYYY-MM-DD.md`

## Step 2 - Run orchestration prompt in Copilot Chat

Paste this prompt (replace `YYYY-MM-DD` first):

```text
Act as Pulse Orchestrator for this repo.

Use `data/intake/weekly-intake-YYYY-MM-DD.md` as the source input.

Tasks:
1) Update these files with this week's signals while preserving schema:
   - data/sample-weekly-status.json
   - data/sample-portfolio-health.json
   - data/sample-executive-portfolio-radar.json
2) Validate all updated JSON files against template usage in templates/reports/.
3) Run report generation using scripts/run_reports.ps1.
4) Provide a short review summary:
   - top 3 wins
   - top 3 risks/blockers
   - decision asks
   - files updated

Constraints:
- Do not change report template structure.
- Do not invent owners or dates when missing; mark as TBD.
- Keep language executive and concise.
```

## Step 3 - Review and publish

Review outputs in:

- `output/`

Optional distribution-ready samples in:

- `reports/`

## Notes

- This mode provides orchestration behavior through Copilot prompts.
- Internal environments may use an ADO->YAML bridge upstream; public repo remains JSON-to-HTML rendering.
- Keep human approval before external sharing.
