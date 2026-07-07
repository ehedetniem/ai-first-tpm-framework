# Playbook: Stakeholder Update

Use this playbook to generate a tailored stakeholder update for a specific audience.

Paste this prompt into GitHub Copilot Chat with the repo open, replacing the bracketed values.

---

## Prompt

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for behavior rules.

Task: stakeholder update
Audience: <executive | engineering-leadership | external-partner>
Program: <program-slug or "Portfolio">
Week ending: <YYYY-MM-DD>

Source inputs:
- Weekly status: data/sample-weekly-status.json
- Portfolio health: data/sample-portfolio-health.json
- Executive briefing: data/sample-executive-briefing.json
- Transcript (optional): data/intake/<program-slug>/meeting-transcript-<YYYY-MM-DD>.md

Steps:
1. Read source inputs and produce a communication draft tailored to the audience:

   For "executive":
   - Lead with health status and one headline win.
   - Name the top risk and the specific ask.
   - Keep to 150 words or fewer.
   - No technical detail.

   For "engineering-leadership":
   - Include milestone status, blockers, and dependency flags.
   - Name the decision needed and the owner.
   - Include next 7 days actions.
   - Acceptable to use technical terms.

   For "external-partner":
   - Surface only what is safe to share externally.
   - Focus on joint commitments, shared dependencies, and ask.
   - Omit internal health status colors.
   - Use neutral, collaborative tone.

2. Output the draft as Markdown text ready for email or chat paste.

3. Return a Pulse Summary with:
   - Audience
   - Key messages surfaced
   - Any governance flags (information that may not be safe to share externally)
   - Required: human review before sending

Constraints:
- Do not include confidential data in external-partner drafts.
- Do not invent claims; derive from source data only.
- Always flag for human review; never send directly.
- Mark missing facts as TBD.
```

---

## Expected outputs

| Output | Format | Location |
|---|---|---|
| Stakeholder draft | Markdown text | Copilot Chat response |
| No files are modified by this playbook | — | — |

The TPM copies the draft from Copilot Chat, reviews it, and sends it manually.

## Human approval checklist

Before sending any stakeholder update:

- [ ] Claims are evidence-based and traceable to source data
- [ ] No confidential or internal-only data in external drafts
- [ ] Owner names and commitments are accurate
- [ ] Tone is appropriate for the audience
- [ ] Reviewed and approved by the accountable TPM or program lead
