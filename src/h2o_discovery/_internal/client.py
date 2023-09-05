import datetime
import ssl
from typing import List
from typing import Optional
from typing import Union

import httpx

from h2o_discovery import model

_ENVIRONMENT_ENDPOINT = "v1/environment"
_SERVICES_ENDPOINT = "v1/services"
_CLIENTS_ENDPOINT = "v1/clients"

DEFAULT_HTTP_TIMEOUT = datetime.timedelta(seconds=5)


class _BaseClient:
    def __init__(
        self,
        uri: str,
        timeout: Optional[datetime.timedelta] = None,
        ssl_context: Optional[ssl.SSLContext] = None,
    ):
        self._uri = uri
        self._ssl_context = ssl_context

        self._timeout = 5.0
        if timeout is not None:
            self._timeout = timeout.total_seconds()

        self._verify: Union[bool, ssl.SSLContext] = True
        if self._ssl_context is not None:
            self._verify = self._ssl_context


class Client(_BaseClient):
    """Synchronous Implementation of the Discovery Service API.

    Listing methods do pagination and always return all of the available objects.
    """

    def __init__(self, uri: str):
        self._uri = uri

    def get_environment(self) -> model.Environment:
        """Returns the information about the environment."""
        with httpx.Client(base_url=self._uri) as client:
            resp = _fetch(client, _ENVIRONMENT_ENDPOINT)
            return model.Environment.from_json_dict(resp.json()["environment"])

    def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        with httpx.Client(base_url=self._uri) as client:
            services: List[model.Service] = []

            pages = _get_all_pages(client, _SERVICES_ENDPOINT)
            for page in pages:
                services.extend(
                    [model.Service.from_json_dict(d) for d in page.get("services", [])]
                )
            return services

    def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        with httpx.Client(base_url=self._uri) as client:
            clients: List[model.Client] = []

            pages = _get_all_pages(client, _CLIENTS_ENDPOINT)
            for page in pages:
                clients.extend(
                    [model.Client.from_json_dict(d) for d in page.get("clients", [])]
                )
            return clients

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
        async with httpx.AsyncClient(base_url=self._uri) as client:
            resp = await _fetch_async(client, _ENVIRONMENT_ENDPOINT)
            return model.Environment.from_json_dict(resp.json()["environment"])

    async def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        async with httpx.AsyncClient(base_url=self._uri) as client:
            services: List[model.Service] = []

            pages = await _get_all_pages_async(client, _SERVICES_ENDPOINT)
            for page in pages:
                services.extend(
                    [model.Service.from_json_dict(d) for d in page.get("services", [])]
                )
            return services

    async def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        async with httpx.AsyncClient(base_url=self._uri) as client:
            clients: List[model.Client] = []

            pages = await _get_all_pages_async(client, _CLIENTS_ENDPOINT)
            for page in pages:
                clients.extend(
                    [model.Client.from_json_dict(d) for d in page.get("clients", [])]
                )
            return clients

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
