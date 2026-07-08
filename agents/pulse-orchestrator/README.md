# Pulse Orchestrator

Pulse Orchestrator is the in-repo TPM agent for the AI-First TPM Framework. It runs today — no external service required.

## What it does

- Routes TPM requests (status update, portfolio rollup, ADR drafting, risk review, stakeholder update) to the right artifact flow
- Extracts signals from meeting transcripts and intake files
- Updates program-scoped or portfolio-scoped JSON data files while preserving schema
- Validates JSON before report generation
- Generates first-draft artifacts with human-in-the-loop governance enforced

It supports two public operating lanes:

1. Per-program execution
2. Portfolio aggregation

## How to use it
### GitHub Copilot Chat (primary)

1. Open this repo in VS Code with GitHub Copilot Chat.
2. Start your prompt with:
   ```
   Act as Pulse Orchestrator for this repo.
   See agents/pulse-orchestrator/system-prompt.md for behavior rules.
   ```
3. Choose a task playbook from `agents/pulse-orchestrator/playbooks/` and paste the prompt.

Typical TPM asks:
- "Show me the current status for my-program in plain English."
- "Validate the program inputs for my-program and generate the reports."
- "Draft an ADR for this decision on my-program."
- "Generate the portfolio reports for this week."

### Implementation note

Pulse also includes implementation utilities behind the scenes, but TPMs do not need to operate them directly in the intended public workflow.

## Files in this package

| File | Purpose |
|---|---|
| `system-prompt.md` | Agent behavior spec — use as Copilot system prompt |
| `commands.md` | Prompt and workflow reference card |
| `pulse.py` | Orchestration engine entrypoint |
| `validate.py` | Validation utility used by the orchestration flow |
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
