# Getting Started for Non-Technical PMs (Copilot-First)

This guide is the easiest way to use this framework if you are not a developer.

The goal is simple: start from the work you already do, not from a technical toolchain. If you have a transcript, notes, a risk discussion, or a decision thread, that is enough to begin.

## Goal for Day 1

By the end of Day 1, you should be able to:

1. Add one intake artifact for one program
2. Ask Copilot to validate and generate successfully
3. Review and publish with human approval

If you only follow one document today, follow this one end-to-end.

## What is true today

- You should use VS Code with GitHub Copilot Chat.
- You do not need a built-in XPO runtime agent to run this framework.
- The current workflow is automation-first, with human review before publish.
- Non-technical TPMs should use Copilot orchestration instead of editing JSON directly.

In practice, this means:
- you bring the raw signal
- Copilot turns it into structure
- you review judgment, risk, and message quality

## Source of truth (important)

Your understanding is correct:

- In your full TPM framework, YAML is the operational source of truth used by downstream artifacts.
- Those YAML files are typically updated by an external bridge/automation from your work tracking system.
- This public repo does not include that private bridge implementation.

What this public repo does include:

- A public per-program workflow and a separate portfolio aggregation workflow.
- Report rendering from structured JSON to HTML in `output/`.
- A Copilot-first workflow to update JSON safely for weekly publishing.

Practical model:

1. Upstream system updates (external bridge) refresh YAML in your internal environment
2. YAML signal is mapped/exported into either program-scoped or portfolio-scoped JSON inputs
3. This repo renders leadership-ready HTML reports

For a concrete field mapping contract, see `docs/report-generation.md` under "Bridge handoff contract example (YAML -> JSON)".

## Day 1 checklist (copy/paste)

- [ ] Open this repo in VS Code
- [ ] Open Copilot Chat
- [ ] Create one intake file for one program slug
- [ ] Ask Copilot to validate the program inputs
- [ ] Ask Copilot to generate the program reports
- [ ] Open files in `output/<program-slug>/YYYY-MM-DD/` and review deltas
- [ ] Publish only after human approval

## Step 1 - Open the repo in VS Code

1. Open VS Code.
2. Open this repository folder.
3. Open Copilot Chat.

## Step 2 - Choose your no-code input

Option A (recommended): Transcript-first

1. Save meeting transcript or notes as `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md`.
2. Use transcript orchestration prompt from `docs/copilot-orchestrated-mode.md`.

Option B: Intake file

1. Open `data/intake/weekly-intake-template.md`.
2. Save a copy as `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md`.
3. Fill sections in plain language.

Use one intake or transcript stream per program so decisions, risks, and owners remain traceable.

## Step 3 - Choose your operating mode

Per-program mode:

- Use one `<program-slug>` only
- Target inputs under `data/programs/<program-slug>/`
- Write outputs to a dated program folder

Portfolio aggregation mode:

- Use rollup inputs under `data/portfolio/`
- Generate leadership-ready cross-program outputs

## Step 4 - Ask Copilot to orchestrate updates

Use the runbook and prompt in:

- `docs/copilot-orchestrated-mode.md`

Copilot will:

1. Update required JSON files
2. Validate schema/fields
3. Run report generation
4. Return a short review summary
5. (Transcript mode) Draft ADR(s) from decisions discussed

CLI is backup only. In the normal flow, Copilot should run validation and generation for you.

For example, you can say:

- "Use the transcript for <program-slug>, validate the program inputs, generate the reports, and tell me what changed."

If you need to run the backup commands yourself:

Per-program mode:

1. `python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug <program-slug>`
2. `python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug <program-slug>`

Portfolio mode:

1. `python agents/pulse-orchestrator/pulse.py validate --mode portfolio`
2. `python agents/pulse-orchestrator/pulse.py reports --mode portfolio`

## Step 5 - Review only what matters

Do not rewrite full reports manually. Review these items:

- Risks, blockers, and decision asks
- Any changed KPI numbers
- Leadership narrative for accuracy and tone

After review, publish to your normal channels. The goal is not to polish every sentence by hand. The goal is to spend your time on judgment, clarity, and decision quality.

## Step 6 - Reuse this weekly rhythm

Each week, repeat:

1. Save one transcript or intake input
2. Run one orchestration prompt
3. Let Copilot validate and generate; use CLI only if Copilot did not already run them for you
4. Review deltas
5. Publish

Over time, the motion should feel lighter: fewer manual rewrites, faster status synthesis, and more TPM attention on decisions and execution.

## Troubleshooting (quick)

- **Validation fails:** ask Copilot to explain which required fields are missing and fix them.
- **No report output:** ask Copilot to rerun report generation and tell you where outputs were written.
- **Confusing prompt behavior:** use the exact prompts in `agents/pulse-orchestrator/playbooks/`.
- **Unclear ownership or dates:** use `TBD` instead of guessing.

## Where to go next

- Weekly operating procedure (SOP): `docs/tpm-weekly-sop.md`
- Orchestration agent guide: `docs/orchestration-agent.md`
- Report generation details: `docs/report-generation.md`
- Orchestrated no-code mode: `docs/copilot-orchestrated-mode.md`
- Report samples: `reports/README.md`
- Decision records (ADR): `docs/adr-instructions.md`
- Starter orchestration pattern: `agents/pulse-orchestrator/README.md`
