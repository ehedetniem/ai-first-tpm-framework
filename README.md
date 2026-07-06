# AI-First TPM Framework

A practical operating system for Technical Program Management teams moving from manual reporting to AI-enabled execution.

This framework helps teams:
- Standardize stakeholder artifacts across programs
- Preserve decision context with ADRs
- Shift TPM time from manual synthesis to judgment and alignment
- Introduce AI safely with human approval gates

## Start here

- Quick onboarding: `docs/getting-started.md`
- Repo navigation: `docs/repository-map.md`
- Lifecycle model: `lifecycle/program-lifecycle.md`
- Governance model: `governance/hitl-governance.md`
- Core templates: `templates/README.md`
- HTML report samples: `reports/README.md`
- Report generator setup: `docs/report-generation.md`
- ADR authoring guide: `docs/adr-instructions.md`
- TPM starter agent concept: `agents/pulse-orchestrator/README.md`

## What this repo contains

- `lifecycle/` - Program phases and gate criteria
- `governance/` - Human-in-the-loop policy and accountability boundaries
- `templates/` - Reusable templates for weekly status, ADRs, risk log, and portfolio rollup
- `upskilling/` - 90-day PM-to-TPM AI upskilling plan
- `automation/` - Maturity path from manual execution to governed AI assistance
- `reports/` - Sample HTML reports for email and chat channels
- `scripts/` - Report generation scripts
- `data/` - Sample input data for report generation
- `agents/` - Starter agent patterns (for example, Pulse Orchestrator)
- `docs/` - Reference narrative and implementation notes

## Recommended adoption paths

### Path A: Individual TPM or small team

1. Start with `docs/getting-started.md`.
2. Use templates in `templates/` for one program.
3. Run weekly cadence for 4 weeks.
4. Add ADR discipline and risk review.

### Path B: Portfolio-scale TPM team

1. Align on lifecycle and gate criteria.
2. Standardize artifact templates across all programs.
3. Establish HITL approval boundaries.
4. Roll up program status weekly with portfolio template.
5. Use maturity model to phase AI adoption.

## Quickstart

1. Read `lifecycle/program-lifecycle.md`.
2. Read `governance/hitl-governance.md`.
3. Copy templates in `templates/` into your program workspace.
4. Run a weekly cycle:
   - Update program status template
   - Capture decisions in ADR template
   - Refresh risk log and portfolio rollup
5. Start AI enablement with `automation/maturity-model.md`.

For a practical onboarding flow, use `docs/getting-started.md`.

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

## Public collaboration and trust

- Contribution guide: `CONTRIBUTING.md`
- Code of conduct: `CODE_OF_CONDUCT.md`
- Security policy: `SECURITY.md`

## Who this is for

- PMs upskilling into TPM execution
- TPM teams operating across cross-org engineering programs
- Leaders needing consistent portfolio health signals

## License

MIT - see `LICENSE`.
