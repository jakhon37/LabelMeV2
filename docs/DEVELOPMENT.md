# Development Guide

This guide covers setting up your development environment and contributing to labelme.

## Table of Contents

- [Environment Setup](#environment-setup)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [Documentation](#documentation)
- [Release Process](#release-process)

## Environment Setup

### Prerequisites

- Python 3.10+ (3.10, 3.11, 3.12, 3.13 supported)
- Git
- (Optional) uv for faster dependency management

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/labelme.git
cd labelme

# Option 1: Using uv (recommended - faster)
uv sync

# Option 2: Using pip
pip install -e ".[dev]"
# Note: If the above fails, install dependencies manually:
pip install -e .
pip install pytest pytest-qt ruff pyqt5-stubs

# Install pre-commit hooks
pip install pre-commit
pre-commit install
```

### Verify Installation

```bash
# Check if labelme is installed
labelme --version

# Run tests to verify setup
pytest

# Check code quality
ruff check .
ruff format --check .
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Follow the coding guidelines in [CONTRIBUTING.md](../CONTRIBUTING.md).

### 3. Test Your Changes

```bash
# Run specific tests
pytest tests/unit/shape_test.py -v

# Run all tests
make test

# Run tests with coverage
pytest --cov=labelme --cov-report=html
# Open htmlcov/index.html to view coverage report
```

### 4. Check Code Quality

```bash
# Format code
make format

# Check linting
make lint

# Or manually
ruff format .
ruff check .
```

### 5. Commit Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commit format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `chore:` - Maintenance tasks

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Testing

### Test Structure

```
tests/
├── unit/              # Unit tests (fast, isolated)
│   ├── config_test.py
│   ├── utils/
│   └── widgets/
└── e2e/               # End-to-end tests (GUI)
    ├── annotation_test.py
    ├── config_test.py
    └── smoke_test.py
```

### Running Tests

```bash
# All tests
pytest

# Unit tests only
pytest tests/unit/

# E2E tests only
pytest tests/e2e/

# GUI tests (requires display)
pytest -m gui

# Specific test
pytest tests/unit/shape_test.py::test_shapes_to_label -v

# With coverage
pytest --cov=labelme --cov-report=term-missing
```

### Writing Tests

#### Unit Test Example

```python
from labelme.shape import Shape

def test_shape_creation():
    shape = Shape("polygon")
    assert shape.shape_type == "polygon"
    assert len(shape.points) == 0
```

#### GUI Test Example

```python
import pytest
from pytestqt.qtbot import QtBot
import labelme.app

@pytest.mark.gui
def test_main_window(qtbot: QtBot):
    win = labelme.app.MainWindow()
    qtbot.addWidget(win)
    win.show()
    assert win.isVisible()
    win.close()
```

## Code Quality

### Linting

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting.

```bash
# Check for issues
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code
ruff format .
```

### Pre-commit Hooks

Pre-commit hooks automatically run checks before each commit:

```bash
# Install hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

### Type Checking

```bash
# Type check with mypy (via ty)
uv run ty check --no-progress

# Or with mypy directly
mypy labelme --ignore-missing-imports
```

## Documentation

### Updating Documentation

1. **README.md**: Main documentation and feature showcase
2. **CONTRIBUTING.md**: Contribution guidelines
3. **docs/**: Detailed guides and references
4. **Docstrings**: Google-style docstrings in code

### Building Documentation

```python
# Example Google-style docstring
def merge_shapes(shapes: list["Shape"]) -> list["Shape"] | None:
    """Merge multiple shapes using geometric union.
    
    Args:
        shapes: List of Shape objects to merge
        
    Returns:
        List of merged Shape objects, or None if merge fails
        
    Example:
        >>> merged = Shape.mergeShapes([shape1, shape2])
    """
```

## Release Process

### Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Creating a Release

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Commit changes: `git commit -m "chore: release v0.1.0"`
4. Tag: `git tag v0.1.0`
5. Push: `git push && git push --tags`
6. GitHub Actions will build and publish

## Debugging

### Enable Debug Logging

```bash
labelme --logger-level debug
```

Or in config file (`~/.labelmerc`):

```yaml
logger_level: debug
```

### Qt Debugging

```python
from loguru import logger

logger.debug(f"Shape points: {shape.points}")
logger.info("File loaded successfully")
logger.warning("Unexpected state")
logger.error("Failed to save file")
```

### GUI Issues

- Use `qtbot` fixtures in tests
- Run with `QT_DEBUG_PLUGINS=1` for Qt debugging
- Check event loop issues with `qtbot.waitSignal()`

## Common Tasks

### Adding a New Feature

1. Update `labelme/shape.py` or relevant module
2. Add UI action in `labelme/app.py`
3. Update `labelme/config/default_config.yaml`
4. Write tests
5. Update documentation

### Fixing a Bug

1. Write a failing test
2. Fix the bug
3. Verify test passes
4. Add regression test if needed

### Performance Optimization

1. Profile code: `python -m cProfile labelme`
2. Identify bottlenecks
3. Optimize critical paths
4. Add performance tests
5. Document changes

## Resources

- [Qt5 Documentation](https://doc.qt.io/qt-5/)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Shapely Documentation](https://shapely.readthedocs.io/)
- [pytest-qt Documentation](https://pytest-qt.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

## Getting Help

- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Ask questions and share ideas
- **Discord**: Real-time community support
- **Stack Overflow**: Tag questions with `labelme`

---

**Happy coding!** 🚀
