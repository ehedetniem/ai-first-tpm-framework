# Start in 10 Minutes (Non-AI TPM Quickstart)

If you are new to AI tools, this page gets you from zero to first report in about 10 minutes.

## What you will do

1. Open the repo in VS Code
2. Add one intake file for one program
3. Run validation
4. Generate reports
5. Review and publish with human approval

## 10-minute checklist

- [ ] Open this repo in VS Code
- [ ] Open Copilot Chat
- [ ] Add one intake file under `data/intake/<program-slug>/`
- [ ] Run `python agents/pulse-orchestrator/pulse.py validate`
- [ ] Run `python agents/pulse-orchestrator/pulse.py reports`
- [ ] Open `output/*.html` and review risks, decision asks, and KPI deltas
- [ ] Publish only after human review

## Step-by-step

### 1) Open the repo

1. Open VS Code
2. Open folder: `ai-first-tpm-framework`
3. Open Copilot Chat

### 2) Add intake (pick one)

**Option A (recommended): transcript-first**

- Create: `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md`

**Option B: weekly intake**

- Copy `data/intake/weekly-intake-template.md`
- Save as `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md`

Keep one intake stream per program for traceability.

### 3) Run validate

From repo root:

```bash
python agents/pulse-orchestrator/pulse.py validate
```

If validation fails, fix missing required fields in `data/*.json` and run again.

### 4) Generate reports

```bash
python agents/pulse-orchestrator/pulse.py reports
```

Generated files are in `output/`.

### 5) Review and publish

Review only high-signal deltas:

- Risks/blockers
- Decision asks (owner + due date, or `TBD`)
- KPI changes

Then publish with human approval.

## If you have 5 more minutes

- Run status summary:

```bash
python agents/pulse-orchestrator/pulse.py status
```

- Read the weekly SOP:
  - `docs/tpm-weekly-sop.md`

## Where to go next

- Full onboarding: `docs/getting-started.md`
- Weekly SOP: `docs/tpm-weekly-sop.md`
- Orchestration agent guide: `docs/orchestration-agent.md`
- Copilot no-code prompts: `docs/copilot-orchestrated-mode.md`
- Pulse CLI + playbooks: `agents/pulse-orchestrator/README.md`
