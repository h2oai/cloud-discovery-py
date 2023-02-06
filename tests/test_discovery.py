import asyncio
from unittest import mock

import pytest

import h2o_discovery
from h2o_discovery import model


@pytest.fixture()
def mock_client():
    client = mock.Mock()
    client.get_environment.return_value = asyncio.Future()
    client.get_environment.return_value.set_result(mock.Mock())
    client.list_services.return_value = asyncio.Future()
    client.list_services.return_value.set_result({})
    client.list_clients.return_value = asyncio.Future()
    client.list_clients.return_value.set_result({})

    return client


ENVIRONMENT_DATA = model.Environment(
    h2o_cloud_environment="https://test.example.com",
    h2o_cloud_platform_oauth2_scope="test-scope",
    issuer_url="https://test.example.com",
)


def test_discovery_environment(mock_client):
    # Given
    mock_client.get_environment.return_value = ENVIRONMENT_DATA

    # When
    discovery = h2o_discovery.Discovery.load(mock_client)

    # Then
    assert discovery.environment == ENVIRONMENT_DATA


@pytest.mark.asyncio
async def test_discovery_environment_async(mock_client):
    # Given
    mock_client.get_environment.return_value = asyncio.Future()
    mock_client.get_environment.return_value.set_result(ENVIRONMENT_DATA)

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.environment == ENVIRONMENT_DATA


def test_discovery_services(mock_client):
    # Given
    mock_client.list_services.return_value = [SERVICE_RECORD]

    # When
    discovery = h2o_discovery.Discovery.load(mock_client)
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
async def test_discovery_services_async(mock_client):
    # Given
    mock_client.list_services.return_value = asyncio.Future()
    mock_client.list_services.return_value.set_result([SERVICE_RECORD])

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.services["test-service"] == SERVICE_RECORD


CLIENT_RECORD = model.Client(
    name="clients/test-client",
    display_name="Test Client",
    oauth2_client_id="test-client-id",
)


def test_discovery_clients(mock_client):
    # Given
    mock_client.list_clients.return_value = [CLIENT_RECORD]

    # When
    discovery = h2o_discovery.Discovery.load(mock_client)

    # Then
    assert discovery.clients["test-client"] == CLIENT_RECORD


@pytest.mark.asyncio
async def test_discovery_clients_async(mock_client):
    # Given
    mock_client.list_clients.return_value = asyncio.Future()
    mock_client.list_clients.return_value.set_result([CLIENT_RECORD])

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.clients["test-client"] == CLIENT_RECORD
