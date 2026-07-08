# Playbook: Portfolio Rollup

Use this playbook to produce a cross-program portfolio health rollup.

Paste this prompt into GitHub Copilot Chat with the repo open, replacing the bracketed values.

---

## Prompt

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for behavior rules.

Task: portfolio rollup
Week ending: <YYYY-MM-DD>
Portfolio owner: <owner name>

Source inputs:
- Current program data: data/programs/<program-slug>/... across active programs
- Existing portfolio: data/portfolio/portfolio-health.json
- Radar: data/portfolio/executive-portfolio-radar.json

Steps:
1. Read all active program data and produce a portfolio-level view:
   - Count of Green / Amber / Red programs
   - One risk per Red or Amber program
   - Whether a decision is pending per program
   - Top 2 leadership asks for the portfolio

2. Update data/portfolio/portfolio-health.json preserving this exact schema:
   {
     "weekEnding": "YYYY-MM-DD",
     "green": number,
     "amber": number,
     "red": number,
     "total": number,
     "rows": [
       {
         "program": "string",
         "health": "Green|Amber|Red",
         "risk": "string",
         "decisionPending": "Yes|No"
       }
     ],
     "leadershipAsks": ["string"]
   }

3. Update data/portfolio/executive-briefing.json with a fresh executive summary.

4. Run `python agents/pulse-orchestrator/pulse.py validate --mode portfolio` to verify all schemas.

5. Run `python agents/pulse-orchestrator/pulse.py reports --mode portfolio` to regenerate HTML outputs.

6. Return a Pulse Summary following the format in the system prompt.

Constraints:
- Do not fabricate program health; derive from source data only.
- Mark missing program data as TBD.
- Keep leadership asks to 2 to 3 maximum.
- Flag all output for human review before sharing.
```

---

## Expected outputs

| Output | Location |
|---|---|
| Updated portfolio JSON | `data/portfolio/portfolio-health.json` |
| Updated executive briefing | `data/portfolio/executive-briefing.json` |
| HTML portfolio chat | `output/portfolio/YYYY-MM-DD/portfolio-health-chat.html` |
| HTML executive briefing | `output/portfolio/YYYY-MM-DD/executive-briefing.html` |
| Terminal summary | Copilot Chat response |

## Human approval checklist

Before publishing any output from this playbook:

- [ ] All program health statuses are current and verified
- [ ] Leadership asks are specific, actionable, and owned
- [ ] No red program is missing an escalation owner
- [ ] Executive briefing language is concise and non-technical
- [ ] No confidential data included
