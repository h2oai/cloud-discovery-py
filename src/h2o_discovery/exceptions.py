class DiscoveryError(Exception):
    """Base class for all exceptions of the H2O Cloud discovery Client."""


class DiscoveryLookupError(DiscoveryError, LookupError):
    """Raised when the discovery URI cannot be determined."""


class H2OCloudEnvironmentError(DiscoveryError):
    """Raised when there seems to be a problem with the deployment of the server
    side.
    """
