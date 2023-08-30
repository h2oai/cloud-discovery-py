from h2o_discovery import model
from h2o_discovery._internal import load


def test_load_credentials(monkeypatch):
    # Given
    clients = {
        "env_client": model.Client(
            name="clients/env_client",
            display_name="Env Client",
            oauth2_client_id="env-client-id",
        ),
        "extra_client": model.Client(
            name="clients/extra_client",
            display_name="Extra Client",
            oauth2_client_id="extra-client-id",
        ),
    }
    monkeypatch.setenv("H2O_CLOUD_CLIENT_ENV_CLIENT_TOKEN", "env-token")

    # When
    result = load.load_credentials(clients=clients)
    # Then
    assert result == {
        "env_client": model.Credentials(client="env_client", refresh_token="env-token")
    }
