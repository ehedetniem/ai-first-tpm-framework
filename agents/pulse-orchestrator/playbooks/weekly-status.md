# Playbook: Weekly Status Update

Use this playbook to produce a complete weekly status update from a transcript or intake file.

Paste this prompt into GitHub Copilot Chat with the repo open, replacing the bracketed values.

---

## Prompt

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for behavior rules.

Task: weekly status update
Program: <program-slug>
Week ending: <YYYY-MM-DD>

Source input (choose one):
- Transcript: data/intake/<program-slug>/meeting-transcript-<YYYY-MM-DD>.md
- Intake form: data/intake/<program-slug>/weekly-intake-<YYYY-MM-DD>.md

Steps:
1. Read the source input and extract:
   - Overall health (Green / Amber / Red)
   - Top 3 highlights / wins
   - Open risks with owners and mitigations
   - Decisions needed with owners and due dates
   - Next 7 days actions

2. Update data/sample-weekly-status.json preserving this exact schema:
   {
     "program": "string",
     "weekEnding": "YYYY-MM-DD",
     "owner": "string",
     "health": "Green|Amber|Red",
     "highlights": ["string"],
     "risks": [{"risk": "string", "owner": "string", "mitigation": "string"}],
     "decisionsNeeded": ["string"],
     "next7Days": ["string"]
   }

3. Update data/sample-portfolio-health.json to reflect the latest health for this program.

4. Run python agents/pulse-orchestrator/validate.py to check schema before generating reports.

5. Run python agents/pulse-orchestrator/pulse.py reports to regenerate HTML outputs.

6. Return a Pulse Summary following the format in the system prompt.

Constraints:
- Do not fabricate owners or dates; mark as TBD.
- Scope to this program only.
- Do not change template structure in templates/reports/.
- Flag all output for human review before sharing.
```

---

## Expected outputs

| Output | Location |
|---|---|
| Updated JSON | `data/sample-weekly-status.json` |
| Updated portfolio row | `data/sample-portfolio-health.json` |
| HTML report | `output/weekly-status-email.html` |
| HTML portfolio | `output/portfolio-health-chat.html` |
| Terminal summary | Copilot Chat response |

## Human approval checklist

Before publishing any output from this playbook:

- [ ] Health status is accurate and evidence-based
- [ ] Risks have real owners (not TBD unless genuinely unknown)
- [ ] Decision asks are actionable with due dates
- [ ] No confidential information included
- [ ] All claims traceable to source input
