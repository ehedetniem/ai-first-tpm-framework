#!/usr/bin/env bash
set -euo pipefail

WEEKLY_JSON="${1:-data/sample-weekly-status.json}"
PORTFOLIO_JSON="${2:-data/sample-portfolio-health.json}"
OUTPUT_DIR="${3:-output}"

echo "[INFO] Installing dependencies..."
python -m pip install -r requirements.txt

echo "[INFO] Generating reports..."
python scripts/generate_reports.py \
  --weekly-json "$WEEKLY_JSON" \
  --portfolio-json "$PORTFOLIO_JSON" \
  --output-dir "$OUTPUT_DIR"

echo "[INFO] Done. Check output in '$OUTPUT_DIR'."
