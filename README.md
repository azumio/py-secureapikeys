# Azumio Secure Api Keys

ASPK uses Google KMS.

## Prerequisite

[Authenticate google account](https://cloud.google.com/docs/authentication/production)

## Installation

```
pip install git+https://github.com/azumio/py-secureapikeys.git#egg=py-secureapikeys
```

## Usage

```python
from secureapikeys.apikeys import SecureApiKeys

sak = SecureApiKeys('azumio-com', 'global', 'my-keyring','my-key')
microservice_api_key = sak.decrypt_key('my encrypted key in base64 format')

# use the microservice_api_key for calling that microservice
```

Decrypt API keys:

```python
api_key = sak.decrypt_key("base64 encodede and KMS encrypted API Key")
```
