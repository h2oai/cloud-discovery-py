import pytest

import h2o_discovery


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_environment(
    discovery_address,
    expected_environment_issuer_url,
    expected_environment_h2o_environment,
):
    # Given
    discovery = h2o_discovery.New(discovery_address=discovery_address)

    # When
    env = await discovery.environment

    # Then
    assert env.h2o_cloud_environment == expected_environment_h2o_environment
    assert env.issuer_url == expected_environment_issuer_url
