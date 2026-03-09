# Roo Code Adapter

This adapter is provided as a project-specific starting point for Roo Code workflows.

It is based on Roo's role / mode-oriented model and should be treated as a configurable project adapter.

## Suggested use
- keep shared OrchLayer rules in `.roo/rules/`
- create or update custom modes so one mode acts as `field-executor`
- keep the executor mode focused on fresh state inspection, structured returns, and blocker visibility

## Required behavior
- inspect current workspace state
- return structured execution summaries
- surface drift, blockers, and decision needs
- do not fake completion
