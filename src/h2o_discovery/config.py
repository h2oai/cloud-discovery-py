import os
from typing import Optional

_WELL_KNOWN_PATH = ".ai.h2o.cloud.discovery"


def discover_uri(environment: Optional[str] = None, discovery: Optional[str] = None) -> str:
    if discovery is not None and environment is not None:
        raise ValueError("cannot specify both discovery and environment")

    if discovery is not None:
        return discovery

    if environment is not None:
        return _discover_uri_from_environment(environment)

    discovery = os.environ.get("H2O_CLOUD_DISCOVERY")
    if discovery is not None:
        return discovery

    environment = os.environ.get("H2O_CLOUD_ENVIRONMENT")
    if environment is not None:
        return _discover_uri_from_environment(environment)

    raise LookupError(
        "Cannot determine discovery URI."
        " Please set H2O_CLOUD_ENVIRONMENT or H2O_CLOUD_DISCOVERY environment variables"
        "or use the environment or discovery parameters."
    )


def _discover_uri_from_environment(environment):
    return f"{environment}/{_WELL_KNOWN_PATH}"
