# ADR Instructions (How To Create Architecture Decision Records)

Use this process any time a technical, scope, or operating decision has meaningful downstream impact.

## When to create an ADR

Create an ADR when a decision:
- affects architecture, platform, or integration path
- changes scope boundaries or sequencing
- introduces a major tradeoff (cost, risk, speed, quality)
- is likely to be revisited later without clear rationale

## Inputs you should gather first

- Decision title
- Context and problem statement
- Options considered
- Selection criteria
- Chosen option and rationale
- Expected consequences
- Approver(s) and decision date

## Step-by-step process

1. Copy `templates/adr-template.md` to your program folder.
2. Name file with a stable pattern, for example:
   - `ADR-2026-07-06-rollout-cadence.md`
3. Fill sections in this order:
   - Context
   - Options considered
   - Decision
   - Rationale
   - Consequences
   - Approvals
4. Set status:
   - `Proposed` while under review
   - `Accepted` once approved
   - `Superseded` if replaced by a later ADR
5. Link ADR in weekly status and portfolio rollup when relevant.

## Quality checklist

Before publishing an ADR, confirm:
- Problem statement is explicit
- Tradeoffs are clear and comparable
- Rationale references evidence
- Consequences include both positive and negative impacts
- Approval details are complete

## Sample naming and indexing pattern

- Keep ADRs in `docs/adrs/` (recommended)
- Prefix with date for sortability
- Add a simple index file mapping ADR titles to status

## AI-assisted drafting guidance

AI can draft a first ADR version, but humans should verify:
- factual correctness
- option framing
- consequence realism
- final decision ownership

## Transcript-first ADR prompt (Copilot)

If you have a meeting transcript, use this prompt to draft an ADR quickly:

```text
Use data/intake/meeting-transcript-YYYY-MM-DD.md as source.

Draft an ADR using templates/adr-template.md style.

Requirements:
1) Pick the highest-impact decision from the transcript.
2) Include context, options considered, decision, rationale, consequences, and approvals.
3) Do not invent facts; mark unknown owners/dates as TBD.
4) Save file as ADR-YYYY-MM-DD-<short-title>.md.
5) Return a 5-bullet summary of what decision was captured and why it matters.
```
