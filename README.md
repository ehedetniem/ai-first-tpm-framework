# AI-First TPM Framework

A practical operating system for Technical Program Management teams moving from manual reporting to AI-enabled execution.

This framework helps teams:
- Standardize stakeholder artifacts across programs
- Preserve decision context with ADRs
- Shift TPM time from manual synthesis to judgment and alignment
- Introduce AI safely with human approval gates

## What this repo contains

- `lifecycle/` - Program phases and gate criteria
- `governance/` - Human-in-the-loop policy and accountability boundaries
- `templates/` - Reusable templates for weekly status, ADRs, risk log, and portfolio rollup
- `upskilling/` - 90-day PM-to-TPM AI upskilling plan
- `automation/` - Maturity path from manual execution to governed AI assistance
- `docs/` - Reference narrative and implementation notes

## Quickstart

1. Read `lifecycle/program-lifecycle.md`.
2. Read `governance/hitl-governance.md`.
3. Copy templates in `templates/` into your program workspace.
4. Run a weekly cycle:
   - Update program status template
   - Capture decisions in ADR template
   - Refresh risk log and portfolio rollup
5. Start AI enablement with `automation/maturity-model.md`.

## Core model

This framework uses three layers:

1. Knowledge layer
   - Lifecycle, gates, ADRs, templates, governance
2. Signal layer
   - Program health, milestones, risks, dependencies
3. Intelligence layer
   - AI-assisted first drafts for synthesis and communications

## Human-in-the-loop position

- AI is used for first-pass synthesis and drafting.
- Humans own approvals, tradeoffs, and accountability.

This is a learning loop, not autopilot.

## Who this is for

- PMs upskilling into TPM execution
- TPM teams operating across cross-org engineering programs
- Leaders needing consistent portfolio health signals

## License

MIT - see `LICENSE`.
