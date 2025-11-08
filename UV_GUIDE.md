# Quick Start with uv

This guide shows you how to work with this project using **uv**, the modern, fast Python package manager.

## What is uv?

uv is a blazingly fast Python package installer and resolver, written in Rust. It's:

- 10-100x faster than pip
- Drop-in replacement for pip and pip-tools
- Handles virtual environments
- Builds packages

## Installation

### Install uv

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**With pip:**

```bash
pip install uv
```

**With Homebrew:**

```bash
brew install uv
```

## Basic Workflow

### 1. Create Virtual Environment

```bash
# Create a virtual environment
uv venv

# Activate it
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 2. Install the Package

**Development mode (editable install):**

```bash
uv pip install -e ".[dev]"
```

**Production mode:**

```bash
uv pip install .
```

**Just the package (no dev dependencies):**

```bash
uv pip install -e .
```

### 3. Common Commands

```bash
# Install dependencies
uv pip install httpx pytest ruff

# Install from requirements
uv pip install -r requirements.txt

# Freeze dependencies
uv pip freeze

# Sync dependencies (install exactly what's in lock file)
uv pip sync requirements.txt

# Uninstall package
uv pip uninstall package-name

# List installed packages
uv pip list

# Show package info
uv pip show package-name
```

## Development Workflow

### Full Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd pritunl-client

# 2. Create and activate venv
uv venv
source .venv/bin/activate

# 3. Install in development mode with all dev dependencies
uv pip install -e ".[dev]"

# 4. Run tests
pytest

# 5. Run linter
ruff check src tests

# 6. Format code
ruff format src tests

# 7. Run type checker
mypy src
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pritunl_client

# Run specific test
pytest tests/test_client.py::TestLogin

# Run in verbose mode
pytest -vv

# Run with output
pytest -s
```

### Code Quality

```bash
# Lint
ruff check src tests

# Auto-fix linting issues
ruff check --fix src tests

# Format code
ruff format src tests

# Check formatting (no changes)
ruff format --check src tests

# Type check
mypy src
```

### Building

```bash
# Build wheel and source distribution
uv build

# Output:
# ✓ Built dist/pritunl_client-0.1.0-py3-none-any.whl
# ✓ Built dist/pritunl_client-0.1.0.tar.gz
```

## Comparison: uv vs pip

| Task              | pip                               | uv                                   |
| ----------------- | --------------------------------- | ------------------------------------ |
| Install package   | `pip install package`             | `uv pip install package`             |
| Install editable  | `pip install -e .`                | `uv pip install -e .`                |
| Install from file | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| Freeze            | `pip freeze > requirements.txt`   | `uv pip freeze > requirements.txt`   |
| Uninstall         | `pip uninstall package`           | `uv pip uninstall package`           |
| Create venv       | `python -m venv .venv`            | `uv venv`                            |
| **Speed**         | Slow                              | **10-100x faster** ⚡                |

## Advantages of uv

### 1. Speed

```bash
# pip: ~30 seconds
time pip install pandas numpy scipy

# uv: ~3 seconds
time uv pip install pandas numpy scipy
```

### 2. Better Dependency Resolution

```bash
# uv has smarter conflict resolution
# Shows conflicts clearly
# Resolves faster
uv pip install conflicting-package-a conflicting-package-b
```

### 3. Built-in Virtual Environment

```bash
# Create venv with uv
uv venv

# No need for python -m venv
# Automatically finds the right Python version
```

### 4. Faster CI/CD

```yaml
# In GitHub Actions, uv is much faster:
- name: Install dependencies
  run: |
    uv venv
    uv pip install -e ".[dev]"
  # ⚡ Saves minutes on every CI run
```

## Advanced Usage

### Pin Python Version

```bash
# Create venv with specific Python
uv venv --python 3.11

# Or use pyenv Python
uv venv --python ~/.pyenv/versions/3.11.0/bin/python
```

### Compile Requirements

```bash
# Create requirements.txt with pinned versions
uv pip compile pyproject.toml -o requirements.txt

# Create dev requirements
uv pip compile pyproject.toml --extra dev -o requirements-dev.txt
```

### Cache Management

```bash
# uv caches packages for faster installs

# Clear cache
uv cache clean

# Show cache info
uv cache dir
```

## Migrating from pip

If you're used to pip, just prefix commands with `uv`:

```bash
pip install package          → uv pip install package
pip install -e .             → uv pip install -e .
pip freeze                   → uv pip freeze
pip list                     → uv pip list
pip uninstall package        → uv pip uninstall package
```

## Troubleshooting

### "No virtual environment found"

```bash
# Create one first:
uv venv

# Then activate:
source .venv/bin/activate
```

### "Package not found"

```bash
# Update package index:
uv pip install --upgrade package-name

# Or use --index-url for custom PyPI:
uv pip install package-name --index-url https://custom.pypi.org/simple
```

### Python version conflicts

```bash
# Specify Python version:
uv venv --python 3.11

# Or set in environment:
export UV_PYTHON=3.11
```

## Tips & Tricks

1. **Use in CI/CD**: uv is much faster for CI pipelines
2. **Cache benefits**: uv automatically caches downloads
3. **Parallel installs**: uv installs packages in parallel
4. **Better errors**: Clear, actionable error messages
5. **No compile needed**: Works with pre-built wheels

## Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [uv Install Guide](https://github.com/astral-sh/uv#getting-started)
- [uv vs pip](https://github.com/astral-sh/uv#benchmarks)

## Need Help?

- Check [uv GitHub Issues](https://github.com/astral-sh/uv/issues)
- Read the [uv Guide](https://github.com/astral-sh/uv/blob/main/README.md)
- Join [uv Discussions](https://github.com/astral-sh/uv/discussions)
