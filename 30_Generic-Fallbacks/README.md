# 30_Generic-Fallbacks

## Purpose

The ultimate fallback for any environment that is unknown, stateless, or doesn't support persistent instruction files.

## Fallback Logic

```mermaid
flowchart TD
    Start[New Agent Environment] --> Known{Is it known?}
    Known -- Yes --> Use_10_20[Use Folder 10 or 20]
    Known -- No --> Use_30[Use 30_Generic-Fallbacks]
    Use_30 --> Paste[Manual Instruction Paste]
    Paste --> Minimal[Minimal portable bridge context]
```

## Contents

Classified as: **archive / stable reference**

- **FIELD-AI-INITIALIZATION-PROMPT.md**: A compact, copy-pasteable version of the core project rules.
- **FIELD-AI-HANDOFF-TEMPLATE.json**: Simplified handoff structure for quick sessions.
