# Intake Inputs

This folder is for no-code TPM inputs used by Copilot orchestration.

Use program-specific subfolders to keep signals isolated:

- `data/intake/<program-slug>/meeting-transcript-YYYY-MM-DD.md`
- `data/intake/<program-slug>/weekly-intake-YYYY-MM-DD.md`

Recommended files:

- `meeting-transcript-YYYY-MM-DD.md` (preferred)
- `weekly-intake-YYYY-MM-DD.md` (fallback when transcript is unavailable)

Start from:

- `weekly-intake-template.md`

Use prompts from:

- `docs/copilot-orchestrated-mode.md`
