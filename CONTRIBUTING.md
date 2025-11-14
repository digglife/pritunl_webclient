# Contributing to pritunl-client

Thank you for your interest in contributing to pritunl-client! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Setting Up Your Development Environment

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/yourusername/pritunl-client.git
   cd pritunl-client
   ```

2. **Install uv** (if not already installed)

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create a virtual environment and install dependencies**

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev]"
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pritunl_webclient

# Run specific test file
pytest tests/test_client.py

# Run specific test
pytest tests/test_client.py::TestLogin::test_login_success
```

### Code Quality

We use several tools to maintain code quality:

#### Linting with Ruff

```bash
# Check for issues
ruff check src tests

# Auto-fix issues
ruff check --fix src tests

# Format code
ruff format src tests
```

#### Type Checking with Mypy

```bash
mypy src
```

### Before Submitting

Before submitting a pull request, make sure to:

1. **Run all tests**

   ```bash
   pytest
   ```

2. **Check code formatting**

   ```bash
   ruff format --check src tests
   ```

3. **Run linter**

   ```bash
   ruff check src tests
   ```

4. **Run type checker**

   ```bash
   mypy src
   ```

5. **Ensure 100% test coverage**
   ```bash
   pytest --cov=pritunl_webclient --cov-report=term-missing
   ```

## Pull Request Process

1. **Create a new branch** for your feature or bugfix

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for any new functionality

4. **Update documentation** if needed (README.md, docstrings, etc.)

5. **Update CHANGELOG.md** under the "Unreleased" section

6. **Commit your changes** with clear, descriptive commit messages

   ```bash
   git commit -m "Add feature: description of your changes"
   ```

7. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub

## Code Style Guidelines

### Python Style

- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Maximum line length: 120 characters
- Use descriptive variable names
- Add docstrings to all public methods and classes

### Docstring Format

We use Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> bool:
    """Brief description of the function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: Description of when this is raised
    """
    pass
```

### Testing Guidelines

- Write tests for all new features
- Maintain or improve code coverage (target: 100%)
- Use descriptive test names
- Use fixtures for common test setup
- Mock external dependencies (HTTP calls, etc.)

Example:

```python
def test_login_success(self, client, base_url):
    """Test successful login with valid credentials."""
    # Arrange
    # ... setup

    # Act
    client.login("user", "pass")

    # Assert
    assert client._username == "user"
```

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- pritunl-client version
- Minimal code example that reproduces the issue
- Expected behavior
- Actual behavior
- Any error messages or stack traces

## Feature Requests

We welcome feature requests! Please:

1. Check if the feature has already been requested
2. Clearly describe the feature and its use case
3. Explain why this feature would be useful to other users
4. Provide examples of how the feature would be used

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the "question" label
- Start a discussion on GitHub Discussions

## License

By contributing to pritunl-client, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
