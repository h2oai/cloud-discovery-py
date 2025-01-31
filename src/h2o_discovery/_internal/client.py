import datetime
import ssl
from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar

import httpx

from h2o_discovery import model

_ENVIRONMENT_ENDPOINT = "v1/environment"
_SERVICES_ENDPOINT = "v1/services"
_CLIENTS_ENDPOINT = "v1/clients"
_LINKS_ENDPOINT = "v1/links"
_COMPONENTS_ENDPOINT = "v1/components"

DEFAULT_HTTP_TIMEOUT = datetime.timedelta(seconds=5)


class _BaseClient:
    def __init__(
        self,
        uri: str,
        timeout: Optional[datetime.timedelta] = None,
        ssl_context: Optional[ssl.SSLContext] = None,
    ):
        self._uri = uri
        self._verify = ssl_context or ssl.create_default_context()

        self._timeout = 5.0
        if timeout is not None:
            self._timeout = timeout.total_seconds()


_T = TypeVar("_T")


class Client(_BaseClient):
    """Synchronous Implementation of the Discovery Service API.

    Listing methods do pagination and always return all of the available objects.
    """

    def get_environment(self) -> model.Environment:
        """Returns the information about the environment."""
        with self._client() as client:
            resp = _fetch(client, _ENVIRONMENT_ENDPOINT)
            return model.Environment.from_json_dict(resp.json()["environment"])

    def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        return self._get_all_entities(
            _SERVICES_ENDPOINT, "services", model.Service.from_json_dict
        )

    def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        return self._get_all_entities(
            _CLIENTS_ENDPOINT, "clients", model.Client.from_json_dict
        )

    def list_links(self) -> List[model.Link]:
        """Returns the list of all registered links."""
        return self._get_all_entities(
            _LINKS_ENDPOINT, "links", model.Link.from_json_dict
        )

    def list_components(self) -> List[model.Component]:
        """Returns the list of all registered components."""
        return self._get_all_entities(
            _COMPONENTS_ENDPOINT, "components", model.Component.from_json_dict
        )

    def _get_all_entities(
        self, endpoint: str, collection_key: str, factory: Callable[[dict], _T]
    ) -> List[_T]:
        with self._client() as client:
            entities: List[_T] = []

            pages = _get_all_pages(client, endpoint)
            for page in pages:
                entities.extend([factory(d) for d in page.get(collection_key, [])])
            return entities

    def _client(self) -> httpx.Client:
        return httpx.Client(
            base_url=self._uri, timeout=self._timeout, verify=self._verify
        )


def _fetch(
    client: httpx.Client, uri: str, next_page_token: Optional[str] = None
) -> httpx.Response:
    params = None
    if next_page_token is not None:
        params = {"pageToken": next_page_token}
    resp = client.get(uri, params=params)
    resp.raise_for_status()
    return resp


def _get_all_pages(client: httpx.Client, uri: str) -> List[dict]:
    next_page_token: Optional[str] = None
    all_pages: List[dict] = []

    while True:
        resp = _fetch(client, uri, next_page_token)
        resp_json = resp.json()
        all_pages.append(resp_json)
        next_page_token = resp_json.get("nextPageToken")
        if next_page_token is None:
            return all_pages


class AsyncClient(_BaseClient):
    """Asynchronous Implementation of the Discovery Service API.

    Listing methods do pagination and always return all of the available objects.
    """

    async def get_environment(self) -> model.Environment:
        """Returns the information about the environment."""
        async with self._client() as client:
            resp = await _fetch_async(client, _ENVIRONMENT_ENDPOINT)
            return model.Environment.from_json_dict(resp.json()["environment"])

    async def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        return await self._get_all_entities(
            _SERVICES_ENDPOINT, "services", model.Service.from_json_dict
        )

    async def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        return await self._get_all_entities(
            _CLIENTS_ENDPOINT, "clients", model.Client.from_json_dict
        )

    async def list_links(self) -> List[model.Link]:
        """Returns the list of all registered links."""
        return await self._get_all_entities(
            _LINKS_ENDPOINT, "links", model.Link.from_json_dict
        )

    async def list_components(self) -> List[model.Component]:
        """Returns the list of all registered components."""
        return await self._get_all_entities(
            _COMPONENTS_ENDPOINT, "components", model.Component.from_json_dict
        )

    async def _get_all_entities(
        self, endpoint: str, collection_key: str, factory: Callable[[dict], _T]
    ) -> List[_T]:
        async with self._client() as client:
            entities: List[_T] = []

            pages = await _get_all_pages_async(client, endpoint)
            for page in pages:
                entities.extend([factory(d) for d in page.get(collection_key, [])])
            return entities

    def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            base_url=self._uri, timeout=self._timeout, verify=self._verify
        )


async def _fetch_async(
    client: httpx.AsyncClient, uri: str, next_page_token: Optional[str] = None
) -> httpx.Response:
    params = None
    if next_page_token is not None:
        params = {"pageToken": next_page_token}
    resp = await client.get(uri, params=params)
    resp.raise_for_status()
    return resp


async def _get_all_pages_async(client: httpx.AsyncClient, uri: str) -> List[dict]:
    next_page_token: Optional[str] = None
    all_pages: List[dict] = []

    while True:
        resp = await _fetch_async(client, uri, next_page_token)
        resp_json = resp.json()
        all_pages.append(resp_json)
        next_page_token = resp_json.get("nextPageToken")
        if next_page_token is None:
            return all_pages
