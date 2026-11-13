
# NEHA — Development Environment Setup

Version: 1.0
Status: Preparation Checklist

## 1. Development Platforms

Primary development:
- macOS (Apple Silicon MacBook)

Current preparation:
- Windows PC

Testing:
- Android device

Future targets:
- Windows
- macOS
- Linux
- Android

## 2. Required Tools

### Core Development
- [ ] Visual Studio Code
- [ ] Git
- [ ] Python
- [ ] Node.js LTS
- [ ] npm
- [ ] GitHub access

### Backend
- [ ] Python virtual environment
- [ ] FastAPI
- [ ] Uvicorn
- [ ] Pydantic
- [ ] Pytest

### AI
- [ ] Ollama
- [ ] Local model download
- [ ] Cloud AI provider configuration
- [ ] Model router

### Frontend
- [ ] React
- [ ] TypeScript
- [ ] Tauri
- [ ] Tailwind CSS

### Database
- [ ] PostgreSQL
- [ ] SQLite
- [ ] Database migration tool

### Android
- [ ] Android Studio
- [ ] Android SDK
- [ ] Kotlin
- [ ] Jetpack Compose

### Quality and Security
- [ ] GitHub Actions
- [ ] Automated tests
- [ ] Secret scanning
- [ ] Dependency checks
- [ ] Backup verification

## 3. First Development Environment

Initial setup will create:

- NEHA repository clone
- Backend development environment
- Frontend development environment
- Test environment
- Local database
- Environment configuration

## 4. Environment Variables

Create a local .env file when implementation
begins.

Never commit real secrets.

Use .env.example for safe placeholders.

## 5. Development Rules

- Use stable, supported software versions.
- Pin project dependencies.
- Keep environments isolated.
- Document installation commands.
- Run tests before every milestone commit.
- Back up working code to GitHub.
- Never place API keys in source files.

## 6. MacBook Arrival Checklist

- [ ] Confirm chip, RAM and storage.
- [ ] Update macOS.
- [ ] Install development tools.
- [ ] Configure Git and SSH.
- [ ] Clone NEHA repository.
- [ ] Create Python environment.
- [ ] Install backend dependencies.
- [ ] Install frontend dependencies.
- [ ] Configure local AI.
- [ ] Run first backend health test.
- [ ] Verify GitHub push and pull.

## 7. Windows Preparation

The Windows PC can be used for:
- Documentation
- Architecture planning
- GitHub management
- Requirements review
- Lightweight coding if desired

Platform-specific setup will be documented
separately.

## 8. Completion Criteria

The development environment is ready when:
- Repository clones successfully.
- Backend starts locally.
- Frontend starts locally.
- Automated tests execute.
- No secrets are exposed.
- Changes can be committed and pushed.
