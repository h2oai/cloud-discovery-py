from h2o_discovery._internal import lookup


def test_determine_local_config_path_param():
    # When
    path = lookup.determine_local_config_path("test-path")

    # Then
    assert path == "test-path"


def test_determine_local_config_path_env(monkeypatch):
    # Given
    monkeypatch.setenv("H2OCONFIG", "test-path-from-env")

    # When
    path = lookup.determine_local_config_path()

    # Then
    assert path == "test-path-from-env"


def test_determine_local_config_path_default_location_does_not_exist(
    monkeypatch, tmp_path
):
    # Given
    home = tmp_path / "home" / "test-user"
    home.mkdir(parents=True)
    monkeypatch.setenv("HOME", str(home))

    # When
    path = lookup.determine_local_config_path()

    # Then
    assert path is None


def test_determine_local_config_path_default_location_does_exists(
    monkeypatch, tmp_path
):
    # Given
    home = tmp_path / "home" / "test-user"
    home.mkdir(parents=True)
    monkeypatch.setenv("HOME", str(home))

    config_dir = home / ".h2oai"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "h2o-cli-config.toml"
    config_file.touch()

    # When
    path = lookup.determine_local_config_path()

    # Then
    assert path == str(config_file)
