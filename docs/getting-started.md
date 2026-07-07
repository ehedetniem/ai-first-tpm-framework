# Getting Started in 30 Minutes

Use this guide to adopt the framework quickly.

## Step 0 - Choose your entry mode (VS Code + GitHub Copilot recommended)

This repo supports three ways to start:

1. VS Code + GitHub Copilot (recommended)
- Open the repo in VS Code.
- Use Copilot Chat to update JSON inputs in `data/`.
- Run `python scripts/generate_reports.py` and review `output/`.

2. Script-first (no agent required)
- Edit templates and data files manually.
- Run `./scripts/run_reports.ps1` (Windows) or `bash ./scripts/run_reports.sh` (macOS/Linux).

3. Starter agent pattern
- Use `agents/pulse-orchestrator/README.md` as a design pattern for your own orchestrator.

Important:
- There is no built-in `XPO` runtime agent in this repository.
- Start with scripts and templates first, then add orchestration only if needed.

## Step 1 - Read the operating model

- `lifecycle/program-lifecycle.md`
- `governance/hitl-governance.md`
- `automation/maturity-model.md`

## Step 2 - Stand up your first weekly cycle

Create a working folder in your environment and copy:
- `templates/weekly-status-template.md`
- `templates/risk-log-template.md`
- `templates/portfolio-rollup-template.md`
- `templates/adr-template.md`

## Step 3 - Define ownership

For your first program, assign:
- Program owner
- Decision approver(s)
- Risk owner(s)
- Weekly status publisher

## Step 4 - Run the cadence

Each week:
1. Update weekly status
2. Refresh risk log
3. Capture decisions in ADRs
4. Update portfolio rollup
5. Review AI-generated drafts using HITL checklist

## Step 5 - Measure progress

After 4 weeks, evaluate:
- Artifact consistency
- Decision traceability
- Reporting cycle time
- Time shifted to higher-value TPM work

## Optional Step 6 - Publish formatted updates

For email or chat-ready formatting, adapt the HTML samples in `reports/README.md`.

## Optional Step 7 - Automate report generation

Use `docs/report-generation.md` to generate HTML reports from JSON inputs.

Suggested Copilot prompts in VS Code:
- "Update `data/sample-executive-portfolio-radar.json` with this week's anonymized signals and keep schema intact."
- "Generate reports and refresh samples in `reports/` from `output/`."
- "Create a weekly status draft from `data/sample-weekly-status.json` and summarize key risks."

## Optional Step 8 - Formalize decision records

Use `docs/adr-instructions.md` to standardize ADR creation and approval.
