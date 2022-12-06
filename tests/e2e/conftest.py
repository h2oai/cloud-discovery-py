import os

import pytest


_PUBLIC_ADDRESS = "DISCOVERY_E2E_TESTS_PUBLIC_ADDRESS"
_INTERNAL_ADDRESS = "DISCOVERY_E2E_TESTS_INTERNAL_ADDRESS"


@pytest.fixture
def public_discovery_address():
    return os.environ[_PUBLIC_ADDRESS]


@pytest.fixture
def internal_discovery_address():
    return os.environ[_INTERNAL_ADDRESS]


@pytest.fixture(params=[_PUBLIC_ADDRESS, _INTERNAL_ADDRESS], ids=["public", "internal"])
def discovery_address(request):
    return os.environ[request.param]


@pytest.fixture
def expected_environment_issuer_url():
    return os.environ["DISCOVERY_E2E_TESTS_EXPECTED_ISSUER_URL"]


@pytest.fixture
def expected_environment_h2o_environment():
    return os.environ["DISCOVERY_E2E_TESTS_EXPECTED_ENVIRONMENT"]
