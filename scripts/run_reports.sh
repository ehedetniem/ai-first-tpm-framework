#!/usr/bin/env bash
set -euo pipefail

WEEKLY_JSON="${1:-data/sample-weekly-status.json}"
PORTFOLIO_JSON="${2:-data/sample-portfolio-health.json}"
EXECUTIVE_JSON="${3:-data/sample-executive-briefing.json}"
RAID_JSON="${4:-data/sample-raid-digest.json}"
ADR_JSON="${5:-data/sample-adr-log.json}"
DAILY_OPS_JSON="${6:-data/sample-daily-ops-pulse.json}"
DEPENDENCY_JSON="${7:-data/sample-dependency-critical-path.json}"
CAPACITY_JSON="${8:-data/sample-capacity-milestone-confidence.json}"
ADOPTION_JSON="${9:-data/sample-adoption-change-readout.json}"
EXECUTIVE_PORTFOLIO_RADAR_JSON="${10:-data/sample-executive-portfolio-radar.json}"
OUTPUT_DIR="${11:-output}"

echo "[INFO] Installing dependencies..."
python -m pip install -r requirements.txt

echo "[INFO] Generating reports..."
python scripts/generate_reports.py \
  --weekly-json "$WEEKLY_JSON" \
  --portfolio-json "$PORTFOLIO_JSON" \
  --executive-json "$EXECUTIVE_JSON" \
  --raid-json "$RAID_JSON" \
  --adr-json "$ADR_JSON" \
  --daily-ops-json "$DAILY_OPS_JSON" \
  --dependency-json "$DEPENDENCY_JSON" \
  --capacity-json "$CAPACITY_JSON" \
  --adoption-json "$ADOPTION_JSON" \
  --executive-portfolio-radar-json "$EXECUTIVE_PORTFOLIO_RADAR_JSON" \
  --output-dir "$OUTPUT_DIR"

echo "[INFO] Done. Check output in '$OUTPUT_DIR'."
