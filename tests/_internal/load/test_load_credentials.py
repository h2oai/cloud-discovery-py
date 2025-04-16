from h2o_discovery import model
from h2o_discovery._internal import config
from h2o_discovery._internal import load

_ENVIRONMENT = model.Environment(
    h2o_cloud_environment="https://example.com",
    issuer_url="https://example.com",
    h2o_cloud_platform_oauth2_scope=["scope1", "scope2"],
)


def test_load_credentials(monkeypatch):
    # Given
    clients = {
        "env_client": model.Client(
            name="clients/env_client",
            display_name="Env Client",
            oauth2_client_id="env-client-id",
        ),
        "config_client": model.Client(
            name="clients/config_client",
            display_name="Config Client",
            oauth2_client_id="config-client-id",
        ),
        "extra_client": model.Client(
            name="clients/extra_client",
            display_name="Extra Client",
            oauth2_client_id="extra-client-id",
        ),
    }
    tokens = {"config-client-id": "config-token"}
    monkeypatch.setenv("H2O_CLOUD_CLIENT_ENV_CLIENT_TOKEN", "env-token")

    discovery = model.Discovery(clients=clients, environment=_ENVIRONMENT, services={})
    cfg = config.Config(tokens=tokens, endpoint=_ENVIRONMENT.h2o_cloud_environment)

    # When
    result = load.load_credentials(discovery=discovery, cfg=cfg)

    # Then
    assert result == {
        "env_client": model.Credentials(client="env_client", refresh_token="env-token"),
        "config_client": model.Credentials(
            client="config_client", refresh_token="config-token"
        ),
    }


def test_load_credentials_not_loaded_from_config_for_different_environment(monkeypatch):
    # Given
    clients = {
        "env_client": model.Client(
            name="clients/env_client",
            display_name="Env Client",
            oauth2_client_id="env-client-id",
        ),
        "config_client": model.Client(
            name="clients/config_client",
            display_name="Config Client",
            oauth2_client_id="config-client-id",
        ),
    }
    tokens = {"config-client-id": "config-token"}
    monkeypatch.setenv("H2O_CLOUD_CLIENT_ENV_CLIENT_TOKEN", "env-token")

    discovery = model.Discovery(clients=clients, environment=_ENVIRONMENT, services={})
    cfg = config.Config(tokens=tokens, endpoint="https://other.com")

    # When
    result = load.load_credentials(discovery=discovery, cfg=cfg)

    # Then
    assert result == {
        "env_client": model.Credentials(client="env_client", refresh_token="env-token")
    }
