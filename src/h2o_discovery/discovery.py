import types
from typing import Optional
from typing import Mapping

from h2o_discovery import config
from h2o_discovery import client
from h2o_discovery import model


def New(environment: Optional[str] = None, discovery: Optional[str] = None):
    uri = config.discover_uri(environment, discovery)
    return Discovery(client=client.New(uri))


class Discovery:
    def __init__(self, client: client.Client):
        self._client = client

        self._environment: Optional[model.Environment] = None
        self._services: Optional[Mapping[str, model.Service]] = None
        self._clients: Optional[Mapping[str, model.Client]] = None

    @property
    def environment(self) -> model.Environment:
        if self._environment is None:
            self._environment = self._client.get_environment()
        return self._environment

    @property
    def services(self) -> Mapping[str, model.Service]:
        if self._services is None:
            self._services = self._get_service_map()
        return self._services

    @property
    def clients(self) -> Mapping[str, model.Client]:
        if self._clients is None:
            self._clients = self._get_client_map()
        return self._clients

    def reload(self):
        self._environment = None
        self._services = None
        self._clients = None

        _ = self.environment
        _ = self.services
        _ = self.clients

    def _get_service_map(self) -> Mapping[str, model.Service]:
        out = {}
        for svc in self._client.list_services():
            out[_service_key(svc.name)] = svc
        return types.MappingProxyType(out)

    def _get_client_map(self) -> Mapping[str, model.Client]:
        out = {}
        for cl in self._client.list_clients():
            out[_client_key(cl.name)] = cl
        return types.MappingProxyType(out)


_CLIENTS_COLLECTION_PREFIX = "clients/"
_SERVICES_COLLECTION_PREFIX = "services/"


def _service_key(name: str) -> str:
    if name.startswith(_SERVICES_COLLECTION_PREFIX):
        return name[len(_SERVICES_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid service name: {name}")


def _client_key(name: str) -> str:
    if name.startswith(_CLIENTS_COLLECTION_PREFIX):
        return name[len(_CLIENTS_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid client name: {name}")
