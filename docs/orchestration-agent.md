# Orchestration Agent Guide

This guide explains how to use the Pulse Orchestrator — the in-repo TPM agent — to manage programs and produce AI-assisted artifacts.

## What is Pulse Orchestrator?

Pulse Orchestrator is the orchestration agent for this framework. It routes TPM requests to the right artifact flow, extracts signals from meeting transcripts and intake files, generates first-draft artifacts, and connects to the HTML report generation pipeline.

It runs in two modes:

| Mode | How to use |
|---|---|
| **CLI mode** | Run `python agents/pulse-orchestrator/pulse.py <command>` from repo root |
| **Copilot Chat mode** | Paste a playbook prompt into GitHub Copilot Chat with this repo open |

Both modes enforce the same governance rules: no fabricated facts, human approval before sharing, and scoped to one program per run.

It also supports two operating lanes:

1. Per-program execution
2. Portfolio aggregation

---

## Quick start

### 1. Run a status summary (30 seconds)

```bash
python agents/pulse-orchestrator/pulse.py status --program-slug my-program
```

Shows health, highlights, risks, and next actions from a program-scoped weekly status file when available.

### 2. Validate all data files before generating reports

```bash
python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug my-program
```

Run this before every report generation to catch missing fields early.

For portfolio aggregation:

```bash
python agents/pulse-orchestrator/pulse.py validate --mode portfolio
```

### 3. Generate all HTML reports

```bash
python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug my-program
```

Runs `scripts/generate_reports.py` and writes HTML files to a mode-aware output folder.

For portfolio aggregation:

```bash
python agents/pulse-orchestrator/pulse.py reports --mode portfolio
```

---

## Supported workflows

### Weekly status update

**What it does:** Extracts signals from a meeting transcript or intake file and updates program-scoped JSON files under `data/programs/<program-slug>/`. Generates weekly status HTML.

**CLI:**
```bash
python agents/pulse-orchestrator/pulse.py status --program-slug my-program
```

**Copilot Chat:** See `agents/pulse-orchestrator/playbooks/weekly-status.md`.

**Full playbook:** `agents/pulse-orchestrator/playbooks/weekly-status.md`

---

### Portfolio rollup

**What it does:** Synthesizes cross-program health into portfolio-scoped JSON files under `data/portfolio/`. Generates portfolio and executive HTML reports.

**CLI:**
```bash
python agents/pulse-orchestrator/pulse.py portfolio
```

**Copilot Chat:** See `agents/pulse-orchestrator/playbooks/portfolio-rollup.md`.

**Full playbook:** `agents/pulse-orchestrator/playbooks/portfolio-rollup.md`

---

### ADR draft creation

**What it does:** Generates a structured Architecture Decision Record draft from a described decision and saves it to `data/adrs/`.

**CLI:**
```bash
python agents/pulse-orchestrator/pulse.py adr "Decision title" \
  --program "Program Name" \
  --context "One sentence problem description"
```

**Copilot Chat:** See `agents/pulse-orchestrator/playbooks/adr-draft.md`.

**Full playbook:** `agents/pulse-orchestrator/playbooks/adr-draft.md`

---

### Risk review

**What it does:** Reviews open risks from the RAID digest, validates owners and next actions, and updates severity where needed.

**CLI (read-only summary):**
```bash
python agents/pulse-orchestrator/pulse.py risks --program-slug my-program
```

**Copilot Chat:** See `agents/pulse-orchestrator/playbooks/risk-review.md`.

**Full playbook:** `agents/pulse-orchestrator/playbooks/risk-review.md`

---

### Stakeholder update

**What it does:** Generates a tailored draft communication for a specific audience (executive, engineering leadership, or external partner).

**CLI:** Not available (Copilot Chat only — no files are modified).

**Copilot Chat:** See `agents/pulse-orchestrator/playbooks/stakeholder-update.md`.

**Full playbook:** `agents/pulse-orchestrator/playbooks/stakeholder-update.md`

---

## How it uses intake inputs

The orchestrator reads from `data/intake/<program-slug>/`:

- `meeting-transcript-YYYY-MM-DD.md` — preferred input; raw or edited meeting transcript
- `weekly-intake-YYYY-MM-DD.md` — fallback structured form if no transcript is available

**To add intake for your program:**

```
data/intake/
  my-program/
    meeting-transcript-2026-07-07.md   ← save transcript here
    weekly-intake-2026-07-07.md        ← or intake form here
```

See `data/intake/sample-program/meeting-transcript-2026-07-07.md` for a working example.

---

## How it respects governance

Pulse Orchestrator enforces these rules on every run:

1. **No fabricated facts.** Missing owners and dates are marked `TBD`.
2. **Draft outputs only.** All Copilot Chat artifacts are labeled as drafts for human review.
3. **Human approval required** before sharing executive communications, portfolio reports, or ADRs.
4. **Scope control.** Each run is scoped to one program unless portfolio mode is explicitly requested.
5. **Schema preservation.** JSON files are only updated with valid, schema-conforming changes.

Full policy: `governance/hitl-governance.md`.

---

## How it connects to report generation

```
intake input
    │
    ▼
Pulse Orchestrator (Copilot Chat or CLI)
    │
  ├─ updates data/programs/<program-slug>/*.json
  ├─ or updates data/portfolio/*.json
    │
    ▼
python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug my-program   ← check schemas
    │
    ▼
python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug my-program
    │
    ▼
output/<program-slug>/YYYY-MM-DD/*.html or output/portfolio/YYYY-MM-DD/*.html   ← review before sharing
```

The orchestrator sits between raw intake and the HTML renderer. It does not modify templates. It only updates structured data JSON files.

---

## All available commands

See `agents/pulse-orchestrator/commands.md` for the complete command reference including CLI options and Copilot Chat prompt templates.

---

## Example end-to-end run

1. Save your meeting transcript:
   ```
   data/intake/my-program/meeting-transcript-2026-07-07.md
   ```

2. Open Copilot Chat and paste the weekly-status playbook prompt from:
   ```
   agents/pulse-orchestrator/playbooks/weekly-status.md
   ```

3. Copilot updates program-scoped JSON files and runs validation.

4. Validate manually:
   ```bash
  python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug my-program
   ```

5. Generate reports:
   ```bash
  python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug my-program
   ```

6. Review outputs in `output/my-program/YYYY-MM-DD/` and approve before sharing.

Total time for a well-prepared TPM: under 10 minutes per weekly cycle.

---

## File layout for this agent

```
agents/pulse-orchestrator/
  README.md              ← entry point
  system-prompt.md       ← agent behavior spec (use as Copilot system prompt)
  commands.md            ← command reference card
  pulse.py               ← CLI entrypoint
  validate.py            ← JSON schema validator
  playbooks/
    weekly-status.md     ← copy-paste prompt for weekly status
    portfolio-rollup.md  ← copy-paste prompt for portfolio rollup
    adr-draft.md         ← copy-paste prompt for ADR drafting
    risk-review.md       ← copy-paste prompt for risk review
    stakeholder-update.md← copy-paste prompt for stakeholder updates
```
