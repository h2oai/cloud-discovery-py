import os
from typing import Optional

_WELL_KNOWN_PATH = ".ai.h2o.cloud.discovery"


def FindURI(environment: Optional[str] = None, discovery: Optional[str] = None) -> str:
    if environment is None:
        environment = os.environ.get("H2O_CLOUD_ENVIRONMENT")
    if discovery is None:
        discovery = os.environ.get("H2O_CLOUD_DISCOVERY")

    if environment is None and discovery is None:
        raise ValueError("environment or discovery is required")

    if discovery is not None:
        return discovery

    return f"{environment}/{_WELL_KNOWN_PATH}"
