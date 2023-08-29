import os
import types
from typing import Iterable
from typing import Mapping
from typing import Optional

from h2o_discovery import model
from h2o_discovery._internal import client


def load_discovery(cl: client.Client) -> model.Discovery:
    """Loads the discovery records from the Discovery Service."""
    environment = cl.get_environment()
    services = _get_service_map(cl.list_services())
    clients = _get_client_map(cl.list_clients())

    return model.Discovery(environment=environment, services=services, clients=clients)


async def load_discovery_async(cl: client.AsyncClient) -> model.Discovery:
    """Loads the discovery records from the Discovery Service."""
    environment = await cl.get_environment()
    services = _get_service_map(await cl.list_services())
    clients = _get_client_map(await cl.list_clients())

    return model.Discovery(environment=environment, services=services, clients=clients)


def load_credentials(
    clients: Mapping[str, model.Client], config_tokens: Optional[Mapping[str, str]]
) -> Mapping[str, model.Credentials]:
    """Loads client credentials from the environment or tokens loaded from the
    config.
    """
    tokens: Mapping[str, str] = {}
    if config_tokens is not None:
        tokens = config_tokens

    out = {}
    for name, cl in clients.items():
        env_name = f"H2O_CLOUD_CLIENT_{name.upper()}_TOKEN"
        token = os.environ.get(env_name) or tokens.get(cl.oauth2_client_id)
        if token:
            out[name] = model.Credentials(refresh_token=token)
    return types.MappingProxyType(out)


def _get_service_map(services: Iterable[model.Service]) -> Mapping[str, model.Service]:
    out = {}
    for s in services:
        out[_service_key(s.name)] = s
    return types.MappingProxyType(out)


def _get_client_map(clients: Iterable[model.Client]) -> Mapping[str, model.Client]:
    out = {}
    for c in clients:
        out[_client_key(c.name)] = c
    return types.MappingProxyType(out)


_SERVICES_COLLECTION_PREFIX = "services/"


def _service_key(name: str) -> str:
    if name.startswith(_SERVICES_COLLECTION_PREFIX):
        return name[len(_SERVICES_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid service name: {name}")


_CLIENTS_COLLECTION_PREFIX = "clients/"


def _client_key(name: str) -> str:
    if name.startswith(_CLIENTS_COLLECTION_PREFIX):
        return name[len(_CLIENTS_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid client name: {name}")
