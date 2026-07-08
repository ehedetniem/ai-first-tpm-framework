# Copilot Orchestrated Mode (No JSON Editing)

This is the recommended public-repo workflow for non-technical TPMs.

## Goal

Use one source input and one Copilot prompt to:

1. Update report input JSON files
2. Validate schema and required fields
3. Run report generation
4. Summarize key deltas for review

CLI commands remain available as optional fallback when you want to run steps manually.

## Option A (recommended) - Transcript-first orchestration

If you have a meeting transcript (or WorkIQ-exported notes), you do not need to fill intake manually.

1. Save transcript or notes to:
   - `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md`
2. Paste this Copilot prompt:

```text
Act as Pulse Orchestrator for this repo.

Primary source input:
- data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md

Scope:
- Update artifacts for <program-slug> only.

Tasks:
1) Extract decisions, risks, blockers, dependencies, owners, and next actions.
2) Draft one ADR from the most significant decision and save it using templates/adr-template.md conventions.
3) Update these files while preserving schema:
   - data/sample-weekly-status.json
   - data/sample-portfolio-health.json
   - data/sample-executive-portfolio-radar.json
4) Validate updated JSON files against template usage in templates/reports/.
5) If command execution is enabled, run `python agents/pulse-orchestrator/pulse.py reports`; otherwise tell me to run it manually.
6) Return a short summary:
   - top 3 wins
   - top 3 risks/blockers
   - decision asks
   - ADR file created
   - files updated

Constraints:
- Do not invent owners or dates when missing; mark as TBD.
- Keep language executive and concise.
```

## Option B - Intake file orchestration

Use this when transcript quality is poor or unavailable.

## Step 1 - Fill intake

Copy or edit:

- `data/intake/weekly-intake-template.md`

Save as:

- `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md`

## Step 2 - Run orchestration prompt in Copilot Chat

Paste this prompt (replace `YYYY-MM-DD` first):

```text
Act as Pulse Orchestrator for this repo.

Use `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md` as the source input.

Scope:
- Update artifacts for <program-slug> only.

Tasks:
1) Update these files with this week's signals while preserving schema:
   - data/sample-weekly-status.json
   - data/sample-portfolio-health.json
   - data/sample-executive-portfolio-radar.json
2) Validate all updated JSON files against template usage in templates/reports/.
3) If command execution is enabled, run `python agents/pulse-orchestrator/pulse.py reports`; otherwise tell me to run it manually.
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

Optional manual fallback commands:

- `python agents/pulse-orchestrator/pulse.py validate`
- `python agents/pulse-orchestrator/pulse.py reports`

Recommended for per-program traceability:

- Copy outputs to a dated, program-specific archive path after each run, for example:
   - `reports/archive/<program-slug>/2026-07-07/executive-portfolio-radar.html`

## Notes

- This mode provides orchestration behavior through Copilot prompts.
- Internal environments may use an ADO->YAML bridge upstream; public repo remains JSON-to-HTML rendering.
- Keep human approval before external sharing.
