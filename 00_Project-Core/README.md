# 00_Project-Core

## Purpose

This directory contains the essential DNA of the OrchLayer project. It defines the schemas and templates that govern how human and AI agents collaborate.

## Visualized Logic

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
    'clusterBkg': '#1e1b4b',
    'clusterBorder': '#4338ca'
  }
}}%%
graph TD
    subgraph Schemas
        Session[FIELD-AI-SESSION-PACKET-SCHEMA.json]
        Handoff[FIELD-AI-HANDOFF-SCHEMA.json]
        Capability[FIELD-AI-CAPABILITY-MANIFEST-SCHEMA.json]
        Return[FIELD-AI-RETURN-PACKET-SCHEMA.json]
    end
    
    subgraph Templates
        Brief[FIELD-AI-TASK-BRIEF-TEMPLATE.md]
        Queue[DISCUSSION-QUEUE-TEMPLATE.md]
    end
    
    subgraph Rules
        Arch[PROJECT-ARCHITECTURE-SUMMARY.md]
        Context[PROJECT-CONTEXT-ORCHLAYER.md]
    end
    
    Rules --> Brief
    Schemas --> Return
    Brief --> Return
```

## Core Contracts (FIELD-AI)

- **Source of Truth**: The JSON schemas in this directory are the canonical definitions for all continuity artifacts. All adapters must conform to these.
- **Immutability Rule**: Mutable working state (e.g., specific session notes) does not belong here; use `01_Project-State/` or `02_Session-Packets/`.
- **Verification**: Capability declarations are environment-specific templates. A capability is only "active" if verified and documented in `01_Project-State/CAPABILITY-MANIFEST.current.json`.
- **Legacy Support**: Older packets missing the `session_frame` must be wrapped into the new structure rather than modified in place.

## Folder Role

Classified as: **stable reference**

- **FIELD-AI-PLATFORM-INITIALIZATION-MATRIX.md**: The master routing log for choosing the right adapter.
- **FIELD-AI-ENV-INIT.md**: The standard "Hello World" for any newly initialized field AI.
- **PROJECT-SPECIFIC-TASK-STARTERS.md**: Curated prompts for common project activities.
