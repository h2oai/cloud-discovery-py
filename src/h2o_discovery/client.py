from typing import List
from typing import Optional

import httpx

from h2o_discovery import model


class Client:
    def __init__(self, uri: str):
        self._uri = uri

    async def get_environment(self) -> model.Environment:
        async with httpx.AsyncClient() as client:
            resp = await self._fetch_environment(client)
            return model.Environment.from_json(resp.json()["environment"])

    async def list_services(self) -> List[model.Service]:
        async with httpx.AsyncClient() as client:
            next_page_token: Optional[str] = None
            services: List[model.Service] = []

            while True:
                resp = await self._fetch_services(client, next_page_token)
                resp_json = resp.json()
                services.extend(
                    [model.Service.from_json(d) for d in resp_json["services"]]
                )
                next_page_token = resp_json.get("nextPageToken")
                if next_page_token is None:
                    return services

    async def list_clients(self) -> List[model.Client]:
        async with httpx.AsyncClient() as client:
            next_page_token: Optional[str] = None
            clients: List[model.Client] = []

            while True:
                resp = await self._fetch_clients(client, next_page_token)
                resp_json = resp.json()
                clients.extend(
                    [model.Client.from_json(d) for d in resp_json["clients"]]
                )
                next_page_token = resp_json.get("nextPageToken")
                if next_page_token is None:
                    return clients

    async def _fetch_environment(self, client: httpx.AsyncClient) -> httpx.Response:
        return await self._fetch(client, self._uri + "/v1/environment")

    async def _fetch_services(
        self, client: httpx.AsyncClient, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        return await self._fetch(
            client, self._uri + "/v1/services", next_page_token=next_page_token
        )

    async def _fetch_clients(
        self, client: httpx.AsyncClient, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        return await self._fetch(
            client, self._uri + "/v1/clients", next_page_token=next_page_token
        )

    async def _fetch(
        self, client: httpx.AsyncClient, uri: str, next_page_token: Optional[str] = None
    ) -> httpx.Response:
        params = None
        if next_page_token is not None:
            params = {"pageToken": next_page_token}
        resp = await client.get(uri, params=params)
        resp.raise_for_status()
        return resp
