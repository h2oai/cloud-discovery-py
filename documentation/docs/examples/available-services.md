---
sidebar_label: Available Services
title: Available Services
---

# Listing Available services

The following example shows how to use `h2o-cloud-discovery` to list all the services
available in the H2O.ai Cloud environment.


:::note Locally
```sh
export H2O_CLOUD_ENVIRONMENT="https://<your H2O.ai Cloud domain>"
```
:::

```python
import h2o_discovery

discovery = h2o_discovery.discover()
for key, svc in discovery.services.items():
    print(f"{key} ({svc.version})")
```

:::info Results may differ between local and in-environment execution.

Your environment may contain the services that are available only internally.
These services are no listed when discovery is accessed from outside of the
environment.
:::
