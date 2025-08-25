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
    )


def test_link_from_json_dict():
    # Given
    json = {
        "name": "links/test-link",
        "uri": "http://test-link.domain:1234",
        "text": "Test Link",
    }

    # When
    result = model.Link.from_json_dict(json)

    # Then
    assert result == model.Link(
        name="links/test-link", uri="http://test-link.domain:1234", text="Test Link"
    )


def test_link_from_json_dict_with_missing_text():
    # Given
    json = {"name": "links/test-link", "uri": "http://test-link.domain:1234"}

    # When
    result = model.Link.from_json_dict(json)

    # Then
    assert result == model.Link(
        name="links/test-link", uri="http://test-link.domain:1234", text=None
    )


def test_component_from_json_dict():
    # Given
    json = {
        "name": "components/test-component",
        "displayName": "Test Component",
        "description": "Test Description",
        "version": "1.0.0",
        "documentation_uri": "https://example.com/docs/test-component",
    }

    # When
    result = model.Component.from_json_dict(json)

    # Then
    assert result == model.Component(
        name="components/test-component",
        display_name="Test Component",
        description="Test Description",
        version="1.0.0",
    )


def test_component_from_json_dict_with_missing_optional_fields():
    # Given
    json = {
        "name": "components/test-component",
        "displayName": "Test Component",
        "version": "1.0.0",
    }

    # When
    result = model.Component.from_json_dict(json)

    # Then
    assert result == model.Component(
        name="components/test-component", display_name="Test Component", version="1.0.0"
    )


def test_discovery_without_new_entities_ok():
    """Test that Discovery can be created without explicitly providing links in
    the constructor to ensure backward compatibility.
    """

    # When
    _ = model.Discovery(
        environment=model.Environment(
            h2o_cloud_environment="https://test.h2o.ai",
            issuer_url="https://test.h2o.ai",
            h2o_cloud_platform_oauth2_scope="test-platform-scope",
        ),
        credentials={},
        services={},
        clients={},
        # No links nor components.
    )

    # Then
    # No exception is raised.
