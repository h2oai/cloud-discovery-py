import pytest

import h2o_discovery


@pytest.mark.e2e
def test_environment(
    discovery_address,
    expected_environment_issuer_url,
    expected_environment_h2o_environment,
):
    # When
    discovery = h2o_discovery.discover(discovery_address=discovery_address)

    # Then
    env = discovery.environment
    assert env.h2o_cloud_environment == expected_environment_h2o_environment
    assert env.issuer_url == expected_environment_issuer_url


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_environment_async(
    discovery_address,
    expected_environment_issuer_url,
    expected_environment_h2o_environment,
):
    # When
    discovery = await h2o_discovery.discover_async(discovery_address=discovery_address)

    # Then
    env = discovery.environment
    assert env.h2o_cloud_environment == expected_environment_h2o_environment
    assert env.issuer_url == expected_environment_issuer_url
