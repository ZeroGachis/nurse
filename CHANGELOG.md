# Changelog

## [2.0.1](https://github.com/ZeroGachis/nurse/compare/2.0.0...2.0.1) (2025-04-30)


### Bug Fixes

* Fix invalid reference to README in pyproject.toml file ([0999f51](https://github.com/ZeroGachis/nurse/commit/0999f51749e4a1a2dc670efd5309ba05a6d71c2a))

## [2.0.0](https://github.com/ZeroGachis/nurse/compare/1.0.1...2.0.0) (2025-04-30)


### ⚠ BREAKING CHANGES

* Enable to serve singleton or factory

### Features

* Enable to serve singleton or factory ([bffde8e](https://github.com/ZeroGachis/nurse/commit/bffde8e8760372be12726d572e34c5f6184eb301))


### Miscellaneous Chores

* **ci:** Remove destroy step ([cddf0b8](https://github.com/ZeroGachis/nurse/commit/cddf0b8c6a889fc063e954aa36f7ff23ac4c779e))
* **docker:** Fix git version ([790e881](https://github.com/ZeroGachis/nurse/commit/790e881a105a8cb6ec440b7c3ebd1bf88ef8b751))
* **docker:** Fix lint issue ([115ba3d](https://github.com/ZeroGachis/nurse/commit/115ba3d8065a061f7c35bcfdaee1748cc88d38ba))
* Remove unused docker-compose & Pycharm config ([1d02512](https://github.com/ZeroGachis/nurse/commit/1d0251219d929b70138e84fcab849fc893e5eeab))
* Simplify README ([3c19d9d](https://github.com/ZeroGachis/nurse/commit/3c19d9d6af0859ffd3f2980687f2a1b5ad301aa6))
* Update mise config and python dev dependencies ([67a8136](https://github.com/ZeroGachis/nurse/commit/67a8136a9545982b0e24879bc701524b3a54075d))
* Upgrade dockerfile base image to use Python3.12 alpine slim ([74b70b8](https://github.com/ZeroGachis/nurse/commit/74b70b8c8d4562b2ff5b87a6e7e327d082d0fc58))

## [1.0.1](https://github.com/ZeroGachis/nurse/compare/1.0.0...1.0.1) (2025-04-24)


### Bug Fixes

* typo in workflow ([0dffbc2](https://github.com/ZeroGachis/nurse/commit/0dffbc2283b5f04af95697484e7b3548479ce9a0))


### Miscellaneous Chores

* **deps:** update dependency ruff to ^0.11.0 ([276127a](https://github.com/ZeroGachis/nurse/commit/276127aa59689aba3b926c9dead6eb3011ec1bf1))


### Continuous Integration

* add permissions on github actions ([8ed1f56](https://github.com/ZeroGachis/nurse/commit/8ed1f56a6887b324abecc30696e692632dc8f5e1))

## [1.0.0](https://github.com/ZeroGachis/nurse/compare/v0.5.1...1.0.0) (2024-11-13)


### ⚠ BREAKING CHANGES

* Expose annotations types + make nurse.get() raise when service is not registered

### Features

* Expose annotations types + make nurse.get() raise when service is not registered ([6010efe](https://github.com/ZeroGachis/nurse/commit/6010efe7ec6c5ddf1258b60eb336b9ce316b1cde))


### Bug Fixes

* Fix wrong cwd in docker image ([e79648f](https://github.com/ZeroGachis/nurse/commit/e79648f1ec0fe782932bac0e2b5ea76ae7c05c37))


### Miscellaneous Chores

* Bump from 0.5.1 to 0.6.0 ([b43eede](https://github.com/ZeroGachis/nurse/commit/b43eedee40fd53df90b17419a8cfc2bf9ce40ddf))
* **docker:** Bump python version from 3.9 to 3.11 ([fc79b8c](https://github.com/ZeroGachis/nurse/commit/fc79b8cc2029fc6a0704aedd7a61d4daafe2abe7))
* ignore asdf config file ([4af5675](https://github.com/ZeroGachis/nurse/commit/4af56750dfc059fae8794ef22a3531b2822bbba3))
* Move dev dependencies to dev group dependencies ([8c67379](https://github.com/ZeroGachis/nurse/commit/8c673791f15593c1c35d69c1da2a653e8db4fe8c))
* Move flake8 to dev dependencies and upgrade to latest version ([1cb2884](https://github.com/ZeroGachis/nurse/commit/1cb2884dd90082582515945f1656cbe9ca707f99))
* On release, push to ghcr instead of pypi ([1961456](https://github.com/ZeroGachis/nurse/commit/196145660fbed3047221a6b07b04e95fca62904e))
* Upgrade python/pytest + migrate to ruff ([1d4c960](https://github.com/ZeroGachis/nurse/commit/1d4c960564675d825fe599d1a2f6f936e1b6ab55))
