"""Helper module for importing backported packages. So that the rest of the
modules is not cluttered with conditional imports.
"""

import sys

# We use version check instead of try/except because mypy does not like it.
if sys.version_info >= (3, 11):
    import tomllib  # noqa: F401
else:
    import tomli as tomllib  # noqa: F401
