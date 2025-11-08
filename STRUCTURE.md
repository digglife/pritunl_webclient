# Project Structure

This document describes the modern Python library structure of pritunl-client.

## Directory Layout

```
pritunl-client/
├── .github/
│   └── workflows/
│       └── tests.yml          # CI/CD pipeline with GitHub Actions
├── .venv/                      # Virtual environment (not in git)
├── dist/                       # Built packages (not in git)
├── htmlcov/                    # Coverage HTML reports (not in git)
├── src/
│   └── pritunl_client/        # Main package (src layout)
│       ├── __init__.py        # Package initialization & exports
│       ├── client.py          # Main PritunlClient class
│       ├── exceptions.py      # Custom exceptions
│       └── py.typed           # PEP 561 type marker
├── tests/
│   ├── __init__.py
│   ├── test_client.py         # Comprehensive test suite
│   └── README.md              # Test documentation
├── .gitignore                 # Git ignore patterns
├── CHANGELOG.md               # Version history
├── CONTRIBUTING.md            # Contributing guidelines
├── LICENSE                    # MIT License
├── MANIFEST.in                # Package data files
├── README.md                  # Main documentation
├── TESTING.md                 # Testing guide
├── pyproject.toml             # Modern Python project configuration
└── pytest.ini                 # Pytest configuration

## Old files (can be removed):
├── pritunl_client/            # Old package location
├── pritunl_client.egg-info/   # Old build artifacts
├── requirements.txt           # Replaced by pyproject.toml
└── pritunl-requests.md        # Project notes
```

## Key Design Decisions

### 1. Src Layout

We use the **src layout** (package in `src/` directory) instead of flat layout because:

- ✅ Prevents accidental imports from the source tree during development
- ✅ Forces proper package installation for testing
- ✅ Cleaner separation between source code and other files
- ✅ Industry best practice for modern Python projects

### 2. Build System: Hatchling

- Modern, standards-compliant build backend
- Faster than setuptools
- Better defaults
- No need for setup.py

### 3. Dependency Management: uv

- **Fast**: Written in Rust, 10-100x faster than pip
- **Modern**: Uses modern Python packaging standards
- **Reliable**: Deterministic dependency resolution
- **Simple**: Single tool for venv, pip, and build

### 4. Tooling

| Tool           | Purpose              | Why?                                 |
| -------------- | -------------------- | ------------------------------------ |
| **pytest**     | Testing framework    | Industry standard, powerful fixtures |
| **pytest-cov** | Coverage reporting   | Integrated coverage with pytest      |
| **respx**      | HTTP mocking         | Clean API mocking for httpx          |
| **ruff**       | Linting & formatting | Extremely fast, replaces 10+ tools   |
| **mypy**       | Type checking        | Catches type errors before runtime   |

### 5. Configuration in pyproject.toml

All tool configuration in one file:

- Project metadata
- Dependencies
- Build system
- pytest settings
- coverage settings
- ruff settings
- mypy settings

### 6. Type Hints & py.typed

- Full type annotations throughout
- `py.typed` marker for PEP 561 compliance
- Better IDE support and error detection

## Package Distribution

The package is distributed as:

1. **Wheel** (.whl): Binary distribution

   - Fast installation
   - No build step needed
   - `pritunl_client-0.1.0-py3-none-any.whl`

2. **Source Distribution** (.tar.gz): Source code archive
   - For platforms needing custom builds
   - Includes all source files
   - `pritunl_client-0.1.0.tar.gz`

## Development Workflow

### Initial Setup

```bash
git clone <repo>
cd pritunl-client
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Daily Workflow

```bash
# Make changes to code

# Run tests
pytest

# Check types
mypy src

# Lint and format
ruff check src tests
ruff format src tests

# Build
uv build
```

## Publishing Workflow

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Run all tests and checks
4. Build: `uv build`
5. Publish to PyPI: `uv publish` or `twine upload dist/*`

## CI/CD

GitHub Actions workflow (`.github/workflows/tests.yml`):

- Runs on multiple OS (Ubuntu, macOS, Windows)
- Tests Python 3.8-3.13
- Runs linting, type checking, and tests
- Generates coverage reports
- Uploads to Codecov

## Migration from Old Structure

Files to remove:

- `pritunl_client/` (old package location)
- `pritunl_client.egg-info/` (old build artifacts)
- `requirements.txt` (replaced by pyproject.toml dependencies)

Files to keep:

- `tests/` (tests work with new structure)
- Documentation files (README, etc.)

## Best Practices Followed

✅ PEP 517/518 - Modern build system
✅ PEP 621 - Project metadata in pyproject.toml
✅ PEP 561 - Type hints (py.typed)
✅ PEP 440 - Version identification
✅ Semantic Versioning
✅ Keep a Changelog format
✅ Conventional Commits
✅ 100% test coverage
✅ Type hints throughout
✅ Modern tooling (uv, ruff, mypy)
✅ Comprehensive documentation
✅ MIT License
✅ GitHub Actions CI/CD

## Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Modern Python packaging](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
