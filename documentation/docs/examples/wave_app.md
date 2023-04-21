---
sidebar_label: Within Wave App
title: Within Wave App
---

# `h2o-cloud-discovery` Within a Wave App

The following example shows how to use `h2o-cloud-discovery` within a Wave App
to setup a connection to the H2O.ai MLOps API.

Apps managed by H2O Cloud Appstore are setup so that there's no configuration
needed. For the local development, the `H2O_CLOUD_ENVIRONMENT`  environment variable
can be used to specify the H2O Cloud environment for which the discovery should be
performed.

```sh
export H2O_CLOUD_ENVIRONMENT="https://<your H2O.ai Cloud domain>"
```

:::tip
We recommend not to use the `environment` argument of the `discover` function
within the Wave App so that it can detect the environment automatically.
(unless you want to do explicit cross-environment calls).
:::

```python
import h2o_authn
import h2o_discovery
import h2o_mlops_client as mlops

from h2o_wave import Q, app
from h2o_wave import main

@app("/")
async def serve(q: Q):
    # Wave App should use asynchronous variant of the discover function.

    discovery = await h2o_discovery.discover_async()

    # We
    token_provider = h2o_authn.AsyncTokenProvider(
        refresh_token=q.auth.refresh_token,
        issuer_url=discovery.environment.issuer_url,

        # In the most of the cases clients need "platform" client.
        client_id=discovery.clients["platform"].oauth2_client_id,
    )

    mlops_client = mlops.Client(
        gateway_url=discovery.services["mlops-api"].uri,
        token_provider=token_provider,
    )

    ...

```
