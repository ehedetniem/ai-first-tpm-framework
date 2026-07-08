# AI Artifact Pack for TPM Reporting

Use these prompts with your AI assistant to convert raw program notes into structured JSON that the report generator can consume.

## 1) Executive briefing JSON prompt

Copy and paste:

You are preparing JSON for an executive TPM report.
Return valid JSON only using this schema:
{
  "title": "Executive Program Briefing",
  "weekEnding": "YYYY-MM-DD",
  "owner": "string",
  "topWin": "string",
  "topRisk": "string",
  "decisionNeeded": "string",
  "programSummary": [
    {"program": "string", "health": "Green|Amber|Red", "trend": "string"}
  ],
  "asks": ["string"]
}
Use concise leadership language and no internal jargon.

## 2) RAID digest JSON prompt

Copy and paste:

Transform the following weekly RAID notes into valid JSON only.
Schema:
{
  "weekEnding": "YYYY-MM-DD",
  "entries": [
    {
      "type": "Risk|Assumption|Issue|Dependency",
      "title": "string",
      "severity": "High|Medium|Low",
      "owner": "string",
      "nextAction": "string"
    }
  ]
}
Normalize wording and remove duplicates.

## 3) ADR log JSON prompt

Copy and paste:

Create a weekly ADR decision log in valid JSON only.
Schema:
{
  "weekEnding": "YYYY-MM-DD",
  "decisions": [
    {
      "id": "ADR-YYYY-MM-DD-or-sequence",
      "title": "string",
      "status": "Proposed|Accepted|Rejected|Superseded",
      "owner": "string",
      "approvedBy": "string",
      "approvedAt": "YYYY-MM-DD or Pending"
    }
  ]
}
Ensure every accepted decision has approver and approval date.

## Suggested operating loop

1. Gather notes from meetings, mail, and tracker.
2. Ask Copilot to use prompt 1/2/3 to produce JSON files in `data/`.
3. Ask Copilot to run the repo's report generation workflow.
4. Review outputs with a human approver before publish.
