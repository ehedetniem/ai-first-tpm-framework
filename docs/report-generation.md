# Report Generation Guide

This repo includes a simple Python generator for HTML reports.

## What it generates

- `output/weekly-status-email.html`
- `output/portfolio-health-chat.html`

## Inputs

- `data/sample-weekly-status.json`
- `data/sample-portfolio-health.json`

## Templates

- `reports/weekly-status-email-template.html.j2`
- `reports/portfolio-health-chat-template.html.j2`

## Setup

1. Install Python 3.10+.
2. Install dependencies:
   - `pip install -r requirements.txt`

## Run

From repo root:
- `python scripts/generate_reports.py`

Optional custom input paths:
- `python scripts/generate_reports.py --weekly-json data/my-weekly.json --portfolio-json data/my-portfolio.json --output-dir output`

## Workflow recommendation

1. Update JSON inputs from your weekly program data.
2. Generate HTML.
3. Review output with human approver.
4. Send via email/chat channel.
