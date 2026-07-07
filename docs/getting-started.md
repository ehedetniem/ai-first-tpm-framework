# Getting Started for Non-Technical PMs (Copilot-First)

This guide is the easiest way to use this framework if you are not a developer.

## What is true today

- You should use VS Code with GitHub Copilot Chat.
- You do not need a built-in XPO runtime agent to run this framework.
- The current workflow is automation-first, with human review before publish.
- Non-technical TPMs should use the orchestrated intake method instead of editing JSON directly.

## Source of truth (important)

Your understanding is correct:

- In your full TPM framework, YAML is the operational source of truth used by downstream artifacts.
- Those YAML files are typically updated by an external bridge/automation from your work tracking system.
- This public repo does not include that private bridge implementation.

What this public repo does include:

- Report rendering from JSON in `data/` to HTML in `output/`.
- A Copilot-first workflow to update JSON safely for weekly publishing.

Practical model:

1. Upstream system updates (external bridge) refresh YAML in your internal environment
2. YAML signal is mapped/exported to JSON report inputs
3. This repo renders leadership-ready HTML reports

For a concrete field mapping contract, see `docs/report-generation.md` under "Bridge handoff contract example (YAML -> JSON)".

## Step 1 - Open the repo in VS Code

1. Open VS Code.
2. Open this repository folder.
3. Open Copilot Chat.

## Step 2 - Use one intake file (no JSON editing)

1. Open `data/intake/weekly-intake-template.md`.
2. Save a copy as `data/intake/weekly-intake-YYYY-MM-DD.md`.
3. Fill the sections in plain language.

## Step 3 - Ask Copilot to orchestrate updates

Use the runbook and prompt in:

- `docs/copilot-orchestrated-mode.md`

Copilot will:

1. Update required JSON files
2. Validate schema/fields
3. Run report generation
4. Return a short review summary

## Step 4 - Ask Copilot to generate reports

Ask Copilot to run one of these:

- `python scripts/generate_reports.py`
- `./scripts/run_reports.ps1` (Windows)

Generated files appear in `output/`.

## Step 5 - Review only what matters

Do not rewrite full reports manually. Review these items:

- Risks, blockers, and decision asks
- Any changed KPI numbers
- Leadership narrative for accuracy and tone

After review, publish to your normal channels.

## Step 6 - Reuse this weekly rhythm

Each week, repeat:

1. Fill one intake file
2. Run one orchestration prompt
3. Review deltas
4. Publish

## Where to go next

- Report generation details: `docs/report-generation.md`
- Orchestrated no-code mode: `docs/copilot-orchestrated-mode.md`
- Report samples: `reports/README.md`
- Decision records (ADR): `docs/adr-instructions.md`
- Starter orchestration pattern: `agents/pulse-orchestrator/README.md`
