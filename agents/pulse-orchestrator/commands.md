# Pulse Orchestrator — Command Reference

Quick reference for every prompt and command available to Copilot-native TPMs.

## Copilot Chat prompts (primary)

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
Source: data/sample-raid-digest.json
Program: <program-slug>

Run the risk-review playbook from agents/pulse-orchestrator/playbooks/risk-review.md.
```

### @pulse stakeholder-update

```
Act as Pulse Orchestrator for this repo. See agents/pulse-orchestrator/system-prompt.md for your behavior rules.

Task: stakeholder update
Audience: <executive | engineering | external>
Source: data/sample-weekly-status.json, data/sample-portfolio-health.json
Program: <program-slug or "Portfolio">

Run the stakeholder-update playbook from agents/pulse-orchestrator/playbooks/stakeholder-update.md.
```

---

## CLI commands (fallback)

Run from the repository root. Requires Python 3.10+ and `pip install -r requirements.txt`.

| Command | What it does |
|---|---|
| `python agents/pulse-orchestrator/pulse.py status` | Print weekly status summary from `data/sample-weekly-status.json` |
| `python agents/pulse-orchestrator/pulse.py portfolio` | Print portfolio health table |
| `python agents/pulse-orchestrator/pulse.py risks` | Print open risks and blockers from RAID digest |
| `python agents/pulse-orchestrator/pulse.py adr "<title>"` | Generate a new ADR draft file in `data/adrs/` |
| `python agents/pulse-orchestrator/pulse.py validate` | Validate all JSON data files against expected schemas |
| `python agents/pulse-orchestrator/pulse.py reports` | Run full HTML report generation |

### `status` options

```bash
python agents/pulse-orchestrator/pulse.py status --json my-program-weekly.json
```

### `adr` options

```bash
python agents/pulse-orchestrator/pulse.py adr "Decision title" \
  --program "My Program" \
  --context "One sentence describing the problem"
```

### `reports` options

```bash
python agents/pulse-orchestrator/pulse.py reports --output-dir custom-output/
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
| `reports` | `output/*.html` (10 HTML files) |
| @pulse status (Copilot) | `data/sample-weekly-status.json`, `data/sample-portfolio-health.json`, `output/*.html` |
| @pulse portfolio (Copilot) | `data/sample-portfolio-health.json`, `data/sample-executive-portfolio-radar.json`, `output/*.html` |
| @pulse adr (Copilot) | `data/adrs/ADR-YYYY-MM-DD-<slug>.md`, `data/sample-adr-log.json` (if accepted) |
| @pulse risks (Copilot) | `data/sample-raid-digest.json`, `output/raid-digest.html` |
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
