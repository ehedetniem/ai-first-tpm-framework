# Playbook: ADR Draft Creation

Use this playbook to produce a structured Architecture Decision Record draft from a described decision.

Two options:
- **Option A (Copilot Chat):** paste the prompt below into GitHub Copilot Chat.
- **Option B (CLI):** run `python agents/pulse-orchestrator/pulse.py adr "<title>"`.

---

## Option A — Copilot Chat Prompt

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for behavior rules.

Task: ADR draft creation
Decision title: <decision title>
Program: <program-slug>
Context: <one or two sentences describing the problem being solved>
Options considered: <list the options if known, otherwise leave TBD>

Steps:
1. Use templates/adr-template.md as the base structure.
2. Fill in:
   - ID: ADR-<today's date>-<slugified title>
   - Status: Proposed
   - Context: from the provided context
   - Decision: TBD (leave for human review)
   - Options considered: from provided list, or TBD
   - Rationale: TBD
   - Consequences: TBD
   - Approvals: TBD

3. Save the draft to:
   data/adrs/ADR-<YYYY-MM-DD>-<slug>.md

4. Return a Pulse Summary with:
   - ADR file path created
   - Missing fields that need human input
   - Governance flag: requires human approval before status changes to Accepted

Constraints:
- Do not fabricate decision rationale or options.
- Do not set status to Accepted; always start at Proposed.
- Do not add to data/sample-adr-log.json until the ADR is approved.
- Mark all unknown fields as TBD.
```

---

## Option B — CLI

```bash
# Basic
python agents/pulse-orchestrator/pulse.py adr "Decision title"

# With program and context
python agents/pulse-orchestrator/pulse.py adr "Decision title" \
  --program "My Program" \
  --context "One sentence describing the problem"
```

The draft is saved to `data/adrs/ADR-<YYYY-MM-DD>-<slug>.md`.

---

## Expected outputs

| Output | Location |
|---|---|
| ADR draft (Markdown) | `data/adrs/ADR-YYYY-MM-DD-<slug>.md` |

## After the draft is created

1. Open the draft and fill in Decision, Options, Rationale, and Consequences.
2. Share with relevant stakeholders for review.
3. Once approved, update status to `Accepted` and add to `data/sample-adr-log.json`.
4. Run `python agents/pulse-orchestrator/pulse.py reports` to regenerate the ADR log HTML.

## Human approval checklist

Before changing an ADR from Proposed to Accepted:

- [ ] Context accurately describes the problem
- [ ] At least two options were considered
- [ ] Rationale explains why the chosen option was selected
- [ ] Consequences (positive and negative) are documented
- [ ] Approver name and date are recorded
- [ ] Related program is correctly identified
