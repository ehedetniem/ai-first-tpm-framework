# Copilot Orchestrated Mode (No JSON Editing)

This is the recommended public-repo workflow for non-technical TPMs.

## Goal

Support two language-first workflows:

1. Per-program orchestration
2. Portfolio aggregation orchestration

In both cases Copilot should:

1. Update structured inputs
2. Validate schema and required fields
3. Run report generation
4. Summarize key deltas for review

## Mode 1 - Per-program orchestration (recommended for TPMs)

### Option A - Transcript-first orchestration

If you have a meeting transcript (or WorkIQ-exported notes), you do not need to fill intake manually.

1. Ask Copilot to save transcript or notes to:
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
3) Update program-scoped structured inputs under `data/programs/<program-slug>/`.
4) Validate updated JSON files against template usage in templates/reports/.
5) Run the repo's report generation workflow for this program and write output to `output/<program-slug>/YYYY-MM-DD`.
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

### Option B - Intake file orchestration

Use this when transcript quality is poor or unavailable.

## Step 1 - Fill intake

Ask Copilot to use `data/intake/weekly-intake-template.md` as the structure and turn your notes into:

- `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md`

## Step 2 - Run orchestration prompt in Copilot Chat

Paste this prompt (replace `YYYY-MM-DD` first):

```text
Act as Pulse Orchestrator for this repo.

Use `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md` as the source input.

Scope:
- Update artifacts for <program-slug> only.

Tasks:
1) Update program-scoped structured inputs under `data/programs/<program-slug>/`.
2) Validate all updated JSON files against template usage in templates/reports/.
3) Run the repo's report generation workflow for this program and write output to `output/<program-slug>/YYYY-MM-DD`.
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

## Mode 2 - Portfolio aggregation orchestration

Use this when combining multiple programs into one leadership view.

Suggested Copilot prompt:

```text
Act as Pulse Orchestrator for this repo.

Scope:
- Portfolio aggregation across multiple programs.

Inputs:
- Use structured rollup inputs under data/portfolio/.
- If needed, read program-level outputs or notes from multiple program folders first.

Tasks:
1) Update portfolio-scoped files such as:
   - data/portfolio/portfolio-health.json
   - data/portfolio/executive-portfolio-radar.json
   - data/portfolio/executive-briefing.json
2) Validate updated files against template usage in templates/reports/.
3) Run the repo's report generation workflow for the portfolio and write output to `output/portfolio/YYYY-MM-DD`.
4) Return a short summary:
   - portfolio wins
   - portfolio risks/blockers
   - decision asks
   - files updated
```

## Review and publish

Review outputs in:

- `output/`

Optional distribution-ready samples in:

- `reports/`

Recommended for per-program traceability:

- Copy outputs to a dated, program-specific archive path after each run, for example:
   - `reports/archive/<program-slug>/2026-07-07/executive-portfolio-radar.html`

## Notes

- This mode provides orchestration behavior through Copilot prompts.
- Internal environments may use an ADO->YAML bridge upstream; public repo remains JSON-to-HTML rendering.
- Keep human approval before external sharing.
