def test_version():
    # When
    import h2o_discovery

    # Then
    assert hasattr(h2o_discovery, "__version__")
    assert h2o_discovery.__version__ != ""
