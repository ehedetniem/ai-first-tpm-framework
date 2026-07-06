#!/usr/bin/env bash
set -euo pipefail

WEEKLY_JSON="${1:-data/sample-weekly-status.json}"
PORTFOLIO_JSON="${2:-data/sample-portfolio-health.json}"
EXECUTIVE_JSON="${3:-data/sample-executive-briefing.json}"
RAID_JSON="${4:-data/sample-raid-digest.json}"
ADR_JSON="${5:-data/sample-adr-log.json}"
OUTPUT_DIR="${6:-output}"

echo "[INFO] Installing dependencies..."
python -m pip install -r requirements.txt

echo "[INFO] Generating reports..."
python scripts/generate_reports.py \
  --weekly-json "$WEEKLY_JSON" \
  --portfolio-json "$PORTFOLIO_JSON" \
  --executive-json "$EXECUTIVE_JSON" \
  --raid-json "$RAID_JSON" \
  --adr-json "$ADR_JSON" \
  --output-dir "$OUTPUT_DIR"

echo "[INFO] Done. Check output in '$OUTPUT_DIR'."
