# `h2o-cloud-discovery`

[![licence](https://img.shields.io/github/license/h2oai/cloud-discovery-py?style=flat-square)](https://github.com/h2oai/cloud-discovery-py/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/h2o-cloud-discovery?style=flat-square)](https://pypi.org/project/h2o-cloud-discovery/)

H2O Cloud Discovery Client.

## Installation

```sh
pip install h2o-cloud-discovery
```

## Usage

Package provides two main functions.  Synchronous `h2o_discovery.discover()`
and asynchronous `h2o_discovery.discover_async()`.  Both functions return
a discovery object that can be used to obtain the information the H2O Cloud
environment, its services and clients.

When used within the [H2O AI Cloud](https://h2o.ai/platform/ai-cloud/)
environment or locally with the
[H2O AI Cloud CLI](https://docs.h2o.ai/h2o-ai-cloud/developerguide/cli)
configured, no further configuration is needed.

Both functions accept a `environment` argument that can be used to specify the
H2O Cloud environment for which the discovery should be performed.
Alternatively, the `H2O_CLOUD_ENVIRONMENT` environment variables can be used.

See API documentation for more details.

```python
import h2o_discovery

discovery = h2o_discovery.discover()

# Print the H2O Cloud environment that was discovered.
print(discovery.environment.h2o_cloud_environment)

# Connect to the my service.
my_service_client = my_service.client(address=discovery.services["my-service"].uri)
```

## Examples

### Example: Use within a notebook to connect to the H2O AI Drive

```py
# Install required packages.

import sys
!{sys.executable} -m pip install h2o-cloud-discovery h2o-authn[discovery]
```

```py
# Load discovery for the current environment.

import h2o_discovery
discovery = h2o_discovery.discover()
```

```py
# Create a token provider using the credentials loaded from the environment.

import h2o_authn.discovery
token_provider = h2o_authn.discovery.create_async(discovery)
```

```py
# Install the H2O AI Drive client in the version specified by the available
# service.

import sys
!{sys.executable} -m pip install '{discovery.services["drive"].python_client}'
```

```py
# Connect to the H2O AI Drive and list home objects.

import h2o_drive
home = await h2o_drive.MyHome(
    token=token_provider,
    endpoint_url=discovery.services["drive"].uri,
)
await home.list_objects()
```

## Development

Project is managed using [Hatch](https://hatch.pypa.io/latest/).

### Testing

For quick development tests use:

```sh
hatch run devtest:pytest
```

Full test matrix can be run using:

```sh
hatch env remove test && hatch run test:pytest
```

### Linting

```sh
hatch run lint:check
```

Formating and imports can be fixed using:

```sh
hatch run lint:fix
```
