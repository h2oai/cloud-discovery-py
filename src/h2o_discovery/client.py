import urllib.parse
from typing import List
from typing import Optional

import httpx

from h2o_discovery import model


ENVIRONMENT_ENDPOINT = "/v1/environment"
SERVICES_ENDPOINT = "/v1/services"
CLIENTS_ENDPOINT = "/v1/clients"


def get_environment_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, ENVIRONMENT_ENDPOINT)


def get_services_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, SERVICES_ENDPOINT)


def get_clients_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, CLIENTS_ENDPOINT)


class Client:
    """Synchronous Implementation of the Discovery Service API.

    Listing methods do pagination and always return all of the available objects.
    """

    def __init__(self, uri: str):
        self._uri = uri

        self._environment_uri = get_environment_uri(uri)
        self._services_uri = get_services_uri(uri)
        self._clients_uri = get_clients_uri(uri)

    def get_environment(self) -> model.Environment:
        """Returns the information about the environment."""
        with httpx.Client() as client:
            resp = _fetch(client, self._environment_uri)
            return model.Environment.from_json_dict(resp.json()["environment"])

    def list_services(self) -> List[model.Service]:
        """Returns the list of all registered services."""
        with httpx.Client() as client:
            services: List[model.Service] = []

            pages = _get_all_pages(client, self._services_uri)
            for page in pages:
                services.extend(
                    [model.Service.from_json_dict(d) for d in page.get("services", [])]
                )
            return services

    def list_clients(self) -> List[model.Client]:
        """Returns the list of all registered clients."""
        with httpx.Client() as client:
            clients: List[model.Client] = []

            pages = _get_all_pages(client, self._clients_uri)
            for page in pages:
                clients.extend(
                    [model.Client.from_json_dict(d) for d in page.get("clients", [])]
                )
            return clients


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
