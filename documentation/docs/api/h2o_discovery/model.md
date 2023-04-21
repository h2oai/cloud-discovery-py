---
sidebar_label: model
title: h2o_discovery.model
---

## Service Objects

```python
@dataclasses.dataclass(frozen=True)
class Service()
```

Representation of a registered service record.

#### name

Name of the Service.

For example: &quot;services/my-service-name&quot;.

#### display\_name

Name of the Service that can be displayed on the front-end.

#### uri

URI for accessing the Service.

This is usually the string that can be passed connection definition to the
client for the particular service.

#### version

Version of the service.

Can be the version of the API or the version of
the service. Clients can utilize this information change their behavior
in accessing the service or downloading the correct client version.

#### oauth2\_scope

OAuth 2.0 Scope required to access the service.

Clients request the access token with this scope in order to access the service.
If the scope is not defined (or empty), clients should use
h2o_cloud_platform_scope.

#### python\_client

Requirement Specifier (PEP 508) for the Python client that can be used for
accessing the service.

Any string that can be `pip install`ed.
Example: my-client==0.1.0

#### from\_json\_dict

```python
@classmethod
def from_json_dict(cls, json: Mapping[str, str]) -> "Service"
```

Create a Service from a JSON dict returned by the server.

## Client Objects

```python
@dataclasses.dataclass(frozen=True)
class Client()
```

Representation of a registered client record.

#### from\_json\_dict

```python
@classmethod
def from_json_dict(cls, json: Mapping[str, str]) -> "Client"
```

Create a Client from a JSON dict returned by the server.

## Environment Objects

```python
@dataclasses.dataclass(frozen=True)
class Environment()
```

Representation of the information about the H2O Cloud environment.

#### h2o\_cloud\_environment

Identifier of the environment.

For example: &quot;https://cloud.h2o.ai&quot;.

This is the base URL of the environment. Clients can use this to validate
that they are talking to the correct environment.

#### issuer\_url

OpenID Connect issuer_url.

This is where clients find the OpenID Connect discovery on the well-known endpoint.

#### h2o\_cloud\_platform\_oauth2\_scope

OAuth 2.0 scope that clients should use to access the H2O Cloud Platform.

This is the default scope that clients should use if the service does not
define its own scope.

#### h2o\_cloud\_version

Version of the H2O Cloud Platform release that is running in the environment.

In XC YY.MM.V format for released versions (e.g. MC 23.04.01 for managed
cloud or HC 23.01.1 for hybrid cloud). Can be arbitrary string for
testing or special environments.

#### from\_json\_dict

```python
@classmethod
def from_json_dict(cls, json: Mapping[str, str]) -> "Environment"
```

Create an Environment from a JSON dict returned by the server.

## Discovery Objects

```python
@dataclasses.dataclass(frozen=True)
class Discovery()
```

Representation of the discovery records.

#### environment

Information about the environment.

#### services

Map of registered services in the {&quot;service-identifier&quot;: Service(...)} format.

#### clients

Map of registered clients in the {&quot;client-identifier&quot;: Client(...)} format.

