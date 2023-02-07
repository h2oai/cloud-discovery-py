import pytest

from h2o_discovery import lookup


def environment_test_cases():
    yield "https://test.h2o.ai", "https://test.h2o.ai/.ai.h2o.cloud.discovery"
    # With trailing slash.
    yield "https://test.h2o.ai/", "https://test.h2o.ai/.ai.h2o.cloud.discovery"
    # With port.
    yield "https://test.h2o.ai:1234", "https://test.h2o.ai:1234/.ai.h2o.cloud.discovery"
    # With port and trailing slash.
    yield (
        "https://test.h2o.ai:1234/",
        "https://test.h2o.ai:1234/.ai.h2o.cloud.discovery",
    )
    # With path.
    yield "https://test.h2o.ai/path", "https://test.h2o.ai/path/.ai.h2o.cloud.discovery"
    # With path and trailing slash.
    yield (
        "https://test.h2o.ai/path/",
        "https://test.h2o.ai/path/.ai.h2o.cloud.discovery",
    )
    # With path and port.
    yield (
        "https://test.h2o.ai:1234/path",
        "https://test.h2o.ai:1234/path/.ai.h2o.cloud.discovery",
    )
    # With path, port and trailing slash.
    yield (
        "https://test.h2o.ai:1234/path/",
        "https://test.h2o.ai:1234/path/.ai.h2o.cloud.discovery",
    )


def discovery_test_cases():
    yield "http://test-service.domain:1234", "http://test-service.domain:1234"
    # With trailing slash.
    yield "http://test-service.domain:1234/", "http://test-service.domain:1234"
    # With path.
    yield "http://test-service.domain:1234/path", "http://test-service.domain:1234/path"
    # With path and trailing slash.
    yield (
        "http://test-service.domain:1234/path/",
        "http://test-service.domain:1234/path",
    )


@pytest.mark.parametrize("test_case", environment_test_cases())
def test_find_uri_environment_param(test_case):
    # Given
    environment_input, expected_uri = test_case

    # When
    uri = lookup.determine_uri(environment=environment_input)

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("test_case", environment_test_cases())
def test_find_uri_environment_env_var(monkeypatch, test_case):

    # Given
    environment_input, expected_uri = test_case
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", environment_input)

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("test_case", discovery_test_cases())
def test_find_uri_discovery_param(test_case):
    # Given
    discovery, expected_uri = test_case

    # When
    uri = lookup.determine_uri(discovery_address=discovery)

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("test_case", discovery_test_cases())
def test_find_uri_discovery_env_var(monkeypatch, test_case):
    # Given
    discovery, expected_uri = test_case
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", discovery)

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == expected_uri


def test_find_uri_both_env_var_discovery_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test.h2o.ai")
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-service.domain:1234")

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == "http://test-service.domain:1234"


def test_find_uri_environment_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test-env.h2o.ai")
    environment = "https://test-param.h2o.ai"

    # When
    uri = lookup.determine_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_uri_discovery_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    discovery = "http://test-param.domain:1234"

    # When
    uri = lookup.determine_uri(discovery_address=discovery)

    # Then
    assert uri == "http://test-param.domain:1234"


def test_find_uri_environment_param_takes_precedence_over_discovery_env_var(
    monkeypatch,
):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    environment = "https://test-param.h2o.ai"

    # When
    uri = lookup.determine_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_cannot_set_both_params():
    # Given
    environment = "https://test.h2o.ai"
    discovery = "http://test-service.domain:1234"

    # When
    with pytest.raises(ValueError) as excinfo:
        lookup.determine_uri(environment=environment, discovery_address=discovery)

    # Then
    assert "cannot specify both discovery and environment" in str(excinfo.value)


def test_find_cannot_determine_url():
    # Given
    environment = None
    discovery = None

    # When
    with pytest.raises(LookupError) as excinfo:
        lookup.determine_uri(environment=environment, discovery_address=discovery)

    # Then
    assert "Cannot determine discovery URI" in str(excinfo.value)
