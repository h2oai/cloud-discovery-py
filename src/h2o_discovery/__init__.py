from typing import Optional

from h2o_discovery import discovery
from h2o_discovery import lookup
from h2o_discovery import client

from h2o_discovery._version import __version__  # noqa: F401


Discovery = discovery.Discovery


async def discover(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> discovery.Discovery:
    uri = lookup.determine_uri(environment, discovery_address)
    cl = client.Client(uri)
    return await Discovery.load(cl)
