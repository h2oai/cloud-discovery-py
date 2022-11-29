import dataclasses
from typing import Mapping
from typing import Optional


@dataclasses.dataclass(frozen=True)
class Service:
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
    # access token with this scope in order to access the service. If the scop
    # is not defined, clients should use h2o_cloud_platform_scope.
    oauth2_scope: Optional[str]

    # Requirement Specifier (PEP 508) for the Python client that can be used
    # for accessing the service.
    # Any string that can be `pip install`ed.
    #
    # Example: my-client==0.1.0
    python_client: Optional[str]

    @classmethod
    def from_json(cls, json: Mapping[str, str]) -> "Service":
        """Create a Service from a JSON object."""
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
    # Name of the Client. For example: "clients/h2o-public-client".
    name: str

    # Name of the Client that can be displayed on the front-end.
    display_name: str

    # Public OAuth 2.0 client ID that the client needs to use to identify
    # itself with the IDP.
    oauth2_client_id: str

    @classmethod
    def from_json(cls, json: Mapping[str, str]) -> "Client":
        """Create a Client from a JSON dict returned by the server."""
        return cls(
            name=json["name"],
            display_name=json["displayName"],
            oauth2_client_id=json["oauth2ClientId"],
        )


@dataclasses.dataclass(frozen=True)
class Environment:
    h2o_cloud_environment: str
    issuer_url: str
    h2o_cloud_platform_oauth2_scope: str

    @classmethod
    def from_json(cls, json: Mapping[str, str]) -> "Environment":
        """Create an Environment from a JSON dict returned by the server."""
        return cls(
            h2o_cloud_environment=json["h2oCloudEnvironment"],
            issuer_url=json["issuerUrl"],
            h2o_cloud_platform_oauth2_scope=json["h2oCloudPlatformOauth2Scope"],
        )
