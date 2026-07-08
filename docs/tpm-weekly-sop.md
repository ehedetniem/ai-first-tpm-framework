# TPM Weekly SOP (Copilot Orchestrated, Per Program)

This SOP is the standard weekly operating procedure for non-technical TPMs using this public repo.

## Purpose

Create leadership-ready updates with a consistent, low-friction process:

1. Use transcript or intake notes as source input
2. Orchestrate updates with Copilot
3. Run validate + reports (via Copilot first, CLI fallback)
4. Review deltas
5. Publish with human approval

## Scope

- One run per program (`<program-slug>`)
- One source input per run
- One approval step before external sharing

## Inputs and paths

Per program input files:

- `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md` (preferred)
- `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md` (fallback)

Generated outputs:

- `output/*.html` (latest run)

Recommended archive location:

- `reports/archive/<program-slug>/YYYY-MM-DD/`

## Weekly cadence (per program)

### 1) Collect source input

- Export meeting transcript or notes and save under the program slug path.
- Keep one intake stream per program to preserve traceability.

### 2) Run Copilot orchestration

- Use prompt from `docs/copilot-orchestrated-mode.md`.
- Ensure prompt scope is program-specific (`<program-slug>`).

### 3) Validate and generate

Copilot-native path (recommended):

- Ask Copilot to run validation and report generation after JSON updates.

CLI fallback from repo root:

1. `python agents/pulse-orchestrator/pulse.py validate`
2. `python agents/pulse-orchestrator/pulse.py reports`

Quality checks:

- No missing owners/dates unless marked `TBD`
- No invented facts
- No cross-program data leakage in one run

### 4) Review exceptions only

Review only high-signal deltas:

- Risks/blockers
- Decision asks
- KPI deltas
- ADR draft quality (if created)

### 5) Approve and publish

- Publish only after human review.
- Archive outputs to dated program folder for traceability.

## ADR handling

If transcript includes meaningful decisions:

- Draft ADR from transcript using `docs/adr-instructions.md` prompt
- Save with stable naming: `ADR-YYYY-MM-DD-<short-title>.md`
- Mark unknowns as `TBD` (no fabricated facts)

## Do / Don't

Do:

- Keep runs scoped to one program
- Keep owner/date fields explicit
- Keep language concise and executive
- Run validate before every report generation
- Keep prompt execution scoped to one program per run

Don't:

- Mix multiple programs in one run
- Publish unreviewed drafts
- Invent missing decision facts
- Skip archive step

## Quality gate checklist

Before publish, confirm:

1. Program scope is correct (`<program-slug>`)
2. Top risks and blockers are accurate
3. Decision asks have owners and due dates (or `TBD`)
4. ADR status and rationale are clear
5. Validation passed with no blocking errors
6. Outputs archived for audit trail

## Escalation rules

Escalate to human reviewer immediately if:

- A risk severity changed to High/Critical
- A decision owner or due date is unknown for an executive ask
- KPI delta is large and explanation is missing
- A dependency blocker impacts milestone confidence

## Source-of-truth note

In internal environments, upstream systems may refresh YAML via bridge automation.
This public repo remains the rendering layer (`data/*.json` -> `output/*.html`).
