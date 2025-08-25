import httpx
import pytest
import respx

from h2o_discovery import model
from h2o_discovery._internal import client


@respx.mock
def test_client_get_environment_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/environment").respond(
        json=ENVIRONMENT_JSON
    )
    cl = client.Client("http://test.example.com:1234")

    # When
    env = cl.get_environment()

    # Then
    assert route.called
    assert env == EXPECTED_ENVIRONMENT_DATA


@respx.mock
def test_client_get_environment_public():
    # Given
    route = respx.get(
        "https://test.example.com/.ai.h2o.cloud.discovery/v1/environment"
    ).respond(json=ENVIRONMENT_JSON)
    cl = client.Client("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    env = cl.get_environment()

    # Then
    assert route.called
    assert env == EXPECTED_ENVIRONMENT_DATA


@respx.mock
@pytest.mark.asyncio
async def test_async_client_get_environment_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/environment").respond(
        json=ENVIRONMENT_JSON
    )
    cl = client.AsyncClient("http://test.example.com:1234")

    # When
    env = await cl.get_environment()

    # Then
    assert route.called
    assert env == EXPECTED_ENVIRONMENT_DATA


@respx.mock
@pytest.mark.asyncio
async def test_async_client_get_environment_public():
    # Given
    route = respx.get(
        "https://test.example.com/.ai.h2o.cloud.discovery/v1/environment"
    ).respond(json=ENVIRONMENT_JSON)
    cl = client.AsyncClient("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    env = await cl.get_environment()

    # Then
    assert route.called
    assert env == EXPECTED_ENVIRONMENT_DATA


@respx.mock
def test_client_list_services_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/services")
    route.side_effect = SERVICES_RESPONSES

    cl = client.Client("http://test.example.com:1234")

    # When
    services = cl.list_services()

    # Then
    assert services == EXPECTED_SERVICES_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_services_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/services")
    route.side_effect = SERVICES_RESPONSES

    cl = client.Client("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    services = cl.list_services()

    # Then
    assert services == EXPECTED_SERVICES_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_services_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/services")
    route.side_effect = SERVICES_RESPONSES

    cl = client.AsyncClient("http://test.example.com:1234")

    # When
    services = await cl.list_services()

    # Then
    assert services == EXPECTED_SERVICES_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_services_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/services")
    route.side_effect = SERVICES_RESPONSES

    cl = client.AsyncClient("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    services = await cl.list_services()

    # Then
    assert services == EXPECTED_SERVICES_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_clients_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/clients")
    route.side_effect = CLIENTS_RESPONSES

    cl = client.Client("http://test.example.com:1234")

    # When
    clients = cl.list_clients()

    # Then

    assert clients == EXPECTED_CLIENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_clients_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/clients")
    route.side_effect = CLIENTS_RESPONSES

    cl = client.Client("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    clients = cl.list_clients()

    # Then

    assert clients == EXPECTED_CLIENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_clients_internal():
    # Given
    route = respx.get("https://test.example.com:1234/v1/clients")
    route.side_effect = CLIENTS_RESPONSES

    cl = client.AsyncClient("https://test.example.com:1234")

    # When
    clients = await cl.list_clients()

    # Then

    assert clients == EXPECTED_CLIENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_clients_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/clients")
    route.side_effect = CLIENTS_RESPONSES

    cl = client.AsyncClient("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    clients = await cl.list_clients()

    # Then

    assert clients == EXPECTED_CLIENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_links_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/links")
    route.side_effect = LINKS_RESPONSES

    cl = client.Client("http://test.example.com:1234")

    # When
    links = cl.list_links()

    # Then
    assert links == EXPECTED_LINKS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_links_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/links")
    route.side_effect = LINKS_RESPONSES

    cl = client.Client("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    links = cl.list_links()

    # Then
    assert links == EXPECTED_LINKS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_links_internal():
    # Given
    route = respx.get("https://test.example.com:1234/v1/links")
    route.side_effect = LINKS_RESPONSES

    cl = client.AsyncClient("https://test.example.com:1234")

    # When
    links = await cl.list_links()

    # Then
    assert links == EXPECTED_LINKS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_links_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/links")
    route.side_effect = LINKS_RESPONSES

    cl = client.AsyncClient("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    links = await cl.list_links()

    # Then
    assert links == EXPECTED_LINKS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_components_internal():
    # Given
    route = respx.get("http://test.example.com:1234/v1/components")
    route.side_effect = COMPONENTS_RESPONSES

    cl = client.Client("http://test.example.com:1234")

    # When
    components = cl.list_components()

    # Then
    assert components == EXPECTED_COMPONENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_components_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/components")
    route.side_effect = COMPONENTS_RESPONSES

    cl = client.Client("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    components = cl.list_components()

    # Then
    assert components == EXPECTED_COMPONENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_components_internal():
    # Given
    route = respx.get("https://test.example.com:1234/v1/components")
    route.side_effect = COMPONENTS_RESPONSES

    cl = client.AsyncClient("https://test.example.com:1234")

    # When
    components = await cl.list_components()

    # Then
    assert components == EXPECTED_COMPONENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_components_public():
    # Given
    route = respx.get("https://test.example.com/.ai.h2o.cloud.discovery/v1/components")
    route.side_effect = COMPONENTS_RESPONSES

    cl = client.AsyncClient("https://test.example.com/.ai.h2o.cloud.discovery")

    # When
    components = await cl.list_components()

    # Then
    assert components == EXPECTED_COMPONENTS_RECORDS
    _assert_pagination_api_calls(route)


@respx.mock
def test_client_list_services_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/services").respond(json={})
    cl = client.Client("https://test.example.com")

    # When
    services = cl.list_services()

    # Then
    assert services == []


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_services_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/services").respond(json={})
    cl = client.AsyncClient("https://test.example.com")

    # When
    services = await cl.list_services()

    # Then
    assert services == []


@respx.mock
def test_client_list_clients_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/clients").respond(json={})
    cl = client.Client("https://test.example.com")

    # When
    services = cl.list_clients()

    # Then
    assert services == []


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_clients_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/clients").respond(json={})
    cl = client.AsyncClient("https://test.example.com")

    # When
    services = await cl.list_clients()

    # Then
    assert services == []


@respx.mock
def test_client_list_links_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/links").respond(json={})
    cl = client.Client("https://test.example.com")

    # When
    links = cl.list_links()

    # Then
    assert links == []


@respx.mock
@pytest.mark.asyncio
async def test_async_client_list_links_can_handle_empty_response():
    # Given
    respx.get("https://test.example.com/v1/links").respond(json={})
    cl = client.AsyncClient("https://test.example.com")

    # When
    links = await cl.list_links()

    # Then
    assert links == []


def _assert_pagination_api_calls(route):
    assert route.call_count == 3
    assert not route.calls[0].request.url.query
    assert route.calls[1].request.url.query == b"pageToken=next-page-token-1"
    assert route.calls[2].request.url.query == b"pageToken=next-page-token-2"


ENVIRONMENT_JSON = {
    "environment": {
        "h2oCloudEnvironment": "https://cloud.fbi.com",
        "h2oCloudPlatformOauth2Scope": "openid profile email",
        "issuerUrl": "https://phantauth.net",
        "h2oCloudVersion": "70.25",
    }
}

EXPECTED_ENVIRONMENT_DATA = model.Environment(
    h2o_cloud_environment="https://cloud.fbi.com",
    h2o_cloud_platform_oauth2_scope="openid profile email",
    issuer_url="https://phantauth.net",
    h2o_cloud_version="70.25",
)

SERVICES_RESPONSES = [
    httpx.Response(
        200,
        json={
            "services": [
                {
                    "name": "services/test-service-1",
                    "displayName": "Test Service 1 ",
                    "uri": "http://test-service-1.domain:1234",
                    "version": "1.0.0",
                    "oauth2Scope": "test-service-scope-1",
                    "pythonClient": "test-client-1==1.0.0",
                },
                {
                    "name": "services/test-service-2",
                    "displayName": "Test Service 2",
                    "uri": "http://test-service-2.domain:1234",
                },
            ],
            "nextPageToken": "next-page-token-1",
        },
    ),
    httpx.Response(
        200,
        json={
            "services": [
                {
                    "name": "services/test-service-3",
                    "displayName": "Test Service 3",
                    "uri": "http://test-service-3.domain:1234",
                }
            ],
            "nextPageToken": "next-page-token-2",
        },
    ),
    httpx.Response(
        200,
        json={
            "services": [
                {
                    "name": "services/test-service-4",
                    "displayName": "Test Service 4",
                    "uri": "http://test-service-4.domain:1234",
                }
            ]
        },
    ),
]

EXPECTED_SERVICES_RECORDS = [
    model.Service(
        name="services/test-service-1",
        display_name="Test Service 1 ",
        uri="http://test-service-1.domain:1234",
        version="1.0.0",
        oauth2_scope="test-service-scope-1",
        python_client="test-client-1==1.0.0",
    ),
    model.Service(
        name="services/test-service-2",
        display_name="Test Service 2",
        uri="http://test-service-2.domain:1234",
    ),
    model.Service(
        name="services/test-service-3",
        display_name="Test Service 3",
        uri="http://test-service-3.domain:1234",
    ),
    model.Service(
        name="services/test-service-4",
        display_name="Test Service 4",
        uri="http://test-service-4.domain:1234",
    ),
]

CLIENTS_RESPONSES = [
    httpx.Response(
        200,
        json={
            "clients": [
                {
                    "name": "clients/test-client-1",
                    "displayName": "Test Client 1",
                    "oauth2ClientId": "test-client-1",
                },
                {
                    "name": "clients/test-client-2",
                    "displayName": "Test Client 2",
                    "oauth2ClientId": "test-client-2",
                },
            ],
            "nextPageToken": "next-page-token-1",
        },
    ),
    httpx.Response(
        200,
        json={
            "clients": [
                {
                    "name": "clients/test-client-3",
                    "displayName": "Test Client 3",
                    "oauth2ClientId": "test-client-3",
                }
            ],
            "nextPageToken": "next-page-token-2",
        },
    ),
    httpx.Response(
        200,
        json={
            "clients": [
                {
                    "name": "clients/test-client-4",
                    "displayName": "Test Client 4",
                    "oauth2ClientId": "test-client-4",
                }
            ]
        },
    ),
]

EXPECTED_CLIENTS_RECORDS = [
    model.Client(
        name="clients/test-client-1",
        display_name="Test Client 1",
        oauth2_client_id="test-client-1",
    ),
    model.Client(
        name="clients/test-client-2",
        display_name="Test Client 2",
        oauth2_client_id="test-client-2",
    ),
    model.Client(
        name="clients/test-client-3",
        display_name="Test Client 3",
        oauth2_client_id="test-client-3",
    ),
    model.Client(
        name="clients/test-client-4",
        display_name="Test Client 4",
        oauth2_client_id="test-client-4",
    ),
]


LINKS_RESPONSES = [
    httpx.Response(
        200,
        json={
            "links": [
                {"name": "links/test-link-1", "uri": "http://test-link-1.domain:1234"},
                {
                    "name": "links/test-link-2",
                    "uri": "http://test-link-2.domain:1234",
                    "text": "Test Link 2",
                },
            ],
            "nextPageToken": "next-page-token-1",
        },
    ),
    httpx.Response(
        200,
        json={
            "links": [
                {
                    "name": "links/test-link-3",
                    "uri": "http://test-link-3.domain:1234",
                    "text": "Test Link 3",
                }
            ],
            "nextPageToken": "next-page-token-2",
        },
    ),
    httpx.Response(
        200,
        json={
            "links": [
                {"name": "links/test-link-4", "uri": "http://test-link-4.domain:1234"}
            ]
        },
    ),
]

EXPECTED_LINKS_RECORDS = [
    model.Link(
        name="links/test-link-1", uri="http://test-link-1.domain:1234", text=None
    ),
    model.Link(
        name="links/test-link-2",
        uri="http://test-link-2.domain:1234",
        text="Test Link 2",
    ),
    model.Link(
        name="links/test-link-3",
        uri="http://test-link-3.domain:1234",
        text="Test Link 3",
    ),
    model.Link(
        name="links/test-link-4", uri="http://test-link-4.domain:1234", text=None
    ),
]

COMPONENTS_RESPONSES = [
    httpx.Response(
        200,
        json={
            "components": [
                {
                    "name": "components/test-component-1",
                    "displayName": "Test Component 1",
                    "version": "1.0.0",
                    "description": "Test Description 1",
                    "documentationUri": "https://example.com/docs/test-component-1",
                },
                {
                    "name": "components/test-component-2",
                    "displayName": "Test Component 2",
                    "version": "2.0.0",
                },
            ],
            "nextPageToken": "next-page-token-1",
        },
    ),
    httpx.Response(
        200,
        json={
            "components": [
                {
                    "name": "components/test-component-3",
                    "displayName": "Test Component 3",
                    "version": "3.0.0",
                    "documentationUri": "https://example.com/docs/test-component-3",
                }
            ],
            "nextPageToken": "next-page-token-2",
        },
    ),
    httpx.Response(
        200,
        json={
            "components": [
                {
                    "name": "components/test-component-4",
                    "displayName": "Test Component 4",
                    "version": "4.0.0",
                    "description": "Test Description 4",
                }
            ]
        },
    ),
]

EXPECTED_COMPONENTS_RECORDS = [
    model.Component(
        name="components/test-component-1",
        display_name="Test Component 1",
        description="Test Description 1",
        version="1.0.0",
        documentation_uri="https://example.com/docs/test-component-1",
    ),
    model.Component(
        name="components/test-component-2",
        display_name="Test Component 2",
        version="2.0.0",
    ),
    model.Component(
        name="components/test-component-3",
        display_name="Test Component 3",
        version="3.0.0",
        documentation_uri="https://example.com/docs/test-component-3",
    ),
    model.Component(
        name="components/test-component-4",
        display_name="Test Component 4",
        version="4.0.0",
        description="Test Description 4",
    ),
]
