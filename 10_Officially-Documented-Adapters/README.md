# 10_Officially-Documented-Adapters

## Purpose

Contains platform-specific configuration and instruction files for AI coding environments with officially supported plugin or rule systems.

## Visualized Adapters

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#6366f1',
    'primaryTextColor': '#fff',
    'primaryBorderColor': '#4f46e5',
    'lineColor': '#818cf8',
    'secondaryColor': '#ec4899',
    'tertiaryColor': '#06b6d4',
    'nodePadding': '10'
  }
}}%%
mindmap
  root((Official Adapters))
    IDC[IDE Configurations]
      VSCode[vscode]
      Copilot[github-copilot]
    AI_Agents[AI Agents]
      Cline[cline]
      Roo[roo-code]
      Claude[claude-code]
      Gemini[gemini]
```

## Selection Guide

Classified as: **stable reference / handoff**

Use these when the platform explicitly supports a `.clinerules`, `.cursorrules`, or similar dedicated instruction file mechanism. These adapters are designed to be the "minimum viable wrapper" around the universal `AGENTS.md` and `00_Project-Core` rules.
