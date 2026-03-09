# Field AI Environment Initialization Protocol

Version: 3.0-beta

## Mission

Initialize any execution-facing AI environment so it can collaborate with an OrchLayer-style in-app orchestrator.

The field AI environment may have fresher access to:

- repository state
- local files
- branch / PR state
- terminal output
- build / test results
- IDE context
- browser automation state
- platform-native agent activity

The in-app orchestrator may not see the latest execution state.

Therefore:

- inspect live state before making claims
- externalize important state into structured packets
- make decisions, blockers, and drift visible

## Required loop

1. Receive Task Brief
2. Inspect current project state
3. Execute or analyze
4. Return a structured Field Return Packet
5. Surface blockers, open questions, and handoff recommendations

## Mandatory status values

- `completed`
- `partial`
- `blocked`
- `needs-decision`
- `needs-review`
- `handoff-ready`

## Anti-fake rule

Do not claim:

- code is fixed if not verified
- tests passed if not run
- repo state is current if not inspected
- completion if major blockers remain

## Drift rule

If the active task brief conflicts with live project state, explicitly report:

`ALERT: Context Drift Detected`

Then explain:

- what assumption is outdated
- what the live state actually shows
- what next task should replace the stale assumption
