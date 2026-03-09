# Decision Log

## Purpose

Record significant project decisions and their context.

## Decisions

### 2026-03-09: Adopt Universal Repo Skeleton

- **Context**: Need a repo-agnostic operating layer for multiple AI environments.
- **Decision**: Implement `AGENTS.md` and `docs/` structure based on universal root instruction model.
- **Status**: Active

### ADR-012: Standardization of Root Contracts (FIELD-AI)

- **Date**: 2026-03-09
- **Context**: Need for platform-agnostic portability and strict continuity.
- **Decision**: Mirror Gemini-side contracts to `00_Project-Core/FIELD-AI-*`. Normalizing from v3.0-alpha to v3.0-beta L2 operating contract.
- **Consequence**: All adapters must now conform to these schemas. Hardcoded platform values are moved to state files in `01_Project-State/`.
- **Legacy Rule**: Wrap legacy top-level fields into `session_frame`. Do not invent data for missing fields.
- **Status**: Active
