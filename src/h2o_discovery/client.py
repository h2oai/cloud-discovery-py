from typing import Optional
from typing import List

import httpx

from h2o_discovery import config
from h2o_discovery import model


def New(environment: Optional[str] = None, discovery: Optional[str] = None):
    uri = config.FindURI(environment, discovery)
    return Client(uri)


class Client:
    def __init__(self, uri: str):
        self._uri = uri

    def get_environment(self) -> model.Environment:
        with httpx.Client() as client:
            resp = self._fetch_environment(client)
            return model.Environment.from_json(resp.json())

    def list_services(self) -> List[model.Service]:
        with httpx.Client() as client:
            resp = self._fetch(client, self._uri + "/v1/services")
            return [model.Service.from_json(d) for d in resp.json()]

    def list_clients(self) -> List[model.Client]:
        with httpx.Client() as client:
            resp = self._fetch(client, self._uri + "/v1/clients")
            return [model.Client.from_json(d) for d in resp.json()]

    def _fetch_environment(self, client: httpx.Client) -> httpx.Response:
        return client.get(self._uri + "/v1/environment")

    def _fetch(self, client: httpx.Client, uri: str) -> httpx.Response:
        resp = client.get(uri)
        resp.raise_for_status()
        return resp
