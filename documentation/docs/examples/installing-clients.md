---
sidebar_label: Installing Clients
title: Installing Clients
---

# Installing Clients For Available Services

You can utilize discovery client to install clients for the services available
in the environment.

## Installing Clients Locally

```sh
export H2O_CLOUD_ENVIRONMENT="https://<your H2O.ai Cloud domain>"
```

```sh
python <<EOF | pip install -r /dev/stdin
import h2o_discovery

discovery = h2o_discovery.discover()
for svc in h2o_discovery.discover().services.values():
    if svc.python_client:
        print(svc.python_client)

EOF
```

:::info Some clients may not be available locally

Your environment may contain the services that are available only internally.
These services are no listed when discovery is accessed from outside of the
environment.
:::

## Installing Clients Within the Notebook

```python
# Cell 1
import h2o_discovery

discovery = h2o_discovery.discover()
```

```python
# Cell 2
!{sys.executable} -m pip install '{discovery.services["drive"].python_client}'
```
