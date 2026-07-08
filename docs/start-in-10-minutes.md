# AI-First Quickstart in 10 Minutes

If you are new to AI tools, this page gets you from zero to first report in about 10 minutes.

You do not need to learn a new system before you get value. Start with one program, one transcript or one intake note, and let the repo show you the workflow.

## What you will do

1. Open the repo in VS Code
2. Add one transcript or intake file for one program
3. Ask Copilot to validate and generate
4. Review and publish with human approval

This first run is meant to build confidence, not perfection.

## 10-minute checklist

- [ ] Open this repo in VS Code
- [ ] Open Copilot Chat
- [ ] Paste one transcript or one set of notes into Copilot for `<program-slug>`
- [ ] Ask Copilot to validate the program inputs
- [ ] Ask Copilot to generate the program reports
- [ ] Open `output/<program-slug>/YYYY-MM-DD/*.html` and review risks, decision asks, and KPI deltas
- [ ] Publish only after human review

## Step-by-step

### 1) Open the repo

1. Open VS Code
2. Open folder: `ai-first-tpm-framework`
3. Open Copilot Chat

### 2) Add intake (pick one)

**Option A (recommended): transcript-first**

- Ask Copilot to create `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md` from the transcript you paste into chat.

**Option B: weekly intake**

- Ask Copilot to create `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md` using `data/intake/weekly-intake-template.md` as the structure.

Keep one intake stream per program for traceability.

### 3) Ask Copilot to validate and generate

Paste this into Copilot Chat:

```text
Act as Pulse Orchestrator for this repo.

Program: <program-slug>
Source input:
- data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md

Tasks:
1. Validate the program-scoped inputs for <program-slug>.
2. Generate the program reports.
3. Tell me:
  - what files were updated
  - where the output was written
  - any missing owners, dates, or blockers marked TBD
```

Generated files should appear in `output/<program-slug>/YYYY-MM-DD/`.

### 4) Review and publish

Review only high-signal deltas:

- Risks/blockers
- Decision asks (owner + due date, or `TBD`)
- KPI changes

Then publish with human approval.

## If you have 5 more minutes

- Ask Copilot: "Show me the current status for <program-slug> in plain English."
- Read the weekly SOP:
  - `docs/tpm-weekly-sop.md`

## Backup path

If Copilot needs more structure, use the prompts and runbooks in:

- `docs/getting-started.md`
- `docs/orchestration-agent.md`

## Where to go next

- Full onboarding: `docs/getting-started.md`
- Weekly SOP: `docs/tpm-weekly-sop.md`
- Orchestration agent guide: `docs/orchestration-agent.md`
- Copilot no-code prompts: `docs/copilot-orchestrated-mode.md`
- Pulse Orchestrator prompts + playbooks: `agents/pulse-orchestrator/README.md`
