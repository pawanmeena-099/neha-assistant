
# NEHA — Database Data Model

Version: 1.0
Status: Initial Database Design

## 1. Overview

NEHA uses structured storage for:
- Users and devices
- Conversations and messages
- Tasks and execution history
- Agents and skills
- Permissions and approvals
- Long-term memory
- Audit events

Primary database: PostgreSQL
Local cache: SQLite
Optional semantic search: pgvector

## 2. Main Entities

### 2.1 Users
Stores account information.

Fields:
- id (UUID, primary key)
- email
- display_name
- created_at
- updated_at

### 2.2 Devices
Stores paired devices.

Fields:
- id (UUID, primary key)
- user_id (foreign key)
- device_name
- platform
- device_status
- paired_at
- last_seen_at
- revoked_at

### 2.3 Sessions
Stores conversation sessions.

Fields:
- id (UUID, primary key)
- user_id (foreign key)
- device_id (foreign key, optional)
- title
- created_at
- updated_at

### 2.4 Messages
Stores conversation messages.

Fields:
- id (UUID, primary key)
- session_id (foreign key)
- role
- content
- model_provider
- created_at

Sensitive content must follow the data retention
and privacy policy.

### 2.5 Tasks
Stores task execution information.

Fields:
- id (UUID, primary key)
- user_id (foreign key)
- session_id (foreign key, optional)
- task_type
- description
- status
- risk_level
- created_at
- started_at
- completed_at

### 2.6 Agents
Stores registered agent definitions.

Fields:
- id (UUID, primary key)
- name
- description
- agent_type
- version
- status
- created_at

### 2.7 Skills
Stores reusable skill definitions.

Fields:
- id (UUID, primary key)
- name
- description
- version
- status
- permission_scope
- created_at
- updated_at

### 2.8 Approvals
Stores user approval decisions.

Fields:
- id (UUID, primary key)
- task_id (foreign key)
- user_id (foreign key)
- action_description
- target_resource
- decision
- created_at
- expires_at

Approval must authorize only the exact
action and target presented to the user.

### 2.9 Memories
Stores user-approved long-term information.

Fields:
- id (UUID, primary key)
- user_id (foreign key)
- memory_type
- content
- source_reference
- confidence
- created_at
- updated_at

Memory categories:
- Profile
- Project
- Episodic
- Procedural

Sensitive information and secrets must not
be stored by default.

### 2.10 Audit Events
Stores security-relevant activity.

Fields:
- id (UUID, primary key)
- user_id (foreign key, optional)
- task_id (foreign key, optional)
- actor_type
- action
- resource
- result
- timestamp

Never store passwords, API keys or tokens
in audit events.

## 3. Relationships

- One user can have multiple devices.
- One user can have multiple sessions.
- One session can have multiple messages.
- One user can create multiple tasks.
- One task can involve multiple agents.
- One task can require multiple approval records.
- One user can have multiple memories.
- One user can have multiple paired devices.

## 4. Data Integrity

- Use UUID identifiers.
- Use foreign key constraints.
- Use database transactions.
- Validate data before storage.
- Define indexes for frequently queried fields.
- Use migrations for schema changes.
- Use UTC timestamps internally.

## 5. Privacy and Retention

- Collect minimum necessary data.
- Separate temporary context from long-term memory.
- Support memory review and deletion.
- Define conversation retention settings.
- Protect database backups.
- Do not store credentials in database records.

## 6. Database Security

- Use parameterized queries or a safe ORM.
- Apply access controls.
- Use encrypted connections for remote databases.
- Restrict database credentials.
- Never expose database credentials to AI agents.
- Maintain backup and recovery procedures.

## 7. Future Extensions

Potential future tables:
- Agent executions
- Tool executions
- Model usage
- Evaluation results
- Skill versions
- Notifications
- Scheduled tasks
- Integration connections

These will be added only when required.

## 8. Implementation Status

This is the initial logical data model.

No database tables have been created yet.
Physical schema and migrations will be
implemented and tested during development.
