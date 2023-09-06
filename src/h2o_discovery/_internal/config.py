import dataclasses
import types
from typing import Mapping
from typing import Optional

from h2o_discovery._internal.compat import tomllib


def _empty_tokens_factory() -> Mapping[str, str]:
    return types.MappingProxyType({})


@dataclasses.dataclass(frozen=True)
class Config:
    """Internal representation of the H2O CLI Configuration."""

    #: Configured URI of environment.
    endpoint: Optional[str] = None

    #: Map of found tokens in the configuration file. in the `{"client-id": "token"}`
    #: format.
    tokens: Mapping[str, str] = dataclasses.field(default_factory=_empty_tokens_factory)


def load_config(path: Optional[str] = None) -> Config:
    """Loads the H2O CLI config from the specified path.

    If no path is specified, an empty configuration is returned.
    """

    if not path:
        return Config()

    with open(path, "rb") as f:
        data = tomllib.load(f)

    endpoint = data.get("Endpoint")
    client_id = data.get("ClientID")
    token = data.get("Token")
    platform_client_id = data.get("PlatformClientID")
    platform_token = data.get("PlatformToken")

    tokens = {}
    if client_id is not None and token is not None:
        tokens[client_id] = token
    if platform_client_id is not None and platform_token is not None:
        tokens[platform_client_id] = platform_token

    return Config(endpoint=endpoint, tokens=types.MappingProxyType(tokens))
