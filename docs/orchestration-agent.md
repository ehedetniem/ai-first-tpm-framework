# Orchestration Agent Guide

This guide explains how to use Pulse Orchestrator, the in-repo TPM agent, through GitHub Copilot Chat.

## What Pulse Orchestrator does

Pulse Orchestrator helps TPMs turn raw working signals into structured artifacts.

It:
- reads transcripts and intake notes
- drafts first-pass artifacts
- updates structured program or portfolio inputs
- validates those inputs
- generates leadership-ready report outputs

The intended TPM experience is language-first. You describe what happened, what changed, or what decision matters. Copilot and the orchestration flow do the structural work.

## Two operating lanes

1. Per-program execution
2. Portfolio aggregation

## Quick start

### 1. Ask for current status

Example:

```text
Show me the current status for my-program in plain English.
```

### 2. Ask Copilot to validate and generate

Example:

```text
Validate the program inputs for my-program and generate the reports.
```

### 3. Review the high-signal deltas

Focus on:
- risks and blockers
- decision asks
- changed KPI meaning
- any owner or due date marked TBD

## Supported workflows

### Weekly status update

What it does:
- reads transcript or intake inputs for one program
- updates program-scoped structured inputs
- generates program report outputs

Use playbook:
- `agents/pulse-orchestrator/playbooks/weekly-status.md`

### Portfolio rollup

What it does:
- reads cross-program inputs
- updates portfolio-scoped structured inputs
- generates portfolio leadership outputs

Use playbook:
- `agents/pulse-orchestrator/playbooks/portfolio-rollup.md`

### ADR draft creation

What it does:
- drafts a structured ADR from a decision discussion
- saves it into the ADR drafts area for review

Use playbook:
- `agents/pulse-orchestrator/playbooks/adr-draft.md`

### Risk review

What it does:
- reviews open risks and blockers
- checks owner/action quality
- flags escalation items

Use playbook:
- `agents/pulse-orchestrator/playbooks/risk-review.md`

### Stakeholder update

What it does:
- drafts audience-specific communications
- tailors tone for executive, engineering, or external audiences

Use playbook:
- `agents/pulse-orchestrator/playbooks/stakeholder-update.md`

## Intake model

Pulse Orchestrator reads from `data/intake/<program-slug>/`.

Preferred input:
- `meeting-transcript-YYYY-MM-DD.md`

Fallback input:
- `weekly-intake-YYYY-MM-DD.md`

Ask Copilot to create or update these files for you.

## Governance

Pulse Orchestrator follows these rules:

1. No fabricated facts
2. Unknown owners or dates become `TBD`
3. Human approval is required before external sharing
4. Each run stays scoped to one program unless portfolio mode is explicitly requested
5. Templates are preserved; structured inputs are updated

See `governance/hitl-governance.md` for the full policy.

## End-to-end flow

```text
transcript or intake
        ↓
Copilot + Pulse Orchestrator
        ↓
structured program or portfolio inputs
        ↓
validation
        ↓
HTML report generation
        ↓
human review and publish
```

## Example end-to-end run

1. Paste a transcript for `my-program` into Copilot.
2. Ask Copilot to save it under `data/intake/my-program/meeting-transcript-YYYY-MM-DD.md`.
3. Ask Copilot to validate inputs and generate reports.
4. Review outputs in `output/my-program/YYYY-MM-DD/`.
5. Approve and publish.

## Prompt reference

See `agents/pulse-orchestrator/commands.md` for short prompts and `agents/pulse-orchestrator/playbooks/` for longer structured prompts.
