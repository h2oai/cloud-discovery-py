import sys

if sys.version_info >= (3, 11):
    import tomllib  # noqa: F401
else:
    import tomli as tomllib  # noqa: F401
