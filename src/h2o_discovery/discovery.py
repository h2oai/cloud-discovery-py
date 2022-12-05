import dataclasses
import types
from typing import Mapping

from h2o_discovery import model
from h2o_discovery import client


@dataclasses.dataclass(frozen=True)
class Discovery:
    """Representation of the discovery records."""

    # Environment information.
    environment: model.Environment

    # Registered services.
    services: Mapping[str, model.Service]

    # Registered clients.
    clients: Mapping[str, model.Client]

    @classmethod
    async def load(cls, cl: client.Client) -> "Discovery":
        """Loads the discovery records from the Discovery Service."""
        environment = await cl.get_environment()
        services = await _get_service_map(cl)
        clients = await _get_client_map(cl)

        return cls(environment=environment, services=services, clients=clients)


async def _get_service_map(cl: client.Client) -> Mapping[str, model.Service]:
    out = {}
    for s in await cl.list_services():
        out[_service_key(s.name)] = s
    return types.MappingProxyType(out)


async def _get_client_map(cl: client.Client) -> Mapping[str, model.Client]:
    out = {}
    for c in await cl.list_clients():
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
