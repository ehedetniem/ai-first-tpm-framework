- **Option B:** ask Copilot to draft the ADR directly from your decision notes.
# Playbook: ADR Draft Creation

Use this playbook to produce a structured Architecture Decision Record draft from a described decision.

## Prompt

Paste this into GitHub Copilot Chat:

```text
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: ADR draft
Program: <program-slug>
Decision title: <decision title>
Context: <one sentence problem description>

Requirements:
1. Draft the ADR using the repo's ADR template.
2. Save it to `data/adrs/ADR-<YYYY-MM-DD>-<slug>.md`.
3. Use these defaults:
   - Status: Proposed
   - Context: from the provided context
   - Decision: TBD (leave for human review)
   - Options considered: from provided evidence, or TBD
   - Rationale: TBD
   - Consequences: TBD
   - Approvals: TBD
4. Return a summary with:
   - ADR file path created
   - Missing fields that need human input
   - Governance reminder: human approval required before status changes to Accepted

Constraints:
- Do not fabricate decision rationale or options.
- Do not set status to Accepted; always start at Proposed.
- Do not add to a program ADR log until the ADR is approved.
- Mark all unknown fields as TBD.
```

## Expected outputs

| Output | Location |
|---|---|
| ADR draft (Markdown) | `data/adrs/ADR-YYYY-MM-DD-<slug>.md` |

## After the draft is created

1. Review the draft with stakeholders.
2. Once approved, update status to `Accepted` and add to `data/programs/<program-slug>/adr-log.json`.
3. Ask Copilot to regenerate the ADR-related report outputs for `<program-slug>`.

## Human approval checklist

Before changing an ADR from Proposed to Accepted:

- [ ] Context accurately describes the problem
- [ ] At least two options were considered
- [ ] Rationale explains why the chosen option was selected
- [ ] Consequences (positive and negative) are documented
- [ ] Approver name and date are recorded
- [ ] Related program is correctly identified
