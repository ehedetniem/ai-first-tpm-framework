Param(
    [string]$WeeklyJson = "data/sample-weekly-status.json",
    [string]$PortfolioJson = "data/sample-portfolio-health.json",
    [string]$ExecutiveJson = "data/sample-executive-briefing.json",
    [string]$RaidJson = "data/sample-raid-digest.json",
    [string]$AdrJson = "data/sample-adr-log.json",
    [string]$OutputDir = "output"
)

$ErrorActionPreference = "Stop"

Write-Host "[INFO] Installing dependencies..."
python -m pip install -r requirements.txt

Write-Host "[INFO] Generating reports..."
python scripts/generate_reports.py --weekly-json $WeeklyJson --portfolio-json $PortfolioJson --executive-json $ExecutiveJson --raid-json $RaidJson --adr-json $AdrJson --output-dir $OutputDir

Write-Host "[INFO] Done. Check output in '$OutputDir'."
