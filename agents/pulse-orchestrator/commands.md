# Pulse Orchestrator — Prompt Reference

Quick reference for the natural-language prompts TPMs can use with GitHub Copilot Chat.

## Quick prompts

| Prompt pattern | What it does |
|---|---|
| `Show me the current status for <program-slug>.` | Summarize weekly status for one program |
| `Show me the portfolio view for this week.` | Summarize cross-program health |
| `Review open risks for <program-slug>.` | Summarize and assess open risks and blockers |
| `Draft an ADR for this decision on <program-slug>.` | Create a new ADR draft |
| `Validate the program inputs for <program-slug>.` | Check program-scoped structured inputs |
| `Validate the portfolio inputs.` | Check portfolio-scoped structured inputs |
| `Generate the reports for <program-slug>.` | Run program-scoped report generation |
| `Generate the portfolio reports.` | Run portfolio aggregation report generation |

## Structured prompts

Paste these into GitHub Copilot Chat with this repo open. Each maps to a specific playbook in `agents/pulse-orchestrator/playbooks/`.

### Weekly status

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: weekly status update
Source: data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md
Program: <program-slug>

Run the weekly-status playbook from agents/pulse-orchestrator/playbooks/weekly-status.md.
```

### Portfolio rollup

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: portfolio rollup
Source: active program inputs and portfolio rollup files

Run the portfolio-rollup playbook from agents/pulse-orchestrator/playbooks/portfolio-rollup.md.
```

### ADR draft

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: ADR draft
Decision title: <decision title>
Program: <program-slug>
Context: <one sentence problem description>

Run the adr-draft playbook from agents/pulse-orchestrator/playbooks/adr-draft.md.
```

### Risk review

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: risk review
Source: data/programs/<program-slug>/raid-digest.json
Program: <program-slug>

Run the risk-review playbook from agents/pulse-orchestrator/playbooks/risk-review.md.
```

### Stakeholder update

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: stakeholder update
Audience: <executive | engineering | external>
Source: program-scoped or portfolio-scoped JSON inputs, depending on request
Program: <program-slug or "Portfolio">

Run the stakeholder-update playbook from agents/pulse-orchestrator/playbooks/stakeholder-update.md.
```

## Artifacts created

| Prompt | Artifacts created or updated |
|---|---|
| status | Copilot summary (read-only) |
| portfolio | Copilot summary (read-only) |
| risks | Copilot summary (read-only) |
| ADR draft | `data/adrs/ADR-YYYY-MM-DD-<slug>.md` |
| validate | Validation summary |
| reports | `output/<program-slug>/YYYY-MM-DD/*.html` or `output/portfolio/YYYY-MM-DD/*.html` |
| weekly status playbook | `data/programs/<program-slug>/weekly-status.json`, related outputs |
| portfolio playbook | `data/portfolio/*.json`, `output/portfolio/YYYY-MM-DD/*.html` |
| ADR playbook | `data/adrs/ADR-YYYY-MM-DD-<slug>.md`, program ADR log when approved |
| risk playbook | `data/programs/<program-slug>/raid-digest.json`, related outputs |
| stakeholder update | Draft text for human review |

## Human approval gates

The following outputs always require human review before sharing:

- Executive briefings
- Portfolio radar reports
- Stakeholder communications
- Any ADR moving from Proposed to Accepted
- Any artifact containing owner names, dates, or budget references

See `governance/hitl-governance.md` for the full policy.
