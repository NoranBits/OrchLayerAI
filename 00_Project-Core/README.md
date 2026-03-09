# 00_Project-Core

## Purpose

This directory contains the essential DNA of the OrchLayer project. It defines the schemas and templates that govern how human and AI agents collaborate.

## Visualized Logic

```mermaid
graph TD
    subgraph Schemas
        Handoff[FIELD-AI-HANDOFF-SCHEMA.json]
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

## Folder Role

Classified as: **stable reference**

- **FIELD-AI-PLATFORM-INITIALIZATION-MATRIX.md**: The master routing log for choosing the right adapter.
- **FIELD-AI-ENV-INIT.md**: The standard "Hello World" for any newly initialized field AI.
- **PROJECT-SPECIFIC-TASK-STARTERS.md**: Curated prompts for common project activities.
