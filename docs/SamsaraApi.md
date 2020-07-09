# samsara.SamsaraApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](SamsaraApi.md#create_address) | **POST** /addresses | Create an address
[**create_carrier_proposed_assignment**](SamsaraApi.md#create_carrier_proposed_assignment) | **POST** /fleet/carrier-proposed-assignments | Create an assignment
[**create_contact**](SamsaraApi.md#create_contact) | **POST** /contacts | Create a contact
[**create_driver**](SamsaraApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**create_dvir**](SamsaraApi.md#create_dvir) | **POST** /fleet/dvirs | Create a mechanic DVIR
[**create_tag**](SamsaraApi.md#create_tag) | **POST** /tags | Create a tag
[**create_user**](SamsaraApi.md#create_user) | **POST** /users | Create a user
[**delete_address**](SamsaraApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
[**delete_carrier_proposed_assignment**](SamsaraApi.md#delete_carrier_proposed_assignment) | **DELETE** /fleet/carrier-proposed-assignments/{id} | Delete an assignment
[**delete_contact**](SamsaraApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete a contact
[**delete_tag**](SamsaraApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**delete_user**](SamsaraApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
[**generate_document_pdf**](SamsaraApi.md#generate_document_pdf) | **POST** /fleet/documents/pdfs | Create a document PDF
[**get_address**](SamsaraApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
[**get_contact**](SamsaraApi.md#get_contact) | **GET** /contacts/{id} | Retrieve a contact
[**get_document_pdf**](SamsaraApi.md#get_document_pdf) | **GET** /fleet/documents/pdfs/{id} | Query a document PDF
[**get_driver**](SamsaraApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_driver_tachograph_activity**](SamsaraApi.md#get_driver_tachograph_activity) | **GET** /fleet/drivers/tachograph-activity/history | Get driver tachograph activity
[**get_driver_tachograph_files**](SamsaraApi.md#get_driver_tachograph_files) | **GET** /fleet/drivers/tachograph-files/history | Get tachograph driver files
[**get_dvir_defects**](SamsaraApi.md#get_dvir_defects) | **GET** /fleet/defects/history | Get all defects
[**get_dvir_history**](SamsaraApi.md#get_dvir_history) | **GET** /fleet/dvirs/history | Get all DVIRs
[**get_equipment**](SamsaraApi.md#get_equipment) | **GET** /fleet/equipment/{id} | Retrieve a unit of equipment
[**get_equipment_locations**](SamsaraApi.md#get_equipment_locations) | **GET** /fleet/equipment/locations | Get most recent locations for all equipment
[**get_equipment_locations_feed**](SamsaraApi.md#get_equipment_locations_feed) | **GET** /fleet/equipment/locations/feed | Follow feed of equipment locations
[**get_equipment_locations_history**](SamsaraApi.md#get_equipment_locations_history) | **GET** /fleet/equipment/locations/history | Get historical equipment locations
[**get_equipment_stats**](SamsaraApi.md#get_equipment_stats) | **GET** /fleet/equipment/stats | Get most recent stats for all equipment
[**get_equipment_stats_feed**](SamsaraApi.md#get_equipment_stats_feed) | **GET** /fleet/equipment/stats/feed | Follow a feed of equipment stats
[**get_equipment_stats_history**](SamsaraApi.md#get_equipment_stats_history) | **GET** /fleet/equipment/stats/history | Get historical equipment stats
[**get_hos_clocks**](SamsaraApi.md#get_hos_clocks) | **GET** /fleet/hos/clocks | Get HOS clocks
[**get_hos_logs**](SamsaraApi.md#get_hos_logs) | **GET** /fleet/hos/logs | Get HOS logs
[**get_safety_events**](SamsaraApi.md#get_safety_events) | **GET** /fleet/safety-events | List all safety events.
[**get_tag**](SamsaraApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
[**get_user**](SamsaraApi.md#get_user) | **GET** /users/{id} | Retrieve a user
[**get_vehicle**](SamsaraApi.md#get_vehicle) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
[**get_vehicle_locations**](SamsaraApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
[**get_vehicle_locations_feed**](SamsaraApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
[**get_vehicle_locations_history**](SamsaraApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations
[**get_vehicle_stats**](SamsaraApi.md#get_vehicle_stats) | **GET** /fleet/vehicles/stats | List most recent vehicle stats
[**get_vehicle_stats_feed**](SamsaraApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Follow a feed of vehicle stats
[**get_vehicle_stats_history**](SamsaraApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Get historical vehicle stats
[**get_vehicle_tachograph_files**](SamsaraApi.md#get_vehicle_tachograph_files) | **GET** /fleet/vehicles/tachograph-files/history | Get tachograph vehicle files
[**list_addresses**](SamsaraApi.md#list_addresses) | **GET** /addresses | List all addresses
[**list_carrier_proposed_assignments**](SamsaraApi.md#list_carrier_proposed_assignments) | **GET** /fleet/carrier-proposed-assignments | Retrieve assignments
[**list_contacts**](SamsaraApi.md#list_contacts) | **GET** /contacts | List all contacts
[**list_drivers**](SamsaraApi.md#list_drivers) | **GET** /fleet/drivers | List all drivers
[**list_equipment**](SamsaraApi.md#list_equipment) | **GET** /fleet/equipment | List all equipment
[**list_tags**](SamsaraApi.md#list_tags) | **GET** /tags | List all tags
[**list_user_roles**](SamsaraApi.md#list_user_roles) | **GET** /user-roles | List all user roles
[**list_users**](SamsaraApi.md#list_users) | **GET** /users | List all users
[**list_vehicles**](SamsaraApi.md#list_vehicles) | **GET** /fleet/vehicles | List all vehicles
[**patch_tag**](SamsaraApi.md#patch_tag) | **PATCH** /tags/{id} | Update a tag
[**replace_tag**](SamsaraApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag
[**update_address**](SamsaraApi.md#update_address) | **PATCH** /addresses/{id} | Update an address
[**update_contact**](SamsaraApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact
[**update_driver**](SamsaraApi.md#update_driver) | **PATCH** /fleet/drivers/{id} | Update a driver
[**update_dvir**](SamsaraApi.md#update_dvir) | **PATCH** /fleet/dvirs/{id} | Resolve a DVIR
[**update_dvir_defect**](SamsaraApi.md#update_dvir_defect) | **PATCH** /fleet/defects/{id} | Update a defect
[**update_user**](SamsaraApi.md#update_user) | **PATCH** /users/{id} | Update a user
[**update_vehicle**](SamsaraApi.md#update_vehicle) | **PATCH** /fleet/vehicles/{id} | Update a vehicle


    # **create_address**
    > AddressResponse create_address(address)

    Create an address

      Creates a new address in the organization

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
address = samsara.CreateAddressRequest() # CreateAddressRequest | The address to create.

try:
    # Create an address
    api_response = api_instance.create_address(address)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_address: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **address** | [**CreateAddressRequest**](CreateAddressRequest.md)| The address to create. | 

    ### Return type

    [**AddressResponse**](AddressResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created address object with ID. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **create_carrier_proposed_assignment**
    > CarrierProposedAssignmentResponse create_carrier_proposed_assignment(carrier_proposed_assignment=carrier_proposed_assignment)

    Create an assignment

      Creates a new assignment that a driver can later use. Each driver can only have one future assignment.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
carrier_proposed_assignment = samsara.CreateCarrierProposedAssignmentRequest() # CreateCarrierProposedAssignmentRequest | The assignment to create. (optional)

try:
    # Create an assignment
    api_response = api_instance.create_carrier_proposed_assignment(carrier_proposed_assignment=carrier_proposed_assignment)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_carrier_proposed_assignment: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **carrier_proposed_assignment** | [**CreateCarrierProposedAssignmentRequest**](CreateCarrierProposedAssignmentRequest.md)| The assignment to create. | [optional] 

    ### Return type

    [**CarrierProposedAssignmentResponse**](CarrierProposedAssignmentResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Return the created assignment |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **create_contact**
    > ContactResponse create_contact(contact)

    Create a contact

      Add a contact to the organization

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
contact = samsara.CreateContactRequest() # CreateContactRequest | The contact create parameters.

try:
    # Create a contact
    api_response = api_instance.create_contact(contact)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_contact: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **contact** | [**CreateContactRequest**](CreateContactRequest.md)| The contact create parameters. | 

    ### Return type

    [**ContactResponse**](ContactResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
driver = samsara.CreateDriverRequest() # CreateDriverRequest | The driver to create.

try:
    # Create a driver
    api_response = api_instance.create_driver(driver)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_driver: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **driver** | [**CreateDriverRequest**](CreateDriverRequest.md)| The driver to create. | 

    ### Return type

    [**DriverResponse**](DriverResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created driver object, with Samsara-generated ID. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **create_dvir**
    > DvirResponse create_dvir(dvir=dvir)

    Create a mechanic DVIR

      Creates a new mechanic DVIR in the organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
dvir = samsara.CreateDvirRequest() # CreateDvirRequest | The DVIR to create. (optional)

try:
    # Create a mechanic DVIR
    api_response = api_instance.create_dvir(dvir=dvir)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_dvir: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **dvir** | [**CreateDvirRequest**](CreateDvirRequest.md)| The DVIR to create. | [optional] 

    ### Return type

    [**DvirResponse**](DvirResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created DVIR. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **create_tag**
    > TagResponse create_tag(tag)

    Create a tag

      Create a new tag for the organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
tag = samsara.CreateTagRequest() # CreateTagRequest | 

try:
    # Create a tag
    api_response = api_instance.create_tag(tag)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **tag** | [**CreateTagRequest**](CreateTagRequest.md)|  | 

    ### Return type

    [**TagResponse**](TagResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
user = samsara.CreateUserRequest() # CreateUserRequest | The user to create.

try:
    # Create a user
    api_response = api_instance.create_user(user)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_user: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **user** | [**CreateUserRequest**](CreateUserRequest.md)| The user to create. | 

    ### Return type

    [**UserResponse**](UserResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

try:
    # Delete an address
    api_instance.delete_address(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_address: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

    ### Return type

    void (empty response body)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **204** | Empty success body |  -  |
        **0** | Unexpected error. |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **delete_carrier_proposed_assignment**
    > delete_carrier_proposed_assignment(id)

    Delete an assignment

      Permanently delete an assignment. You can only delete assignments that are not yet active. To override a currently active assignment, create a new empty one, instead.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the assignment.

try:
    # Delete an assignment
    api_instance.delete_carrier_proposed_assignment(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_carrier_proposed_assignment: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the assignment. | 

    ### Return type

    void (empty response body)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **204** | Empty success body |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **delete_contact**
    > delete_contact(id)

    Delete a contact

      Delete the given contact.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the contact.

try:
    # Delete a contact
    api_instance.delete_contact(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_contact: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the contact. | 

    ### Return type

    void (empty response body)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the tag.

try:
    # Delete a tag
    api_instance.delete_tag(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the tag. | 

    ### Return type

    void (empty response body)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the user.

try:
    # Delete a user
    api_instance.delete_user(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_user: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the user. | 

    ### Return type

    void (empty response body)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **204** | Returns an empty success response. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **generate_document_pdf**
    > DocumentPdfGenerationResponse generate_document_pdf(document=document)

    Create a document PDF

      Request creation of a document PDF.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
document = samsara.DocumentPdfGenerationRequest() # DocumentPdfGenerationRequest | Specifies the document for which to generate a PDF. (optional)

try:
    # Create a document PDF
    api_response = api_instance.generate_document_pdf(document=document)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->generate_document_pdf: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **document** | [**DocumentPdfGenerationRequest**](DocumentPdfGenerationRequest.md)| Specifies the document for which to generate a PDF. | [optional] 

    ### Return type

    [**DocumentPdfGenerationResponse**](DocumentPdfGenerationResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created PDF generation job. |  -  |
        **0** | Error response. |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_address**
    > AddressResponse get_address(id)

    Retrieve an address

      Returns a specific address.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`

try:
    # Retrieve an address
    api_response = api_instance.get_address(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_address: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 

    ### Return type

    [**AddressResponse**](AddressResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the contact.

try:
    # Retrieve a contact
    api_response = api_instance.get_contact(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_contact: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the contact. | 

    ### Return type

    [**ContactResponse**](ContactResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns the specified contact. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_document_pdf**
    > DocumentPdfQueryResponse get_document_pdf(id)

    Query a document PDF

      Returns generation job status and download URL for a PDF.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the pdf.

try:
    # Query a document PDF
    api_response = api_instance.get_document_pdf(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_document_pdf: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the pdf. | 

    ### Return type

    [**DocumentPdfQueryResponse**](DocumentPdfQueryResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Document PDF job status and download URL. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_driver**
    > DriverResponse get_driver(id)

    Retrieve a driver

      Get information about a driver.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`

try:
    # Retrieve a driver
    api_response = api_instance.get_driver(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_driver: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 

    ### Return type

    [**DriverResponse**](DriverResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns the specified driver. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_driver_tachograph_activity**
    > DriverTachographActivityResponse get_driver_tachograph_activity(start_time, end_time, after=after, driver_ids=driver_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    Get driver tachograph activity

      Returns all known tachograph activity for all specified drivers in the time range.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. It can't be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
driver_ids = ['driver_ids_example'] # list[str] | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # Get driver tachograph activity
    api_response = api_instance.get_driver_tachograph_activity(start_time, end_time, after=after, driver_ids=driver_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_driver_tachograph_activity: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. It can&#39;t be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **driver_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of driver IDs. Example: &#x60;driverIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**DriverTachographActivityResponse**](DriverTachographActivityResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all driver tachograph activities in a specified time range. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_driver_tachograph_files**
    > TachographDriverFilesResponse get_driver_tachograph_files(start_time, end_time, after=after, driver_ids=driver_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    Get tachograph driver files

      Returns all known tachograph files for all specified drivers in the time range.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
driver_ids = ['driver_ids_example'] # list[str] | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # Get tachograph driver files
    api_response = api_instance.get_driver_tachograph_files(start_time, end_time, after=after, driver_ids=driver_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_driver_tachograph_files: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **driver_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of driver IDs. Example: &#x60;driverIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**TachographDriverFilesResponse**](TachographDriverFilesResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all driver tachograph files in a specified time range. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_dvir_defects**
    > DefectsResponse get_dvir_defects(start_time, end_time, limit=limit, after=after, is_resolved=is_resolved)

    Get all defects

      Returns a list of DVIR defects in an organization, filtered by creation time. The maximum time period you can query for is 30 days.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
is_resolved = True # bool | A filter on the data based on resolution status. Example: `isResolved=true` (optional)

try:
    # Get all defects
    api_response = api_instance.get_dvir_defects(start_time, end_time, limit=limit, after=after, is_resolved=is_resolved)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_dvir_defects: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.* | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.* | 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **is_resolved** | **bool**| A filter on the data based on resolution status. Example: &#x60;isResolved&#x3D;true&#x60; | [optional] 

    ### Return type

    [**DefectsResponse**](DefectsResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all DVIR defects in the organization |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_dvir_history**
    > DvirsListResponse get_dvir_history(start_time, end_time, limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    Get all DVIRs

      Returns a list of all DVIRs in an organization

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # Get all DVIRs
    api_response = api_instance.get_dvir_history(start_time, end_time, limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_dvir_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**DvirsListResponse**](DvirsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all DVIRs in the organization |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment**
    > EquipmentResponse get_equipment(id)

    Retrieve a unit of equipment

      Retrieves the unit of equipment with the given Samsara ID.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Samsara ID of the Equipment.

try:
    # Retrieve a unit of equipment
    api_response = api_instance.get_equipment(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Samsara ID of the Equipment. | 

    ### Return type

    [**EquipmentResponse**](EquipmentResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The specified equipment object |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_locations**
    > EquipmentLocationsResponse get_equipment_locations(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Get most recent locations for all equipment

      Returns last known locations for all equipment. This can be optionally filtered by tags or specific equipment IDs.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Get most recent locations for all equipment
    api_response = api_instance.get_equipment_locations(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_locations: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentLocationsResponse**](EquipmentLocationsResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The most recent equipment locations and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_locations_feed**
    > EquipmentLocationsListResponse get_equipment_locations_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Follow feed of equipment locations

      Follow a continuous feed of all equipment locations from Samsara AG24s.  Your first call to this endpoint will provide you with the most recent location for each unit of equipment and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment location updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Follow feed of equipment locations
    api_response = api_instance.get_equipment_locations_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_locations_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentLocationsListResponse**](EquipmentLocationsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The feed of equipment locations and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_locations_history**
    > EquipmentLocationsListResponse get_equipment_locations_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Get historical equipment locations

      Returns historical equipment locations during the given time range. This can be optionally filtered by tags or specific equipment IDs.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Get historical equipment locations
    api_response = api_instance.get_equipment_locations_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_locations_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentLocationsListResponse**](EquipmentLocationsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Historical equipment locations and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_stats**
    > EquipmentStatsResponse get_equipment_stats(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Get most recent stats for all equipment

      Returns the last known stats for all equipment. This can be optionally filtered by tags or specific equipment IDs.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Get most recent stats for all equipment
    api_response = api_instance.get_equipment_stats(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_stats: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentStatsResponse**](EquipmentStatsResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The most recent equipment stats and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_stats_feed**
    > EquipmentStatsListResponse get_equipment_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Follow a feed of equipment stats

      Follow a continuous feed of all equipment stats from Samsara AG24s.  Your first call to this endpoint will provide you with the most recent stats for each unit of equipment and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment stats updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Follow a feed of equipment stats
    api_response = api_instance.get_equipment_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_stats_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentStatsListResponse**](EquipmentStatsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The feed of equipment stats and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_equipment_stats_history**
    > EquipmentStatsListResponse get_equipment_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)

    Get historical equipment stats

      Returns historical equipment status during the given time range. This can be optionally filtered by tags or specific equipment IDs.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
equipment_ids = ['equipment_ids_example'] # list[str] | A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678` (optional)

try:
    # Get historical equipment stats
    api_response = api_instance.get_equipment_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, equipment_ids=equipment_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_equipment_stats_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **equipment_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of equipment IDs. Example: &#x60;equipmentIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentStatsListResponse**](EquipmentStatsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Historical equipment stats and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_hos_clocks**
    > HosClocksResponse get_hos_clocks(tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, driver_ids=driver_ids, after=after, limit=limit)

    Get HOS clocks

      Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogsSummary).

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
driver_ids = ['driver_ids_example'] # list[str] | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678` (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)

try:
    # Get HOS clocks
    api_response = api_instance.get_hos_clocks(tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, driver_ids=driver_ids, after=after, limit=limit)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_hos_clocks: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **driver_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of driver IDs. Example: &#x60;driverIds&#x3D;1234,5678&#x60; | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]

    ### Return type

    [**HosClocksResponse**](HosClocksResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of current HOS clock information for the specified drivers. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_hos_logs**
    > HosLogsResponse get_hos_logs(tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, driver_ids=driver_ids, start_time=start_time, end_time=end_time, after=after)

    Get HOS logs

      Returns HOS logs between a given `startTime` and `endTime`. The logs can be further filtered using tags or by providing a list of driver IDs (including external IDs). The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogs).  **Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
driver_ids = ['driver_ids_example'] # list[str] | A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678` (optional)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # Get HOS logs
    api_response = api_instance.get_hos_logs(tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, driver_ids=driver_ids, start_time=start_time, end_time=end_time, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_hos_logs: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **driver_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of driver IDs. Example: &#x60;driverIds&#x3D;1234,5678&#x60; | [optional] 
 **start_time** | **str**| A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **end_time** | **str**| An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**HosLogsResponse**](HosLogsResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of the last known HOS log entries for the specified drivers. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_safety_events**
    > SafetyEventsListResponse get_safety_events(start_time, end_time, after=after, tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, vehicle_ids=vehicle_ids)

    List all safety events.

      Fetch safety events for the organization in a given time period.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # List all safety events.
    api_response = api_instance.get_safety_events(start_time, end_time, after=after, tag_ids=tag_ids, parent_tag_ids=parent_tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_safety_events: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**SafetyEventsListResponse**](SafetyEventsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of safety events from given time period. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_tag**
    > TagResponse get_tag(id)

    Retrieve a tag

      Fetch a tag by id.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the tag.

try:
    # Retrieve a tag
    api_response = api_instance.get_tag(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the tag. | 

    ### Return type

    [**TagResponse**](TagResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the user.

try:
    # Retrieve a user
    api_response = api_instance.get_user(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_user: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the user. | 

    ### Return type

    [**UserResponse**](UserResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.

try:
    # Retrieve a vehicle
    api_response = api_instance.get_vehicle(id)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.vin:1HGBH41JXMN109186&#x60;. | 

    ### Return type

    [**VehicleResponse**](VehicleResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleLocationsResponse get_vehicle_locations(after=after, time=time, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    Get most recent vehicle locations

      Returns last known locations for the given time for all vehicles (connected via Samsara Vehicle Gateways). If no time is specified the current time is used. This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
time = 'time_example' # str | A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`). (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Get most recent vehicle locations
    api_response = api_instance.get_vehicle_locations(after=after, time=time, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_locations: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **time** | **str**| A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: &#x60;2020-01-27T07:06:25Z&#x60;). | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleLocationsResponse**](VehicleLocationsResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleLocationsListResponse get_vehicle_locations_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    Follow a feed of vehicle locations

      Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.  See [this guide](https://developers.samsara.com/docs/vehicle-locations#section-follow-a-real-time-feed-of-vehicle-locations) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Follow a feed of vehicle locations
    api_response = api_instance.get_vehicle_locations_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_locations_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleLocationsListResponse get_vehicle_locations_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    Get historical vehicle locations

      Returns all known vehicle locations during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-locations) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Get historical vehicle locations
    api_response = api_instance.get_vehicle_locations_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_locations_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleLocationsListResponse**](VehicleLocationsListResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleStatsResponse get_vehicle_stats(types, after=after, time=time, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    List most recent vehicle stats

      Returns last known stats for the given time for all vehicles (connected via Samsara Vehicle Gateways). Currently, up to 3 stat types are supported per request. If no time is specified the current time is used. This can be optionally filtered by tags or specific vehicle IDs. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on.   - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `engineRpm`: The revolutions per minute of the engine. - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `batteryMilliVolts`: The vehicle battery voltage reading. - `auxInput1`: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType1` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput2`: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType2` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput3-10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType3-10` fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - `nfcCardScans`: NFC cards scan data.  - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
time = 'time_example' # str | A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`). (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # List most recent vehicle stats
    api_response = api_instance.get_vehicle_stats(types, after=after, time=time, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on.   - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;auxInput1&#x60;: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType1&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput2&#x60;: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType2&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput3-10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType3-10&#x60; fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - &#x60;nfcCardScans&#x60;: NFC cards scan data.  - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **time** | **str**| A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: &#x60;2020-01-27T07:06:25Z&#x60;). | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleStatsResponse**](VehicleStatsResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleStatsListResponse get_vehicle_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    Follow a feed of vehicle stats

      Follow a continuous feed of vehicle stats from Samsara Vehicle Gateways. Currently only one stat type is accepted per request.   Your first call to this endpoint will provide you with the most recent stats for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get vehicle stat updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates. See [this guide](https://developers.samsara.com/docs/vehicle-stats#section-follow-a-real-time-feed-of-vehicle-stats) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on.   - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `engineRpm`: The revolutions per minute of the engine. - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `batteryMilliVolts`: The vehicle battery voltage reading. - `auxInput1`: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType1` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput2`: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType2` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput3-10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType3-10` fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - `nfcCardScans`: NFC cards scan data.  - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Follow a feed of vehicle stats
    api_response = api_instance.get_vehicle_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on.   - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;auxInput1&#x60;: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType1&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput2&#x60;: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType2&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput3-10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType3-10&#x60; fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - &#x60;nfcCardScans&#x60;: NFC cards scan data.  - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleStatsListResponse**](VehicleStatsListResponse.md)

    ### Authorization

    No authorization required

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
    > VehicleStatsListResponse get_vehicle_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)

    Get historical vehicle stats

      Returns vehicle stats events during the given time range for all vehicles (connected via Samsara Vehicle Gateways). This can be optionally filtered by tags or specific vehicle IDs. Currently only one stat type is accepted per request. See [here](https://developers.samsara.com/docs/vehicle-stats) for more details.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
types = ['types_example'] # list[str] | The stat type you want this endpoint to return information on.   - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `engineRpm`: The revolutions per minute of the engine. - `obdOdometerMeters`: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using `gpsOdometerMeters`. - `gpsOdometerMeters`: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara's dashboard UI or through the `odometerMeters` field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. `gpsOdometerMeters` is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to on-board diagnostics. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `batteryMilliVolts`: The vehicle battery voltage reading. - `auxInput1`: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType1` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput2`: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType2` field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - `auxInput3-10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the `data.auxInputType3-10` fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - `nfcCardScans`: NFC cards scan data.  - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Get historical vehicle stats
    api_response = api_instance.get_vehicle_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | [**list[str]**](str.md)| The stat type you want this endpoint to return information on.   - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to on-board diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. In these cases, we recommend using &#x60;gpsOdometerMeters&#x60;. - &#x60;gpsOdometerMeters&#x60;: The odometer reading according to GPS calculations. This calculation is based off GPS distance traveled and a manual odometer offset for a given vehicle, specified by the user in Samsara&#39;s dashboard UI or through the &#x60;odometerMeters&#x60; field in the [PATCH /fleet/vehicles/{id}](#operation/updateVehicleById) endpoint. &#x60;gpsOdometerMeters&#x60; is equal to the manual offset plus the GPS distance traveled since the offset was set. The value for this stat type will be omitted if a manual offset is not provided for a given vehicle. *A manual offset can only be provided when we do not have diagnostic coverage for a particular vehicle.* - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to on-board diagnostics. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;auxInput1&#x60;: Stat events from the [auxiliary input 1](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType1&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput2&#x60;: Stat events from the [auxiliary input 2](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType2&#x60; field in the response body for [Retrieving a Vehicle](#operation/getVehicle). - &#x60;auxInput3-10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. For more details see the &#x60;data.auxInputType3-10&#x60; fields in the response body for [Retrieving a Vehicle](#operation/getVehicle). Note, ports 3-10 are only available on gateways with the aux expander. - &#x60;nfcCardScans&#x60;: NFC cards scan data.  - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**VehicleStatsListResponse**](VehicleStatsListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of vehicle stats for the specified vehicles, stat type, and time range. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_vehicle_tachograph_files**
    > TachographVehicleFilesResponse get_vehicle_tachograph_files(start_time, end_time, after=after, vehicle_ids=vehicle_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    Get tachograph vehicle files

      Returns all known tachograph files for all specified vehicles in the time range.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
start_time = 'start_time_example' # str | A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
end_time = 'end_time_example' # str | An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # Get tachograph vehicle files
    api_response = api_instance.get_vehicle_tachograph_files(start_time, end_time, after=after, vehicle_ids=vehicle_ids, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_tachograph_files: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**TachographVehicleFilesResponse**](TachographVehicleFilesResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all vehicle tachograph files in a specified time range. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **list_addresses**
    > ListAddressesResponse list_addresses(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, created_after_time=created_after_time)

    List all addresses

      Returns a list of all addresses in an organization

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
created_after_time = 'created_after_time_example' # str | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

try:
    # List all addresses
    api_response = api_instance.list_addresses(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, created_after_time=created_after_time)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_addresses: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **created_after_time** | **str**| A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

    ### Return type

    [**ListAddressesResponse**](ListAddressesResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all addresses in the organization |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **list_carrier_proposed_assignments**
    > ListCarrierProposedAssignmentResponse list_carrier_proposed_assignments(limit=limit, after=after, driver_ids=driver_ids, active_time=active_time)

    Retrieve assignments

      Show the assignments that are active for drivers and that would currently be visible to them in the driver app.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
driver_ids = ['driver_ids_example'] # list[str] | If specified, limits the results to those for these drivers. e.g. `driverIds=1,2,3` (optional)
active_time = 'active_time_example' # str | If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

try:
    # Retrieve assignments
    api_response = api_instance.list_carrier_proposed_assignments(limit=limit, after=after, driver_ids=driver_ids, active_time=active_time)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_carrier_proposed_assignments: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **driver_ids** | [**list[str]**](str.md)| If specified, limits the results to those for these drivers. e.g. &#x60;driverIds&#x3D;1,2,3&#x60; | [optional] 
 **active_time** | **str**| If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

    ### Return type

    [**ListCarrierProposedAssignmentResponse**](ListCarrierProposedAssignmentResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns the assignments that drivers would see in the future, if any. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **list_contacts**
    > ListContactsResponse list_contacts(limit=limit, after=after)

    List all contacts

      Returns a list of all contacts in an organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all contacts
    api_response = api_instance.list_contacts(limit=limit, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_contacts: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**ListContactsResponse**](ListContactsResponse.md)

    ### Authorization

    No authorization required

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
    > ListDriversResponse list_drivers(driver_activation_status=driver_activation_status, limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)

    List all drivers

      Get all drivers in organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
driver_activation_status = 'driver_activation_status_example' # str | If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers). (optional)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
updated_after_time = 'updated_after_time_example' # str | A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)
created_after_time = 'created_after_time_example' # str | A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). (optional)

try:
    # List all drivers
    api_response = api_instance.list_drivers(driver_activation_status=driver_activation_status, limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, updated_after_time=updated_after_time, created_after_time=created_after_time)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_drivers: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **driver_activation_status** | **str**| If value is &#x60;deactivated&#x60;, only drivers that are deactivated will appear in the response. This parameter will default to &#x60;active&#x60; if not provided (fetching only active drivers). | [optional] 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **updated_after_time** | **str**| A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
 **created_after_time** | **str**| A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 

    ### Return type

    [**ListDriversResponse**](ListDriversResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all driver objects. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **list_equipment**
    > EquipmentListResponse list_equipment(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    List all equipment

      Returns a list of all equipment in an organization. Equipment objects represent powered assets connected to a [Samsara AG24](https://www.samsara.com/products/models/ag24) via an APWR, CAT, or J1939 cable. They are automatically created with a unique Samsara Equipment ID whenever an AG24 is activated in your organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all equipment
    api_response = api_instance.list_equipment(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_equipment: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**EquipmentListResponse**](EquipmentListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all equipment objects, and pagination information |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **list_tags**
    > ListTagsResponse list_tags(limit=limit, after=after)

    List all tags

      Return all of the tags for an organization.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all tags
    api_response = api_instance.list_tags(limit=limit, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_tags: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**ListTagsResponse**](ListTagsResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all user roles
    api_response = api_instance.list_user_roles(limit=limit, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_user_roles: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**ListUserRolesResponse**](ListUserRolesResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # List all users
    api_response = api_instance.list_users(limit=limit, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_users: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**ListUsersResponse**](ListUsersResponse.md)

    ### Authorization

    No authorization required

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
    > ListVehiclesResponse list_vehicles(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    List all vehicles

      Returns a list of all vehicles.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)

try:
    # List all vehicles
    api_response = api_instance.list_vehicles(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->list_vehicles: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**ListVehiclesResponse**](ListVehiclesResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all vehicle objects, and pagination parameters. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **patch_tag**
    > TagResponse patch_tag(id, tag)

    Update a tag

      Update an existing tag. **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.    This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.    For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the tag.
tag = samsara.PatchTagRequest() # PatchTagRequest | 

try:
    # Update a tag
    api_response = api_instance.patch_tag(id, tag)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->patch_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the tag. | 
 **tag** | [**PatchTagRequest**](PatchTagRequest.md)|  | 

    ### Return type

    [**TagResponse**](TagResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns updated tag object. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **replace_tag**
    > TagResponse replace_tag(id, tag)

    Update a tag

      Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the tag.
tag = samsara.ReplaceTagRequest() # ReplaceTagRequest | 

try:
    # Update a tag
    api_response = api_instance.replace_tag(id, tag)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->replace_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the tag. | 
 **tag** | [**ReplaceTagRequest**](ReplaceTagRequest.md)|  | 

    ### Return type

    [**TagResponse**](TagResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
address = samsara.UpdateAddressRequest() # UpdateAddressRequest | The address fields to update.

try:
    # Update an address
    api_response = api_instance.update_address(id, address)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_address: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60; | 
 **address** | [**UpdateAddressRequest**](UpdateAddressRequest.md)| The address fields to update. | 

    ### Return type

    [**AddressResponse**](AddressResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the contact.
contact = samsara.UpdateContactRequest() # UpdateContactRequest | Updates to the contact.

try:
    # Update a contact
    api_response = api_instance.update_contact(id, contact)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_contact: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the contact. | 
 **contact** | [**UpdateContactRequest**](UpdateContactRequest.md)| Updates to the contact. | 

    ### Return type

    [**ContactResponse**](ContactResponse.md)

    ### Authorization

    No authorization required

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

      Update a specific driver's information. This can also be used to activate or de-activate a given driver by setting the driverActivationStatus field.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
driver = samsara.UpdateDriverRequest() # UpdateDriverRequest | Updates to the driver properties.

try:
    # Update a driver
    api_response = api_instance.update_driver(id, driver)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_driver: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;payrollId:ABFS18600&#x60; | 
 **driver** | [**UpdateDriverRequest**](UpdateDriverRequest.md)| Updates to the driver properties. | 

    ### Return type

    [**DriverResponse**](DriverResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Updated driver object, with ID. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **update_dvir**
    > DvirResponse update_dvir(id, dvir=dvir)

    Resolve a DVIR

      Resolves a given DVIR by marking its `isResolved` field to `true`.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the DVIR.
dvir = samsara.UpdateDvirRequest() # UpdateDvirRequest | The dvir fields to update. (optional)

try:
    # Resolve a DVIR
    api_response = api_instance.update_dvir(id, dvir=dvir)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_dvir: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the DVIR. | 
 **dvir** | [**UpdateDvirRequest**](UpdateDvirRequest.md)| The dvir fields to update. | [optional] 

    ### Return type

    [**DvirResponse**](DvirResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Updated dvir object with ID. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **update_dvir_defect**
    > DefectResponse update_dvir_defect(id, defect=defect)

    Update a defect

      Updates a given defect. Can be used to resolve a defect by marking its `isResolved` field to `true`.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the defect.
defect = samsara.DefectPatch() # DefectPatch | The DVIR defect fields to update. (optional)

try:
    # Update a defect
    api_response = api_instance.update_dvir_defect(id, defect=defect)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_dvir_defect: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the defect. | 
 **defect** | [**DefectPatch**](DefectPatch.md)| The DVIR defect fields to update. | [optional] 

    ### Return type

    [**DefectResponse**](DefectResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Return the modified defect entity |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **update_user**
    > UserResponse update_user(id, user)

    Update a user

      Update a specific user's information.

    ### Example

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | Unique identifier for the user.
user = samsara.UpdateUserRequest() # UpdateUserRequest | Updates to the user.

try:
    # Update a user
    api_response = api_instance.update_user(id, user)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_user: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Unique identifier for the user. | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)| Updates to the user. | 

    ### Return type

    [**UserResponse**](UserResponse.md)

    ### Authorization

    No authorization required

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

      ```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
  with samsara.ApiClient() as api_client:
# Create an instance of the API class
api_instance = samsara.SamsaraApi(api_client)
id = 'id_example' # str | ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.
vehicle = samsara.UpdateVehicleRequest() # UpdateVehicleRequest | Fields that can be patched on a vehicle.

try:
    # Update a vehicle
    api_response = api_instance.update_vehicle(id, vehicle)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_vehicle: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;maintenanceId:250020&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.vin:1HGBH41JXMN109186&#x60;. | 
 **vehicle** | [**UpdateVehicleRequest**](UpdateVehicleRequest.md)| Fields that can be patched on a vehicle. | 

    ### Return type

    [**VehicleResponse**](VehicleResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns the specified vehicle object. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

