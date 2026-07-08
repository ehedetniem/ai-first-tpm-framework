# Pulse Orchestrator — Command Reference

Quick reference for every command and prompt available to TPMs.

---

## CLI commands

Run from the repository root. Requires Python 3.10+ and `pip install -r requirements.txt`.

| Command | What it does |
|---|---|
| `python agents/pulse-orchestrator/pulse.py status --program-slug <program-slug>` | Print weekly status summary for one program |
| `python agents/pulse-orchestrator/pulse.py portfolio` | Print portfolio health table |
| `python agents/pulse-orchestrator/pulse.py risks --program-slug <program-slug>` | Print open risks and blockers for one program |
| `python agents/pulse-orchestrator/pulse.py adr "<title>"` | Generate a new ADR draft file in `data/adrs/` |
| `python agents/pulse-orchestrator/pulse.py validate --mode program --program-slug <program-slug>` | Validate program-scoped JSON data files |
| `python agents/pulse-orchestrator/pulse.py validate --mode portfolio` | Validate portfolio-scoped JSON data files |
| `python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug <program-slug>` | Run program-scoped HTML report generation |
| `python agents/pulse-orchestrator/pulse.py reports --mode portfolio` | Run portfolio aggregation HTML report generation |

### `status` options

```bash
python agents/pulse-orchestrator/pulse.py status --program-slug my-program
```

### `adr` options

```bash
python agents/pulse-orchestrator/pulse.py adr "Decision title" \
  --program "My Program" \
  --context "One sentence describing the problem"
```

### `reports` options

```bash
python agents/pulse-orchestrator/pulse.py reports --mode program --program-slug my-program --output-dir custom-output/
```

---

## Copilot Chat prompts

Paste these prompts into GitHub Copilot Chat with this repo open. Each prompt maps to a specific playbook in `agents/pulse-orchestrator/playbooks/`.

### @pulse status

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: weekly status update
Source: data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md
Program: <program-slug>

Run the weekly-status playbook from agents/pulse-orchestrator/playbooks/weekly-status.md.
```

### @pulse portfolio

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: portfolio rollup
Source: all active program data in data/

Run the portfolio-rollup playbook from agents/pulse-orchestrator/playbooks/portfolio-rollup.md.
```

### @pulse adr

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: ADR draft
Decision title: <decision title>
Program: <program-slug>
Context: <one sentence problem description>

Run the adr-draft playbook from agents/pulse-orchestrator/playbooks/adr-draft.md.
```

### @pulse risks

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: risk review
Source: data/programs/<program-slug>/raid-digest.json
Program: <program-slug>

Run the risk-review playbook from agents/pulse-orchestrator/playbooks/risk-review.md.
```

### @pulse stakeholder-update

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: stakeholder update
Audience: <executive | engineering | external>
Source: program-scoped or portfolio-scoped JSON inputs, depending on request
Program: <program-slug or "Portfolio">

Run the stakeholder-update playbook from agents/pulse-orchestrator/playbooks/stakeholder-update.md.
```

---

## Artifacts created per command

| Command | Artifacts created or updated |
|---|---|
| `status` | Terminal summary (read-only) |
| `portfolio` | Terminal summary (read-only) |
| `risks` | Terminal summary (read-only) |
| `adr <title>` | `data/adrs/ADR-YYYY-MM-DD-<slug>.md` |
| `validate` | Terminal validation report |
| `reports` | `output/<program-slug>/YYYY-MM-DD/*.html` or `output/portfolio/YYYY-MM-DD/*.html` |
| @pulse status (Copilot) | `data/programs/<program-slug>/weekly-status.json`, related outputs |
| @pulse portfolio (Copilot) | `data/portfolio/*.json`, `output/portfolio/YYYY-MM-DD/*.html` |
| @pulse adr (Copilot) | `data/adrs/ADR-YYYY-MM-DD-<slug>.md`, `data/programs/<program-slug>/adr-log.json` (if accepted) |
| @pulse risks (Copilot) | `data/programs/<program-slug>/raid-digest.json`, related outputs |
| @pulse stakeholder-update (Copilot) | Draft text for human review |

---

## Human approval gates

The following outputs **always require human review** before sharing:

- Executive briefings
- Portfolio radar reports
- Stakeholder communications
- Any ADR moving from Proposed to Accepted
- Any artifact containing owner names, dates, or budget references

See `governance/hitl-governance.md` for the full policy.
