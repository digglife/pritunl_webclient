# pritunl-webclient — AGENTS.md

Single-package Python library (`src/pritunl_webclient/`) with a bundled CLI (`pritunl`). Build with `uv`, test with `pytest`/`respx`, lint with `ruff`, typecheck with `mypy`.

## Commands

```bash
uv sync --frozen --extra dev     # install everything (CI-style)
pytest                            # auto-discovers tests/, adds --cov
pytest tests/test_client.py -v   # single file
pytest tests/test_client.py::TestLogin -v  # single class
ruff check src tests              # lint
ruff format --check src tests     # format check (omit --check to write)
mypy src                          # typecheck (not enforced in CI)
uv build                          # produces dist/*.whl + dist/*.tar.gz
```

## Architecture

- **`src/pritunl_webclient/client.py`** — `Client` class wrapping `httpx.Client`, `@require_auth` decorator, CSRF token management, auto-re-auth on session expiry.
- **`src/pritunl_webclient/cli.py`** — argparse-based CLI. Reads config from env vars only (`PRITUNL_URL`, `PRITUNL_USERNAME`, `PRITUNL_PASSWORD`, `PRITUNL_VERIFY_TLS`). Entrypoint: `pritunl_webclient.cli:main`.
- **`src/pritunl_webclient/exceptions.py`** — `PritunlError` > `AuthenticationError`, `NotAuthenticated`, `ServerNotFound`.
- **`src/pritunl_webclient/__init__.py`** — exports `Client`, `PritunlError`. Note: `__version__ = "0.2.1"` is stale (pyproject.toml is source of truth at 0.4.0).

## Testing

- All HTTP mocked via `respx` — no real network.
- No integration test prerequisites; everything runs offline.
- Two test files: `tests/test_client.py` (Client unit tests), `tests/test_cli.py` (CLI unit tests).
- CLI tests use `monkeypatch` for env vars and `respx` for HTTP mocking.

## CI (tests.yml)

Runs on push/PR to `main`/`develop`. Order: `ruff check` → `ruff format --check` → `mypy src` (continue-on-error) → `pytest --cov`. Python 3.10–3.13 on ubuntu.

## Release

Push a tag matching `vX.Y.Z` where X.Y.Z matches `pyproject.toml` version. GitHub Actions publish workflow verifies the match before building and publishing to PyPI.

## Style quirks

- Line length: **120** (not the ruff default of 88).
- Ruff target-version set to `"py38"` but `requires-python = ">=3.10"` — likely stale.
- No `.env` file loading by the CLI; all config is env-var driven.
