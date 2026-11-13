
# NEHA — Technology Stack

Version: 1.0
Status: Proposed Baseline

## 1. Backend
- Language: Python
- Framework: FastAPI
- API format: REST
- Realtime communication: WebSocket
- Validation: Pydantic
- Testing: Pytest

## 2. AI Infrastructure

### Local AI
- Ollama
- Configurable open-source models
- Initial model candidates: Qwen family

### Cloud AI
- Provider-independent AI adapter
- Configurable cloud model providers
- Usage and cost tracking
- Fallback and timeout handling

## 3. Model Router
- Task classification
- Local/cloud selection
- Privacy-aware routing
- Cost-aware routing
- Provider fallback

## 4. Desktop Application
- Framework: Tauri
- Frontend: React
- Language: TypeScript
- Styling: Tailwind CSS

## 5. Android Application
- Language: Kotlin
- UI: Jetpack Compose
- Networking: HTTPS API
- Notifications: Android-supported services

## 6. Database and Storage
- Main database: PostgreSQL
- Semantic search: pgvector when required
- Local cache: SQLite
- File storage: User-controlled storage

## 7. Background Processing
- Initial implementation: Python background tasks
- Future queue: Redis
- Future workers: Separate worker process

## 8. Development Tools
- VS Code
- Git
- GitHub
- Docker
- Python virtual environment
- Automated testing and CI

## 9. Hosting
- Initial development: Local machine
- Optional cloud backend: Railway
- Local model inference: User's own device
- Secrets: Secure environment/OS storage

## 10. Security
- Authentication and session management
- Permission engine
- Sandboxed execution
- Approval workflow
- Audit logging
- Backup and recovery

## 11. Engineering Principles
- Modular monolith initially
- Provider-independent model integration
- Platform-specific device adapters
- Automated tests for critical features
- Version-controlled configuration
- No secrets in source control

## 12. Hardware Validation

Final local model selection and performance
targets will be decided after benchmarking
on the actual MacBook hardware.

## 13. Change Policy

Technology changes must be documented
with their reason, impact and migration plan.
