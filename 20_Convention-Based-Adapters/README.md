# 20_Convention-Based-Adapters

## Purpose

Focuses on AI environments that rely on file-name conventions or root-level instructions rather than a formal API or plugin system.

## Comparison Map

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#6366f1',
    'primaryTextColor': '#fff',
    'primaryBorderColor': '#4f46e5',
    'lineColor': '#818cf8',
    'secondaryColor': '#ec4899',
    'tertiaryColor': '#06b6d4'
  }
}}%%
graph LR
    A[Cursor] --> B[.cursorrules]
    C[Windsurf] --> D[.windsurfrules]
    E[Antigravity] --> F[ANTIGRAVITY.md]
    G[Roo Code] --> H[.clinerules]
```

## Strategy

Classified as: **implementation / overlay**

These files often "mirror" the root `AGENTS.md` but are tailored to the specific quirks and context windows of each tool. They ensure that even if the tool doesn't have a formal plugin, it still adheres to the OrchLayer L1 contract.
