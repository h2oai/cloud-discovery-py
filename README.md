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

Both accept a `environment` argument that can be used to specify the H2O Cloud
environment for which the discovery should be performed. It's handy when for
local development.
Alternatively, the `H2O_CLOUD_ENVIRONMENT` environment variable can be used.

```python
import h2o_discovery

discovery = h2o_discovery.discover()

# Print the H2O Cloud environment that was discovered.
print(discovery.environment.h2o_cloud_environment)

# Connect to the my service.
my_service_client = my_service.client(address=discovery.services["my-service"].uri)
```

## Examples

### Example: Use with H2O.ai MLOps Python Client within the Wave App

```python
import h2o_authn
import h2o_discovery
import h2o_mlops_client as mlops
from h2o_wave import Q, app, ui
from h2o_wave import main

@app("/")
async def serve(q: Q):
    discovery = await h2o_discovery.discover_async()

    token_provider = h2o_authn.AsyncTokenProvider(
        refresh_token=q.auth.refresh_token,
        issuer_url=discovery.environment.issuer_url,
        client_id=discovery.clients["platform"].oauth2_client_id,
    )

    mlops_client = mlops.Client(
        gateway_url=discovery.services["mlops-api"].uri,
        token_provider=token_provider,
    )

    ...

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
