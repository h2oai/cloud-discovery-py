import dataclasses
from typing import Mapping
from typing import Optional


@dataclasses.dataclass(frozen=True)
class Service:
    """Internal representation of a registered service record."""

    # Name of the Service. For example: "services/my-service-name".
    name: str

    # Name of the Service that can be displayed on the front-end.
    display_name: str

    # URI for accessing the Service.
    uri: str

    # Version of the service. Can be the version of the API or the version of
    # the service. Clients can utilize this information change their behavior
    # in accessing the service or downloading the correct client version.
    version: Optional[str]

    # OAuth 2.0 Scope required to access the service. Clients request the
    # access token with this scope in order to access the service. If the scope
    # is not defined, clients should use h2o_cloud_platform_scope.
    oauth2_scope: Optional[str]

    # Requirement Specifier (PEP 508) for the Python client that can be used
    # for accessing the service.
    # Any string that can be `pip install`ed.
    #
    # Example: my-client==0.1.0
    python_client: Optional[str]

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
    """Internal representation of a registered client record."""

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
    """Internal representation of the environment."""

    # Identifier of the environment. For example: "https://cloud.h2o.ai".
    # This is the base URL of the environment. Clients can use this to validate
    # that they are talking to the correct environment.
    h2o_cloud_environment: str

    # OpenID Connect issuer_url. This is where clients find the OpenID Connect discovery
    # on the well-known endpoint.
    issuer_url: str

    # OAuth 2.0 scope that clients should use to access the H2O Cloud Platform.
    # This is the default scope that clients should use if the service does not
    # define its own scope.
    h2o_cloud_platform_oauth2_scope: str

    # Version of the H2O Cloud Platform release that is running in the environment.
    # In XC YY.MM.V format for released versions (e.g. MC 23.04.01 for managed
    # cloud or HC 23.01.1 for hybrid cloud). Can be arbitrary string for
    # testing environments.
    h2o_cloud_version: Optional[str]

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

    # Environment information.
    environment: Environment

    # Registered services.
    services: Mapping[str, Service]

    # Registered clients.
    clients: Mapping[str, Client]
