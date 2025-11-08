# Quick Test Commands

## Setup (one-time)

```bash
# Install package in development mode
pip install -e .

# Or install with dev dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest tests/test_client.py -v

# Run with coverage
pytest --cov=pritunl_client tests/test_client.py

# Run with coverage and show missing lines
pytest --cov=pritunl_client tests/test_client.py --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=pritunl_client tests/test_client.py --cov-report=html
# Then open htmlcov/index.html in your browser

# Run specific test class
pytest tests/test_client.py::TestLogin -v

# Run specific test
pytest tests/test_client.py::TestLogin::test_login_success -v

# Run with verbose output
pytest tests/test_client.py -vv

# Run with stdout/stderr shown
pytest tests/test_client.py -s
```

## Coverage Results

Current coverage: **100%** ✅

- `pritunl_client/__init__.py` - 100%
- `pritunl_client/client.py` - 100%
- `pritunl_client/exceptions.py` - 100%

All 36 tests passing!
