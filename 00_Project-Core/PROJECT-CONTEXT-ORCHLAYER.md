# Project Context: OrchLayer

## What this project is

OrchLayer is a structured L1 orchestration pattern for long-running human-AI and AI-AI collaboration.

It is optimized around these principles:
- project-first continuity
- stateless honesty
- knowledge minimalism
- explicit Session Packets
- explicit Handoff Packages
- structured review and drift detection
- human-visible decision boundaries
- tool realism

## What the field AI environment must understand

The repository or workspace may contain fresher implementation state than the in-app orchestrator can see.

Therefore the execution-facing AI environment must:
- inspect current project state before making claims
- report structured findings back to the orchestrator
- separate completed work from attempted work
- raise blockers and decisions instead of pretending completion
- recommend the next smallest valid task

## Core collaboration loop

1. In-app orchestrator sends a task brief
2. Field AI environment inspects live project state
3. Field AI environment executes or analyzes
4. Field AI environment returns a structured return packet
5. Orchestrator turns that into next tasks, questions, and handoffs

## Success criteria

A successful field integration:
- reduces context drift
- preserves project intent
- improves execution-state visibility
- helps multiple AI systems collaborate without fake certainty
