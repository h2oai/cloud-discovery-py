import types
from typing import Optional
from typing import Mapping

from h2o_discovery import client
from h2o_discovery import model


class Discovery:
    def __init__(self, client: client.Client):
        self._client = client

        self._environment: Optional[model.Environment] = None
        self._services: Optional[Mapping[str, model.Service]] = None
        self._clients: Optional[Mapping[str, model.Client]] = None

    @property
    async def environment(self) -> model.Environment:
        if self._environment is None:
            self._environment = await self._client.get_environment()
        return self._environment

    @property
    async def services(self) -> Mapping[str, model.Service]:
        if self._services is None:
            self._services = await self._get_service_map()
        return self._services

    @property
    async def clients(self) -> Mapping[str, model.Client]:
        if self._clients is None:
            self._clients = await self._get_client_map()
        return self._clients

    async def load(self):
        self._environment = None
        self._services = None
        self._clients = None

        _ = await self.environment
        _ = await self.services
        _ = await self.clients

    async def _get_service_map(self) -> Mapping[str, model.Service]:
        out = {}
        for svc in await self._client.list_services():
            out[_service_key(svc.name)] = svc
        return types.MappingProxyType(out)

    async def _get_client_map(self) -> Mapping[str, model.Client]:
        out = {}
        for cl in await self._client.list_clients():
            out[_client_key(cl.name)] = cl
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
