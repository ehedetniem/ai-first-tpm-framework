# Report Generation Guide

This repo includes a Python generator for a leadership-ready HTML reporting pack.

## What it generates

- `output/weekly-status-email.html`
- `output/portfolio-health-chat.html`
- `output/executive-briefing.html`
- `output/raid-digest.html`
- `output/adr-log.html`
- `output/daily-ops-pulse.html`
- `output/dependency-critical-path-review.html`
- `output/capacity-milestone-confidence.html`
- `output/adoption-change-readout.html`

## Inputs

- `data/sample-weekly-status.json`
- `data/sample-portfolio-health.json`
- `data/sample-executive-briefing.json`
- `data/sample-raid-digest.json`
- `data/sample-adr-log.json`
- `data/sample-daily-ops-pulse.json`
- `data/sample-dependency-critical-path.json`
- `data/sample-capacity-milestone-confidence.json`
- `data/sample-adoption-change-readout.json`

## Templates

- `templates/reports/weekly-status-email-template.html`
- `templates/reports/portfolio-health-chat-template.html`
- `templates/reports/executive-briefing-template.html`
- `templates/reports/raid-digest-template.html`
- `templates/reports/adr-log-template.html`
- `templates/reports/daily-ops-pulse-template.html`
- `templates/reports/dependency-critical-path-template.html`
- `templates/reports/capacity-milestone-confidence-template.html`
- `templates/reports/adoption-change-readout-template.html`
- `templates/reports/_theme.css`

## Setup

1. Install Python 3.10+.
2. Install dependencies:
   - `pip install -r requirements.txt`

## One-command runners

- Windows PowerShell:
   - `./scripts/run_reports.ps1`
- macOS/Linux:
   - `bash ./scripts/run_reports.sh`

## Run

From repo root:
- `python scripts/generate_reports.py`

Optional custom input paths:
- `python scripts/generate_reports.py --weekly-json data/my-weekly.json --portfolio-json data/my-portfolio.json --executive-json data/my-exec.json --raid-json data/my-raid.json --adr-json data/my-adr.json --daily-ops-json data/my-daily-ops.json --dependency-json data/my-dependencies.json --capacity-json data/my-capacity.json --adoption-json data/my-adoption.json --output-dir output`

PowerShell with custom inputs:
- `./scripts/run_reports.ps1 -WeeklyJson data/my-weekly.json -PortfolioJson data/my-portfolio.json -ExecutiveJson data/my-exec.json -RaidJson data/my-raid.json -AdrJson data/my-adr.json -DailyOpsJson data/my-daily-ops.json -DependencyJson data/my-dependencies.json -CapacityJson data/my-capacity.json -AdoptionJson data/my-adoption.json -OutputDir output`

Shell with custom inputs:
- `bash ./scripts/run_reports.sh data/my-weekly.json data/my-portfolio.json data/my-exec.json data/my-raid.json data/my-adr.json data/my-daily-ops.json data/my-dependencies.json data/my-capacity.json data/my-adoption.json output`

## Workflow recommendation

1. Update JSON inputs from your weekly program data.
2. Generate HTML pack.
3. Review outputs with a human approver.
4. Publish to email/chat/executive review channels.
