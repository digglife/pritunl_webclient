"""Command-line interface for pritunl-webclient."""

import argparse
import os
import sys
from typing import Any, Dict, List, Optional

from .client import Client
from .exceptions import PritunlError, ServerNotFound


def _build_client() -> Client:
    """Build a Client from environment variables.

    Required env vars: PRITUNL_URL, PRITUNL_USERNAME, PRITUNL_PASSWORD
    Optional env var:  PRITUNL_VERIFY_TLS (default: true; set to 'false' to skip)
    """
    url = os.environ.get("PRITUNL_URL")
    username = os.environ.get("PRITUNL_USERNAME")
    password = os.environ.get("PRITUNL_PASSWORD")

    missing = [name for name, val in [("PRITUNL_URL", url), ("PRITUNL_USERNAME", username), ("PRITUNL_PASSWORD", password)] if not val]
    if missing:
        print(f"Error: missing required environment variable(s): {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    verify_tls = os.environ.get("PRITUNL_VERIFY_TLS", "true").strip().lower() != "false"

    return Client(url, verify=verify_tls, username=username, password=password)  # type: ignore[arg-type]


def _find_server(servers: List[Dict[str, Any]], name_or_id: str) -> Optional[Dict[str, Any]]:
    """Return the first server matching the given name or id (case-insensitive name match)."""
    for s in servers:
        if s.get("id") == name_or_id or s.get("name", "").lower() == name_or_id.lower():
            return s
    return None


def cmd_list(_args: argparse.Namespace) -> None:
    with _build_client() as client:
        try:
            servers = client.list_servers()
        except PritunlError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

    if not servers:
        print("No servers found.")
        return

    # Determine column widths
    id_w = max(len("ID"), max(len(s.get("id", "")) for s in servers))
    name_w = max(len("NAME"), max(len(s.get("name", "")) for s in servers))
    status_w = max(len("STATUS"), max(len(s.get("status", "")) for s in servers))

    fmt = f"{{:<{id_w}}}  {{:<{name_w}}}  {{:<{status_w}}}"
    print(fmt.format("ID", "NAME", "STATUS"))
    print(fmt.format("-" * id_w, "-" * name_w, "-" * status_w))
    for s in servers:
        print(fmt.format(s.get("id", ""), s.get("name", ""), s.get("status", "")))


def cmd_start(args: argparse.Namespace) -> None:
    with _build_client() as client:
        try:
            servers = client.list_servers()
        except PritunlError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

        server = _find_server(servers, args.server)
        if server is None:
            print(f"Error: server '{args.server}' not found", file=sys.stderr)
            sys.exit(1)

        try:
            result = client.start_server(server["id"], server_obj=server)
        except (PritunlError, ServerNotFound) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

    print(f"Started server '{server.get('name', server['id'])}' — status: {result.get('status', 'unknown')}")


def cmd_stop(args: argparse.Namespace) -> None:
    with _build_client() as client:
        try:
            servers = client.list_servers()
        except PritunlError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

        server = _find_server(servers, args.server)
        if server is None:
            print(f"Error: server '{args.server}' not found", file=sys.stderr)
            sys.exit(1)

        try:
            result = client.stop_server(server["id"], server_obj=server)
        except (PritunlError, ServerNotFound) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

    print(f"Stopped server '{server.get('name', server['id'])}' — status: {result.get('status', 'unknown')}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pritunl",
        description="Manage Pritunl VPN servers via the web API.",
        epilog=(
            "Credentials are read from environment variables:\n"
            "  PRITUNL_URL        Base URL of the Pritunl web UI\n"
            "  PRITUNL_USERNAME   Admin username\n"
            "  PRITUNL_PASSWORD   Admin password\n"
            "  PRITUNL_VERIFY_TLS Set to 'false' to skip TLS verification (default: true)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = True

    sub.add_parser("list", help="List all servers")

    start_p = sub.add_parser("start", help="Start a server")
    start_p.add_argument("server", metavar="NAME_OR_ID", help="Server name or ID")

    stop_p = sub.add_parser("stop", help="Stop a server")
    stop_p.add_argument("server", metavar="NAME_OR_ID", help="Server name or ID")

    args = parser.parse_args()

    dispatch = {"list": cmd_list, "start": cmd_start, "stop": cmd_stop}
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
