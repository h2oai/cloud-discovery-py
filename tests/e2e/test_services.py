import pytest

import h2o_discovery
from h2o_discovery import model


PUBLIC_ONLY_TEST_SERVICE = model.Service(
    name="services/public-only-test-service",
    display_name="Public Only Test Service",
    uri="https://public-only-test-service.cloud.fbi.com",
    version="public-only-test-service-v1",
    oauth2_scope="public-only-test-service-v1 scope",
    python_client="public-only-test-service-client",
)

INTERNAL_ONLY_TEST_SERVICE = model.Service(
    name="services/internal-only-test-service",
    display_name="Internal Only Test Service",
    uri="http://internal-only-test-service:8080",
    version="internal-only-test-service-v1",
    oauth2_scope="internal-only-test-service-v1 scope",
    python_client="internal-only-test-service-client",
)

TEST_SERVICE_ON_PUBLIC = model.Service(
    name="services/test-service",
    display_name="Test Service",
    uri="https://test-service.cloud.fbi.com",
    version="test-service-v1",
    oauth2_scope="test-service-v1 scope",
    python_client="test-service-client",
)

TEST_SERVICE_ON_INTERNAL = model.Service(
    name="services/test-service",
    display_name="Test Service",
    uri="http://test-service:8080",
    version="test-service-v1",
    oauth2_scope="test-service-v1 scope",
    python_client="test-service-client",
)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_services_on_public_endpoint_async(public_discovery_address):
    # When
    discovery = await h2o_discovery.discover_async(
        discovery_address=public_discovery_address
    )

    # Then
    services = discovery.services
    assert services["public-only-test-service"] == PUBLIC_ONLY_TEST_SERVICE
    assert services["test-service"] == TEST_SERVICE_ON_PUBLIC
    assert "internal-only-test-service" not in services
    assert INTERNAL_ONLY_TEST_SERVICE not in services.values()


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_services_on_internal_endpoint_async(internal_discovery_address):
    # When
    discovery = await h2o_discovery.discover_async(
        discovery_address=internal_discovery_address
    )

    # Then
    services = discovery.services
    assert services["public-only-test-service"] == PUBLIC_ONLY_TEST_SERVICE
    assert services["test-service"] == TEST_SERVICE_ON_INTERNAL
    assert services["internal-only-test-service"] == INTERNAL_ONLY_TEST_SERVICE
