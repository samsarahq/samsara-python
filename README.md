# Samsara Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fsamsarahq%2Fsamsara-python-sdk)
[![pypi](https://img.shields.io/pypi/v/samsara-api)](https://pypi.python.org/pypi/samsara-api)

The Samsara Python library provides convenient access to the Samsara API from Python.

## Table of Contents

- [Requirements](#requirements)
- [Documentation](#documentation)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Async Client](#async-client)
  - [Exception Handling](#exception-handling)
  - [Pagination](#pagination)
- [Webhook Signature Verification](#webhook-signature-verification)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [AWS Lambda / Serverless](#aws-lambda--serverless)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Requirements

- Python 3.7+
- A Samsara account with API access
- An API token (available from your [Samsara Dashboard](https://cloud.samsara.com/) > Settings > Developer > API Tokens)

## Documentation

API reference documentation is available [here](https://developers.samsara.com/reference/overview).

## Installation

```sh
pip install samsara-api
```

## Quick Start

Get started with the Samsara SDK in just a few lines of code:

```python
from samsara import Samsara

# Initialize the client with your API token
client = Samsara(
    token="YOUR_TOKEN",  # Get your token at https://cloud.samsara.com/settings/api-tokens
)

# Get your organization information
org_info = client.organization_info.get_organization_info()
print(f"Organization: {org_info.data.name}")

# List all vehicles in your fleet
vehicles = client.vehicles.list()
for vehicle in vehicles:
    print(f"Vehicle: {vehicle.name} (ID: {vehicle.id})")

# Get specific vehicle details
vehicle = client.vehicles.get(id="YOUR_VEHICLE_ID")
print(f"Vehicle VIN: {vehicle.data.vin}")
```

For more detailed examples, see the [Examples](#examples) section.

## Features

The Samsara Python SDK provides:

- **Type Safety**: Full type hints for better IDE support and autocomplete
- **Automatic Pagination**: Seamlessly iterate through large result sets
- **Async Support**: Both synchronous and asynchronous clients
- **Smart Retries**: Automatic retry logic with exponential backoff
- **Error Handling**: Comprehensive exception handling for all API errors
- **Webhook Verification**: Built-in utilities for webhook signature validation
- **Raw Response Access**: Get headers and raw response data when needed
- **Flexible Configuration**: Customize timeouts, retries, and HTTP clients

## Reference

A full reference for this library is available [here](https://github.com/samsarahq/samsara-python/blob/HEAD/./reference.md).

## Usage

### Basic Usage

Instantiate and use the client with the following:

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)

# The SDK handles pagination automatically - just iterate through results
response = client.vehicles.list()
for item in response:
    print(item)  # Process each vehicle stat

# Alternatively, you can paginate page-by-page for more control
for page in response.iter_pages():
    print(f"Processing page with {len(page.items)} items")
    for item in page.items:
        print(item)
```

### Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio
from samsara import AsyncSamsara

client = AsyncSamsara(
    token="YOUR_TOKEN",
)


async def main() -> None:
    # The SDK handles pagination automatically - just iterate through results
    response = await client.vehicles.list()
    async for item in response:
        print(item)  # Process each vehicle stat

    # Alternatively, you can paginate page-by-page for more control
    async for page in response.iter_pages():
        print(f"Processing page with {len(page.items)} items")
        for item in page.items:
            print(item)


asyncio.run(main())
```

### Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from samsara.core.api_error import ApiError

try:
    client.vehicles.list()
except ApiError as e:
    print(f"API Error: {e.status_code}")
    print(f"Response: {e.body}")
```

### Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as iterators for the underlying objects.

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)

# Automatic pagination - SDK fetches pages as needed
response = client.addresses.list()
for address in response:
    print(f"Address: {address.formatted_address}")

# Manual page-by-page iteration for more control
response = client.addresses.list()
for page in response.iter_pages():
    print(f"Page contains {len(page.items)} addresses")
    for address in page.items:
        print(f"  - {address.formatted_address}")
```

## Webhook Signature Verification

The SDK provides utility methods that allow you to verify webhook signatures and ensure
that all webhook events originate from Samsara. This is a critical security measure to validate
that incoming webhook requests are authentic.

### Setting Up Webhooks

1. Configure webhooks in your [Samsara Dashboard](https://cloud.samsara.com/) > Settings > Developer > Webhooks
2. Note your webhook signature key (used for verification)
3. Specify the notification URL where Samsara will send events

### Verifying Webhook Signatures

```python
from samsara.utils.webhooks_helper import verify_signature

# In your webhook endpoint handler (e.g., Flask, FastAPI)
def webhook_handler(request):
    # Verify the webhook signature
    is_valid = verify_signature(
        request_body=request.body,  # Raw request body as string
        signature_header=request.headers['x-samsara-signature'],
        signature_key="YOUR_SIGNATURE_KEY",  # From Samsara Dashboard
        notification_url="https://example.com/webhook",  # Your webhook URL
    )
    
    if not is_valid:
        return {"error": "Invalid signature"}, 401
    
    # Process the webhook event
    event_data = request.json()
    print(f"Received event: {event_data['eventType']}")
    
    return {"status": "success"}, 200
```

### Example with Flask

```python
from flask import Flask, request, jsonify
from samsara.utils.webhooks_helper import verify_signature

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def samsara_webhook():
    # Verify signature
    is_valid = verify_signature(
        request_body=request.get_data(as_text=True),
        signature_header=request.headers.get('x-samsara-signature'),
        signature_key="YOUR_SIGNATURE_KEY",
        notification_url="https://yourdomain.com/webhook",
    )
    
    if not is_valid:
        return jsonify({"error": "Invalid signature"}), 401
    
    # Handle the event
    event = request.get_json()
    print(f"Event type: {event.get('eventType')}")
    
    return jsonify({"status": "received"}), 200
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
response = client.vehicles.with_raw_response.list(...)
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
client.vehicles.list(..., request_options={
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
client.vehicles.list(..., request_options={
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

## Examples

### Getting Vehicle Locations

Track your fleet in real-time by fetching current vehicle locations:

```python
from samsara import Samsara
from datetime import datetime, timedelta

client = Samsara(token="YOUR_TOKEN")

# Get current locations for all vehicles
locations = client.vehicle_locations.get_vehicle_locations()
for vehicle_data in locations.data:
    print(f"Vehicle {vehicle_data.name}: {vehicle_data.location.latitude}, {vehicle_data.location.longitude}")
    print(f"  Speed: {vehicle_data.location.speed} mph")
    print(f"  Time: {vehicle_data.location.time}")
```

### Monitoring Driver Hours of Service

Check driver HOS status to ensure compliance:

```python
from samsara import Samsara

client = Samsara(token="YOUR_TOKEN")

# List all drivers
drivers = client.drivers.list()
for driver in drivers:
    print(f"Driver: {driver.name}")
    
    # Get HOS logs for a specific driver
    hos_logs = client.hours_of_service.get_hos_logs(driver_ids=[driver.id])
    for hos_log in hos_logs.data:
        for log in hos_log.hos_logs:
            print(f"  Status: {log.hos_status_type} at {log.log_start_time}")
```

### Managing Vehicle Maintenance

Track vehicle health and maintenance schedules:

```python
from samsara import Samsara

client = Samsara(token="YOUR_TOKEN")

# Get vehicle stats including engine hours and odometer
stats = client.vehicles.list()
for stat in stats:
    print(f"Vehicle: {stat.name}")
    print(f"  Engine Hours: {stat.engine_hours}")
    print(f"  Odometer: {stat.odometer_meters / 1609.34:.1f} miles")
    
# List maintenance issues
issues = client.issues.list()
for issue in issues:
    print(f"Issue: {issue.type} - {issue.description}")
    print(f"  Vehicle: {issue.vehicle.name}")
    print(f"  Severity: {issue.severity}")
```

### Retrieving Historical Trip Data

Analyze past trips for reporting and optimization:

```python
from samsara import Samsara
from datetime import datetime, timedelta

client = Samsara(token="YOUR_TOKEN")

# Get trips from the last 7 days
end_time = datetime.now()
start_time = end_time - timedelta(days=7)

trips = client.trips.list(
    start_time=start_time.isoformat(),
    end_time=end_time.isoformat()
)

total_distance = 0
for trip in trips:
    print(f"Trip: {trip.start_location} -> {trip.end_location}")
    print(f"  Distance: {trip.distance_meters / 1609.34:.1f} miles")
    print(f"  Duration: {trip.duration_ms / 60000:.1f} minutes")
    total_distance += trip.distance_meters

print(f"\nTotal distance traveled: {total_distance / 1609.34:.1f} miles")
```

### Working with Vehicle Groups (Tags)

Organize and filter your fleet using tags:

```python
from samsara import Samsara

client = Samsara(token="YOUR_TOKEN")

# List all tags (vehicle groups)
tags = client.tags.list()
for tag in tags:
    print(f"Tag: {tag.name}")
    print(f"  Vehicles: {len(tag.vehicles)}")

# Get vehicles with a specific tag
tag_id = "YOUR_TAG_ID"
vehicles = client.vehicles.list(tag_ids=[tag_id])
for vehicle in vehicles:
    print(f"  - {vehicle.name}")
```

### Batch Operations with Async Client

Process multiple API calls concurrently for better performance:

```python
import asyncio
from samsara import AsyncSamsara

async def get_fleet_summary():
    client = AsyncSamsara(token="YOUR_TOKEN")
    
    # Fetch multiple resources concurrently
    vehicles_task = client.vehicles.list()
    drivers_task = client.drivers.list()
    assets_task = client.assets.list()
    
    # Wait for all requests to complete
    vehicles = []
    async for vehicle in vehicles_task:
        vehicles.append(vehicle)
    drivers = []
    async for driver in drivers_task:
        drivers.append(driver)
    assets = []
    async for asset in assets_task:
        assets.append(asset)
    
    print(f"Fleet Summary:")
    print(f"  Vehicles: {len(vehicles)}")
    print(f"  Drivers: {len(drivers)}")
    print(f"  Assets: {len(assets)}")

asyncio.run(get_fleet_summary())
```

## AWS Lambda / Serverless

The Samsara SDK works seamlessly in serverless environments like AWS Lambda. Here's how to set it up:

### Creating a Lambda Layer

The SDK can be packaged as a Lambda Layer for reuse across multiple functions:

```bash
# Create a directory for the layer
mkdir -p python/lib/python3.9/site-packages

# Install the SDK and dependencies
pip install samsara-api -t python/lib/python3.9/site-packages

# Create a zip file
zip -r samsara-layer.zip python
```

### Lambda Function Example

```python
import json
from samsara import Samsara

def lambda_handler(event, context):
    # Initialize client (API token from environment variable)
    import os
    client = Samsara(token=os.environ['SAMSARA_API_TOKEN'])
    
    # Get vehicle locations
    locations = client.vehicle_locations.list()
    
    result = []
    for location in locations:
        result.append({
            'name': location.name,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'speed': location.speed_miles_per_hour
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
```

### Lambda Configuration Tips

- **Memory**: Allocate at least 256 MB for optimal performance
- **Timeout**: Set timeout to 30+ seconds for API calls with pagination
- **Environment Variables**: Store your API token in `SAMSARA_API_TOKEN`
- **VPC**: Not required unless you need to access private resources
- **Cold Starts**: The SDK initializes quickly, but consider using provisioned concurrency for time-sensitive applications

## Troubleshooting

### Authentication Errors

**Problem**: `401 Unauthorized` errors

**Solution**:
- Verify your API token is correct
- Check that the token hasn't expired
- Ensure the token has the necessary permissions for the endpoints you're accessing
- Get your token from [Samsara Dashboard → API Tokens](https://cloud.samsara.com/settings/api-tokens)

### Rate Limiting

**Problem**: `429 Too Many Requests` errors

**Solution**:
- The SDK automatically retries with exponential backoff
- Reduce request frequency or implement batching
- Contact Samsara support to increase your rate limits
- Use pagination to fetch data in smaller chunks

### Timeout Errors

**Problem**: Requests timing out

**Solution**:
```python
# Increase timeout at client level
client = Samsara(token="YOUR_TOKEN", timeout=120.0)

# Or per request
client.vehicles.list(request_options={"timeout_in_seconds": 60})
```

### SSL/Certificate Errors

**Problem**: SSL verification failures

**Solution**:
```python
import httpx
from samsara import Samsara

# For corporate proxies or custom certificates
client = Samsara(
    token="YOUR_TOKEN",
    httpx_client=httpx.Client(verify=False)  # Not recommended for production
)
```

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'samsara'`

**Solution**:
```bash
# Ensure the package is installed
pip install samsara-api

# Verify installation
pip show samsara-api

# Check Python version (requires 3.7+)
python --version
```

### Pagination Issues

**Problem**: Not all results are returned

**Solution**:
```python
# Always iterate through the pager object
response = client.vehicles.list()
all_vehicles = []
for vehicle in response:  # This automatically handles pagination
    all_vehicles.append(vehicle)

print(f"Total vehicles: {len(all_vehicles)}")
```

### Type Hints Not Working

**Problem**: IDE not showing autocomplete

**Solution**:
- Ensure you're using Python 3.7+
- Update your IDE's Python language server
- The SDK includes full type hints via `py.typed`
- Try restarting your IDE or Python language server

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
