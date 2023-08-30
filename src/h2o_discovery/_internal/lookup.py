import os
from typing import Optional
from typing import Union
import urllib.parse

_WELL_KNOWN_PATH = ".ai.h2o.cloud.discovery"
_DEFAULT_LOCAL_CONFIG_PATH = "~/.h2oai/h2o-cli-config.toml"


def determine_uri(
    environment: Optional[str] = None, discovery_address: Optional[str] = None
) -> str:
    """Uses passed parameters and environment variables to get the uri of the discovery
    service.
    """
    if discovery_address is not None and environment is not None:
        raise ValueError("cannot specify both discovery and environment")

    if discovery_address is not None:
        return discovery_address.rstrip("/")

    if environment is not None:
        return _discovery_uri_from_environment(environment)

    discovery_address = os.environ.get("H2O_CLOUD_DISCOVERY")
    if discovery_address is not None:
        return discovery_address.rstrip("/")

    environment = os.environ.get("H2O_CLOUD_ENVIRONMENT")
    if environment is not None:
        return _discovery_uri_from_environment(environment)

    raise LookupError(
        "Cannot determine discovery URI."
        " Please set H2O_CLOUD_ENVIRONMENT or H2O_CLOUD_DISCOVERY environment variables"
        "or use the environment or discovery parameters."
    )


def _discovery_uri_from_environment(environment: str):
    return urllib.parse.urljoin(environment + "/", _WELL_KNOWN_PATH)


def determine_local_config_path(
    config_path: Optional[Optional[Union[str, bytes, os.PathLike]]] = None
) -> Optional[str]:
    """Uses passed parameter, environment variable and H2O CLI default to get the
    path to the local config file.
    """
    if config_path is not None:
        return str(os.fspath(config_path))

    config_path = os.environ.get("H2OCONFIG")
    if config_path is not None:
        return config_path

    local_config_path = os.path.expanduser(_DEFAULT_LOCAL_CONFIG_PATH)
    if not os.path.isfile(local_config_path):
        return None
    return local_config_path
