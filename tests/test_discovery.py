import asyncio
from unittest import mock

import pytest

import h2o_discovery
from h2o_discovery import model


@pytest.mark.asyncio
async def test_discovery_environment():
    # Given
    environment = model.Environment(
        h2o_cloud_environment="https://test.example.com",
        h2o_cloud_platform_oauth2_scope="test-scope",
        issuer_url="https://test.example.com",
    )

    client = mock.Mock()
    client.get_environment.return_value = asyncio.Future()
    client.get_environment.return_value.set_result(environment)

    discovery = h2o_discovery.Discovery(client=client)

    # When
    result = await discovery.environment

    # Then
    assert result == environment


@pytest.mark.asyncio
async def test_discovery_services():
    # Given
    service = model.Service(
        name="services/test-service",
        display_name="Test Service",
        uri="http://test-service.domain:1234",
        version="1.0.0",
        oauth2_scope="test-service-scope",
        python_client="test-client==1.0.0",
    )

    client = mock.Mock()
    client.list_services.return_value = asyncio.Future()
    client.list_services.return_value.set_result([service])
    discovery = h2o_discovery.Discovery(client=client)

    # When
    result = (await discovery.services)["test-service"]

    # Then
    assert result == service


@pytest.mark.asyncio
async def test_discovery_clients():
    # Given
    client_record = model.Client(
        name="clients/test-client",
        display_name="Test Client",
        oauth2_client_id="test-client-id",
    )

    client = mock.Mock()
    client.list_clients.return_value = asyncio.Future()
    client.list_clients.return_value.set_result([client_record])
    discovery = h2o_discovery.Discovery(client=client)

    # When
    result = (await discovery.clients)["test-client"]

    # Then
    assert result == client_record
