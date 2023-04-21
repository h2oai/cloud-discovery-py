---
sidebar_label: h2o_discovery
title: h2o_discovery
---

#### discover

```python
def discover(environment: Optional[str] = None,
             discovery_address: Optional[str] = None) -> Discovery
```

Obtains and returns a Discovery object from the discovery service.

Both arguments are optional. If neither is provided, the environment variable
H2O_CLOUD_ENVIRONMENT is used. If that is not set, the environment variable
H2O_CLOUD_DISCOVERY is used. If that is not set, a LookupError is raised.

**Arguments**:

- `environment` - The H2O Cloud environment URL to use (e.g. https://cloud.h2o.ai).
- `discovery_address` - The address of the discovery service.

#### discover\_async

```python
async def discover_async(environment: Optional[str] = None,
                         discovery_address: Optional[str] = None) -> Discovery
```

Obtains and returns a Discovery object from the discovery service.

Both arguments are optional. If neither is provided, the environment variable
H2O_CLOUD_ENVIRONMENT is used. If that is not set, the environment variable
H2O_CLOUD_DISCOVERY is used. If that is not set, a LookupError is raised.

**Arguments**:

- `environment` - The H2O Cloud environment URL to use (e.g. https://cloud.h2o.ai).
- `discovery_address` - The address of the discovery service.

