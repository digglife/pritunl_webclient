"""pritunl_webclient

A modern Python client for Pritunl Web API.

Main exports:
 - Client
"""

from .client import Client
from .exceptions import PritunlError

__version__ = "0.2.1"
__all__ = [
    "Client",
    "PritunlError",
]
