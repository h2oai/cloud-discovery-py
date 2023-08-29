import os
import dataclasses
from typing import Optional
from typing import Tuple
from typing import Union


from h2o_discovery import model
from h2o_discovery._internal import client
from h2o_discovery._internal import load
from h2o_discovery._internal import lookup
from h2o_discovery._internal import config
from h2o_discovery._version import __version__  # noqa: F401

Discovery = model.Discovery


def discover(
    environment: Optional[str] = None,
    discovery_address: Optional[str] = None,
    config_path: Optional[Union[str, bytes, os.PathLike]] = None,
) -> Discovery:
    """Obtains and returns a Discovery object from the discovery service.

    All arguments are optional. Discovery determined with the following precedence:
     - discovery_address parameter
     - H2O_CLOUD_DISCOVERY environment variable
     - environment parameter
     - H2O_CLOUD_ENVIRONMENT environment variable
     - environment URI loaded from the local configuration file

    Config path is determined with the following precedence:
        - config_path parameter
        - H2OCONFIG environment variable
        - default H2O CLI configuration configuration path

    Args:
        environment: The H2O Cloud environment URL to use (e.g. https://cloud.h2o.ai).
        discovery_address: The address of the discovery service.
        config_path: The path to the H2O CLI configuration file.

    Raises:
        LookupError: If the URI cannot be determined.
    """
    uri, cfg = _lookup(environment, discovery_address, config_path)
    discovery = load.load_discovery(client.Client(uri))
    credentials = load.load_credentials(discovery.clients, cfg.tokens)

    return dataclasses.replace(discovery, credentials=credentials)


async def discover_async(
    environment: Optional[str] = None,
    discovery_address: Optional[str] = None,
    config_path: Optional[Union[str, bytes, os.PathLike]] = None,
) -> Discovery:
    """Obtains and returns a Discovery object from the discovery service.

    All arguments are optional. Discovery determined with the following precedence:
     - discovery_address parameter
     - H2O_CLOUD_DISCOVERY environment variable
     - environment parameter
     - H2O_CLOUD_ENVIRONMENT environment variable
     - environment URI loaded from the local configuration file

    Config path is determined with the following precedence:
        - config_path parameter
        - H2OCONFIG environment variable
        - default H2O CLI configuration configuration path

    Args:
        environment: The H2O Cloud environment URL to use (e.g. https://cloud.h2o.ai).
        discovery_address: The address of the discovery service.
        config_path: The path to the H2O CLI configuration file.

    Raises:
        LookupError: If the URI cannot be determined.
    """
    uri, cfg = _lookup(environment, discovery_address, config_path)
    discovery = await load.load_discovery_async(client.AsyncClient(uri))
    credentials = load.load_credentials(discovery.clients, cfg.tokens)

    return dataclasses.replace(discovery, credentials=credentials)


def _lookup(
    environment: Optional[str] = None,
    discovery_address: Optional[str] = None,
    config_path: Optional[Union[str, bytes, os.PathLike]] = None,
) -> Tuple[str, config.Config]:
    cfg = config.Config()
    if config_path is not None:
        config_path = str(os.fspath(config_path))
    config_path = lookup.determine_local_config_path(config_path)
    if config_path:
        cfg = config.load_config(config_path)

    try:
        uri = lookup.determine_uri(environment, discovery_address, cfg.endpoint)
    except lookup.DetermineURIError:
        raise LookupError(
            "Cannot determine discovery URI."
            " Please set H2O_CLOUD_ENVIRONMENT or H2O_CLOUD_DISCOVERY environment"
            " variables or use the environment or discovery parameters."
            " Alternatively, you can create configure your local environment with"
            " the with H2O CLI with and/or use H2OCONFIG environment variable"
            " (see https://docs.h2o.ai/h2o-ai-cloud/developerguide/cli)."
        )

    return uri, cfg
