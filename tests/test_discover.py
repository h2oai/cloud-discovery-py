import pytest

from h2o_discovery import discover


def test_find_uri_environment_param():
    # Given
    environment = "https://test.h2o.ai"

    # When
    uri = discover.discover_uri(environment=environment)

    # Then
    assert uri == "https://test.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_uri_environment_trailing_slash():
    # Given
    environment = "https://test.h2o.ai/"

    # When
    uri = discover.discover_uri(environment=environment)

    # Then
    assert uri == "https://test.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_uri_discovery_param():
    # Given
    discovery = "http://test-service.domain:1234"

    # When
    uri = discover.discover_uri(discovery_address=discovery)

    # Then
    assert uri == "http://test-service.domain:1234"


def test_find_uri_environment_env_var(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test.h2o.ai")

    # When
    uri = discover.discover_uri()

    # Then
    assert uri == "https://test.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_uri_discovery_env_var(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-service.domain:1234")

    # When
    uri = discover.discover_uri()

    # Then
    assert uri == "http://test-service.domain:1234"


def test_find_uri_both_env_var_discovery_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test.h2o.ai")
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-service.domain:1234")

    # When
    uri = discover.discover_uri()

    # Then
    assert uri == "http://test-service.domain:1234"


def test_find_uri_environment_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_ENVIRONMENT", "https://test-env.h2o.ai")
    environment = "https://test-param.h2o.ai"

    # When
    uri = discover.discover_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_uri_discovery_param_takes_precedence(monkeypatch):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    discovery = "http://test-param.domain:1234"

    # When
    uri = discover.discover_uri(discovery_address=discovery)

    # Then
    assert uri == "http://test-param.domain:1234"


def test_find_uri_environment_param_takes_precedence_over_discovery_env_var(
    monkeypatch,
):
    # Given
    monkeypatch.setenv("H2O_CLOUD_DISCOVERY", "http://test-env.domain:1234")
    environment = "https://test-param.h2o.ai"

    # When
    uri = discover.discover_uri(environment=environment)

    # Then
    assert uri == "https://test-param.h2o.ai/.ai.h2o.cloud.discovery"


def test_find_cannot_set_both_params():
    # Given
    environment = "https://test.h2o.ai"
    discovery = "http://test-service.domain:1234"

    # When
    with pytest.raises(ValueError) as excinfo:
        discover.discover_uri(environment=environment, discovery_address=discovery)

    # Then
    assert "cannot specify both discovery and environment" in str(excinfo.value)


def test_find_cannot_determine_url():
    # Given
    environment = None
    discovery = None

    # When
    with pytest.raises(LookupError) as excinfo:
        discover.discover_uri(environment=environment, discovery_address=discovery)

    # Then
    assert "Cannot determine discovery URI" in str(excinfo.value)
