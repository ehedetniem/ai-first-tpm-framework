# Getting Started for Non-Technical PMs (Copilot-First)

This guide is the easiest way to use this framework if you are not a developer.

## What is true today

- You should use VS Code with GitHub Copilot Chat.
- You do not need a built-in XPO runtime agent to run this framework.
- The current workflow is automation-first, with human review before publish.
- You can start from sample data and replace only business content each week.

## Step 1 - Open the repo in VS Code

1. Open VS Code.
2. Open this repository folder.
3. Open Copilot Chat.

## Step 2 - Start from ready-made samples

Use these files as your starting point:

- `data/sample-weekly-status.json`
- `data/sample-portfolio-health.json`
- `data/sample-executive-portfolio-radar.json`

You can keep the same file structure and only change values.

## Step 3 - Ask Copilot to update your weekly signals

Paste one of these prompts into Copilot Chat:

- Update `data/sample-executive-portfolio-radar.json` with this week's anonymized portfolio signals. Keep the same schema.
- Update `data/sample-weekly-status.json` using these notes and keep field names unchanged.
- Validate all files in `data/` and fix missing required fields for report generation.

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

1. Paste fresh notes into Copilot
2. Update JSON signals
3. Generate reports
4. Review deltas
5. Publish

## Where to go next

- Report generation details: `docs/report-generation.md`
- Report samples: `reports/README.md`
- Decision records (ADR): `docs/adr-instructions.md`
- Starter orchestration pattern: `agents/pulse-orchestrator/README.md`
