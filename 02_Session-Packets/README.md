# 02_Session-Packets

## Purpose

This directory stores compact, machine-readable active-state checkpoints (Session Packets).

## Role

Classified as: **state / handoff**

- **FILE-AI-SESSION-PACKET.json**: Standardized continuity artifact.

## Storage Rule

One packet per significant execution phase. Legacy packets missing the `session_frame` should be wrapped according to the v3.1 compatibility rules.
