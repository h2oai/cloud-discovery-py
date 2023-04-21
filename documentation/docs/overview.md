# Overview

`h2o-cloud-discovery` is a Python library that provides a simple way how to
discover available services in the H2O.ai Cloud environment, find out their
endpoints and versions, and and Python clients for them.

## Installation

Library is [available on PyPI](https://pypi.org/project/h2o-cloud-discovery/)
and can be installed using `pip`:

```bash
pip install h2o-cloud-discovery
```

## Usage

Package provides two main functions.
Synchronous [`h2o_discovery.discover()`](/api/h2o_discovery#discover)
and asynchronous [`h2o_discovery.discover_async()`](/api/h2o_discovery#discover_async).
Both functions return a [discovery object](/api/h2o_discovery/model#discovery-objects)
that can be used to obtain the information the H2O Cloud environment, its services and clients.

See [API documentation](/api) for more details.

## Configuration

Wave Apps and managed notebooks are automatically setup so that you don't need
to configure anything. For the local development, the `H2O_CLOUD_ENVIRONMENT`
environment variable can be used to specify the H2O Cloud environment for which
the discovery should be performed.

```bash
export H2O_CLOUD_ENVIRONMENT="https://<your H2O.ai Cloud domain>"
```
