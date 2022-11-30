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


@pytest.mark.asyncio
async def test_discovery_load():
    # Given
    client_record = model.Client(
        name="clients/test-client",
        display_name="Test Client",
        oauth2_client_id="test-client-id",
    )
    service = model.Service(
        name="services/test-service",
        display_name="Test Service",
        uri="http://test-service.domain:1234",
        version="1.0.0",
        oauth2_scope="test-service-scope",
        python_client="test-client==1.0.0",
    )
    environment = model.Environment(
        h2o_cloud_environment="https://test.example.com",
        h2o_cloud_platform_oauth2_scope="test-scope",
        issuer_url="https://test.example.com",
    )

    new_client_record = model.Client(
        name="clients/new-test-client",
        display_name="New Test Client",
        oauth2_client_id="new-test-client-id",
    )
    new_service = model.Service(
        name="services/new-test-service",
        display_name="New Test Service",
        uri="http://new-test-service.domain:1234",
        version="2.0.0",
        oauth2_scope="new-test-service-scope",
        python_client="new-test-client==1.0.0",
    )
    new_environment = model.Environment(
        h2o_cloud_environment="https://new-test.example.com",
        h2o_cloud_platform_oauth2_scope="new-test-scope",
        issuer_url="https://new-test.example.com",
    )

    client = mock.Mock()

    client_future = asyncio.Future()
    client_future.set_result(client_record)

    new_client_future = asyncio.Future()
    new_client_future.set_result(new_client_record)
    client.get_client.side_effect = [client_future, new_client_future]

    service_future = asyncio.Future()
    service_future.set_result(service)
    new_service_future = asyncio.Future()
    new_service_future.set_result(new_service)
    client.get_service.side_effect = [service_future, new_service_future]

    environment_future = asyncio.Future()
    environment_future.set_result(environment)
    new_environment_future = asyncio.Future()
    new_environment_future.set_result(new_environment)
    client.get_environment.side_effect = [environment_future, new_environment_future]

    discovery = h2o_discovery.Discovery(client=client)

    _ = await discovery.clients
    _ = await discovery.services
    _ = await discovery.environment

    # When
    clients = (await discovery.clients).values()
    services = (await discovery.services).values()
    environment = await discovery.environment

    # Then
    assert clients == [client_record]
    assert services == [service]
    assert environment == environment
