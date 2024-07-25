# Changelog

## [2.1.0](https://github.com/h2oai/cloud-discovery-py/compare/v2.0.0...v2.1.0) (2024-07-25)


### Features

* ✨ expose http timeout and ssl_context options on the entry functions ([#101](https://github.com/h2oai/cloud-discovery-py/issues/101)) ([f63a371](https://github.com/h2oai/cloud-discovery-py/commit/f63a371e4837a6b04a17f3e9cc6ef6050a944a52)), closes [#100](https://github.com/h2oai/cloud-discovery-py/issues/100)
* Use default ssl context by default ([f63a371](https://github.com/h2oai/cloud-discovery-py/commit/f63a371e4837a6b04a17f3e9cc6ef6050a944a52))


### Bug Fixes

* Use nase inherited constructor in sync `Client` ([f63a371](https://github.com/h2oai/cloud-discovery-py/commit/f63a371e4837a6b04a17f3e9cc6ef6050a944a52))

## [2.0.0](https://github.com/h2oai/cloud-discovery-py/compare/v1.1.1...v2.0.0) (2024-04-19)


### ⚠ BREAKING CHANGES

* Python 3.7 is no longer supported. The minimum supported version is now Python 3.8.

### Documentation

* 📝 remove confusing example from README ([#95](https://github.com/h2oai/cloud-discovery-py/issues/95)) ([3da6c74](https://github.com/h2oai/cloud-discovery-py/commit/3da6c7451368fabf835e5966ac258ee79cf790e8))


### Build System

* 💥 remove support for Python 3.7 ([be67542](https://github.com/h2oai/cloud-discovery-py/commit/be67542550151c2673e38d640391793b8295bde2))


### Continuous Integration

* 👷 extend testing matrix of the httpx dependency ([#88](https://github.com/h2oai/cloud-discovery-py/issues/88)) ([b6fca62](https://github.com/h2oai/cloud-discovery-py/commit/b6fca62f0ed94b5edb9825945ca6d0028b7f65c1))

## [1.1.1](https://github.com/h2oai/cloud-discovery-py/compare/v1.1.0...v1.1.1) (2023-12-04)


### Documentation

* 📝 Reflect new features in the README ([#79](https://github.com/h2oai/cloud-discovery-py/issues/79)) ([375969b](https://github.com/h2oai/cloud-discovery-py/commit/375969b3ca8682f1ce94a0d06028b8bd5fddd92d))

## [1.1.0](https://github.com/h2oai/cloud-discovery-py/compare/v1.0.1...v1.1.0) (2023-09-18)


### Features

* ✨ add support for reading client credentials from the local H2O CLI config file ([#68](https://github.com/h2oai/cloud-discovery-py/issues/68)) ([16eb15f](https://github.com/h2oai/cloud-discovery-py/commit/16eb15fd01fc769e38d824bad8331c854608014a))
* ✨ add support for reading credentials from the environment variables ([#67](https://github.com/h2oai/cloud-discovery-py/issues/67)) ([f7e44fe](https://github.com/h2oai/cloud-discovery-py/commit/f7e44fe2353556e56eaadaa71fcac84d1108b3a2))
* ✨ add support for reading endpoint from the local H2O CLI configuration file ([#69](https://github.com/h2oai/cloud-discovery-py/issues/69)) ([89727c3](https://github.com/h2oai/cloud-discovery-py/commit/89727c3f452ec341e1c7cf55dcb59e17bb72ffa6))
* ✨ allow to set timeout and ssl_context for the underlying http client. ([#76](https://github.com/h2oai/cloud-discovery-py/issues/76)) ([d164e30](https://github.com/h2oai/cloud-discovery-py/commit/d164e307319939e159faf74015f8dc0240b44db4)), closes [#28](https://github.com/h2oai/cloud-discovery-py/issues/28)
* 🏷️ mark package as typed ([#73](https://github.com/h2oai/cloud-discovery-py/issues/73)) ([13ad7db](https://github.com/h2oai/cloud-discovery-py/commit/13ad7db2562c7030978a5d1feef3bd1d63aa0fd8))
* 🥅 handle errors that hint discovery server not being enabled in environment. ([#71](https://github.com/h2oai/cloud-discovery-py/issues/71)) ([3e4a0e3](https://github.com/h2oai/cloud-discovery-py/commit/3e4a0e38ee7be2e519091f3292926a3d5e8f4c6d))

## [1.0.1](https://github.com/h2oai/cloud-discovery-py/compare/v1.0.0...v1.0.1) (2023-05-12)


### Documentation

* 📝 document environment version format ([#29](https://github.com/h2oai/cloud-discovery-py/issues/29)) ([1bf6f4a](https://github.com/h2oai/cloud-discovery-py/commit/1bf6f4a2a1faefce3e5141130cd05c7bdfaf48bd))
* 📝 use Sphinx `#:` comments to document model fields ([#51](https://github.com/h2oai/cloud-discovery-py/issues/51)) ([ff3a4f8](https://github.com/h2oai/cloud-discovery-py/commit/ff3a4f8f646eb304f741dae83ca260460d0f41be))
