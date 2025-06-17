# Samsara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fsamsarahq%2Fsamsara-python-sdk)
[![pypi](https://img.shields.io/pypi/v/samsara-api)](https://pypi.python.org/pypi/samsara-api)

The Samsara Python library provides convenient access to the Samsara API from Python.

## Documentation

API reference documentation is available [here](https://developers.samsara.com/reference/overview).

## Installation

```sh
pip install samsara-api
```

## Reference

A full reference for this library is available [here](https://github.com/samsarahq/samsara-python-sdk/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.vehicles.stats.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from samsara import AsyncSamsara

client = AsyncSamsara(
    token="YOUR_TOKEN",
)


async def main() -> None:
    response = await client.vehicles.stats.list()
    async for item in response:
        yield item

    # alternatively, you can paginate page-by-page
    async for page in response.iter_pages():
        yield page


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from samsara.core.api_error import ApiError

try:
    client.vehicles.stats.list(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.addresses.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Webhook Signature Verification

The SDK provides utility methods that allow you to verify webhook signatures and ensure
that all webhook events originate from Samsara. The `verify_signature` method will verify
the signature.

```python
from samsara.utils.webhooks_helper import verify_signature

is_valid = verify_signature(
    request_body=request_body,
    signature_header=request.headers['x-samsara-hmacsha256-signature'],
    signature_key="YOUR_SIGNATURE_KEY",
    notification_url="https://example.com/webhook", # The URL where event notifications are sent.
)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from samsara import Samsara

client = Samsara(
    ...,
)
response = client.vehicles.stats.with_raw_response.list(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.addresses.list(...)
print(pager.response.headers)  # access the response headers for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response.headers)  # access the response headers for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.vehicles.stats.list(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from samsara import Samsara

client = Samsara(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.vehicles.stats.list(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from samsara import Samsara

client = Samsara(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
