# Decrypt Function
[Evervault](https://evervault.com) makes it easy to encrypt data at source, process it in a secure, serverless function that you can re-build and deploy anytime.

The best practice is to never let sensitive data touch your server or be stored at rest in your data stores. However, there may be cases where you need to decrypt data on your own server.

This function will decrypt any data passed into it.

## Getting started with Evervault

Evervault consists of two parts, encrypting your data at source, using either our any of our SDKs and then sending that encrypted data to a Function to be processed securely.

This Function takes a payload that should contain a `name` key. Running the Function is very simple.

## The steps
1. Encrypt your data at source, using one of our SDKs.
2. Process the encrypted data in a Function and return the decrypted data

### Encrypting at source
```python
# This example uses the Evervault Python SDK.
import evervault

# Initialize the client with your app's API key
evervault.init("<YOUR_API_KEY>")

# Encrypt your data
encrypted = evervault.encrypt({ "name": "Claude" })
```

### Obtain the encrypted data in a Function
You should encrypt this payload using any SDKs, then run it in the Hello Function:

```python
# Process the encrypted data in a Function
result = evervault.run("<YOUR_FUNCTION_NAME>", encrypted)
```

## Return the decrypted data to your server
This Function is very simple. Here is the full code:

```python
def handler(data, context):
    return {'data': data}
```

Or check it out in [main.py](./main.py).

--- 
If you want to know more about Evervault, check out our [documentation](https://docs.evervault.com).
