# Repository Map

## Purpose

This file explains the repository structure in a way that any AI environment can reuse.

## Folder Template

For each important folder, document:

### /00_Project-Core

- Purpose: Defines the core L1 orchestration schemas, templates, and architectural principles.
- Main contents: Schemas (Handoff, Return Packet), Templates (Task Brief, Discussion Queue), Architecture summaries.
- Typical changes: Schema updates, architectural refinements.
- Dependencies: Foundation for all other components.
- Notes: Stable reference for all AI environments.

### /10_Officially-Documented-Adapters

- Purpose: Platform-specific instruction sets for well-documented AI environments.
- Main contents: Adapters for GitHub Copilot, Cline, Gemini, etc.
- Typical changes: Updates to match platform capability changes.
- Dependencies: Depends on `00_Project-Core` for rules.
- Notes: Classification: stable reference / handoff.

### /20_Convention-Based-Adapters

- Purpose: Adapters for platforms relying on file conventions rather than explicit APIs.
- Main contents: Adapters for Cursor, Windsurf, Antigravity, etc.
- Typical changes: Adjusting to evolving IDE behavior.
- Dependencies: Depends on `00_Project-Core`.
- Notes: Classification: implementation / overlay.

### /30_Generic-Fallbacks

- Purpose: Minimal, portable bridge contract for unknown or fast-changing environments.
- Main contents: Generic AI-IDE prompts and simplified instructions.
- Typical changes: Rarely, unless a new universal pattern emerges.
- Dependencies: None.
- Notes: Classification: archive / stable reference.

### /docs

- Purpose: Human-readable project tracking and visualization for the "Universal Skeleton".
- Main contents: Workflow, Repo Map, Changelog, Progress Board.
- Typical changes: Continuous updates as work progresses.
- Dependencies: Reflects current repo state.
- Notes: Classification: project state / audit.

## Classification Guide

Use these labels where relevant:

- stable reference
- implementation
- project state
- handoff
- audit / log
- overlay
- archive
