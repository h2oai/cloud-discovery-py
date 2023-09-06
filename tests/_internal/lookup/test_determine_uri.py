import pytest

from h2o_discovery._internal import lookup


def environment_test_cases():
    yield pytest.param(
        "https://test.h2o.ai", "https://test.h2o.ai/.ai.h2o.cloud.discovery", id="clean"
    )
    yield pytest.param(
        "https://test.h2o.ai/",
        "https://test.h2o.ai/.ai.h2o.cloud.discovery",
        id="with trailing slash",
    )
    yield pytest.param(
        "https://test.h2o.ai:1234",
        "https://test.h2o.ai:1234/.ai.h2o.cloud.discovery",
        id="with port",
    )
    yield pytest.param(
        "https://test.h2o.ai:1234/",
        "https://test.h2o.ai:1234/.ai.h2o.cloud.discovery",
        id="with port and trailing slash",
    )
    yield pytest.param(
        "https://test.h2o.ai/path",
        "https://test.h2o.ai/path/.ai.h2o.cloud.discovery",
        id="with path",
    )
    yield pytest.param(
        "https://test.h2o.ai/path/",
        "https://test.h2o.ai/path/.ai.h2o.cloud.discovery",
        id="with path and trailing slash",
    )
    yield pytest.param(
        "https://test.h2o.ai:1234/path",
        "https://test.h2o.ai:1234/path/.ai.h2o.cloud.discovery",
        id="with path and port",
    )
    yield pytest.param(
        "https://test.h2o.ai:1234/path/",
        "https://test.h2o.ai:1234/path/.ai.h2o.cloud.discovery",
        id="with path, port and trailing slash",
    )


def discovery_test_cases():
    yield pytest.param(
        "http://test-service.domain:1234", "http://test-service.domain:1234", id="clean"
    )
    yield pytest.param(
        "http://test-service.domain:1234/",
        "http://test-service.domain:1234",
        id="with trailing slash",
    )
    yield pytest.param(
        "http://test-service.domain:1234/path",
        "http://test-service.domain:1234/path",
        id="with path",
    )
    yield pytest.param(
        "http://test-service.domain:1234/path/",
        "http://test-service.domain:1234/path",
        id="with path and trailing slash",
    )


@pytest.mark.parametrize("environment_input,expected_uri", environment_test_cases())
def test_determine_uri_environment_param(environment_input, expected_uri):
    # When
    uri = lookup.determine_uri(environment=environment_input)

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("environment_input,expected_uri", environment_test_cases())
def test_determine_uri_environment_env_var(
    monkeypatch, environment_input, expected_uri
):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", environment_input)

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("discovery_input,expected_uri", discovery_test_cases())
def test_determine_uri_discovery_param(discovery_input, expected_uri):
    # When
    uri = lookup.determine_uri(discovery_address=discovery_input)

    # Then
    assert uri == expected_uri


@pytest.mark.parametrize("discovery_input,expected_uri", discovery_test_cases())
def test_determine_uri_discovery_env_var(monkeypatch, discovery_input, expected_uri):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", discovery_input)

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == expected_uri


def test_determine_uri_both_env_var_discovery_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test.h2o.ai")
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-service.domain:1234")

    # When
    uri = lookup.determine_uri()

    # Then
    assert uri == "http://test-service.domain:1234"


def test_determine_uri_environment_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test-env.h2o.ai")
    environment = "https://test-param.h2o.ai"

    # When
    uri = lookup.determine_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_determine_uri_discovery_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    discovery = "http://test-param.domain:1234"

    # When
    uri = lookup.determine_uri(discovery_address=discovery)

    # Then
    assert uri == "http://test-param.domain:1234"


def test_determine_uri_environment_param_takes_precedence_over_discovery_env_var(
    monkeypatch,
):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    environment = "https://test-param.h2o.ai"

    # When
    uri = lookup.determine_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_determine_uri_cannot_set_both_params():
    # Given
    environment = "https://test.h2o.ai"
    discovery = "http://test-service.domain:1234"

    # When
    with pytest.raises(ValueError) as excinfo:
        lookup.determine_uri(environment=environment, discovery_address=discovery)

    # Then
    assert "cannot specify both discovery and environment" in str(excinfo.value)


def test_determine_uri_cannot_determine_url():
    # Given
    environment = None
    discovery = None

    # When / Then
    with pytest.raises(lookup.DetermineURIError):
        lookup.determine_uri(environment=environment, discovery_address=discovery)
