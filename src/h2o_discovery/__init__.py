from typing import Optional

from h2o_discovery import async_client, client, discovery, lookup

Discovery = discovery.Discovery

__version__ = "0.0.0"


def discover(
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
    cl = client.Client(uri)
    return Discovery.load(cl)


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
