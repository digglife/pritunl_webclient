"""Unit tests for CLI commands."""

import argparse
import sys

import httpx
import pytest
import respx

from pritunl_webclient.cli import _find_server, cmd_list, cmd_start, cmd_stop, main

BASE_URL = "https://pritunl.example.com"

SERVERS_DATA = {
    "servers": [
        {"id": "abc123", "name": "US East", "status": "online"},
        {"id": "def456", "name": "EU West", "status": "offline"},
    ]
}


@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    """Set required env vars for every test."""
    monkeypatch.setenv("PRITUNL_URL", BASE_URL)
    monkeypatch.setenv("PRITUNL_USERNAME", "admin")
    monkeypatch.setenv("PRITUNL_PASSWORD", "secret")
    monkeypatch.setenv("PRITUNL_VERIFY_TLS", "false")


def _mock_auth():
    """Return respx routes that stub login + state."""
    login_route = respx.post(f"{BASE_URL}/auth/session").mock(return_value=httpx.Response(200, json={}))
    state_route = respx.get(f"{BASE_URL}/state").mock(
        return_value=httpx.Response(200, json={"csrf_token": "tok", "authenticated": True})
    )
    return login_route, state_route


def _args(**kwargs):
    """Create a minimal argparse.Namespace from keyword args."""
    return argparse.Namespace(**kwargs)


# ---------------------------------------------------------------------------
# _find_server helper
# ---------------------------------------------------------------------------


class TestFindServer:
    def test_find_by_id(self):
        servers = [{"id": "abc123", "name": "US East", "status": "online"}]
        result = _find_server(servers, "abc123")
        assert result is not None
        assert result["id"] == "abc123"

    def test_find_by_name_exact(self):
        servers = [{"id": "abc123", "name": "US East", "status": "online"}]
        result = _find_server(servers, "US East")
        assert result is not None
        assert result["id"] == "abc123"

    def test_find_by_name_case_insensitive(self):
        servers = [{"id": "abc123", "name": "US East", "status": "online"}]
        result = _find_server(servers, "us east")
        assert result is not None
        assert result["id"] == "abc123"

    def test_not_found(self):
        servers = [{"id": "abc123", "name": "US East", "status": "online"}]
        assert _find_server(servers, "nonexistent") is None

    def test_empty_list(self):
        assert _find_server([], "anything") is None


# ---------------------------------------------------------------------------
# Missing env vars
# ---------------------------------------------------------------------------


class TestMissingEnvVars:
    def test_missing_url(self, monkeypatch):
        monkeypatch.delenv("PRITUNL_URL")
        with pytest.raises(SystemExit) as exc_info:
            cmd_list(_args())
        assert exc_info.value.code == 1

    def test_missing_username(self, monkeypatch):
        monkeypatch.delenv("PRITUNL_USERNAME")
        with pytest.raises(SystemExit) as exc_info:
            cmd_list(_args())
        assert exc_info.value.code == 1

    def test_missing_password(self, monkeypatch):
        monkeypatch.delenv("PRITUNL_PASSWORD")
        with pytest.raises(SystemExit) as exc_info:
            cmd_list(_args())
        assert exc_info.value.code == 1

    def test_missing_multiple(self, monkeypatch, capsys):
        monkeypatch.delenv("PRITUNL_USERNAME")
        monkeypatch.delenv("PRITUNL_PASSWORD")
        with pytest.raises(SystemExit):
            cmd_list(_args())
        err = capsys.readouterr().err
        assert "PRITUNL_USERNAME" in err
        assert "PRITUNL_PASSWORD" in err


# ---------------------------------------------------------------------------
# cmd_list
# ---------------------------------------------------------------------------


class TestCmdList:
    @respx.mock
    def test_list_success(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))

        cmd_list(_args())

        out = capsys.readouterr().out
        assert "abc123" in out
        assert "US East" in out
        assert "online" in out
        assert "def456" in out
        assert "EU West" in out
        assert "offline" in out

    @respx.mock
    def test_list_empty(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json={"servers": []}))

        cmd_list(_args())

        out = capsys.readouterr().out
        assert "No servers found" in out

    @respx.mock
    def test_list_api_error(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(500, json={"error": "oops"}))

        with pytest.raises(SystemExit) as exc_info:
            cmd_list(_args())
        assert exc_info.value.code == 1
        assert "Error" in capsys.readouterr().err


# ---------------------------------------------------------------------------
# cmd_start
# ---------------------------------------------------------------------------


class TestCmdStart:
    @respx.mock
    def test_start_by_id(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/start").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "online"})
        )

        cmd_start(_args(server="abc123"))

        out = capsys.readouterr().out
        assert "Started" in out
        assert "US East" in out

    @respx.mock
    def test_start_by_name(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/start").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "online"})
        )

        cmd_start(_args(server="US East"))

        out = capsys.readouterr().out
        assert "Started" in out

    @respx.mock
    def test_start_by_name_case_insensitive(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/start").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "online"})
        )

        cmd_start(_args(server="us east"))
        assert "Started" in capsys.readouterr().out

    @respx.mock
    def test_start_server_not_found(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))

        with pytest.raises(SystemExit) as exc_info:
            cmd_start(_args(server="nonexistent"))
        assert exc_info.value.code == 1
        assert "not found" in capsys.readouterr().err

    @respx.mock
    def test_start_operation_failure(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/start").mock(
            return_value=httpx.Response(500, json={"error": "internal"})
        )

        with pytest.raises(SystemExit) as exc_info:
            cmd_start(_args(server="abc123"))
        assert exc_info.value.code == 1


# ---------------------------------------------------------------------------
# cmd_stop
# ---------------------------------------------------------------------------


class TestCmdStop:
    @respx.mock
    def test_stop_by_id(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/stop").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "offline"})
        )

        cmd_stop(_args(server="abc123"))

        out = capsys.readouterr().out
        assert "Stopped" in out
        assert "US East" in out

    @respx.mock
    def test_stop_by_name(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/stop").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "offline"})
        )

        cmd_stop(_args(server="US East"))
        assert "Stopped" in capsys.readouterr().out

    @respx.mock
    def test_stop_server_not_found(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))

        with pytest.raises(SystemExit) as exc_info:
            cmd_stop(_args(server="ghost"))
        assert exc_info.value.code == 1
        assert "not found" in capsys.readouterr().err

    @respx.mock
    def test_stop_operation_failure(self, capsys):
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/stop").mock(
            return_value=httpx.Response(500, json={"error": "internal"})
        )

        with pytest.raises(SystemExit) as exc_info:
            cmd_stop(_args(server="abc123"))
        assert exc_info.value.code == 1


# ---------------------------------------------------------------------------
# main() / argument parsing
# ---------------------------------------------------------------------------


class TestMain:
    @respx.mock
    def test_main_list(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["pritunl", "list"])
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        main()
        assert "US East" in capsys.readouterr().out

    def test_main_no_command(self):
        # argparse exits with code 2 when required subcommand is missing
        with pytest.raises(SystemExit) as exc_info:
            import sys

            sys.argv = ["pritunl"]
            main()
        assert exc_info.value.code == 2

    @respx.mock
    def test_main_start(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["pritunl", "start", "abc123"])
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/start").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "online"})
        )
        main()
        assert "Started" in capsys.readouterr().out

    @respx.mock
    def test_main_stop(self, capsys, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["pritunl", "stop", "abc123"])
        _mock_auth()
        respx.get(f"{BASE_URL}/server").mock(return_value=httpx.Response(200, json=SERVERS_DATA))
        respx.put(f"{BASE_URL}/server/abc123/operation/stop").mock(
            return_value=httpx.Response(200, json={"id": "abc123", "name": "US East", "status": "offline"})
        )
        main()
        assert "Stopped" in capsys.readouterr().out
