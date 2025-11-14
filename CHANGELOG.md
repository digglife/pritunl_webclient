# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-01-08

### Added

- Initial release of pritunl-client
- Full support for Pritunl VPN API operations
- Authentication with automatic session management
- Server management (list, start, stop, status)
- Context manager support for automatic cleanup
- Comprehensive test suite with 100% coverage
- Type hints throughout the codebase
- Auto-reconnection on session expiry
- Modern packaging with pyproject.toml
- Support for Python 3.10+

### Features

- `PritunlClient` class for API interactions
- `login()` method for authentication
- `list_servers()` for server listing
- `start_server()` to start VPN servers
- `stop_server()` to stop VPN servers
- `check_server_status()` for status monitoring
- Custom exceptions for better error handling
- Decorator-based authentication enforcement

[Unreleased]: https://github.com/yourusername/pritunl-client/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/pritunl-client/releases/tag/v0.1.0
