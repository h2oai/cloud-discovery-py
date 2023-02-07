from typing import List
from typing import Optional

import httpx

from h2o_discovery import model
from h2o_discovery import client


class AsyncClient:
    """Asynchronous Implementation of the Discovery Service API.

    Listing methods do pagination and always return all of the available objects.
    """

    def __init__(self, uri: str):
        self._environment_uri = client.get_environment_uri(uri)
        self._services_uri = client.get_services_uri(uri)
        self._clients_uri = client.get_clients_uri(uri)

    async def get_environment(self) -> model.Environment:
        """Returns the information about the environment."""
        async with httpx.AsyncClient() as client:
            resp = await _fetch(client, self._environment_uri)
            return model.Environment.from_json_dict(resp.json()["environment"])

    async def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        async with httpx.AsyncClient() as client:
            services: List[model.Service] = []

            pages = await _get_all_pages(client, self._services_uri)
            for page in pages:
                services.extend(
                    [model.Service.from_json_dict(d) for d in page.get("services", [])]
                )
            return services

    async def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        async with httpx.AsyncClient() as client:
            clients: List[model.Client] = []

            pages = await _get_all_pages(client, self._clients_uri)
            for page in pages:
                clients.extend(
                    [model.Client.from_json_dict(d) for d in page.get("clients", [])]
                )
            return clients


async def _fetch(
    client: httpx.AsyncClient, uri: str, next_page_token: Optional[str] = None
) -> httpx.Response:
    params = None
    if next_page_token is not None:
        params = {"pageToken": next_page_token}
    resp = await client.get(uri, params=params)
    resp.raise_for_status()
    return resp


async def _get_all_pages(client: httpx.AsyncClient, uri: str) -> List[dict]:
    next_page_token: Optional[str] = None
    all_pages: List[dict] = []

    while True:
        resp = await _fetch(client, uri, next_page_token)
        resp_json = resp.json()
        all_pages.append(resp_json)
        next_page_token = resp_json.get("nextPageToken")
        if next_page_token is None:
            return all_pages
