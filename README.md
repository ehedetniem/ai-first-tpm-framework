# AI-First TPM Framework

A practical operating system for Technical Program Management teams moving from manual reporting to AI-enabled execution.

The intended experience is language-first.

Instead of starting with spreadsheets, status-chasing, or manual report writing, a TPM starts with the conversation that already happened: a meeting transcript, a set of notes, a decision that needs to be captured, or a blocker that needs to be escalated.

From there:
- TPMs bring transcripts, notes, and decisions into GitHub Copilot Chat
- Copilot drafts artifacts, updates structured inputs, and runs report generation
- CLI commands remain available as a backup path, not the primary user experience

This framework helps teams:
- Standardize stakeholder artifacts across programs
- Preserve decision context with ADRs
- Shift TPM time from manual synthesis to judgment and alignment
- Introduce AI safely with human approval gates

## Start here (non-AI TPM quick path)

If you are new to AI tools, follow this exact order:

1. **Start in 10 minutes (fastest path):** `docs/start-in-10-minutes.md`
2. **Quick onboarding (30-45 min):** `docs/getting-started.md`
3. **First weekly run SOP:** `docs/tpm-weekly-sop.md`
4. **Orchestration agent workflows:** `docs/orchestration-agent.md`
5. **Run the CLI status check:** `python agents/pulse-orchestrator/pulse.py status --program-slug <program-slug>`
6. **Validate data before report generation:** `python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug <program-slug>`

If you do only one thing today, complete the **10-minute checklist** in `docs/start-in-10-minutes.md`.

## Core docs and workflows

- **Start in 10 minutes:** `docs/start-in-10-minutes.md`
- **Orchestration agent (primary):** `docs/orchestration-agent.md`
- **Pulse Orchestrator CLI + playbooks:** `agents/pulse-orchestrator/README.md`
- **Quick onboarding:** `docs/getting-started.md`
- **TPM Weekly SOP (per-program workflow):** `docs/tpm-weekly-sop.md`
- **Copilot orchestrated no-code mode:** `docs/copilot-orchestrated-mode.md`
- **Repo navigation:** `docs/repository-map.md`
- **Lifecycle model:** `lifecycle/program-lifecycle.md`
- **Governance model:** `governance/hitl-governance.md`
- **Core templates:** `templates/README.md`
- **HTML report samples:** `reports/README.md`
- **Report generator setup:** `docs/report-generation.md`
- **ADR authoring guide:** `docs/adr-instructions.md`
- **AI prompt pack for artifacts:** `docs/ai-artifact-pack.md`

## Using with VS Code + GitHub Copilot

Recommended setup for this repo is VS Code with GitHub Copilot Chat enabled.

Think of this as a transition path:
- first, learn the weekly rhythm
- next, let Copilot do the first pass
- finally, use CLI only when you need verification or backup

1. Open this folder in VS Code.
2. Open `docs/start-in-10-minutes.md` for your first successful run.
3. Open `docs/getting-started.md` for full Day 1 onboarding.
4. Open `docs/tpm-weekly-sop.md` to understand the repeatable weekly flow.
5. Run `python agents/pulse-orchestrator/pulse.py status --program-slug <program-slug>` to see the current program status.
6. Use a playbook from `agents/pulse-orchestrator/playbooks/` in Copilot Chat.
7. Run `python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug <program-slug>` before report generation.
8. Review rendered outputs in `output/<program-slug>/YYYY-MM-DD/` and optional samples in `reports/`.

Important:
- The in-repo orchestration agent is `agents/pulse-orchestrator/`.
- Use `python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug <program-slug>` before every program report run.
- This repo does not include an `XPO` runtime agent.
- CLI and scripts are available as backup when Copilot orchestration is not available.
- You can run the full framework without Copilot by using Pulse CLI, templates, and scripts directly.

## Two Public Modes

1. Per-program mode
- One TPM run for one `<program-slug>`
- Inputs live under `data/programs/<program-slug>/`
- Outputs should be written to a program/date-specific folder

2. Portfolio aggregation mode
- One aggregation run across multiple programs
- Inputs live under `data/portfolio/`
- Outputs produce leadership rollups such as portfolio health and executive radar

## CLI Backup

From repo root:

- Windows PowerShell:
   - `./scripts/run_reports.ps1`
- macOS/Linux:
   - `bash ./scripts/run_reports.sh`

Generated outputs:
- `output/weekly-status-email.html`
- `output/portfolio-health-chat.html`
- `output/executive-briefing.html`
- `output/raid-digest.html`
- `output/adr-log.html`
- `output/daily-ops-pulse.html`
- `output/dependency-critical-path-review.html`
- `output/capacity-milestone-confidence.html`
- `output/adoption-change-readout.html`
- `output/executive-portfolio-radar.html`

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

1. Start with `docs/start-in-10-minutes.md`.
2. Continue with `docs/getting-started.md`.
3. Use transcript-first orchestration for one program.
4. Review generated artifacts and approve.
5. Add ADR discipline and risk review.

### Path B: Portfolio-scale TPM team

1. Align on lifecycle and gate criteria.
2. Standardize artifact templates across all programs.
3. Establish HITL approval boundaries.
4. Roll up program status weekly with portfolio template.
5. Use maturity model to phase AI adoption.

## Quickstart

1. Open VS Code with GitHub Copilot Chat.
2. Start with `docs/getting-started.md`.
3. Use transcript-first or intake orchestration to generate artifacts.
4. Review only exceptions, decisions, and deltas.
5. Use CLI backup only if Copilot orchestration is unavailable.

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
