from h2o_discovery import model


def test_service_from_json_dict():
    # Given
    json = {
        "name": "services/test-service",
        "displayName": "Test Service",
        "uri": "http://test-service.domain:1234",
        "version": "1.0.0",
        "oauth2Scope": "test-service-scope",
        "pythonClient": "test-client==1.0.0",
    }

    # When
    result = model.Service.from_json_dict(json)

    # Then
    assert result == model.Service(
        name="services/test-service",
        display_name="Test Service",
        uri="http://test-service.domain:1234",
        version="1.0.0",
        oauth2_scope="test-service-scope",
        python_client="test-client==1.0.0",
    )


def test_client_from_json_dict():
    # Given
    json = {
        "name": "test-client",
        "displayName": "Test Client",
        "oauth2ClientId": "test-client-id",
    }

    # When
    result = model.Client.from_json_dict(json)

    # Then
    assert result == model.Client(
        name="test-client",
        display_name="Test Client",
        oauth2_client_id="test-client-id",
    )


def test_environment_from_json_dict():
    # Given
    json = {
        "h2oCloudEnvironment": "https://test.h2o.ai",
        "issuerUrl": "https://test.h2o.ai",
        "h2oCloudPlatformOauth2Scope": "test-platform-scope",
        "h2oCloudVersion": "test-version",
    }

    # When
    result = model.Environment.from_json_dict(json)

    # Then
    assert result == model.Environment(
        h2o_cloud_environment="https://test.h2o.ai",
        issuer_url="https://test.h2o.ai",
        h2o_cloud_platform_oauth2_scope="test-platform-scope",
        h2o_cloud_version="test-version",
    )


def test_environment_from_json_dict_with_missing_version():
    # Given
    json = {
        "h2oCloudEnvironment": "https://test.h2o.ai",
        "issuerUrl": "https://test.h2o.ai",
        "h2oCloudPlatformOauth2Scope": "test-platform-scope",
    }

    # When
    result = model.Environment.from_json_dict(json)

    # Then
    assert result == model.Environment(
        h2o_cloud_environment="https://test.h2o.ai",
        issuer_url="https://test.h2o.ai",
        h2o_cloud_platform_oauth2_scope="test-platform-scope",
        h2o_cloud_version=None,
    )
