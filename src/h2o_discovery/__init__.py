from typing import Optional

from h2o_discovery import async_client
from h2o_discovery import discovery
from h2o_discovery import lookup

from h2o_discovery._version import __version__  # noqa: F401


Discovery = discovery.Discovery


async def discover_async(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> Discovery:
    """Obtains and returns a Discovery object from the discovery service.

    Both arguments are optional. If neither is provided, the environment variable
    H2O_CLOUD_ENVIRONMENT is used. If that is not set, the environment variable
    H2O_CLOUD_DISCOVERY is used. If that is not set, a LookupError is raised.

    Args:
        environment: The H2O Cloud environment URL to use (e.g. https://cloud.h2o.ai).
        discovery_address: The address of the discovery service.

    """
    uri = lookup.determine_uri(environment, discovery_address)
    cl = async_client.AsyncClient(uri)
    return await Discovery.load_async(cl)
