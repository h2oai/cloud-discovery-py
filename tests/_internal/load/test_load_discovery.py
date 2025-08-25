import asyncio
from unittest import mock

import httpx
import pytest

from h2o_discovery import model
from h2o_discovery._internal import load


def mock_async_client():
    client = mock.Mock()
    client.get_environment.return_value = asyncio.Future()
    client.get_environment.return_value.set_result(mock.Mock())
    client.list_services.return_value = asyncio.Future()
    client.list_services.return_value.set_result({})
    client.list_clients.return_value = asyncio.Future()
    client.list_clients.return_value.set_result({})
    client.list_links.return_value = asyncio.Future()
    client.list_links.return_value.set_result({})
    client.list_components.return_value = asyncio.Future()
    client.list_components.return_value.set_result({})

    return client


def mock_sync_client():
    client = mock.Mock()
    client.get_environment.return_value = {}
    client.list_services.return_value = {}
    client.list_clients.return_value = {}
    client.list_clients.return_value = {}
    client.list_links.return_value = {}
    client.list_components.return_value = {}

    return client


ENVIRONMENT_DATA = model.Environment(
    h2o_cloud_environment="https://test.example.com",
    h2o_cloud_platform_oauth2_scope="test-scope",
    issuer_url="https://test.example.com",
    h2o_cloud_version="test-version",
)


def test_load_environment():
    # Given
    mock_client = mock_sync_client()
    mock_client.get_environment.return_value = ENVIRONMENT_DATA

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.environment == ENVIRONMENT_DATA


@pytest.mark.asyncio
async def test_load_environment_async():
    # Given
    mock_client = mock_async_client()
    mock_client.get_environment.return_value = asyncio.Future()
    mock_client.get_environment.return_value.set_result(ENVIRONMENT_DATA)

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.environment == ENVIRONMENT_DATA


def test_load_services():
    # Given
    mock_client = mock_sync_client()
    mock_client.list_services.return_value = [SERVICE_RECORD]

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.services["test-service"] == SERVICE_RECORD


SERVICE_RECORD = model.Service(
    name="services/test-service",
    display_name="Test Service",
    uri="http://test-service.domain:1234",
    version="1.0.0",
    oauth2_scope="test-service-scope",
    python_client="test-client==1.0.0",
)


@pytest.mark.asyncio
async def test_load_services_async():
    # Given
    mock_client = mock_async_client()
    mock_client.list_services.return_value = asyncio.Future()
    mock_client.list_services.return_value.set_result([SERVICE_RECORD])

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.services["test-service"] == SERVICE_RECORD


CLIENT_RECORD = model.Client(
    name="clients/test-client",
    display_name="Test Client",
    oauth2_client_id="test-client-id",
)


def test_load_clients():
    # Given
    mock_client = mock_sync_client()
    mock_client.list_clients.return_value = [CLIENT_RECORD]

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.clients["test-client"] == CLIENT_RECORD


@pytest.mark.asyncio
async def test_load_clients_async():
    # Given
    mock_client = mock_async_client()
    mock_client.list_clients.return_value = asyncio.Future()
    mock_client.list_clients.return_value.set_result([CLIENT_RECORD])

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.clients["test-client"] == CLIENT_RECORD


LINK_RECORD = model.Link(
    name="links/test-link", uri="http://test-link.domain:1234", text="Test Link"
)


def test_load_links():
    # Given
    mock_client = mock_sync_client()
    mock_client.list_links.return_value = [LINK_RECORD]

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.links["test-link"] == LINK_RECORD


@pytest.mark.asyncio
async def test_load_links_async():
    # Given
    mock_client = mock_async_client()
    mock_client.list_links.return_value = asyncio.Future()
    mock_client.list_links.return_value.set_result([LINK_RECORD])

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.links["test-link"] == LINK_RECORD


def test_load_links_not_found_returns_empty_map():
    # Given
    not_found_exception = httpx.HTTPStatusError(
        "Test Error", request=mock.Mock(), response=mock.Mock(status_code=404)
    )
    mock_client = mock_sync_client()
    mock_client.list_links.side_effect = not_found_exception

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.links == {}


@pytest.mark.asyncio
async def test_load_links_async_not_found_returns_empty_map():
    # Given
    not_found_exception = httpx.HTTPStatusError(
        "Test Error", request=mock.Mock(), response=mock.Mock(status_code=404)
    )
    mock_client = mock_async_client()
    mock_client.list_links.side_effect = not_found_exception

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.links == {}


COMPONENT_RECORD = model.Component(
    name="components/test-component",
    display_name="Test Component",
    description="Test Description",
    version="1.0.0",
    documentation_uri="http://test-docs.domain:1234",
)


def test_load_components():
    # Given
    mock_client = mock_sync_client()
    mock_client.list_components.return_value = [COMPONENT_RECORD]

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.components["test-component"] == COMPONENT_RECORD


@pytest.mark.asyncio
async def test_load_components_async():
    # Given
    mock_client = mock_async_client()
    mock_client.list_components.return_value = asyncio.Future()
    mock_client.list_components.return_value.set_result([COMPONENT_RECORD])

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.components["test-component"] == COMPONENT_RECORD


def test_load_components_not_found_returns_empty_map():
    # Given
    not_found_exception = httpx.HTTPStatusError(
        "Test Error", request=mock.Mock(), response=mock.Mock(status_code=404)
    )
    mock_client = mock_sync_client()
    mock_client.list_components.side_effect = not_found_exception

    # When
    discovery = load.load_discovery(mock_client)

    # Then
    assert discovery.components == {}


@pytest.mark.asyncio
async def test_load_components_async_not_found_returns_empty_map():
    # Given
    not_found_exception = httpx.HTTPStatusError(
        "Test Error", request=mock.Mock(), response=mock.Mock(status_code=404)
    )
    mock_client = mock_async_client()
    mock_client.list_components.side_effect = not_found_exception

    # When
    discovery = await load.load_discovery_async(mock_client)

    # Then
    assert discovery.components == {}
