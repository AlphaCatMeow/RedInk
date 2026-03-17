# Contributing to RedInk

Thank you for your interest in contributing to RedInk! This guide will help you get started.

## Development Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- pnpm
- uv

### Getting Started

```bash
# Clone the repository
git clone https://github.com/HisMax/RedInk.git
cd RedInk

# Install backend dependencies
uv sync

# Install frontend dependencies
cd frontend
pnpm install

# Copy config templates
cd ..
cp text_providers.yaml.example text_providers.yaml
cp image_providers.yaml.example image_providers.yaml
```

### Running Locally

```bash
# Backend
uv run python -m backend.app

# Frontend (in another terminal)
cd frontend
pnpm dev
```

### Running Tests

```bash
# Backend tests
uv run pytest tests/ -v

# Frontend build check
cd frontend
pnpm build
```

## How to Contribute

### Reporting Bugs

Use the [Bug Report](https://github.com/HisMax/RedInk/issues/new?template=bug_report.yml) template. Include:

- Clear description and steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Deployment method (Docker / Local)

### Suggesting Features

Use the [Feature Request](https://github.com/HisMax/RedInk/issues/new?template=feature_request.yml) template.

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Ensure tests pass and frontend builds
5. Commit with a clear message
6. Push and open a Pull Request

### Commit Message Convention

```
type: brief description

Types: feat, fix, docs, refactor, test, chore
```

Examples:
- `feat: add image export as PDF`
- `fix: resolve API timeout on large outlines`
- `docs: update deployment instructions`

## Code Style

- **Python**: Follow PEP 8
- **TypeScript/Vue**: Follow existing project conventions
- **Commits**: Use conventional commit format

## Questions?

- Open a [GitHub Issue](https://github.com/HisMax/RedInk/issues)
- Email: histonemax@gmail.com
