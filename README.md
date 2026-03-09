# OrchLayer Universal AI IDE Integration Pack

Version: v3.0-beta

This pack extends the OrchLayer project into a repository-ready integration layer for execution-facing AI environments.

It is tailored to the current OrchLayer project content:

- L1 orchestration
- project-first continuity (Invariant Core Contracts)
- stateless honesty
- knowledge minimalism (Mutable State stays in Project State)
- explicit Session Packets and Handoff Packages
- capability-aware execution bridge
- human-visible decision boundaries

## Goal

Create one reusable, project-specific initialization pack that lets multiple AI coding environments work with the same collaboration contract.

The pack is designed for:

- GitHub Copilot
- VS Code agent workflows
- Gemini / Gems + Google Workspace
- Claude Code
- Cline
- Continue
- Cursor
- Windsurf
- Antigravity AI IDE
- Roo Code
- unknown future environments via generic fallbacks

## Important scope note

This pack is intentionally split into:

- `10_Officially-Documented-Adapters` for platforms where current documentation was reviewed before generating the adapter
- `20_Convention-Based-Adapters` for platforms where practical file conventions are widely used but product behavior may evolve faster than docs
- `30_Generic-Fallbacks` for any future or unknown execution environment

This means the pack is broad and reusable, but not a claim that every platform loads every file identically.

## Project-specific assumptions

This pack assumes the project is OrchLayer-like:

- the in-app orchestrator is not always the freshest execution-state observer
- the field AI environment may have better repo / IDE / terminal / browser awareness
- the field layer should return structured packets, not only prose
- major decisions, blockers, and unresolved questions must flow back to the orchestrator and user

## Recommended use

1. Start with `00_Project-Core/`.
2. Copy one platform adapter into the project root, preserving its directory structure.
3. Keep the generic protocol files in the repo as stable collaboration artifacts.
4. If multiple AI IDEs are used at once, prefer one shared core protocol and multiple thin adapters.
5. Keep the orchestrator responsible for planning and continuity; keep the field AI responsible for fresh execution-facing truth.
