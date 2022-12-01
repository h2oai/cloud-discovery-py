import pytest

import h2o_discovery
from h2o_discovery import model


TEST_CLIENT = model.Client(
    name="clients/test-client",
    display_name="Test Client",
    oauth2_client_id="test-client-id",
)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_clients(discovery_address):
    # Given

    discovery = h2o_discovery.New(discovery_address=discovery_address)

    # When
    clients = await discovery.clients

    # Then
    assert clients["test-client"] == TEST_CLIENT
