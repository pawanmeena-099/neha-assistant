
# NEHA — Architecture Decision Register

Version: 1.0
Status: Initial Decisions

## ADR-001: Project Architecture

Decision:
Use a modular monolith initially.

Reason:
Simpler development, testing and maintenance.

Future:
Split services only when necessary.

## ADR-002: Backend

Decision:
Python + FastAPI.

Reason:
Suitable for AI integration, APIs and automation.

## ADR-003: Desktop Application

Decision:
Tauri + React + TypeScript.

Reason:
Cross-platform desktop interface with web technologies.

## ADR-004: Android Application

Decision:
Kotlin + Jetpack Compose.

Reason:
Native Android development and platform integration.

## ADR-005: Hybrid AI

Decision:
Support local and cloud AI through separate adapters.

Reason:
Privacy, flexibility, performance and provider choice.

## ADR-006: Local AI

Decision:
Use Ollama as the initial local model runtime.

Reason:
Simple local model management and integration.

## ADR-007: Database

Decision:
PostgreSQL as primary database.
SQLite for local device storage.

Reason:
Structured data, reliability and local caching.

## ADR-008: Memory

Decision:
Separate temporary context from long-term memory.

Reason:
Better privacy, control and memory quality.

## ADR-009: Agent Architecture

Decision:
Central orchestrator with specialized agents.

Reason:
Controlled coordination and separate permissions.

## ADR-010: Security

Decision:
Use one central permission and approval system.

Reason:
No agent or model should bypass security rules.

## ADR-011: Coding Agent

Decision:
Use isolated Git worktrees and automated tests.

Reason:
Protect existing projects and enable rollback.

## ADR-012: Learning Engine

Decision:
New skills must be evaluated before registration.

Reason:
Prevent unsafe or unreliable automation.

## ADR-013: Cloud Hosting

Decision:
Develop locally first.
Use Railway or another host when required.

Reason:
Avoid unnecessary hosting costs during development.

## ADR-014: Version Control

Decision:
Use a private GitHub repository.

Reason:
Version history, backup and collaboration.

## ADR-015: Decision Changes

Every significant change must record:
- Decision ID
- Date
- Previous decision
- New decision
- Reason
- Impact
- Migration plan

## Current Status

These are initial architectural decisions.
Hardware benchmarks and implementation tests
may require documented changes.
