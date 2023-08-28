import dataclasses
from typing import Optional
from typing import Tuple


from h2o_discovery import model
from h2o_discovery._internal import client
from h2o_discovery._internal import load
from h2o_discovery._internal import lookup
from h2o_discovery._internal import config
from h2o_discovery._version import __version__  # noqa: F401

Discovery = model.Discovery


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
    uri, cfg = _lookup(environment, discovery_address)
    discovery = load.load_discovery(client.Client(uri))
    credentials = load.load_credentials(discovery.clients, cfg.tokens)

    return dataclasses.replace(discovery, credentials=credentials)


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
    uri, cfg = _lookup(environment, discovery_address)
    discovery = await load.load_discovery_async(client.AsyncClient(uri))
    credentials = load.load_credentials(discovery.clients, cfg.tokens)

    return dataclasses.replace(discovery, credentials=credentials)


def _lookup(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> Tuple[str, config.Config]:
    cfg = config.Config()
    config_path = lookup.determine_local_config_path()
    if config_path:
        cfg = config.load_config(config_path)

    uri = lookup.determine_uri(environment, discovery_address)

    return uri, cfg
