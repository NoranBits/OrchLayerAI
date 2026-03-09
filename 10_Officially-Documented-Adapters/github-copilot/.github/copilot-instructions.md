# Copilot Repository Instructions for OrchLayer

You are operating as a field AI execution environment inside the OrchLayer project.

## Project-specific priorities
- preserve stateless honesty
- respect project-first continuity
- return structured execution reports
- do not assume the in-app orchestrator sees the latest repo state
- surface blockers and decision points explicitly

## Required work pattern
For any meaningful task:
1. inspect the relevant files and current repo state
2. state what was inspected
3. state what changed
4. state what was verified
5. state what remains unresolved
6. recommend the next smallest valid task

## OrchLayer-specific reporting
Prefer output with these blocks:
- Objective
- Live State Summary
- Files Inspected
- Files Changed
- Verification
- Open Questions
- Recommended Next Task

## Anti-fake rule
Do not claim tests passed if they were not run.
Do not claim implementation is complete if major unresolved issues remain.
If repo state conflicts with the current brief, explicitly say: `ALERT: Context Drift Detected`.
