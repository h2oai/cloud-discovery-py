import asyncio
import json
import os
import types
from typing import Iterable
from typing import List
from typing import Mapping

import httpx

from h2o_discovery import error
from h2o_discovery import model
from h2o_discovery._internal import client
from h2o_discovery._internal import config


def load_discovery(cl: client.Client) -> model.Discovery:
    """Loads the discovery records from the Discovery Service."""
    try:
        environment = cl.get_environment()
        services = _get_service_map(cl.list_services())
        clients = _get_client_map(cl.list_clients())
        links = _get_link_map(_list_links(cl))
        components = _get_component_map(_list_components(cl))
    except Exception as e:
        _handle_specific_client_exceptions(e)
        raise
    return model.Discovery(
        environment=environment,
        services=services,
        clients=clients,
        links=links,
        components=components,
    )


async def load_discovery_async(cl: client.AsyncClient) -> model.Discovery:
    """Loads the discovery records from the Discovery Service."""
    try:
        return await _gather_discovery_async(cl)
    except Exception as e:
        _handle_specific_client_exceptions(e)
        raise


async def _gather_discovery_async(cl: client.AsyncClient) -> model.Discovery:
    environment_future = cl.get_environment()
    services_future = cl.list_services()
    clients_future = cl.list_clients()
    links_future = _list_links_async(cl)
    components_future = _list_components_async(cl)

    environment, services, clients, links, components = await asyncio.gather(
        environment_future,
        services_future,
        clients_future,
        links_future,
        components_future,
    )

    return model.Discovery(
        environment=environment,
        services=_get_service_map(services),
        clients=_get_client_map(clients),
        links=_get_link_map(links),
        components=_get_component_map(components),
    )


def _list_links(cl: client.Client) -> List[model.Link]:
    try:
        return cl.list_links()
    except Exception as e:
        # Links are added in the server version 2.5.0. In order to have client that
        # is backwards compatible, we won't fail if the links are not available.
        if isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 404:
            return []
        raise


async def _list_links_async(cl: client.AsyncClient) -> List[model.Link]:
    try:
        return await cl.list_links()
    except Exception as e:
        # Links are added in the server version 2.5.0. In order to have client that
        # is backwards compatible, we won't fail if the links are not available.
        if isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 404:
            return []
        raise


def _list_components(cl: client.Client) -> List[model.Component]:
    try:
        return cl.list_components()
    except Exception as e:
        # Components are added in the server version 2.6.0. In order to have client that
        # is backwards compatible, we won't fail if the components are not available.
        if isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 404:
            return []
        raise


async def _list_components_async(cl: client.AsyncClient) -> List[model.Component]:
    try:
        return await cl.list_components()
    except Exception as e:
        # Components are added in the server version 2.6.0. In order to have client that
        # is backwards compatible, we won't fail if the components are not available.
        if isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 404:
            return []
        raise


def load_credentials(
    discovery: model.Discovery, cfg: config.Config
) -> Mapping[str, model.Credentials]:
    """Loads client credentials from the environment or tokens loaded from the
    config.
    """
    h2o_cloud_environment = discovery.environment.h2o_cloud_environment.rstrip("/")
    config_matches = cfg.endpoint and h2o_cloud_environment == cfg.endpoint.rstrip("/")
    tokens: Mapping[str, str] = {}
    if config_matches and cfg.tokens is not None:
        # Load tokens from the config only when the environments match.
        tokens = cfg.tokens

    out = {}
    for name, cl in discovery.clients.items():
        env_name = f"H2O_CLOUD_CLIENT_{name.upper()}_TOKEN"
        token = os.environ.get(env_name) or tokens.get(cl.oauth2_client_id)
        if token:
            out[name] = model.Credentials(client=name, refresh_token=token)
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


def _get_link_map(links: Iterable[model.Link]) -> Mapping[str, model.Link]:
    out = {}
    for ln in links:
        out[_link_key(ln.name)] = ln
    return types.MappingProxyType(out)


def _get_component_map(
    components: Iterable[model.Component],
) -> Mapping[str, model.Component]:
    out = {}
    for c in components:
        out[_component_key(c.name)] = c
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


_LINKS_COLLECTION_PREFIX = "links/"


def _link_key(name: str) -> str:
    if name.startswith(_LINKS_COLLECTION_PREFIX):
        return name[len(_LINKS_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid link name: {name}")


_COMPONENTS_COLLECTION_PREFIX = "components/"


def _component_key(name: str) -> str:
    if name.startswith(_COMPONENTS_COLLECTION_PREFIX):
        return name[len(_COMPONENTS_COLLECTION_PREFIX) :]
    raise ValueError(f"invalid component name: {name}")


_ENV_ERROR = error.H2OCloudEnvironmentError(
    "Received an unexpected response from the server."
    " Please make sure that the environment you are trying to connect to is"
    " configured correctly and has the H2O Cloud Discovery Service enabled."
)


def _handle_specific_client_exceptions(e: Exception) -> None:
    if isinstance(e, json.decoder.JSONDecodeError):
        raise _ENV_ERROR from e
    if isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 404:
        raise _ENV_ERROR from e
