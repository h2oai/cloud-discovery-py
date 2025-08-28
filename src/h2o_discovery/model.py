import dataclasses
import types
from typing import Mapping
from typing import Optional


@dataclasses.dataclass(frozen=True)
class Service:
    """Representation of a registered service record."""

    #: Name of the Service. For example: "services/my-service-name".
    name: str

    #: Name of the Service that can be displayed on the front-end
    display_name: str

    #: URI for accessing the Service.
    #: This is usually the string that can be passed connection definition to the
    #: client for the particular service.
    uri: str

    #: Version of the service.
    #: Can be the version of the API or the version of
    #: the service. Clients can utilize this information change their behavior
    #: in accessing the service or downloading the correct client version.
    version: Optional[str] = None

    #: OAuth 2.0 Scope required to access the service.
    #: Clients request the access token with this scope in order to access the service.
    #: If the scope is not defined (or empty), clients should use
    #: h2o_cloud_platform_scope.
    oauth2_scope: Optional[str] = None

    #: Requirement Specifier (PEP 508) for the Python client that can be used for
    #: accessing the service.
    #: Any string that can be `pip install`ed.
    #:     Example: my-client==0.1.0
    python_client: Optional[str] = None

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

    #: Name of the Client. For example: "clients/h2o-public-client".
    name: str

    #: Name of the Client that can be displayed on the front-end.
    display_name: str

    #: Public OAuth 2.0 client ID that the client needs to use to identify
    #: itself with the IDP.
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

    #: Identifier of the environment. For example: "https://cloud.h2o.ai".
    #: This is the base URL of the environment. Clients can use this to validate
    #: that they are talking to the correct environment.
    h2o_cloud_environment: str

    #: OpenID Connect issuer_url.
    #: This is where clients find the OpenID Connect discovery on the well-known e
    #: endpoint.
    issuer_url: str

    #: OAuth 2.0 scope that clients should use to access the H2O Cloud Platform.
    #: This is the default scope that clients should use if the service does not
    #: define its own scope.
    h2o_cloud_platform_oauth2_scope: str

    #: Version of the H2O Cloud Platform release that is running in the environment.
    #: In the XC YY.MM.V format for released versions (e.g. MC 23.04.01 for managed
    #: cloud or HC 23.01.1 for hybrid cloud). Can be arbitrary string for
    #: testing or special environments.
    h2o_cloud_version: Optional[str] = None

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
class Link:
    """Representation of the navigation link."""

    #: Canonical name of the Link. For example: "links/app-link".
    name: str

    #: Value that applications can put into the HTML anchor's href
    #: attribute to navigate to link.
    uri: str

    #: Preferred text to use as a link text. This usually make sense
    #: only as part of the navigation menus.
    #:     Example: <a href="{{ link.uri }}">{{ link.text }}</a>
    text: Optional[str]

    @classmethod
    def from_json_dict(cls, json: Mapping[str, str]) -> "Link":
        """Create a Link from a JSON dict returned by the server."""
        return cls(name=json["name"], uri=json["uri"], text=json.get("text"))


@dataclasses.dataclass(frozen=True)
class Component:
    """Representation of a registered component record."""

    #: Name of the Component. For example: "components/h2o-component".
    name: str

    #: Name of the Component that can be displayed on the front-end.
    display_name: str

    #: Version of the component.
    version: str

    #: Description of the Component. This will be displayed on the front-end.
    #: This should explain what the component does and why it belongs
    #: in the environment.
    description: Optional[str] = None

    #: Link to the documentation of the Component. This will be used on the front-end
    #: (browser) as a link to the component's documentation.
    documentation_uri: Optional[str] = None

    @classmethod
    def from_json_dict(cls, json: Mapping[str, str]) -> "Component":
        """Create a Component from a JSON dict returned by the server."""
        return cls(
            name=json["name"],
            display_name=json["displayName"],
            version=json["version"],
            description=json.get("description"),
            documentation_uri=json.get("documentationUri"),
        )


@dataclasses.dataclass(frozen=True)
class Credentials:
    """Contain credentials associated with single registered client.

    Credentials are only determined locally and are not returned by the server.
    """

    #: Client identifier that the credentials are associated with.
    client: str

    #: Opaque string containing refresh token that can be used to obtain access token.
    refresh_token: str = dataclasses.field(
        # We don't want to show the refresh token to accidentally leak when printing
        # the object.
        repr=False
    )


def _empty_credentials_factory() -> Mapping[str, Credentials]:
    return types.MappingProxyType({})


def _empty_links_factory() -> Mapping[str, Link]:
    return types.MappingProxyType({})


def _empty_components_factory() -> Mapping[str, Component]:
    return types.MappingProxyType({})


@dataclasses.dataclass(frozen=True)
class Discovery:
    """Representation of the discovery records."""

    #: Information about the environment.
    environment: Environment

    #: Map of registered services in the `{"service-identifier": Service(...)}` format.
    services: Mapping[str, Service]

    #: Map of registered clients in the `{"client-identifier": Client(...)}` format.
    clients: Mapping[str, Client]

    #: Map of registered links in the `{"link-identifier": Link(...)}` format.
    links: Mapping[str, Link] = dataclasses.field(default_factory=_empty_links_factory)

    #: Map of registered components in the
    #: `{"component-identifier": Component(...)}` format.
    components: Mapping[str, Component] = dataclasses.field(
        default_factory=_empty_components_factory
    )

    #: Map of credentials in the `{"client-identifier": Credentials(...)}` format.
    credentials: Mapping[str, Credentials] = dataclasses.field(
        default_factory=_empty_credentials_factory
    )
