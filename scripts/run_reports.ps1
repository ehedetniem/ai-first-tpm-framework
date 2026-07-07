Param(
    [string]$WeeklyJson = "data/sample-weekly-status.json",
    [string]$PortfolioJson = "data/sample-portfolio-health.json",
    [string]$ExecutiveJson = "data/sample-executive-briefing.json",
    [string]$RaidJson = "data/sample-raid-digest.json",
    [string]$AdrJson = "data/sample-adr-log.json",
    [string]$DailyOpsJson = "data/sample-daily-ops-pulse.json",
    [string]$DependencyJson = "data/sample-dependency-critical-path.json",
    [string]$CapacityJson = "data/sample-capacity-milestone-confidence.json",
    [string]$AdoptionJson = "data/sample-adoption-change-readout.json",
    [string]$ExecutivePortfolioRadarJson = "data/sample-executive-portfolio-radar.json",
    [string]$OutputDir = "output"
)

$ErrorActionPreference = "Stop"

Write-Host "[INFO] Installing dependencies..."
python -m pip install -r requirements.txt

Write-Host "[INFO] Generating reports..."
python scripts/generate_reports.py --weekly-json $WeeklyJson --portfolio-json $PortfolioJson --executive-json $ExecutiveJson --raid-json $RaidJson --adr-json $AdrJson --daily-ops-json $DailyOpsJson --dependency-json $DependencyJson --capacity-json $CapacityJson --adoption-json $AdoptionJson --executive-portfolio-radar-json $ExecutivePortfolioRadarJson --output-dir $OutputDir

Write-Host "[INFO] Done. Check output in '$OutputDir'."
