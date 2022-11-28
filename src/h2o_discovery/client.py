from typing import List
from typing import Optional

import httpx

from h2o_discovery import model


class Client:
    def __init__(self, uri: str):
        self._uri = uri

    def get_environment(self) -> model.Environment:
        with httpx.Client() as client:
            resp = self._fetch_environment(client)
            return model.Environment.from_json(resp.json())

    def list_services(self) -> List[model.Service]:
        with httpx.Client() as client:
            next_page_token: Optional[str] = None
            services: List[model.Service] = []

            while True:
                resp = self._fetch_services(client, next_page_token).json()
                services.extend([model.Service.from_json(d) for d in resp["services"]])
                next_page_token = resp.get("nextPageToken")
                if next_page_token is None:
                    return services

    def list_clients(self) -> List[model.Client]:
        with httpx.Client() as client:
            next_page_token: Optional[str] = None
            clients: List[model.Client] = []

            while True:
                resp = self._fetch_clients(client, next_page_token).json()
                clients.extend([model.Client.from_json(d) for d in resp["clients"]])
                next_page_token = resp.get("nextPageToken")
                if next_page_token is None:
                    return clients

    def _fetch_environment(self, client: httpx.Client) -> httpx.Response:
        return self._fetch(client, self._uri + "/v1/environment")

    def _fetch_services(
        self, client: httpx.Client, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        return self._fetch(
            client, self._uri + "/v1/services", next_page_token=next_page_token
        )

    def _fetch_clients(
        self, client: httpx.Client, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        return self._fetch(
            client, self._uri + "/v1/clients", next_page_token=next_page_token
        )

    def _fetch(
        self, client: httpx.Client, uri: str, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        params = None
        if next_page_token is not None:
            params = {"nextPageToken": next_page_token}
        resp = client.get(uri, params=params)
        resp.raise_for_status()
        return resp
