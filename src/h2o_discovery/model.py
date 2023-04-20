import dataclasses
from typing import Mapping
from typing import Optional


@dataclasses.dataclass(frozen=True)
class Service:
    """Representation of a registered service record."""

    name: str
    """Name of the Service.

    For example: "services/my-service-name".
    """

    display_name: str
    """Name of the Service that can be displayed on the front-end."""

    uri: str
    """URI for accessing the Service.

    This is usually the string that can be passed connection definition to the
    client for the particular service.
    """

    version: Optional[str]
    """Version of the service.

    Can be the version of the API or the version of
    the service. Clients can utilize this information change their behavior
    in accessing the service or downloading the correct client version.
    """

    oauth2_scope: Optional[str]
    """OAuth 2.0 Scope required to access the service.

    Clients request the access token with this scope in order to access the service.
    If the scope is not defined (or empty), clients should use
    h2o_cloud_platform_scope.
    """

    python_client: Optional[str]
    """Requirement Specifier (PEP 508) for the Python client that can be used for
    accessing the service.

    Any string that can be `pip install`ed.
        Example: my-client==0.1.0
    """

    @classmethod
    def from_json_dict(cls, json: Mapping[str, str]) -> "Service":
        """Create a Service from a JSON dict returned by the server."""
        return cls(
            name=json["name"],
            display_name=json["displayName"],
            uri=json["uri"],
            version=json.get("version"),
            oauth2_scope=json.get("oauth2Scope"),
            python_client=json.get("pythonClient"),
        )


@dataclasses.dataclass(frozen=True)
class Client:
    """Representation of a registered client record."""

    # Name of the Client. For example: "clients/h2o-public-client".
    name: str

    # Name of the Client that can be displayed on the front-end.
    display_name: str

    # Public OAuth 2.0 client ID that the client needs to use to identify
    # itself with the IDP.
    oauth2_client_id: str

    @classmethod
    def from_json_dict(cls, json: Mapping[str, str]) -> "Client":
        """Create a Client from a JSON dict returned by the server."""
        return cls(
            name=json["name"],
            display_name=json["displayName"],
            oauth2_client_id=json["oauth2ClientId"],
        )


@dataclasses.dataclass(frozen=True)
class Environment:
    """Representation of the information about the H2O Cloud environment."""

    h2o_cloud_environment: str
    """Identifier of the environment.

    For example: "https://cloud.h2o.ai".

    This is the base URL of the environment. Clients can use this to validate
    that they are talking to the correct environment.
    """

    issuer_url: str
    """OpenID Connect issuer_url.

    This is where clients find the OpenID Connect discovery on the well-known endpoint.
    """

    h2o_cloud_platform_oauth2_scope: str
    """OAuth 2.0 scope that clients should use to access the H2O Cloud Platform.

    This is the default scope that clients should use if the service does not
    define its own scope.
    """

    h2o_cloud_version: Optional[str]
    """Version of the H2O Cloud Platform release that is running in the environment.

    In XC YY.MM.V format for released versions (e.g. MC 23.04.01 for managed
    cloud or HC 23.01.1 for hybrid cloud). Can be arbitrary string for
    testing or special environments.
    """

    @classmethod
    def from_json_dict(cls, json: Mapping[str, str]) -> "Environment":
        """Create an Environment from a JSON dict returned by the server."""
        return cls(
            h2o_cloud_environment=json["h2oCloudEnvironment"],
            issuer_url=json["issuerUrl"],
            h2o_cloud_platform_oauth2_scope=json["h2oCloudPlatformOauth2Scope"],
            h2o_cloud_version=json.get("h2oCloudVersion"),
        )


@dataclasses.dataclass(frozen=True)
class Discovery:
    """Representation of the discovery records."""

    environment: Environment
    """Information about the environment."""

    services: Mapping[str, Service]
    """Map of registered services in the {"service-identifier": Service(...)} format."""

    clients: Mapping[str, Client]
    """Map of registered clients in the {"client-identifier": Client(...)} format."""
