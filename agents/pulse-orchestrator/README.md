# Pulse Orchestrator (TPM Starter Agent)

Pulse Orchestrator is a starter agent concept for teams adopting this framework.

Purpose:
- route TPM requests to the right artifact flow
- preserve decision and risk context
- enforce human approval boundaries for critical outputs

## Core responsibilities

1. Intake and classify requests
- status update
- portfolio rollup
- ADR drafting
- risk review
- stakeholder communication

2. Build context pack
- latest weekly status
- open risks
- pending decisions
- relevant prior ADRs

3. Generate first-pass artifacts
- weekly status draft
- portfolio summary draft
- ADR draft
- leadership communication draft

4. Apply governance checks
- identify where human approval is mandatory
- flag unsupported claims
- surface missing data before publishing

## Suggested commands (conceptual)

- `@pulse status [program]`
- `@pulse portfolio`
- `@pulse adr [decision-title]`
- `@pulse risks [program]`
- `@pulse stakeholder-update [audience]`

## Implementation note

This repository provides process and templates first. You can implement Pulse Orchestrator in the AI platform of your choice using these docs as the control plane.
