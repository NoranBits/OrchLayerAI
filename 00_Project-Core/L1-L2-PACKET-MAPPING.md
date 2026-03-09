# L1-L2 Packet Mapping (v3.1)

## Purpose

This document defines the explicit translation boundary between the **L1 Orchestrator** continuity model and the **L2 Field AI** execution schemas.

## 1. Session Packet Mapping

L1 Session Packets define the "continuity frame," while L2 Field AI Session Packets focus on the "active context."

| L1 Field (Expectation) | L2 Field (Schema) | Notes |
|-----------------------|-------------------|-------|
| `goal` | `current_objective` | The high-level objective of the current session. |
| `active_scope` | `active_context` | The boundaries of what the agent is currently touching. |
| `current_step` | `progress_status` | L2 maps this to an enum (in-progress/blocked/completed). |
| `required_output` | `working_notes` | Detailed notes on what is being produced. |
| `open_risks` | `working_notes` | Included as part of the working state in L2. |
| `last_decisions` | `working_notes` | Included as historical context for the current session. |
| `artifacts_produced` | `artifacts_produced` | Direct 1:1 mapping. |

## 2. Return Packet Mapping

L2 Return Packets (evidence) map back to L1 next-step updates.

| L2 Return Field | L1 Update Target | Notes |
|-----------------|------------------|-------|
| `status` | `current_step` status | Updates the orchestrator on task completion level. |
| `findings.risks` | `open_risks` | Bubbles up execution risks to the plan level. |
| `findings.resolved` | `last_decisions` | Documents verified architectural or logic choices. |
| `recommended_next_tasks` | `next_action` | Provides the basis for the next orchestrator brief. |

## 3. Handoff Mapping

Standardized for agent-to-agent and agent-to-human transfers.

| L1 Handoff Field | L2 Handoff Field | Notes |
|------------------|------------------|-------|
| `handoff_id` | `handoff_id` | Unique transfer identifier. |
| `target` | `target_id` | The recipient (Human, Reviewer, etc.). |
| `handoff_reason` | `handoff_reason` | Why the transfer is happening. |
| `expected_artifact`| `expected_artifact`| What the next actor should produce. |
| `continuity_ids` | `critical_links` | Links to the project root and latest packets. |
