# samsara.DefaultApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](DefaultApi.md#create_address) | **POST** /addresses | Create an address
[**create_contact**](DefaultApi.md#create_contact) | **POST** /contacts | Create a contact
[**create_driver**](DefaultApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**create_tag**](DefaultApi.md#create_tag) | **POST** /tags | Create a tag
[**create_user**](DefaultApi.md#create_user) | **POST** /users | Create a user
[**delete_address**](DefaultApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
[**delete_contact**](DefaultApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete a contact
[**delete_tag**](DefaultApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
[**get_address**](DefaultApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
[**get_contact**](DefaultApi.md#get_contact) | **GET** /contacts/{id} | Retrieve a contact
[**get_driver**](DefaultApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_tag**](DefaultApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{id} | Retrieve a user
[**get_vehicle**](DefaultApi.md#get_vehicle) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
[**get_vehicle_locations**](DefaultApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
[**get_vehicle_locations_feed**](DefaultApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
[**get_vehicle_locations_history**](DefaultApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations
[**get_vehicle_stats**](DefaultApi.md#get_vehicle_stats) | **GET** /fleet/vehicles/stats | List most recent vehicle stats
[**get_vehicle_stats_feed**](DefaultApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Follow a feed of vehicle stats
[**get_vehicle_stats_history**](DefaultApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Get historical vehicle stats
[**list_addresses**](DefaultApi.md#list_addresses) | **GET** /addresses | List all addresses
[**list_contacts**](DefaultApi.md#list_contacts) | **GET** /contacts | List all contacts
[**list_drivers**](DefaultApi.md#list_drivers) | **GET** /fleet/drivers | List all drivers
[**list_tags**](DefaultApi.md#list_tags) | **GET** /tags | List all tags
[**list_user_roles**](DefaultApi.md#list_user_roles) | **GET** /user-roles | List all user roles
[**list_users**](DefaultApi.md#list_users) | **GET** /users | List all users
[**list_vehicles**](DefaultApi.md#list_vehicles) | **GET** /fleet/vehicles | List all vehicles
[**replace_tag**](DefaultApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag
[**update_address**](DefaultApi.md#update_address) | **PATCH** /addresses/{id} | Update an address
[**update_contact**](DefaultApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact
[**update_driver**](DefaultApi.md#update_driver) | **PATCH** /fleet/drivers/{id} | Update a driver
[**update_user**](DefaultApi.md#update_user) | **PATCH** /users/{id} | Update a user
[**update_vehicle**](DefaultApi.md#update_vehicle) | **PATCH** /fleet/vehicles/{id} | Update a vehicle


# **create_address**
> AddressResponse create_address(address)

Create an address

Creates a new address in the organization

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    address = samsara.CreateAddressRequest() # CreateAddressRequest | The address to create.

    try:
        # Create an address
        api_response = api_instance.create_address(address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**CreateAddressRequest**](CreateAddressRequest.md)| The address to create. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ContactResponse create_contact(contact)

Create a contact

Add a contact to the organization

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    contact = samsara.CreateContactRequest() # CreateContactRequest | The contact create parameters.

    try:
        # Create a contact
        api_response = api_instance.create_contact(contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**CreateContactRequest**](CreateContactRequest.md)| The contact create parameters. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact was successfully added. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_driver**
> DriverResponse create_driver(driver)

Create a driver

Add a driver to the organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    driver = samsara.CreateDriverRequest() # CreateDriverRequest | The driver to create.

    try:
        # Create a driver
        api_response = api_instance.create_driver(driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**CreateDriverRequest**](CreateDriverRequest.md)| The driver to create. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created driver object, with Samsara-generated ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> TagResponse create_tag(tag)

Create a tag

Create a new tag for the organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    tag = samsara.CreateTagRequest() # CreateTagRequest | 

    try:
        # Create a tag
        api_response = api_instance.create_tag(tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**CreateTagRequest**](CreateTagRequest.md)|  | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created tag object, including the new tag ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserResponse create_user(user)

Create a user

Add a user to the organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    user = samsara.CreateUserRequest() # CreateUserRequest | The user to create.

    try:
        # Create a user
        api_response = api_instance.create_user(user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**CreateUserRequest**](CreateUserRequest.md)| The user to create. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created user object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address**
> delete_address(id)

Delete an address

Delete a specific address.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

    try:
        # Delete an address
        api_instance.delete_address(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty success body |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a contact

Delete the given contact.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.

    try:
        # Delete a contact
        api_instance.delete_contact(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns an empty success response. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(id)

Delete a tag

Permanently deletes a tag.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Delete a tag
        api_instance.delete_tag(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the tag. No response body is returned. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Delete a user

Delete the given user.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.

    try:
        # Delete a user
        api_instance.delete_user(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns an empty success response. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> AddressResponse get_address(id)

Retrieve an address

Returns a specific address.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

    try:
        # Retrieve an address
        api_response = api_instance.get_address(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Address. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> ContactResponse get_contact(id)

Retrieve a contact

Get a specific contact's information.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.

    try:
        # Retrieve a contact
        api_response = api_instance.get_contact(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified contact. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_driver**
> DriverResponse get_driver(id)

Retrieve a driver

Get information about a driver.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`

    try:
        # Retrieve a driver
        api_response = api_instance.get_driver(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified driver. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagResponse get_tag(id)

Retrieve a tag

Fetch a tag by id.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.

    try:
        # Retrieve a tag
        api_response = api_instance.get_tag(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag corresponding to request id. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(id)

Retrieve a user

Get a specific user's information.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.

    try:
        # Retrieve a user
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified user. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle**
> VehicleResponse get_vehicle(id)

Retrieve a vehicle

Get information about a specific vehicle.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`

    try:
        # Retrieve a vehicle
        api_response = api_instance.get_vehicle(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60; | 

### Return type

[**VehicleResponse**](VehicleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified vehicle object. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations**
> VehicleLocationsResponse get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get most recent vehicle locations

Returns last known location for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get most recent vehicle locations
        api_response = api_instance.get_vehicle_locations(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsResponse**](VehicleLocationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the most recent locations for the specified vehicles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_feed**
> VehicleLocationsListResponse get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a feed of vehicle locations

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Follow a feed of vehicle locations
        api_response = api_instance.get_vehicle_locations_feed(after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_locations_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of locations events for the specified vehicles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_locations_history**
> VehicleLocationsListResponse get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle locations

Returns all known vehicle locations during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get historical vehicle locations
        api_response = api_instance.get_vehicle_locations_history(start_time, end_time, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_locations_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **datetime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all locations for the specified vehicles and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats**
> VehicleStatsResponse get_vehicle_stats(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

List most recent vehicle stats

Returns last known stats for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # List most recent vehicle stats
        api_response = api_instance.get_vehicle_stats(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsResponse**](VehicleStatsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the most recent stats for the specified vehicles and stat types. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_feed**
> VehicleStatsListResponse get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Follow a feed of vehicle stats

Follow a continuous feed of vehicle stats from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent stats for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get vehicle stat updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates. See [this guide](https://developers.samsara.com/docs/vehicle-stats#section-follow-a-real-time-feed-of-vehicle-stats) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Follow a feed of vehicle stats
        api_response = api_instance.get_vehicle_stats_feed(types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stat events for the specified vehicles and stat types. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_stats_history**
> VehicleStatsListResponse get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

Get historical vehicle stats

Returns vehicle stats events during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

    try:
        # Get historical vehicle stats
        api_response = api_instance.get_vehicle_stats_history(start_time, end_time, types, after=after, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_vehicle_stats_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **datetime**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on. Currently only one stat type is accepted per request.  - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**VehicleStatsListResponse**](VehicleStatsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vehicle stats for the specified vehicles, stat type, and time range. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addresses**
> ListAddressesResponse list_addresses(limit=limit, after=after, tag_ids=tag_ids)

List all addresses

Returns a list of all addresses in an organization

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

    try:
        # List all addresses
        api_response = api_instance.list_addresses(limit=limit, after=after, tag_ids=tag_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**ListAddressesResponse**](ListAddressesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all addresses in the organization |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> ListContactsResponse list_contacts(limit=limit, after=after)

List all contacts

Returns a list of all contacts in an organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all contacts
        api_response = api_instance.list_contacts(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListContactsResponse**](ListContactsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all contacts |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drivers**
> ListDriversResponse list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)

List all drivers

Get all drivers in organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    is_deactivated = True # bool | If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
updated_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
created_after_time = '2013-10-20T19:20:30+01:00' # datetime | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

    try:
        # List all drivers
        api_response = api_instance.list_drivers(is_deactivated=is_deactivated, limit=limit, after=after, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deactivated** | **bool**| If value is true, only drivers that are deactivated will appear in the response. This parameter will default to false if not provided (fetching only active drivers). | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **updated_after_time** | **datetime**| A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **created_after_time** | **datetime**| A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

### Return type

[**ListDriversResponse**](ListDriversResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all driver objects. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> ListTagsResponse list_tags(limit=limit, after=after)

List all tags

Return all of the tags for an organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all tags
        api_response = api_instance.list_tags(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tags. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_roles**
> ListUserRolesResponse list_user_roles(limit=limit, after=after)

List all user roles

Returns a list of all user roles in an organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all user roles
        api_response = api_instance.list_user_roles(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListUserRolesResponse**](ListUserRolesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all user roles. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(limit=limit, after=after)

List all users

Returns a list of all users in an organization.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

    try:
        # List all users
        api_response = api_instance.list_users(limit=limit, after=after)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all users. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vehicles**
> ListVehiclesResponse list_vehicles(limit=limit, after=after, tag_ids=tag_ids)

List all vehicles

Returns a list of all vehicles.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

    try:
        # List all vehicles
        api_response = api_instance.list_vehicles(limit=limit, after=after, tag_ids=tag_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_vehicles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

### Return type

[**ListVehiclesResponse**](ListVehiclesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all vehicle objects, and pagination parameters. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tag**
> TagResponse replace_tag(id, tag)

Update a tag

Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the tag.
tag = samsara.ReplaceTagRequest() # ReplaceTagRequest | 

    try:
        # Update a tag
        api_response = api_instance.replace_tag(id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->replace_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the tag. | 
 **tag** | [**ReplaceTagRequest**](ReplaceTagRequest.md)|  | 

### Return type

[**TagResponse**](TagResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated tag data. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> AddressResponse update_address(id, address)

Update an address

Update a specific address.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
address = samsara.UpdateAddressRequest() # UpdateAddressRequest | The address fields to update.

    try:
        # Update an address
        api_response = api_instance.update_address(id, address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 
 **address** | [**UpdateAddressRequest**](UpdateAddressRequest.md)| The address fields to update. | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated address object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ContactResponse update_contact(id, contact)

Update a contact

Update a specific contact's information.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the contact.
contact = samsara.UpdateContactRequest() # UpdateContactRequest | Updates to the contact.

    try:
        # Update a contact
        api_response = api_instance.update_contact(id, contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the contact. | 
 **contact** | [**UpdateContactRequest**](UpdateContactRequest.md)| Updates to the contact. | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated contact object with given ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver**
> DriverResponse update_driver(id, driver)

Update a driver

Update a specific driver's information. This can also be used to activate or de-activate a given driver

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
driver = samsara.UpdateDriverRequest() # UpdateDriverRequest | Updates to the driver properties.

    try:
        # Update a driver
        api_response = api_instance.update_driver(id, driver)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **driver** | [**UpdateDriverRequest**](UpdateDriverRequest.md)| Updates to the driver properties. | 

### Return type

[**DriverResponse**](DriverResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated driver object, with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserResponse update_user(id, user)

Update a user

Update a specific user's information.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | Unique identifier for the user.
user = samsara.UpdateUserRequest() # UpdateUserRequest | Updates to the user.

    try:
        # Update a user
        api_response = api_instance.update_user(id, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the user. | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)| Updates to the user. | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user object with ID. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle**
> VehicleResponse update_vehicle(id, vehicle)

Update a vehicle

Updates the given Vehicle object.  **Note:** Vehicle objects are automatically created when Samsara Vehicle Gateways are installed. You cannot create a Vehicle object via API.  You are able to *update* many of the fields of a Vehicle.  **Note**: There are no required fields in the request body, and you only need to provide the fields you wish to update.

### Example

* Api Key Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
configuration = samsara.Configuration()
# Configure API key authorization: bearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.samsara.com
configuration.host = "https://api.samsara.com"
# Enter a context with an instance of the API client
with samsara.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = samsara.DefaultApi(api_client)
    id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`
vehicle = samsara.UpdateVehicleRequest() # UpdateVehicleRequest | Fields that can be patched on a vehicle.

    try:
        # Update a vehicle
        api_response = api_instance.update_vehicle(id, vehicle)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60; | 
 **vehicle** | [**UpdateVehicleRequest**](UpdateVehicleRequest.md)| Fields that can be patched on a vehicle. | 

### Return type

[**VehicleResponse**](VehicleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the specified vehicle object. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

