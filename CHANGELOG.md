# Changelog

## 1.4.0 (2026-05-01)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/Benchify/formalize-python/compare/v1.3.0...v1.4.0)

### Features

* get rid of legacy routes ([5da5279](https://github.com/Benchify/formalize-python/commit/5da527973b1d2d994bf3dfeccd5e69bc65aa12f5))
* **internal:** implement indices array format for query and form serialization ([563c58c](https://github.com/Benchify/formalize-python/commit/563c58cb935ec2baf52614b9a2b8f7f2ac4178e7))
* support setting headers via env ([799fdc0](https://github.com/Benchify/formalize-python/commit/799fdc05dfafc29f30f553861ec6ee524410b20a))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([cb1116e](https://github.com/Benchify/formalize-python/commit/cb1116e13d34679fa2cd73fe17cbf3bfa74c106b))
* ensure file data are only sent as 1 parameter ([f2e61d8](https://github.com/Benchify/formalize-python/commit/f2e61d8e07e220de2b785c0b9985e403bf97fca1))
* sanitize endpoint path params ([f9b35f6](https://github.com/Benchify/formalize-python/commit/f9b35f6d04184131168dde207f7d8dac47a7ecd7))
* use correct field name format for multipart file arrays ([6630691](https://github.com/Benchify/formalize-python/commit/66306915b66d66bc80074de143ce101ba7f3c3c0))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([aa8ebe4](https://github.com/Benchify/formalize-python/commit/aa8ebe4e973bdabed6e614b86ea7662918925955))


### Chores

* **ci:** skip lint on metadata-only changes ([f3ad8e3](https://github.com/Benchify/formalize-python/commit/f3ad8e3e3f5a4f4a49bad8f60ff3202d5e487152))
* **internal:** more robust bootstrap script ([f3e33d5](https://github.com/Benchify/formalize-python/commit/f3e33d5e7b7652b0764ae2f39ca186aaba690a4c))
* **internal:** reformat pyproject.toml ([cc326cf](https://github.com/Benchify/formalize-python/commit/cc326cfca752a635b78a66cc326fae8b58f62ad4))
* **internal:** update gitignore ([05eef18](https://github.com/Benchify/formalize-python/commit/05eef18b272c2be5047fa6c51504fc1e49aca1cb))

## 1.3.0 (2026-03-17)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/Benchify/formalize-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([ae84d36](https://github.com/Benchify/formalize-python/commit/ae84d362d47748dab900d9593210843ff8bfee17))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([79b5f12](https://github.com/Benchify/formalize-python/commit/79b5f1214c8b556d252340414befaac56c439e9d))
* **pydantic:** do not pass `by_alias` unless set ([6de4065](https://github.com/Benchify/formalize-python/commit/6de4065d83cec7638c0bff30ee895852e2145960))


### Chores

* **internal:** tweak CI branches ([409c07e](https://github.com/Benchify/formalize-python/commit/409c07eb5296d05266be5e9fc24c6d794b0e60bf))

## 1.2.0 (2026-03-16)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/Benchify/formalize-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** manual updates ([f6cccf6](https://github.com/Benchify/formalize-python/commit/f6cccf6388d8b3b25837d2386704c65478336c72))
* **api:** manual updates ([5fbadc3](https://github.com/Benchify/formalize-python/commit/5fbadc3a1e2496fad356aee31e48568eaf8433b8))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([b2a03bc](https://github.com/Benchify/formalize-python/commit/b2a03bcfe6b3091bb71a5a7c8d26a15649022b2c))
* update placeholder string ([6b55582](https://github.com/Benchify/formalize-python/commit/6b555821785b082a042906593fcc8e984623b0de))

## 1.1.0 (2026-03-06)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/Benchify/formalize-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** manual updates ([dfe90dd](https://github.com/Benchify/formalize-python/commit/dfe90ddefabf9523ffacb51ebd28210e159f856b))

## 1.0.0 (2026-03-05)

Full Changelog: [v0.0.3...v1.0.0](https://github.com/Benchify/formalize-python/compare/v0.0.3...v1.0.0)

### Chores

* update SDK settings ([b64f037](https://github.com/Benchify/formalize-python/commit/b64f03751166f206e8dca5ec9b01867614e78b82))

## 0.0.3 (2026-03-05)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/Benchify/formalize-python/compare/v0.0.2...v0.0.3)

### Chores

* update SDK settings ([50d401a](https://github.com/Benchify/formalize-python/commit/50d401a736de5d2621b56814ce65f0871b5ee5cb))

## 0.0.2 (2026-03-05)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/Benchify/formalize-python/compare/v0.0.1...v0.0.2)

### Chores

* update SDK settings ([b5e9389](https://github.com/Benchify/formalize-python/commit/b5e9389e3dd97e47ecbf46f6243b94650817b030))
* update SDK settings ([af29af6](https://github.com/Benchify/formalize-python/commit/af29af642ad813efd20eb92ae50e7559c89aff79))
* update SDK settings ([572be36](https://github.com/Benchify/formalize-python/commit/572be36db5ff5fc25123c413fcb3c65163cedf21))
* update SDK settings ([d979303](https://github.com/Benchify/formalize-python/commit/d97930319515cd0495719fb3ee5b862c9eff14c5))
