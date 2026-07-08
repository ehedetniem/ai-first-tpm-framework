# Playbook: Risk Review

Use this playbook to review, prioritize, and update open risks and blockers.

Paste this prompt into GitHub Copilot Chat with the repo open, replacing the bracketed values.

---

## Prompt

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for behavior rules.

Task: risk review
Program: <program-slug or "Portfolio">
Week ending: <YYYY-MM-DD>

Source inputs:
- RAID digest: data/programs/<program-slug>/raid-digest.json
- Meeting transcript (optional): data/intake/<program-slug>/meeting-transcript-<YYYY-MM-DD>.md

Steps:
1. Read current RAID digest and (if provided) the meeting transcript.

2. For each Risk and Issue entry:
   - Confirm it is still open or mark for removal if resolved.
   - Verify it has a real owner (not TBD if avoidable).
   - Confirm the next action is specific and due-dated.
   - Raise severity to High if any of these are true:
     * Blocks a milestone in the next 14 days
     * Has no owner
     * No next action in over 7 days

3. If the transcript contains new risks or issues not in the RAID digest, add them.

4. Update data/programs/<program-slug>/raid-digest.json preserving this exact schema:
   {
     "weekEnding": "YYYY-MM-DD",
     "entries": [
       {
         "type": "Risk|Assumption|Issue|Dependency",
         "title": "string",
         "severity": "High|Medium|Low",
         "owner": "string",
         "nextAction": "string"
       }
     ]
   }

5. Validate the updated RAID inputs for `<program-slug>`.

6. Generate the updated RAID digest HTML for `<program-slug>`.

7. Return a Pulse Summary with:
   - Count of High / Medium / Low items
   - Any items with no owner (governance flag)
   - Items requiring escalation
   - Recommended decision asks

Constraints:
- Do not remove risks without confirming they are resolved.
- Do not fabricate owners; mark as TBD if unknown.
- Flag any High risk with no owner for immediate escalation.
```

---

## Quick Copilot risk summary

Ask Copilot:

```text
Review the current open risks for <program-slug> and summarize the escalation items.
```

---

## Expected outputs

| Output | Location |
|---|---|
| Updated RAID JSON | `data/programs/<program-slug>/raid-digest.json` |
| HTML RAID digest | `output/<program-slug>/YYYY-MM-DD/raid-digest.html` |
| Summary | Copilot Chat response |

## Human approval checklist

Before sharing a risk review output:

- [ ] Every High risk has a named owner
- [ ] Every High risk has a specific next action with a due date
- [ ] Escalations are flagged to the right person
- [ ] No fabricated facts introduced
- [ ] Resolved items confirmed before removal
