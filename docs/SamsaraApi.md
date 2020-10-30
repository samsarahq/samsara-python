# samsara.SamsaraApi

All URIs are relative to *https://api.samsara.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](SamsaraApi.md#create_address) | **POST** /addresses | Create an address
[**create_attribute**](SamsaraApi.md#create_attribute) | **POST** /attributes | [beta] Create an attribute
[**create_carrier_proposed_assignment**](SamsaraApi.md#create_carrier_proposed_assignment) | **POST** /fleet/carrier-proposed-assignments | Create an assignment
[**create_contact**](SamsaraApi.md#create_contact) | **POST** /contacts | Create a contact
[**create_driver**](SamsaraApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
[**create_dvir**](SamsaraApi.md#create_dvir) | **POST** /fleet/dvirs | Create a mechanic DVIR
[**create_industrial_asset**](SamsaraApi.md#create_industrial_asset) | **POST** /industrial/assets | Create an asset
[**create_tag**](SamsaraApi.md#create_tag) | **POST** /tags | Create a tag
[**create_user**](SamsaraApi.md#create_user) | **POST** /users | Create a user
[**delete_address**](SamsaraApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
[**delete_attribute**](SamsaraApi.md#delete_attribute) | **DELETE** /attributes/{id} | [beta] Deleting an attribute
[**delete_carrier_proposed_assignment**](SamsaraApi.md#delete_carrier_proposed_assignment) | **DELETE** /fleet/carrier-proposed-assignments/{id} | Delete an assignment
[**delete_contact**](SamsaraApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete a contact
[**delete_industrial_asset**](SamsaraApi.md#delete_industrial_asset) | **DELETE** /industrial/assets/{id} | Delete an existing asset
[**delete_tag**](SamsaraApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**delete_user**](SamsaraApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
[**generate_document_pdf**](SamsaraApi.md#generate_document_pdf) | **POST** /fleet/documents/pdfs | Create a document PDF
[**get_address**](SamsaraApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
[**get_attribute**](SamsaraApi.md#get_attribute) | **GET** /attributes/{id} | [beta] Retrieve an attribute
[**get_attributes_by_entity_type**](SamsaraApi.md#get_attributes_by_entity_type) | **GET** /attributes | [beta] List all attributes by entity type
[**get_contact**](SamsaraApi.md#get_contact) | **GET** /contacts/{id} | Retrieve a contact
[**get_data_input_data_feed**](SamsaraApi.md#get_data_input_data_feed) | **GET** /industrial/data-inputs/data-points/feed | Follow a real-time feed of data points for data inputs
[**get_data_input_data_history**](SamsaraApi.md#get_data_input_data_history) | **GET** /industrial/data-inputs/data-points/history | List historical data points for data inputs
[**get_data_input_data_snapshot**](SamsaraApi.md#get_data_input_data_snapshot) | **GET** /industrial/data-inputs/data-points | List most recent data points for data inputs
[**get_data_inputs**](SamsaraApi.md#get_data_inputs) | **GET** /industrial/data-inputs | List all data inputs
[**get_document_pdf**](SamsaraApi.md#get_document_pdf) | **GET** /fleet/documents/pdfs/{id} | Query a document PDF
[**get_driver**](SamsaraApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
[**get_driver_efficiency**](SamsaraApi.md#get_driver_efficiency) | **GET** /fleet/drivers/efficiency | [beta] List driver efficiency
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
[**get_industrial_assets**](SamsaraApi.md#get_industrial_assets) | **GET** /industrial/assets | List all assets
[**get_organization_info**](SamsaraApi.md#get_organization_info) | **GET** /me | Get information about your organization
[**get_route_feed**](SamsaraApi.md#get_route_feed) | **GET** /fleet/routes/audit-logs/feed | [beta] Get route updates
[**get_safety_events**](SamsaraApi.md#get_safety_events) | **GET** /fleet/safety-events | List all safety events.
[**get_tag**](SamsaraApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
[**get_user**](SamsaraApi.md#get_user) | **GET** /users/{id} | Retrieve a user
[**get_vehicle**](SamsaraApi.md#get_vehicle) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
[**get_vehicle_locations**](SamsaraApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Locations snapshot
[**get_vehicle_locations_feed**](SamsaraApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Locations feed
[**get_vehicle_locations_history**](SamsaraApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Historical locations
[**get_vehicle_stats**](SamsaraApi.md#get_vehicle_stats) | **GET** /fleet/vehicles/stats | Stats snapshot
[**get_vehicle_stats_feed**](SamsaraApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Stats feed
[**get_vehicle_stats_history**](SamsaraApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Historical stats
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
[**patch_industrial_asset**](SamsaraApi.md#patch_industrial_asset) | **PATCH** /industrial/assets/{id} | Update an asset
[**patch_tag**](SamsaraApi.md#patch_tag) | **PATCH** /tags/{id} | Update a tag
[**replace_tag**](SamsaraApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag
[**update_address**](SamsaraApi.md#update_address) | **PATCH** /addresses/{id} | Update an address
[**update_attribute**](SamsaraApi.md#update_attribute) | **PATCH** /attributes/{id} | [beta] Update an attribute
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

    # **create_attribute**
    > AttributeExpandedResponse create_attribute(attribute)

    [beta] Create an attribute

      Creates a new attribute in the organization.

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
attribute = samsara.CreateAttributeRequest() # CreateAttributeRequest | The attribute to create.

try:
    # [beta] Create an attribute
    api_response = api_instance.create_attribute(attribute)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_attribute: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **attribute** | [**CreateAttributeRequest**](CreateAttributeRequest.md)| The attribute to create. | 

    ### Return type

    [**AttributeExpandedResponse**](AttributeExpandedResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created attribute object with ID. |  -  |
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

    # **create_industrial_asset**
    > InlineResponse200 create_industrial_asset(asset=asset)

    Create an asset

      Create an asset with optional configuration parameters

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
asset = samsara.AssetCreate() # AssetCreate | The asset to create (optional)

try:
    # Create an asset
    api_response = api_instance.create_industrial_asset(asset=asset)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->create_industrial_asset: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **asset** | [**AssetCreate**](AssetCreate.md)| The asset to create | [optional] 

    ### Return type

    [**InlineResponse200**](InlineResponse200.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created asset object |  -  |
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

    # **delete_attribute**
    > delete_attribute(id, entity_type)

    [beta] Deleting an attribute

      Delete an attribute by id, including all of its applications

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
id = 'id_example' # str | Samsara-provided UUID of the attribute.
entity_type = 'entity_type_example' # str | Denotes the type of entity, driver or vehicle.

try:
    # [beta] Deleting an attribute
    api_instance.delete_attribute(id, entity_type)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_attribute: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Samsara-provided UUID of the attribute. | 
 **entity_type** | **str**| Denotes the type of entity, driver or vehicle. | 

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

    # **delete_industrial_asset**
    > delete_industrial_asset(id)

    Delete an existing asset

      Delete asset

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
id = 'id_example' # str | Id of the asset to be deleted.

try:
    # Delete an existing asset
    api_instance.delete_industrial_asset(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_industrial_asset: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Id of the asset to be deleted. | 

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
        **204** | Successfully deleted the asset. No response body. |  -  |
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
id = 'id_example' # str | ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.

try:
    # Delete a tag
    api_instance.delete_tag(id)
except ApiException as e:
print("Exception when calling SamsaraApi->delete_tag: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.name:ELD-exempt&#x60;. | 

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

    # **get_attribute**
    > AttributeExpandedResponse get_attribute(id, entity_type)

    [beta] Retrieve an attribute

      Fetch an attribute by id, including all of its applications

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
id = 'id_example' # str | Samsara-provided UUID of the attribute.
entity_type = 'entity_type_example' # str | Denotes the type of entity, driver or vehicle.

try:
    # [beta] Retrieve an attribute
    api_response = api_instance.get_attribute(id, entity_type)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_attribute: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Samsara-provided UUID of the attribute. | 
 **entity_type** | **str**| Denotes the type of entity, driver or vehicle. | 

    ### Return type

    [**AttributeExpandedResponse**](AttributeExpandedResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The attribute corresponding to request id. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_attributes_by_entity_type**
    > GetAttributesByEntityTypeResponse get_attributes_by_entity_type(entity_type, limit=limit, after=after)

    [beta] List all attributes by entity type

      Fetch all attributes in an organization associated with either drivers or vehicles.

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
entity_type = 'entity_type_example' # str | Denotes the type of entity, driver or vehicle.
limit = 512 # int | The limit for how many objects will be in the response. Default and max for this value is 512 objects. (optional) (default to 512)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)

try:
    # [beta] List all attributes by entity type
    api_response = api_instance.get_attributes_by_entity_type(entity_type, limit=limit, after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_attributes_by_entity_type: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **entity_type** | **str**| Denotes the type of entity, driver or vehicle. | 
 **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    [**GetAttributesByEntityTypeResponse**](GetAttributesByEntityTypeResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | All attributes in an organization for an entity type |  -  |
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

    # **get_data_input_data_feed**
    > DataInputListResponse get_data_input_data_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)

    Follow a real-time feed of data points for data inputs

      Follow a continuous feed of all data input data points.  Your first call to this endpoint will provide you with the most recent data points for each data input and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get data point updates since that `endCursor`.  If `hasNextPage` is `false`, no updates are readily available yet. We suggest waiting a minimum of 5 seconds before requesting updates.

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
data_input_ids = ['data_input_ids_example'] # list[str] | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678` (optional)
asset_ids = ['asset_ids_example'] # list[str] | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544` (optional)

try:
    # Follow a real-time feed of data points for data inputs
    api_response = api_instance.get_data_input_data_feed(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_data_input_data_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **data_input_ids** | [**list[str]**](str.md)| A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | [optional] 
 **asset_ids** | [**list[str]**](str.md)| A comma-separated list of industrial asset UUIDs. Example: &#x60;assetIds&#x3D;076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544&#x60; | [optional] 

    ### Return type

    [**DataInputListResponse**](DataInputListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all data points for specified data inputs |  -  |
        **0** | Unexpected error. |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_data_input_data_history**
    > DataInputListResponse get_data_input_data_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)

    List historical data points for data inputs

      Returns all known data points during the given time range for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs.

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
data_input_ids = ['data_input_ids_example'] # list[str] | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678` (optional)
asset_ids = ['asset_ids_example'] # list[str] | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544` (optional)

try:
    # List historical data points for data inputs
    api_response = api_instance.get_data_input_data_history(start_time, end_time, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_data_input_data_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **data_input_ids** | [**list[str]**](str.md)| A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | [optional] 
 **asset_ids** | [**list[str]**](str.md)| A comma-separated list of industrial asset UUIDs. Example: &#x60;assetIds&#x3D;076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544&#x60; | [optional] 

    ### Return type

    [**DataInputListResponse**](DataInputListResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all data points for the specified data inputs and time range. |  -  |
        **0** | Unexpected error. |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_data_input_data_snapshot**
    > DataInputSnapshotResponse get_data_input_data_snapshot(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)

    List most recent data points for data inputs

      Returns last known data points for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs.

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
data_input_ids = ['data_input_ids_example'] # list[str] | A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678` (optional)
asset_ids = ['asset_ids_example'] # list[str] | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544` (optional)

try:
    # List most recent data points for data inputs
    api_response = api_instance.get_data_input_data_snapshot(after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, data_input_ids=data_input_ids, asset_ids=asset_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_data_input_data_snapshot: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **data_input_ids** | [**list[str]**](str.md)| A comma-separated list of data input IDs. Example: &#x60;dataInputIds&#x3D;1234,5678&#x60; | [optional] 
 **asset_ids** | [**list[str]**](str.md)| A comma-separated list of industrial asset UUIDs. Example: &#x60;assetIds&#x3D;076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544&#x60; | [optional] 

    ### Return type

    [**DataInputSnapshotResponse**](DataInputSnapshotResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of last known data input data points and pagination parameters |  -  |
        **0** | Unexpected error. |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_data_inputs**
    > DataInputsTinyResponse get_data_inputs(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, asset_ids=asset_ids)

    List all data inputs

      Returns all data inputs, optionally filtered by tags or asset ids.

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
asset_ids = ['asset_ids_example'] # list[str] | A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544` (optional)

try:
    # List all data inputs
    api_response = api_instance.get_data_inputs(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, asset_ids=asset_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_data_inputs: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **asset_ids** | [**list[str]**](str.md)| A comma-separated list of industrial asset UUIDs. Example: &#x60;assetIds&#x3D;076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544&#x60; | [optional] 

    ### Return type

    [**DataInputsTinyResponse**](DataInputsTinyResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of data inputs with names, ids, and other metadata. |  -  |
        **0** | Unexpected error. |  -  |

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

    # **get_driver_efficiency**
    > DriverEfficienciesResponse get_driver_efficiency(driver_activation_status=driver_activation_status, driver_ids=driver_ids, after=after, driver_tag_ids=driver_tag_ids, driver_parent_tag_ids=driver_parent_tag_ids, start_time=start_time, end_time=end_time)

    [beta] List driver efficiency

      Get all drivers' efficiencies.

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
driver_ids = ['driver_ids_example'] # list[str] | A filter on the data based on this comma-separated list of driver IDs. Cannot be used with tag filtering or driver status. Example: `driverIds=1234,5678` (optional)
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
driver_tag_ids = ['driver_tag_ids_example'] # list[str] | Filters summary to drivers based on this comma-separated list of tag IDs. Data from all the drivers' respective vehicles will be included in the summary, regardless of which tag the vehicle is associated with. Should not be provided in addition to `driverIds`. Example: driverTagIds=1234,5678 (optional)
driver_parent_tag_ids = ['driver_parent_tag_ids_example'] # list[str] | Filters like `driverTagIds` but includes descendants of all the given parent tags. Should not be provided in addition to `driverIds`. Example: `driverParentTagIds=1234,5678` (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | A start time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `startTime` is 2020-03-17T12:06:19Z then the results will include data starting from 2020-03-17T12:00:00Z. The provided start time cannot be in the future. Start time can be at most 31 days before the end time. If the start time is within the last hour, the results will be empty. Default: 24 hours prior to endTime. (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | An end time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `endTime` is 2020-03-17T12:06:19Z then the results will include data up until 2020-03-17T12:00:00Z. The provided end time cannot be in the future. End time can be at most 31 days after the start time.   Default: The current time truncated to the hour mark. (optional)

try:
    # [beta] List driver efficiency
    api_response = api_instance.get_driver_efficiency(driver_activation_status=driver_activation_status, driver_ids=driver_ids, after=after, driver_tag_ids=driver_tag_ids, driver_parent_tag_ids=driver_parent_tag_ids, start_time=start_time, end_time=end_time)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_driver_efficiency: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **driver_activation_status** | **str**| If value is &#x60;deactivated&#x60;, only drivers that are deactivated will appear in the response. This parameter will default to &#x60;active&#x60; if not provided (fetching only active drivers). | [optional] 
 **driver_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of driver IDs. Cannot be used with tag filtering or driver status. Example: &#x60;driverIds&#x3D;1234,5678&#x60; | [optional] 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **driver_tag_ids** | [**list[str]**](str.md)| Filters summary to drivers based on this comma-separated list of tag IDs. Data from all the drivers&#39; respective vehicles will be included in the summary, regardless of which tag the vehicle is associated with. Should not be provided in addition to &#x60;driverIds&#x60;. Example: driverTagIds&#x3D;1234,5678 | [optional] 
 **driver_parent_tag_ids** | [**list[str]**](str.md)| Filters like &#x60;driverTagIds&#x60; but includes descendants of all the given parent tags. Should not be provided in addition to &#x60;driverIds&#x60;. Example: &#x60;driverParentTagIds&#x3D;1234,5678&#x60; | [optional] 
 **start_time** | **datetime**| A start time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if &#x60;startTime&#x60; is 2020-03-17T12:06:19Z then the results will include data starting from 2020-03-17T12:00:00Z. The provided start time cannot be in the future. Start time can be at most 31 days before the end time. If the start time is within the last hour, the results will be empty. Default: 24 hours prior to endTime. | [optional] 
 **end_time** | **datetime**| An end time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if &#x60;endTime&#x60; is 2020-03-17T12:06:19Z then the results will include data up until 2020-03-17T12:00:00Z. The provided end time cannot be in the future. End time can be at most 31 days after the start time.   Default: The current time truncated to the hour mark. | [optional] 

    ### Return type

    [**DriverEfficienciesResponse**](DriverEfficienciesResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | List of all drivers&#39; efficiencies |  -  |
        **0** | Unexpected error. |  -  |

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
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
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
     **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;gatewayJ1939EngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
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
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
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
     **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;gatewayJ1939EngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
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
types = ['types_example'] # list[str] | The type of equipment stat you want to query. Currently, you may only submit one type.  - `engineRpm`: The revolutions per minute of the engine. - `fuelPercents`: The percent of fuel in the unit of equipment. - `obdEngineSeconds`: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`. - `gatewayEngineStates`: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be `Off` or `On`. - `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard.
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
 **types** | [**list[str]**](str.md)| The type of equipment stat you want to query. Currently, you may only submit one type.  - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;fuelPercents&#x60;: The percent of fuel in the unit of equipment. - &#x60;obdEngineSeconds&#x60;: The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics. - &#x60;gatewayEngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via APWR/AOPEN cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;gatewayJ1939EngineSeconds&#x60;: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG24 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard. - &#x60;obdEngineStates&#x60;: The state of the engine read from on-board diagnostics. Can be &#x60;Off&#x60;, &#x60;On&#x60;, or &#x60;Idle&#x60;. - &#x60;gatewayEngineStates&#x60;: An approximation of engine state based on readings the AG24 receives from the aux/digio cable. Can be &#x60;Off&#x60; or &#x60;On&#x60;. - &#x60;gpsOdometerMeters&#x60;: An approximation of odometer reading based on GPS calculations since the AG24 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. | 
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

    # **get_industrial_assets**
    > ListIndustrialAssetsResponse get_industrial_assets(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)

    List all assets

      List all assets in the organization

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
    # List all assets
    api_response = api_instance.get_industrial_assets(limit=limit, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_industrial_assets: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **limit** | **int**| The limit for how many objects will be in the response. Default and max for this value is 512 objects. | [optional] [default to 512]
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 

    ### Return type

    [**ListIndustrialAssetsResponse**](ListIndustrialAssetsResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Assets in the organization. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_organization_info**
    > OrganizationInfoResponse get_organization_info()

    Get information about your organization

      Get information about your organization

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

try:
    # Get information about your organization
    api_response = api_instance.get_organization_info()
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_organization_info: %s\n" % e)
```

    ### Parameters
    This endpoint does not need any parameter.
    
    ### Return type

    [**OrganizationInfoResponse**](OrganizationInfoResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns information about your organization. |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_route_feed**
    > object get_route_feed(after=after)

    [beta] Get route updates

      Subscribes to a feed of immutable, append-only updates for routes. The initial request to this feed endpoint returns a cursor, which can be used on the next request to fetch updated routes that have had state changes since that request.

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

try:
    # [beta] Get route updates
    api_response = api_instance.get_route_feed(after=after)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_route_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 

    ### Return type

    **object**

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: Not defined
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Returns the route updates that have occurred since the previous cursor. |  -  |
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
id = 'id_example' # str | ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.

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
     **id** | **str**| ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.name:ELD-exempt&#x60;. | 

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

    Locations snapshot

      ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](#operation/getVehicleStats) instead.***  Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.  Related guide: [Vehicle Locations](https://developers.samsara.com/docs/vehicle-locations)

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
    # Locations snapshot
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

    Locations feed

      ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](#operation/getVehicleStatsFeed) instead.***  Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.  Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.  You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.   If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.  Related guide: [Vehicle Locations](https://developers.samsara.com/docs/vehicle-locations)

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
    # Locations feed
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

    Historical locations

      ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](#operation/getVehicleStatsHistory) instead.***  Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.  Related guide: [Vehicle Locations](https://developers.samsara.com/docs/vehicle-locations)

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
    # Historical locations
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

    Stats snapshot

      Returns the last known stats of all vehicles at the given `time`. If no `time` is specified, the current time is used.  Related guide: [Telematics](https://developers.samsara.com/docs/vehicle-stats)

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
types = ['types_example'] # list[str] | The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.  *Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.  - `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius. - `auxInput1`-`auxInput10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - `barometricPressurePa`: The barometric pressure reading in pascals. - `batteryMilliVolts`: The vehicle battery voltage reading. - `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc). - `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU. - `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius. - `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc). - `engineOilPressureKPa`: The engine oil pressure reading in kilopascals. - `engineRpm`: The revolutions per minute of the engine. - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`. - `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius. - `nfcCardScans`: ID card scans. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. - `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`.  - `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
time = 'time_example' # str | A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`). (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)

try:
    # Stats snapshot
    api_response = api_instance.get_vehicle_stats(types, after=after, time=time, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: &#x60;types&#x3D;gps,engineStates,obdOdometerMeters&#x60;.  *Note:* &#x60;auxInput3&#x60;-&#x60;auxInput10&#x60; count as a single type against the limit of 3. For example, you could list &#x60;types&#x3D;engineStates,obdOdometerMeters,auxInput3,auxInput4&#x60; because &#x60;auxInput3&#x60; and &#x60;auxInput4&#x60; count as a single stat type. &#x60;auxInput1&#x60; and &#x60;auxInput2&#x60; still count as their own individual types.  - &#x60;ambientAirTemperatureMilliC&#x60;: The ambient air temperature reading in millidegree Celsius. - &#x60;auxInput1&#x60;-&#x60;auxInput10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - &#x60;barometricPressurePa&#x60;: The barometric pressure reading in pascals. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;defLevelMilliPercent&#x60;: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. &#x60;99001&#x60;, &#x60;49999&#x60;, etc). - &#x60;ecuSpeedMph&#x60;: The speed of the engine in miles per hour according to the ECU. - &#x60;engineCoolantTemperatureMilliC&#x60;: The engine coolant temperature reading in millidegree Celsius. - &#x60;engineLoadPercent&#x60;: The engine load in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineOilPressureKPa&#x60;: The engine oil pressure reading in kilopascals. - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;gpsOdometerMeters&#x60;: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with &#x60;obdOdometerMeters&#x60;. - &#x60;intakeManifoldTemperatureMilliC&#x60;: The intake manifold temperature reading in millidegree Celsius. - &#x60;nfcCardScans&#x60;: ID card scans. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to onboard diagnostics. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with &#x60;gpsOdometerMeters&#x60;.  - &#x60;syntheticEngineSeconds&#x60;: Data for the synthetic engine seconds for the vehicle. | 
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
        **200** | Vehicle stats snapshot |  -  |
        **0** | Error response |  -  |

    [[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

    # **get_vehicle_stats_feed**
    > VehicleStatsListResponse get_vehicle_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids, decorations=decorations)

    Stats feed

      Follow a feed of vehicle stats.   Your first call to this endpoint will provide you with the most recent stats for each vehicle and an `endCursor`.  You can the provide the `endCursor` value to the `after` query parameter to get all updates since the last call you made.  If `hasNextPage` is `false`, no new data is immediately available. You should wait a minimum of 5 seconds making a subsequent request.  Related guide: [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats)

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
types = ['types_example'] # list[str] | The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.  *Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.  - `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius. - `auxInput1`-`auxInput10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - `barometricPressurePa`: The barometric pressure reading in pascals. - `batteryMilliVolts`: The vehicle battery voltage reading. - `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc). - `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU. - `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius. - `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc). - `engineOilPressureKPa`: The engine oil pressure reading in kilopascals. - `engineRpm`: The revolutions per minute of the engine. - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`. - `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius. - `nfcCardScans`: ID card scans. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. - `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`.  - `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)
decorations = ['decorations_example'] # list[str] | Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.  You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  Note that decorations may significantly increase the response payload size.  - `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius. - `auxInput1`-`auxInput10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - `batteryMilliVolts`: The vehicle battery voltage reading. - `barometricPressurePa`: The barometric pressure reading in pascals. - `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU. - `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius. - `engineOilPressureKPa`: The engine oil pressure reading in kilopascals. - `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc). - `engineRpm`: The revolutions per minute of the engine. - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius. - `nfcCardScans`: ID card scans. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. - `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. - `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.   (optional)

try:
    # Stats feed
    api_response = api_instance.get_vehicle_stats_feed(types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids, decorations=decorations)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats_feed: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **types** | [**list[str]**](str.md)| The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: &#x60;types&#x3D;gps,engineStates,obdOdometerMeters&#x60;.  *Note:* &#x60;auxInput3&#x60;-&#x60;auxInput10&#x60; count as a single type against the limit of 3. For example, you could list &#x60;types&#x3D;engineStates,obdOdometerMeters,auxInput3,auxInput4&#x60; because &#x60;auxInput3&#x60; and &#x60;auxInput4&#x60; count as a single stat type. &#x60;auxInput1&#x60; and &#x60;auxInput2&#x60; still count as their own individual types.  - &#x60;ambientAirTemperatureMilliC&#x60;: The ambient air temperature reading in millidegree Celsius. - &#x60;auxInput1&#x60;-&#x60;auxInput10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - &#x60;barometricPressurePa&#x60;: The barometric pressure reading in pascals. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;defLevelMilliPercent&#x60;: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. &#x60;99001&#x60;, &#x60;49999&#x60;, etc). - &#x60;ecuSpeedMph&#x60;: The speed of the engine in miles per hour according to the ECU. - &#x60;engineCoolantTemperatureMilliC&#x60;: The engine coolant temperature reading in millidegree Celsius. - &#x60;engineLoadPercent&#x60;: The engine load in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineOilPressureKPa&#x60;: The engine oil pressure reading in kilopascals. - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;gpsOdometerMeters&#x60;: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with &#x60;obdOdometerMeters&#x60;. - &#x60;intakeManifoldTemperatureMilliC&#x60;: The intake manifold temperature reading in millidegree Celsius. - &#x60;nfcCardScans&#x60;: ID card scans. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to onboard diagnostics. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with &#x60;gpsOdometerMeters&#x60;.  - &#x60;syntheticEngineSeconds&#x60;: Data for the synthetic engine seconds for the vehicle. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 
 **decorations** | [**list[str]**](str.md)| Decorations to add to the primary stats listed in the &#x60;types&#x60; parameter. For example, if you wish to know the vehicle&#39;s location whenever the engine changes state, you may set &#x60;types&#x3D;engineStates&amp;decorations&#x3D;gps&#x60;.  You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the &#x60;types&#x60; parameter, the decorations will be added to each one. For example: &#x60;types&#x3D;engineStates,obdOdometerMeters,faultCodes&amp;decorations&#x3D;gps,fuelPercents&#x60; will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  Note that decorations may significantly increase the response payload size.  - &#x60;ambientAirTemperatureMilliC&#x60;: The ambient air temperature reading in millidegree Celsius. - &#x60;auxInput1&#x60;-&#x60;auxInput10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;barometricPressurePa&#x60;: The barometric pressure reading in pascals. - &#x60;ecuSpeedMph&#x60;: The speed of the engine in miles per hour according to the ECU. - &#x60;engineCoolantTemperatureMilliC&#x60;: The engine coolant temperature reading in millidegree Celsius. - &#x60;engineOilPressureKPa&#x60;: The engine oil pressure reading in kilopascals. - &#x60;engineLoadPercent&#x60;: The engine load in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;intakeManifoldTemperatureMilliC&#x60;: The intake manifold temperature reading in millidegree Celsius. - &#x60;nfcCardScans&#x60;: ID card scans. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to onboard diagnostics. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. - &#x60;syntheticEngineSeconds&#x60;: Data for the synthetic engine seconds for the vehicle.   | [optional] 

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
    > VehicleStatsListResponse get_vehicle_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids, decorations=decorations)

    Historical stats

      Returns vehicle stats during the given time range for all vehicles. This can be optionally filtered by tags or specific vehicle IDs.  Related guide: [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats)

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
types = ['types_example'] # list[str] | The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.  *Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.  - `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius. - `auxInput1`-`auxInput10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - `barometricPressurePa`: The barometric pressure reading in pascals. - `batteryMilliVolts`: The vehicle battery voltage reading. - `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc). - `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU. - `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius. - `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc). - `engineOilPressureKPa`: The engine oil pressure reading in kilopascals. - `engineRpm`: The revolutions per minute of the engine. - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`. - `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius. - `nfcCardScans`: ID card scans. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. - `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with `gpsOdometerMeters`.  - `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.
after = 'after_example' # str | If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. (optional)
parent_tag_ids = ['parent_tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678` (optional)
tag_ids = ['tag_ids_example'] # list[str] | A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678` (optional)
vehicle_ids = ['vehicle_ids_example'] # list[str] | A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678` (optional)
decorations = ['decorations_example'] # list[str] | Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.  You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  Note that decorations may significantly increase the response payload size.  - `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius. - `auxInput1`-`auxInput10`: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - `batteryMilliVolts`: The vehicle battery voltage reading. - `barometricPressurePa`: The barometric pressure reading in pascals. - `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU. - `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius. - `engineOilPressureKPa`: The engine oil pressure reading in kilopascals. - `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc). - `engineRpm`: The revolutions per minute of the engine. - `engineStates`: The state of the engine (`Off`, `On`, `Idle`). - `faultCodes`: The diagnostic fault codes for the vehicle. - `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc). - `gps`: GPS data including lat/long, heading, speed, and a reverse geocoded address. - `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius. - `nfcCardScans`: ID card scans. - `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. - `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. - `syntheticEngineSeconds`: Data for the synthetic engine seconds for the vehicle.   (optional)

try:
    # Historical stats
    api_response = api_instance.get_vehicle_stats_history(start_time, end_time, types, after=after, parent_tag_ids=parent_tag_ids, tag_ids=tag_ids, vehicle_ids=vehicle_ids, decorations=decorations)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->get_vehicle_stats_history: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **start_time** | **str**| A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **end_time** | **str**| An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | 
 **types** | [**list[str]**](str.md)| The stat types you want this endpoint to return information on. See also the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  You may list ***up to 3*** types using comma-separated format. For example: &#x60;types&#x3D;gps,engineStates,obdOdometerMeters&#x60;.  *Note:* &#x60;auxInput3&#x60;-&#x60;auxInput10&#x60; count as a single type against the limit of 3. For example, you could list &#x60;types&#x3D;engineStates,obdOdometerMeters,auxInput3,auxInput4&#x60; because &#x60;auxInput3&#x60; and &#x60;auxInput4&#x60; count as a single stat type. &#x60;auxInput1&#x60; and &#x60;auxInput2&#x60; still count as their own individual types.  - &#x60;ambientAirTemperatureMilliC&#x60;: The ambient air temperature reading in millidegree Celsius. - &#x60;auxInput1&#x60;-&#x60;auxInput10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - &#x60;barometricPressurePa&#x60;: The barometric pressure reading in pascals. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;defLevelMilliPercent&#x60;: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. &#x60;99001&#x60;, &#x60;49999&#x60;, etc). - &#x60;ecuSpeedMph&#x60;: The speed of the engine in miles per hour according to the ECU. - &#x60;engineCoolantTemperatureMilliC&#x60;: The engine coolant temperature reading in millidegree Celsius. - &#x60;engineLoadPercent&#x60;: The engine load in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineOilPressureKPa&#x60;: The engine oil pressure reading in kilopascals. - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;gpsOdometerMeters&#x60;: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](#operation/updateVehicle) endpoint or through the [cloud dasbhoard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with &#x60;obdOdometerMeters&#x60;. - &#x60;intakeManifoldTemperatureMilliC&#x60;: The intake manifold temperature reading in millidegree Celsius. - &#x60;nfcCardScans&#x60;: ID card scans. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to onboard diagnostics. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. Try combining with &#x60;gpsOdometerMeters&#x60;.  - &#x60;syntheticEngineSeconds&#x60;: Data for the synthetic engine seconds for the vehicle. | 
 **after** | **str**| If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results. | [optional] 
 **parent_tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: &#x60;parentTagIds&#x3D;345,678&#x60; | [optional] 
 **tag_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of tag IDs. Example: &#x60;tagIds&#x3D;1234,5678&#x60; | [optional] 
 **vehicle_ids** | [**list[str]**](str.md)| A filter on the data based on this comma-separated list of vehicle IDs. Example: &#x60;vehicleIds&#x3D;1234,5678&#x60; | [optional] 
 **decorations** | [**list[str]**](str.md)| Decorations to add to the primary stats listed in the &#x60;types&#x60; parameter. For example, if you wish to know the vehicle&#39;s location whenever the engine changes state, you may set &#x60;types&#x3D;engineStates&amp;decorations&#x3D;gps&#x60;.  You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the &#x60;types&#x60; parameter, the decorations will be added to each one. For example: &#x60;types&#x3D;engineStates,obdOdometerMeters,faultCodes&amp;decorations&#x3D;gps,fuelPercents&#x60; will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the [Vehicle Stats](https://developers.samsara.com/docs/vehicle-stats#query-parameters) guide for more details.  Note that decorations may significantly increase the response payload size.  - &#x60;ambientAirTemperatureMilliC&#x60;: The ambient air temperature reading in millidegree Celsius. - &#x60;auxInput1&#x60;-&#x60;auxInput10&#x60;: Stat events from the [auxiliary inputs](https://kb.samsara.com/hc/en-us/articles/232232368-Auxiliary-Inputs) for the vehicle. - &#x60;batteryMilliVolts&#x60;: The vehicle battery voltage reading. - &#x60;barometricPressurePa&#x60;: The barometric pressure reading in pascals. - &#x60;ecuSpeedMph&#x60;: The speed of the engine in miles per hour according to the ECU. - &#x60;engineCoolantTemperatureMilliC&#x60;: The engine coolant temperature reading in millidegree Celsius. - &#x60;engineOilPressureKPa&#x60;: The engine oil pressure reading in kilopascals. - &#x60;engineLoadPercent&#x60;: The engine load in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;engineRpm&#x60;: The revolutions per minute of the engine. - &#x60;engineStates&#x60;: The state of the engine (&#x60;Off&#x60;, &#x60;On&#x60;, &#x60;Idle&#x60;). - &#x60;faultCodes&#x60;: The diagnostic fault codes for the vehicle. - &#x60;fuelPercents&#x60;: The engine fuel level in percentage points (e.g. &#x60;99&#x60;, &#x60;50&#x60;, etc). - &#x60;gps&#x60;: GPS data including lat/long, heading, speed, and a reverse geocoded address. - &#x60;gpsDistanceMeters&#x60;: The distance the vehicle has traveled since the gateway was installed based on GPS calculations. - &#x60;intakeManifoldTemperatureMilliC&#x60;: The intake manifold temperature reading in millidegree Celsius. - &#x60;nfcCardScans&#x60;: ID card scans. - &#x60;obdEngineSeconds&#x60;: The cumulative number of seconds the engine has run according to onboard diagnostics. - &#x60;obdOdometerMeters&#x60;: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted. - &#x60;syntheticEngineSeconds&#x60;: Data for the synthetic engine seconds for the vehicle.   | [optional] 

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

    # **patch_industrial_asset**
    > InlineResponse200 patch_industrial_asset(id, asset=asset)

    Update an asset

      Update an existing asset. Only the provided fields will be updated.

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
id = 'id_example' # str | Id of the asset to be updated
asset = samsara.AssetPatch() # AssetPatch | The updated asset fields (optional)

try:
    # Update an asset
    api_response = api_instance.patch_industrial_asset(id, asset=asset)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->patch_industrial_asset: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Id of the asset to be updated | 
 **asset** | [**AssetPatch**](AssetPatch.md)| The updated asset fields | [optional] 

    ### Return type

    [**InlineResponse200**](InlineResponse200.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | The updated asset |  -  |
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
id = 'id_example' # str | ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
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
     **id** | **str**| ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.name:ELD-exempt&#x60;. | 
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
id = 'id_example' # str | ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
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
     **id** | **str**| ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: &#x60;key:value&#x60;. For example, &#x60;crmId:abc123&#x60;. Automatically populated external IDs are prefixed with &#x60;samsara.&#x60;. For example, &#x60;samsara.name:ELD-exempt&#x60;. | 
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

    # **update_attribute**
    > AttributeExpandedResponse update_attribute(id, attribute)

    [beta] Update an attribute

      Updates an attribute in the organization.

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
id = 'id_example' # str | Samsara-provided UUID of the attribute.
attribute = samsara.UpdateAttributeRequest() # UpdateAttributeRequest | The attribute to update.

try:
    # [beta] Update an attribute
    api_response = api_instance.update_attribute(id, attribute)
  pprint(api_response)
except ApiException as e:
print("Exception when calling SamsaraApi->update_attribute: %s\n" % e)
```

    ### Parameters
    
      Name | Type | Description  | Notes
      ------------- | ------------- | ------------- | -------------
     **id** | **str**| Samsara-provided UUID of the attribute. | 
 **attribute** | [**UpdateAttributeRequest**](UpdateAttributeRequest.md)| The attribute to update. | 

    ### Return type

    [**AttributeExpandedResponse**](AttributeExpandedResponse.md)

    ### Authorization

    No authorization required

    ### HTTP request headers

    - **Content-Type**: application/json
    - **Accept**: application/json

      ### HTTP response details
      | Status code | Description | Response headers |
      |-------------|-------------|------------------|
        **200** | Newly created attribute object with ID. |  -  |
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

