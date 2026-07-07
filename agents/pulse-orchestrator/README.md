# Pulse Orchestrator

Pulse Orchestrator is the in-repo TPM agent for the AI-First TPM Framework. It runs today — no external service required.

## What it does

- Routes TPM requests (status update, portfolio rollup, ADR drafting, risk review, stakeholder update) to the right artifact flow
- Extracts signals from meeting transcripts and intake files
- Updates JSON data files while preserving schema
- Validates JSON before report generation
- Generates first-draft artifacts with human-in-the-loop governance enforced

## How to use it

### Option A — CLI (fastest path)

```bash
# Weekly status summary
python agents/pulse-orchestrator/pulse.py status

# Portfolio health summary
python agents/pulse-orchestrator/pulse.py portfolio

# Open risks and blockers
python agents/pulse-orchestrator/pulse.py risks

# Generate a new ADR draft
python agents/pulse-orchestrator/pulse.py adr "Decision title" --program "My Program"

# Validate all data JSON files
python agents/pulse-orchestrator/pulse.py validate

# Generate all HTML reports
python agents/pulse-orchestrator/pulse.py reports
```

### Option B — GitHub Copilot Chat

1. Open this repo in VS Code with GitHub Copilot Chat.
2. Start your prompt with:
   ```
   Act as Pulse Orchestrator for this repo.
   See agents/pulse-orchestrator/system-prompt.md for behavior rules.
   ```
3. Choose a task playbook from `agents/pulse-orchestrator/playbooks/` and paste the prompt.

## Files in this package

| File | Purpose |
|---|---|
| `system-prompt.md` | Agent behavior spec — use as Copilot system prompt |
| `commands.md` | Full command reference card |
| `pulse.py` | CLI entrypoint |
| `validate.py` | JSON schema validation utility |
| `playbooks/weekly-status.md` | Prompt playbook: weekly status update |
| `playbooks/portfolio-rollup.md` | Prompt playbook: portfolio rollup |
| `playbooks/adr-draft.md` | Prompt playbook: ADR draft creation |
| `playbooks/risk-review.md` | Prompt playbook: risk review |
| `playbooks/stakeholder-update.md` | Prompt playbook: stakeholder update |

## Governance

All outputs are first drafts. Human approval is required before sharing any artifact externally.
See `governance/hitl-governance.md`.

## Full documentation

`docs/orchestration-agent.md`
