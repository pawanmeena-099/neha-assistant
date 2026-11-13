
# NEHA — Acceptance Test Plan

Version: 1.0
Status: Initial Test Specification

## 1. Purpose

Define measurable tests for NEHA features.

A feature is complete only when its acceptance
tests pass on the supported target platform.

## 2. Test Status

- NOT_STARTED
- IN_PROGRESS
- PASSED
- FAILED
- BLOCKED

Never mark an untested feature as PASSED.

## 3. Core Chat Tests

### CHAT-001: Basic Chat
- Send a text message.
- Receive a valid AI response.
- Display the response in the UI.
- Verify error handling.

Expected: Conversation completes successfully.

### CHAT-002: Invalid Input
- Submit empty or invalid input.
- Validate the request.

Expected: Invalid input is rejected safely.

### CHAT-003: Cancellation
- Start a long-running request.
- Cancel the task.

Expected: Task stops or reports that cancellation
is not supported by the current operation.

## 4. Hybrid AI Tests

### AI-001: Local Model
- Configure a supported local model.
- Send a test prompt.

Expected: Response comes from local inference.

### AI-002: Cloud Model
- Configure an approved cloud provider.
- Send a test prompt.

Expected: Response comes from the selected provider.

### AI-003: Local-only Privacy
- Mark a task as local-only.
- Simulate cloud routing.

Expected: Cloud request is blocked.

### AI-004: Provider Failure
- Simulate a provider timeout.

Expected: Clear error or approved fallback.

## 5. Memory Tests

### MEM-001: Store Memory
Expected: Approved memory is stored correctly.

### MEM-002: Retrieve Memory
Expected: Relevant stored information is retrieved.

### MEM-003: Correct Memory
Expected: Updated information replaces the old value.

### MEM-004: Delete Memory
Expected: Deleted memory is no longer retrievable.

### MEM-005: Secret Protection
Expected: Secrets are not automatically saved as memory.

## 6. Permission Tests

### SEC-001: Unauthorized Tool
Expected: Tool execution is blocked.

### SEC-002: Approval Required
Expected: Restricted action waits for user approval.

### SEC-003: Approval Mismatch
Expected: Approval for one action cannot authorize
a different action or target.

### SEC-004: Revoked Device
Expected: Revoked device cannot execute tasks.

### SEC-005: Secret Leakage
Expected: API keys and passwords do not appear
in source code, logs or responses.

## 7. File and OS Tests

### OS-001: Approved Folder Read
Expected: Files inside approved folders can be read.

### OS-002: Unauthorized Folder
Expected: Access outside permitted folders is blocked.

### OS-003: Sandbox Write
Expected: File creation is limited to the sandbox.

### OS-004: Path Traversal
Expected: Attempts to escape the sandbox are blocked.

### OS-005: Destructive Action
Expected: Deletion requires explicit approval.

## 8. Coding Agent Tests

### CODE-001: Repository Inspection
Expected: Correct repository structure is reported.

### CODE-002: Isolated Changes
Expected: Changes happen in an isolated worktree.

### CODE-003: Automated Testing
Expected: Relevant tests execute and results are reported.

### CODE-004: Git Diff Review
Expected: Modified files and changes are visible.

### CODE-005: Protected Branch
Expected: Agent cannot directly modify protected branches.

## 9. Multi-Agent Tests

### AGENT-001: Agent Registration
Expected: Only registered agents are available.

### AGENT-002: Agent Permissions
Expected: Agents cannot exceed their assigned scopes.

### AGENT-003: Agent Handoff
Expected: Task information passes correctly between agents.

### AGENT-004: Agent Failure
Expected: Failure is reported and task state remains consistent.

## 10. Learning Engine Tests

### LEARN-001: Skill Draft
Expected: Candidate skill is generated in isolation.

### LEARN-002: Skill Evaluation
Expected: Tests run before registration.

### LEARN-003: Skill Approval
Expected: Unapproved skill cannot perform real actions.

### LEARN-004: Skill Rollback
Expected: Previous stable skill version can be restored.

## 11. Voice and Vision Tests

### VV-001: Microphone Permission
Expected: Voice capture requires permission.

### VV-002: Recording Indicator
Expected: Recording state is visible to the user.

### VV-003: Image Permission
Expected: Image and camera access follow explicit permissions.

### VV-004: Privacy
Expected: Audio and images follow configured retention rules.

## 12. Android Tests

### AND-001: Device Pairing
Expected: Authorized device pairs successfully.

### AND-002: Device Revocation
Expected: Revoked device loses access.

### AND-003: Notifications
Expected: Task notifications display correct status.

### AND-004: Approval
Expected: User can review and decide pending approvals.

## 13. Reliability Tests

### REL-001: Network Failure
Expected: Clear failure state and safe recovery.

### REL-002: Retry Limit
Expected: Retries remain within configured limits.

### REL-003: Backup Restore
Expected: A valid backup can be restored.

### REL-004: Audit Trail
Expected: Security-relevant actions are recorded.

## 14. Test Evidence

For every test, record:

- Test ID
- Build/version
- Platform
- Test date
- Steps performed
- Expected result
- Actual result
- PASS / FAIL / BLOCKED
- Evidence or log reference

## 15. Release Gate

NEHA cannot be released unless:

- Critical tests pass.
- Security tests pass.
- No unresolved critical security issues remain.
- Backup and recovery are verified.
- Known limitations are documented.
- Release version is recorded.

## 16. Current Test Status

Test execution: NOT_STARTED

Reason: Implementation has not started.

This document defines tests, not test results.
