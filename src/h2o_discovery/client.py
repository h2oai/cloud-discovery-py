import urllib.parse


ENVIRONMENT_ENDPOINT = "/v1/environment"
SERVICES_ENDPOINT = "/v1/services"
CLIENTS_ENDPOINT = "/v1/clients"


def get_environment_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, ENVIRONMENT_ENDPOINT)


def get_services_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, SERVICES_ENDPOINT)


def get_clients_uri(uri: str) -> str:
    return urllib.parse.urljoin(uri, CLIENTS_ENDPOINT)
