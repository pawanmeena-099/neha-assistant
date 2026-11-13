
# NEHA — API Specification

Version: 1.0
Status: Initial API Design

## 1. Overview

The NEHA API connects:
- Desktop application
- Android application
- AI orchestrator
- Model router
- Memory engine
- Agent system
- Tool execution engine

Base URL (local development):
http://127.0.0.1:8000

API prefix:
/v1

## 2. API Principles

- REST for standard requests.
- WebSocket for realtime events.
- JSON request and response format.
- Pydantic validation.
- Versioned API endpoints.
- Authentication for protected endpoints.
- Consistent error responses.

## 3. Health

GET /health

Purpose:
Check backend availability.

## 4. Chat

POST /v1/chat

Request:
{
  "message": "Hello NEHA",
  "session_id": "session-id",
  "model_preference": "auto"
}

Response:
{
  "task_id": "task-id",
  "status": "completed",
  "response": "Hello! How can I help?"
}

## 5. Tasks

POST /v1/tasks
GET /v1/tasks/{task_id}
POST /v1/tasks/{task_id}/cancel

Purpose:
Create, inspect and cancel tasks.

## 6. Approvals

GET /v1/approvals
POST /v1/approvals/{approval_id}/decision

Purpose:
Review and approve or reject restricted actions.

Approval must be bound to the exact action,
target and task being authorized.

## 7. Memory

GET /v1/memory
POST /v1/memory
PATCH /v1/memory/{memory_id}
DELETE /v1/memory/{memory_id}

Purpose:
Review, create, update and delete permitted memories.

## 8. Agents

GET /v1/agents
GET /v1/agents/{agent_id}

Purpose:
Inspect registered agents and their status.

## 9. Skills

GET /v1/skills
POST /v1/skills
GET /v1/skills/{skill_id}
POST /v1/skills/{skill_id}/evaluate
POST /v1/skills/{skill_id}/disable

Purpose:
Manage candidate and validated skills.

New skills must pass evaluation and approval
before they can execute real tasks.

## 10. Models

GET /v1/models
GET /v1/models/status
POST /v1/models/select

Purpose:
Inspect available local and cloud models
and select an allowed model preference.

## 11. Devices

GET /v1/devices
POST /v1/devices/pair
POST /v1/devices/{device_id}/revoke

Purpose:
Pair, inspect and revoke connected devices.

## 12. Realtime Events

WebSocket:
/v1/events

Planned event types:
- task.created
- task.updated
- task.completed
- task.failed
- approval.required
- agent.started
- agent.completed
- device.connected
- device.disconnected

## 13. Standard Error Format

{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request",
    "request_id": "request-id"
  }
}

## 14. Security Requirements

- Authenticated access for protected routes.
- Input validation on every endpoint.
- Rate limiting where appropriate.
- Secure device pairing.
- Permission checks before tool execution.
- Audit logging for sensitive actions.
- No secrets in responses or logs.
- TLS for remote connections.

## 15. API Development Rules

- Keep request and response schemas documented.
- Use consistent HTTP status codes.
- Add automated tests for every endpoint.
- Support cancellation and task status reporting.
- Avoid exposing internal agent credentials.
- Keep backward compatibility where practical.

## 16. Implementation Status

This document defines the initial API contract.

Endpoints are planned, not yet implemented.
Request and response schemas may be refined
during implementation and testing.
