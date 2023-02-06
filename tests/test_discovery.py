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


@pytest.mark.asyncio
async def test_discovery_environment_async(mock_client):
    # Given
    environment = model.Environment(
        h2o_cloud_environment="https://test.example.com",
        h2o_cloud_platform_oauth2_scope="test-scope",
        issuer_url="https://test.example.com",
    )

    mock_client.get_environment.return_value = asyncio.Future()
    mock_client.get_environment.return_value.set_result(environment)

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.environment == environment


@pytest.mark.asyncio
async def test_discovery_services_async(mock_client):
    # Given
    service = model.Service(
        name="services/test-service",
        display_name="Test Service",
        uri="http://test-service.domain:1234",
        version="1.0.0",
        oauth2_scope="test-service-scope",
        python_client="test-client==1.0.0",
    )

    mock_client.list_services.return_value = asyncio.Future()
    mock_client.list_services.return_value.set_result([service])

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.services["test-service"] == service


@pytest.mark.asyncio
async def test_discovery_clients_async(mock_client):
    # Given
    client_record = model.Client(
        name="clients/test-client",
        display_name="Test Client",
        oauth2_client_id="test-client-id",
    )

    mock_client.list_clients.return_value = asyncio.Future()
    mock_client.list_clients.return_value.set_result([client_record])

    # When
    discovery = await h2o_discovery.Discovery.load_async(mock_client)

    # Then
    assert discovery.clients["test-client"] == client_record
