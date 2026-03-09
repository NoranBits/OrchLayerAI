# AGENTS.md

Version: 3.0-beta
Purpose: Universal repository operating instructions for any AI coding environment

## Mission

This repository is a reusable, adaptable project skeleton.

Do not treat it as bound to one framework, language, or runtime unless the files clearly prove that.
Your job is to help humans and AI environments understand, track, and evolve the repository with high clarity and low noise.

## Core priorities

1. Accuracy

- Inspect actual files before making architectural claims
- Do not assume hidden implementation exists
- Prefer verified repo state over guesses

1. Adaptability

- Treat this repository as a cross-project skeleton
- Keep guidance reusable across different stacks
- Infer patterns from visible files, not assumptions

1. Trackability

- Always make workflow progress easy to follow
- Keep repo changes easy to audit
- Show what changed, why it changed, and what should happen next

1. Token efficiency

- Use compact structured outputs
- Avoid repeating repo context unnecessarily
- Prefer short operational summaries over long prose

## Default output shape

When analyzing or updating the repository, prefer this structure:

### Repository Snapshot

- purpose
- current apparent architecture
- maturity level
- missing pieces

### Folder Map

For each important folder:

- purpose
- how it works
- what depends on it
- what usually changes there

### Workflow View

- current phase
- active work
- blockers
- next step

### Top Problems

- highest-impact issues only

### Top Solutions

- smallest high-value fixes first

### Change Summary

- files inspected
- files changed
- structural effect
- unresolved items

### Recommended Next Task

- one best next action

## Visualization rule

Whenever architecture, workflow, or progress is discussed:

- generate a compact visualization
- prefer Mermaid if supported
- otherwise use short ASCII diagrams
- keep diagrams simple and operational

Preferred diagram types:

- flowchart
- sequence diagram
- dependency map

## Folder explanation rule

Always explain folders in plain language.

Classify folders when possible as:

- stable reference
- active implementation
- state / checkpoints
- handoffs
- logs / audit
- overlays / policy
- archive

## Change reporting rule

Every meaningful repo change should be described as:

- What changed
- Why it changed
- What it affects
- What remains unresolved

## Problem-solution rule

Compress findings like this:

- Problem: one-line issue
- Impact: why it matters
- Fix: smallest practical correction

## Anti-fake rule

Do not claim:

- implementation exists unless visible
- workflow exists unless supported by files
- a fix is complete unless verified
- structure is final if the repo is still a skeleton

Honest partial understanding is preferred.

## Cross-tool rule

This file is intended to work across multiple AI coding environments.
If a tool supports its own rule format, those files may extend this one, but should not contradict it.
