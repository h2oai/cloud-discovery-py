import pytest

from h2o_discovery._internal import config


def config_test_cases():
    yield pytest.param("", config.Config(endpoint=None, tokens={}), id="empty config")
    yield pytest.param(
        """
        Endpoint = "https://cloud.h2o.ai"
        ClientID = "client-id"
        Token = "TestToken"
        PlatformClientID = "platform-client-id"
        PlatformToken = "TestPlatformToken"
        """,
        config.Config(
            endpoint="https://cloud.h2o.ai",
            tokens={
                "client-id": "TestToken",
                "platform-client-id": "TestPlatformToken",
            },
        ),
        id="full config",
    )
    yield pytest.param(
        """
        ClientID = "client-id"
        Token = "TestToken"
        """,
        config.Config(tokens={"client-id": "TestToken"}),
        id="cli token only",
    )
    yield pytest.param(
        """
        PlatformClientID = "platform-client-id"
        PlatformToken = "TestPlatformToken"
        """,
        config.Config(tokens={"platform-client-id": "TestPlatformToken"}),
        id="platform token only",
    )
    yield pytest.param(
        """
        Endpoint = "https://cloud.h2o.ai"
        """,
        config.Config(endpoint="https://cloud.h2o.ai", tokens={}),
        id="endpoint only",
    )


@pytest.mark.parametrize("config_content,expected_results", config_test_cases())
def test_load_config(config_content, expected_results, tmp_path):
    # Given
    config_file = tmp_path / "config.toml"
    config_file.write_text(config_content)

    # When
    result = config.load_config(config_file)

    # Then
    assert result == expected_results


def test_load_config_no_path(tmp_path):
    # When
    result = config.load_config()

    # Then
    assert result == config.Config()
