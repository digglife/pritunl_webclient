# pritunl-client

[![PyPI version](https://badge.fury.io/py/pritunl-client.svg)](https://badge.fury.io/py/pritunl-client)
[![Python Versions](https://img.shields.io/pypi/pyversions/pritunl-client.svg)](https://pypi.org/project/pritunl-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/digglife/pritunl_client/workflows/tests/badge.svg)](https://github.com/digglife/pritunl_client/actions)
[![Coverage](https://codecov.io/gh/digglife/pritunl_client/branch/main/graph/badge.svg)](https://codecov.io/gh/digglife/pritunl_client)

A modern, fully-typed Python client for interacting with the Pritunl VPN API.

## Features

- 🚀 **Modern & Async-Ready**: Built with `httpx` for both sync usage
- 🔒 **Type-Safe**: Fully typed with comprehensive type hints
- ✅ **Well-Tested**: 100% test coverage with 36+ unit tests
- 🎯 **Simple API**: Clean, intuitive interface
- 🔄 **Auto-Reconnection**: Automatic session management and re-authentication
- 📦 **Zero Config**: Works out of the box with sensible defaults

## Installation

### Using uv (recommended)

```bash
uv pip install pritunl-client
```

### Using pip

```bash
pip install pritunl-client
```

### From source

```bash
git clone https://github.com/digglife/pritunl_client.git
cd pritunl_client
uv pip install -e .
```

## Quick Start

```python
from pritunl_client import PritunlClient

# Create a client instance
client = PritunlClient("https://vpn.example.com", verify=False)

# Login
client.login("admin", "password")

# List servers
servers = client.list_servers()
print(servers)

# Start a server
server_id = "5fefecb610135c15af1b472b"
result = client.start_server(server_id)

# Check server status
status = client.check_server_status(server_id)
print(status)

# Stop a server
client.stop_server(server_id)

# Always close when done
client.close()
```

### Using as a Context Manager

```python
from pritunl_client import PritunlClient

with PritunlClient("https://vpn.example.com", verify=False) as client:
    client.login("admin", "password")
    servers = client.list_servers()
    print(servers)
# Client automatically closes
```

## API Reference

### PritunlClient

#### `__init__(base_url: str, verify: bool = True, timeout: int = 10)`

Create a new Pritunl client.

**Parameters:**

- `base_url`: Base URL of the Pritunl web UI (e.g., `https://vpn.example.com`)
- `verify`: Whether to verify TLS certificates. Set to `False` for self-signed certificates
- `timeout`: Request timeout in seconds (default: 10)

#### `login(username: str, password: str) -> None`

Authenticate with the Pritunl server.

**Parameters:**

- `username`: Admin username
- `password`: Admin password

**Raises:**

- `AuthenticationError`: If login fails

#### `list_servers(page: int = 0) -> List[Dict[str, Any]]`

List all servers.

**Parameters:**

- `page`: Page number for pagination (default: 0)

**Returns:**

- List of server dictionaries

**Raises:**

- `NotAuthenticated`: If not logged in
- `PritunlError`: If request fails

#### `start_server(server_id: str, server_obj: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`

Start a server.

**Parameters:**

- `server_id`: Server ID to start
- `server_obj`: Optional server object. If not provided, will be fetched automatically

**Returns:**

- Server response dictionary

**Raises:**

- `NotAuthenticated`: If not logged in
- `ServerNotFound`: If server doesn't exist
- `PritunlError`: If operation fails

#### `stop_server(server_id: str, server_obj: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`

Stop a server.

**Parameters:**

- `server_id`: Server ID to stop
- `server_obj`: Optional server object. If not provided, will be fetched automatically

**Returns:**

- Server response dictionary

**Raises:**

- `NotAuthenticated`: If not logged in
- `ServerNotFound`: If server doesn't exist
- `PritunlError`: If operation fails

#### `check_server_status(server_id: str) -> List[Dict[str, Any]]`

Check server host status.

**Parameters:**

- `server_id`: Server ID to check

**Returns:**

- List of host status dictionaries

**Raises:**

- `NotAuthenticated`: If not logged in
- `PritunlError`: If request fails

#### `close() -> None`

Close the HTTP client connection.

## Exceptions

- `PritunlError`: Base exception for all Pritunl errors
- `AuthenticationError`: Raised when authentication fails
- `NotAuthenticated`: Raised when an operation requires authentication
- `ServerNotFound`: Raised when a server is not found

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pritunl-client.git
cd pritunl-client

# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pritunl_client

# Run with verbose output
pytest -vv

# Run specific test file
pytest tests/test_client.py
```

### Linting and Type Checking

```bash
# Run ruff linter
ruff check src tests

# Run ruff formatter
ruff format src tests

# Run type checker
mypy src
```

### Building

```bash
# Build distribution packages
uv build

# This creates:
# - dist/pritunl_client-*.whl
# - dist/pritunl_client-*.tar.gz
```

## Notes

- If your Pritunl server uses a self-signed certificate, set `verify=False` when creating the client
- The client automatically manages session cookies and CSRF tokens
- Credentials are stored in memory for auto-reconnection on session expiry
- All operations require authentication via `login()` first

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [httpx](https://www.python-httpx.org/)
- Tested with [pytest](https://pytest.org/)
- Type hints validated with [mypy](https://mypy.readthedocs.io/)

## Links

- **Documentation**: [GitHub README](https://github.com/yourusername/pritunl-client#readme)
- **Source Code**: [GitHub](https://github.com/yourusername/pritunl-client)
- **Issue Tracker**: [GitHub Issues](https://github.com/yourusername/pritunl-client/issues)
- **PyPI**: [pritunl-client](https://pypi.org/project/pritunl-client/)
