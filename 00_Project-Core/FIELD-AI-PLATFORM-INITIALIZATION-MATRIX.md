# Field AI Platform Initialization Matrix

## Officially-documented adapters in this pack

- GitHub Copilot
- VS Code Copilot custom agents / instruction files
- Gemini / Gems + Google Workspace
- Claude Code
- Cline
- Continue

## Convention-based adapters in this pack

- Cursor
- Windsurf
- Antigravity AI IDE
- Roo Code

## Universal fallback

Use `30_Generic-Fallbacks/` when:

- the execution environment is unknown
- the platform changes too quickly to trust hard-coded file paths
- you need a minimal, portable bridge contract first

## Selection rule

1. Use the platform-specific adapter if the file mechanism is documented and available.
2. If the platform supports multiple instruction layers, keep the shared OrchLayer rules in the repo and add the smallest possible platform wrapper.
3. If the platform is uncertain, use the generic adapter and manually paste the initialization prompt.

### Antigravity AI IDE

Initialization assets:

- `ANTIGRAVITY.md`
- `ANTIGRAVITY-RETURN-PACKET.json`
- `FIELD-AI-ENV-INIT.md`
- `AGENTS.md`

Use when:

- agent-first IDE workflow
- multi-agent execution
- artifact-based execution trace
- browser + terminal + editor orchestration
- manager-level supervision of parallel tasks

Special rules:

- treat artifacts as primary evidence
- report per-agent subtask ownership
- require confirmation for destructive actions
- surface cross-agent coordination failures explicitly
