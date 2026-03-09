# Project Architecture Summary

## High-level model

- **User**: owns priorities and decisions
- **In-app orchestrator**: planning, review, handoff, continuity, decomposition
- **Field AI environment**: freshest execution-facing observer
- **Optional sub-agents**: platform- or task-specific specialists

## Source-of-truth order

1. Verified live execution-state report
2. Current repository / workspace files
3. Current project decision log
4. Latest Session Packet / Handoff Package
5. Stable knowledge and policy files

## Non-negotiable boundaries

- no fake completion
- no pretending hidden memory exists
- no silent architecture or security decisions
- no hiding blockers
- no unstructured final reporting for meaningful tasks

## Expected project artifact classes

- Task Brief
- Field Return Packet
- Discussion Queue
- Session Packet
- Handoff Package
- Decision Log Entry
