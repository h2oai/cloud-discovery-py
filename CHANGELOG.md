# Changelog

## [3.2.0](https://github.com/h2oai/cloud-discovery-py/compare/v3.1.0...v3.2.0) (2025-08-28)


### Features

* Add support for component documentation URI ([#127](https://github.com/h2oai/cloud-discovery-py/issues/127)) ([6c5893d](https://github.com/h2oai/cloud-discovery-py/commit/6c5893d261a6f9417c957d5c8e2fbaf9bbfec604))
* Improve compatibility with Python 3.14 ([#121](https://github.com/h2oai/cloud-discovery-py/issues/121)) ([aa7e702](https://github.com/h2oai/cloud-discovery-py/commit/aa7e7026c8c68f7ba16b8064effd4565764950ff))


### Bug Fixes

* 🐛 don't load credentials when config does not match the discovered environment ([#122](https://github.com/h2oai/cloud-discovery-py/issues/122)) ([2305d75](https://github.com/h2oai/cloud-discovery-py/commit/2305d752185d488871041de5544c268ec6aa6903))

## [3.1.0](https://github.com/h2oai/cloud-discovery-py/compare/v3.0.0...v3.1.0) (2025-02-03)


### Features

* ✨ Discover registered components when available ([#119](https://github.com/h2oai/cloud-discovery-py/issues/119)) ([03aed56](https://github.com/h2oai/cloud-discovery-py/commit/03aed56bb1612a4ca3be4cd03f554654f95920ce))

## [3.0.0](https://github.com/h2oai/cloud-discovery-py/compare/v2.2.1...v3.0.0) (2025-01-22)


### ⚠ BREAKING CHANGES

* Now requires requires `httpx >= 0.23.0`
* Do not officially support Python 3.8 anymore

### Performance Improvements

* ⚡️ Fetch data concurrently in async mode ([#117](https://github.com/h2oai/cloud-discovery-py/issues/117)) ([2a8f8ea](https://github.com/h2oai/cloud-discovery-py/commit/2a8f8eaab15953f91dec908e4d77c84c039f14a4))


### Build System

* Do not officially support Python 3.8 anymore ([5a6972e](https://github.com/h2oai/cloud-discovery-py/commit/5a6972e233288e9b2cda39bbdd43f108a2b81e9b))
* Now requires requires `httpx &gt;= 0.23.0` ([5a6972e](https://github.com/h2oai/cloud-discovery-py/commit/5a6972e233288e9b2cda39bbdd43f108a2b81e9b))

## [2.2.1](https://github.com/h2oai/cloud-discovery-py/compare/v2.2.0...v2.2.1) (2025-01-09)


### Bug Fixes

* 🐛 Make addition of links to the discovery model backward compatible ([#115](https://github.com/h2oai/cloud-discovery-py/issues/115)) ([fd994c4](https://github.com/h2oai/cloud-discovery-py/commit/fd994c4fdd5a07f4aaeae9e5ca4445c5ef309658))

## [2.2.0](https://github.com/h2oai/cloud-discovery-py/compare/v2.1.1...v2.2.0) (2025-01-08)


### Features

* ✨ Discover registered links when available ([#112](https://github.com/h2oai/cloud-discovery-py/issues/112)) ([8d584dd](https://github.com/h2oai/cloud-discovery-py/commit/8d584ddf5a437a533b40a6b25460f4028b45f9a6))

## [2.1.1](https://github.com/h2oai/cloud-discovery-py/compare/v2.1.0...v2.1.1) (2024-11-11)


### Bug Fixes

* 🐛 pass the timeout and ssl_context to the httpx ([#105](https://github.com/h2oai/cloud-discovery-py/issues/105)) ([106dbf2](https://github.com/h2oai/cloud-discovery-py/commit/106dbf27732cacf1dd795a694e95ab7e14b86b41)), closes [#104](https://github.com/h2oai/cloud-discovery-py/issues/104)

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
