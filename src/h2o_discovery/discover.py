import os
from typing import Optional
import urllib.parse

_WELL_KNOWN_PATH = ".ai.h2o.cloud.discovery"


def discover_uri(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> str:
    """Uses passed parameters and environment variables to get the uri of the discovery
    service.
    """
    if discovery_address is not None and environment is not None:
        raise ValueError("cannot specify both discovery and environment")

    if discovery_address is not None:
        return discovery_address

    if environment is not None:
        return _discover_uri_from_environment(environment)

    discovery_address = os.environ.get("H2O_CLOUD_DISCOVERY")
    if discovery_address is not None:
        return discovery_address

    environment = os.environ.get("H2O_CLOUD_ENVIRONMENT")
    if environment is not None:
        return _discover_uri_from_environment(environment)

    raise LookupError(
        "Cannot determine discovery URI."
        " Please set H2O_CLOUD_ENVIRONMENT or H2O_CLOUD_DISCOVERY environment variables"
        "or use the environment or discovery parameters."
    )


def _discover_uri_from_environment(environment):
    return urllib.parse.urljoin(environment, _WELL_KNOWN_PATH)
