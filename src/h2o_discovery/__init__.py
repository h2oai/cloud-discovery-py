from typing import Optional

from h2o_discovery import client
from h2o_discovery import discover
from h2o_discovery import discovery
from h2o_discovery._version import __version__  # noqa: F401


Discovery = discovery.Discovery


def New(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> discovery.Discovery:
    uri = discover.discover_uri(environment, discovery_address)
    cl = client.Client(uri)
    return discovery.Discovery(client=cl)
