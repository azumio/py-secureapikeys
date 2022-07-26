# Azumio Secure Api Keys

ASPK uses Google KMS.

## Prerequisite

[Authenticate google account](https://cloud.google.com/docs/authentication/production)

## Installation

```
pip install py_secureapikeys_azumio
```

## Usage

```python
from py_secureapikeys_azumio.apikeys import SecureApiKeys

sak = SecureApiKeys('azumio-com', 'global', 'my-keyring','my-key')
microservice_api_key = sak.decrypt_key('my encrypted key in base64 format')

# use the microservice_api_key for calling that microservice
```

Decrypt API keys:

```python
api_key = sak.decrypt_key("base64 encodede and KMS encrypted API Key")
```

## Developers

Project uses Github actions.

Push to `main` branch it will deploy to https://test.pypi.org/

### Production release

1. Create tag

```
git tag 1.0.1
```

2. Upgrade version in `setup.py` and `pyproject.toml`.

3. Push tags:

```
git push origin --tags
```
