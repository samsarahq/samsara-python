# samsara

  No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2019-12-12
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import samsara
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import samsara
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

  
  # Defining host is optional and default to https://api.samsara.com
  configuration.host = "https://api.samsara.com"
  # Enter a context with an instance of the API client
  with samsara.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *https://api.samsara.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SamsaraApi* | [**create_address**](docs/SamsaraApi.md#create_address) | **POST** /addresses | Create an address
*SamsaraApi* | [**create_carrier_proposed_assignment**](docs/SamsaraApi.md#create_carrier_proposed_assignment) | **POST** /fleet/carrier-proposed-assignments | Create an assignment
*SamsaraApi* | [**create_contact**](docs/SamsaraApi.md#create_contact) | **POST** /contacts | Create a contact
*SamsaraApi* | [**create_driver**](docs/SamsaraApi.md#create_driver) | **POST** /fleet/drivers | Create a driver
*SamsaraApi* | [**create_dvir**](docs/SamsaraApi.md#create_dvir) | **POST** /fleet/dvirs | Create a mechanic DVIR
*SamsaraApi* | [**create_tag**](docs/SamsaraApi.md#create_tag) | **POST** /tags | Create a tag
*SamsaraApi* | [**create_user**](docs/SamsaraApi.md#create_user) | **POST** /users | Create a user
*SamsaraApi* | [**delete_address**](docs/SamsaraApi.md#delete_address) | **DELETE** /addresses/{id} | Delete an address
*SamsaraApi* | [**delete_carrier_proposed_assignment**](docs/SamsaraApi.md#delete_carrier_proposed_assignment) | **DELETE** /fleet/carrier-proposed-assignments/{id} | Delete an assignment
*SamsaraApi* | [**delete_contact**](docs/SamsaraApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete a contact
*SamsaraApi* | [**delete_tag**](docs/SamsaraApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
*SamsaraApi* | [**delete_user**](docs/SamsaraApi.md#delete_user) | **DELETE** /users/{id} | Delete a user
*SamsaraApi* | [**generate_document_pdf**](docs/SamsaraApi.md#generate_document_pdf) | **POST** /fleet/documents/pdfs | Create a document PDF
*SamsaraApi* | [**get_address**](docs/SamsaraApi.md#get_address) | **GET** /addresses/{id} | Retrieve an address
*SamsaraApi* | [**get_contact**](docs/SamsaraApi.md#get_contact) | **GET** /contacts/{id} | Retrieve a contact
*SamsaraApi* | [**get_document_pdf**](docs/SamsaraApi.md#get_document_pdf) | **GET** /fleet/documents/pdfs/{id} | Query a document PDF
*SamsaraApi* | [**get_driver**](docs/SamsaraApi.md#get_driver) | **GET** /fleet/drivers/{id} | Retrieve a driver
*SamsaraApi* | [**get_driver_tachograph_activity**](docs/SamsaraApi.md#get_driver_tachograph_activity) | **GET** /fleet/drivers/tachograph-activity/history | Get driver tachograph activity
*SamsaraApi* | [**get_driver_tachograph_files**](docs/SamsaraApi.md#get_driver_tachograph_files) | **GET** /fleet/drivers/tachograph-files/history | Get tachograph driver files
*SamsaraApi* | [**get_dvir_defects**](docs/SamsaraApi.md#get_dvir_defects) | **GET** /fleet/defects/history | Get all defects
*SamsaraApi* | [**get_dvir_history**](docs/SamsaraApi.md#get_dvir_history) | **GET** /fleet/dvirs/history | Get all DVIRs
*SamsaraApi* | [**get_equipment**](docs/SamsaraApi.md#get_equipment) | **GET** /fleet/equipment/{id} | Retrieve a unit of equipment
*SamsaraApi* | [**get_equipment_locations**](docs/SamsaraApi.md#get_equipment_locations) | **GET** /fleet/equipment/locations | Get most recent locations for all equipment
*SamsaraApi* | [**get_equipment_locations_feed**](docs/SamsaraApi.md#get_equipment_locations_feed) | **GET** /fleet/equipment/locations/feed | Follow feed of equipment locations
*SamsaraApi* | [**get_equipment_locations_history**](docs/SamsaraApi.md#get_equipment_locations_history) | **GET** /fleet/equipment/locations/history | Get historical equipment locations
*SamsaraApi* | [**get_equipment_stats**](docs/SamsaraApi.md#get_equipment_stats) | **GET** /fleet/equipment/stats | Get most recent stats for all equipment
*SamsaraApi* | [**get_equipment_stats_feed**](docs/SamsaraApi.md#get_equipment_stats_feed) | **GET** /fleet/equipment/stats/feed | Follow a feed of equipment stats
*SamsaraApi* | [**get_equipment_stats_history**](docs/SamsaraApi.md#get_equipment_stats_history) | **GET** /fleet/equipment/stats/history | Get historical equipment stats
*SamsaraApi* | [**get_tag**](docs/SamsaraApi.md#get_tag) | **GET** /tags/{id} | Retrieve a tag
*SamsaraApi* | [**get_user**](docs/SamsaraApi.md#get_user) | **GET** /users/{id} | Retrieve a user
*SamsaraApi* | [**get_vehicle**](docs/SamsaraApi.md#get_vehicle) | **GET** /fleet/vehicles/{id} | Retrieve a vehicle
*SamsaraApi* | [**get_vehicle_locations**](docs/SamsaraApi.md#get_vehicle_locations) | **GET** /fleet/vehicles/locations | Get most recent vehicle locations
*SamsaraApi* | [**get_vehicle_locations_feed**](docs/SamsaraApi.md#get_vehicle_locations_feed) | **GET** /fleet/vehicles/locations/feed | Follow a feed of vehicle locations
*SamsaraApi* | [**get_vehicle_locations_history**](docs/SamsaraApi.md#get_vehicle_locations_history) | **GET** /fleet/vehicles/locations/history | Get historical vehicle locations
*SamsaraApi* | [**get_vehicle_stats**](docs/SamsaraApi.md#get_vehicle_stats) | **GET** /fleet/vehicles/stats | List most recent vehicle stats
*SamsaraApi* | [**get_vehicle_stats_feed**](docs/SamsaraApi.md#get_vehicle_stats_feed) | **GET** /fleet/vehicles/stats/feed | Follow a feed of vehicle stats
*SamsaraApi* | [**get_vehicle_stats_history**](docs/SamsaraApi.md#get_vehicle_stats_history) | **GET** /fleet/vehicles/stats/history | Get historical vehicle stats
*SamsaraApi* | [**get_vehicle_tachograph_files**](docs/SamsaraApi.md#get_vehicle_tachograph_files) | **GET** /fleet/vehicles/tachograph-files/history | Get tachograph vehicle files
*SamsaraApi* | [**list_addresses**](docs/SamsaraApi.md#list_addresses) | **GET** /addresses | List all addresses
*SamsaraApi* | [**list_carrier_proposed_assignments**](docs/SamsaraApi.md#list_carrier_proposed_assignments) | **GET** /fleet/carrier-proposed-assignments | Retrieve assignments
*SamsaraApi* | [**list_contacts**](docs/SamsaraApi.md#list_contacts) | **GET** /contacts | List all contacts
*SamsaraApi* | [**list_drivers**](docs/SamsaraApi.md#list_drivers) | **GET** /fleet/drivers | List all drivers
*SamsaraApi* | [**list_equipment**](docs/SamsaraApi.md#list_equipment) | **GET** /fleet/equipment | List all equipment
*SamsaraApi* | [**list_tags**](docs/SamsaraApi.md#list_tags) | **GET** /tags | List all tags
*SamsaraApi* | [**list_user_roles**](docs/SamsaraApi.md#list_user_roles) | **GET** /user-roles | List all user roles
*SamsaraApi* | [**list_users**](docs/SamsaraApi.md#list_users) | **GET** /users | List all users
*SamsaraApi* | [**list_vehicles**](docs/SamsaraApi.md#list_vehicles) | **GET** /fleet/vehicles | List all vehicles
*SamsaraApi* | [**patch_tag**](docs/SamsaraApi.md#patch_tag) | **PATCH** /tags/{id} | Update a tag
*SamsaraApi* | [**replace_tag**](docs/SamsaraApi.md#replace_tag) | **PUT** /tags/{id} | Update a tag
*SamsaraApi* | [**update_address**](docs/SamsaraApi.md#update_address) | **PATCH** /addresses/{id} | Update an address
*SamsaraApi* | [**update_contact**](docs/SamsaraApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact
*SamsaraApi* | [**update_driver**](docs/SamsaraApi.md#update_driver) | **PATCH** /fleet/drivers/{id} | Update a driver
*SamsaraApi* | [**update_dvir**](docs/SamsaraApi.md#update_dvir) | **PATCH** /fleet/dvirs/{id} | Resolve a DVIR
*SamsaraApi* | [**update_dvir_defect**](docs/SamsaraApi.md#update_dvir_defect) | **PATCH** /fleet/defects/{id} | Update a defect
*SamsaraApi* | [**update_user**](docs/SamsaraApi.md#update_user) | **PATCH** /users/{id} | Update a user
*SamsaraApi* | [**update_vehicle**](docs/SamsaraApi.md#update_vehicle) | **PATCH** /fleet/vehicles/{id} | Update a vehicle


## Documentation For Models

 - [Address](docs/Address.md)
 - [AddressExternalIds](docs/AddressExternalIds.md)
 - [AddressGeofence](docs/AddressGeofence.md)
 - [AddressGeofenceCircle](docs/AddressGeofenceCircle.md)
 - [AddressGeofencePolygon](docs/AddressGeofencePolygon.md)
 - [AddressGeofencePolygonVertices](docs/AddressGeofencePolygonVertices.md)
 - [AddressResponse](docs/AddressResponse.md)
 - [CarrierProposedAssignment](docs/CarrierProposedAssignment.md)
 - [CarrierProposedAssignmentDriver](docs/CarrierProposedAssignmentDriver.md)
 - [CarrierProposedAssignmentResponse](docs/CarrierProposedAssignmentResponse.md)
 - [CarrierProposedAssignmentVehicle](docs/CarrierProposedAssignmentVehicle.md)
 - [Contact](docs/Contact.md)
 - [ContactResponse](docs/ContactResponse.md)
 - [ContactTinyResponse](docs/ContactTinyResponse.md)
 - [CreateAddressRequest](docs/CreateAddressRequest.md)
 - [CreateCarrierProposedAssignmentRequest](docs/CreateCarrierProposedAssignmentRequest.md)
 - [CreateContactRequest](docs/CreateContactRequest.md)
 - [CreateDriverRequest](docs/CreateDriverRequest.md)
 - [CreateDvirRequest](docs/CreateDvirRequest.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [Defect](docs/Defect.md)
 - [DefectPatch](docs/DefectPatch.md)
 - [DefectResolvedBy](docs/DefectResolvedBy.md)
 - [DefectResponse](docs/DefectResponse.md)
 - [DefectsResponse](docs/DefectsResponse.md)
 - [DocumentPdfGenerationRequest](docs/DocumentPdfGenerationRequest.md)
 - [DocumentPdfGenerationResponse](docs/DocumentPdfGenerationResponse.md)
 - [DocumentPdfGenerationResponseData](docs/DocumentPdfGenerationResponseData.md)
 - [DocumentPdfQueryResponse](docs/DocumentPdfQueryResponse.md)
 - [DocumentPdfQueryResponseData](docs/DocumentPdfQueryResponseData.md)
 - [Driver](docs/Driver.md)
 - [DriverActivationStatus](docs/DriverActivationStatus.md)
 - [DriverCarrierSettings](docs/DriverCarrierSettings.md)
 - [DriverEldRuleset](docs/DriverEldRuleset.md)
 - [DriverEldRulesetCycle](docs/DriverEldRulesetCycle.md)
 - [DriverEldRulesetDailyOffDuty](docs/DriverEldRulesetDailyOffDuty.md)
 - [DriverEldRulesetRestBreak](docs/DriverEldRulesetRestBreak.md)
 - [DriverEldRulesetRestart](docs/DriverEldRulesetRestart.md)
 - [DriverEldRulesetShift](docs/DriverEldRulesetShift.md)
 - [DriverEldRulesetUsShortHaulType](docs/DriverEldRulesetUsShortHaulType.md)
 - [DriverEldSettings](docs/DriverEldSettings.md)
 - [DriverExternalIds](docs/DriverExternalIds.md)
 - [DriverLocale](docs/DriverLocale.md)
 - [DriverResponse](docs/DriverResponse.md)
 - [DriverStaticAssignedVehicle](docs/DriverStaticAssignedVehicle.md)
 - [DriverTachographActivityResponse](docs/DriverTachographActivityResponse.md)
 - [DriverTinyResponse](docs/DriverTinyResponse.md)
 - [DriverVehicleGroupTag](docs/DriverVehicleGroupTag.md)
 - [Dvir](docs/Dvir.md)
 - [DvirAuthorSignature](docs/DvirAuthorSignature.md)
 - [DvirResponse](docs/DvirResponse.md)
 - [DvirSecondSignature](docs/DvirSecondSignature.md)
 - [DvirSignature](docs/DvirSignature.md)
 - [DvirThirdSignature](docs/DvirThirdSignature.md)
 - [DvirTrailer](docs/DvirTrailer.md)
 - [DvirTrailerDefectsItems](docs/DvirTrailerDefectsItems.md)
 - [DvirVehicle](docs/DvirVehicle.md)
 - [DvirsListResponse](docs/DvirsListResponse.md)
 - [Equipment](docs/Equipment.md)
 - [EquipmentEngineRpm](docs/EquipmentEngineRpm.md)
 - [EquipmentEngineSeconds](docs/EquipmentEngineSeconds.md)
 - [EquipmentEngineState](docs/EquipmentEngineState.md)
 - [EquipmentFuelPercent](docs/EquipmentFuelPercent.md)
 - [EquipmentGatewayEngineSeconds](docs/EquipmentGatewayEngineSeconds.md)
 - [EquipmentGatewayEngineState](docs/EquipmentGatewayEngineState.md)
 - [EquipmentGpsOdometerMeters](docs/EquipmentGpsOdometerMeters.md)
 - [EquipmentListResponse](docs/EquipmentListResponse.md)
 - [EquipmentLocation](docs/EquipmentLocation.md)
 - [EquipmentLocationsListResponse](docs/EquipmentLocationsListResponse.md)
 - [EquipmentLocationsListResponseData](docs/EquipmentLocationsListResponseData.md)
 - [EquipmentLocationsResponse](docs/EquipmentLocationsResponse.md)
 - [EquipmentLocationsResponseData](docs/EquipmentLocationsResponseData.md)
 - [EquipmentObdEngineSeconds](docs/EquipmentObdEngineSeconds.md)
 - [EquipmentObdEngineState](docs/EquipmentObdEngineState.md)
 - [EquipmentResponse](docs/EquipmentResponse.md)
 - [EquipmentStatsListResponse](docs/EquipmentStatsListResponse.md)
 - [EquipmentStatsListResponseData](docs/EquipmentStatsListResponseData.md)
 - [EquipmentStatsResponse](docs/EquipmentStatsResponse.md)
 - [EquipmentStatsResponseData](docs/EquipmentStatsResponseData.md)
 - [ListAddressesResponse](docs/ListAddressesResponse.md)
 - [ListCarrierProposedAssignmentResponse](docs/ListCarrierProposedAssignmentResponse.md)
 - [ListContactsResponse](docs/ListContactsResponse.md)
 - [ListDriversResponse](docs/ListDriversResponse.md)
 - [ListTagsResponse](docs/ListTagsResponse.md)
 - [ListUserRolesResponse](docs/ListUserRolesResponse.md)
 - [ListUsersResponse](docs/ListUsersResponse.md)
 - [ListVehiclesResponse](docs/ListVehiclesResponse.md)
 - [PaginationResponse](docs/PaginationResponse.md)
 - [ParentTag](docs/ParentTag.md)
 - [PatchTagRequest](docs/PatchTagRequest.md)
 - [ReplaceTagRequest](docs/ReplaceTagRequest.md)
 - [ResolvedBy](docs/ResolvedBy.md)
 - [StandardErrorResponse](docs/StandardErrorResponse.md)
 - [TachographActivity](docs/TachographActivity.md)
 - [TachographActivityListWrapper](docs/TachographActivityListWrapper.md)
 - [TachographDriverFile](docs/TachographDriverFile.md)
 - [TachographDriverFileListWrapper](docs/TachographDriverFileListWrapper.md)
 - [TachographDriverFilesResponse](docs/TachographDriverFilesResponse.md)
 - [TachographVehicleFile](docs/TachographVehicleFile.md)
 - [TachographVehicleFileListWrapper](docs/TachographVehicleFileListWrapper.md)
 - [TachographVehicleFilesResponse](docs/TachographVehicleFilesResponse.md)
 - [Tag](docs/Tag.md)
 - [TagAllOf](docs/TagAllOf.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagTinyResponse](docs/TagTinyResponse.md)
 - [TaggedObject](docs/TaggedObject.md)
 - [TinyTag](docs/TinyTag.md)
 - [TrailerNameOnlyResponse](docs/TrailerNameOnlyResponse.md)
 - [TrailerTinyResponse](docs/TrailerTinyResponse.md)
 - [UpdateAddressRequest](docs/UpdateAddressRequest.md)
 - [UpdateContactRequest](docs/UpdateContactRequest.md)
 - [UpdateDriverRequest](docs/UpdateDriverRequest.md)
 - [UpdateDvirRequest](docs/UpdateDvirRequest.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateVehicleRequest](docs/UpdateVehicleRequest.md)
 - [User](docs/User.md)
 - [UserAuthType](docs/UserAuthType.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserRole](docs/UserRole.md)
 - [UserRoleAssignment](docs/UserRoleAssignment.md)
 - [UserRoleAssignmentRequest](docs/UserRoleAssignmentRequest.md)
 - [UserTinyResponse](docs/UserTinyResponse.md)
 - [Vehicle](docs/Vehicle.md)
 - [VehicleAuxInputType](docs/VehicleAuxInputType.md)
 - [VehicleAuxInputType1](docs/VehicleAuxInputType1.md)
 - [VehicleAuxInputType2](docs/VehicleAuxInputType2.md)
 - [VehicleExternalIds](docs/VehicleExternalIds.md)
 - [VehicleHarshAccelerationSettingType](docs/VehicleHarshAccelerationSettingType.md)
 - [VehicleLocation](docs/VehicleLocation.md)
 - [VehicleLocationReverseGeo](docs/VehicleLocationReverseGeo.md)
 - [VehicleLocationTime](docs/VehicleLocationTime.md)
 - [VehicleLocationsListResponse](docs/VehicleLocationsListResponse.md)
 - [VehicleLocationsListResponseData](docs/VehicleLocationsListResponseData.md)
 - [VehicleLocationsResponse](docs/VehicleLocationsResponse.md)
 - [VehicleLocationsResponseData](docs/VehicleLocationsResponseData.md)
 - [VehicleResponse](docs/VehicleResponse.md)
 - [VehicleStaticAssignedDriver](docs/VehicleStaticAssignedDriver.md)
 - [VehicleStatsAuxInput](docs/VehicleStatsAuxInput.md)
 - [VehicleStatsBatteryVoltage](docs/VehicleStatsBatteryVoltage.md)
 - [VehicleStatsEngineState](docs/VehicleStatsEngineState.md)
 - [VehicleStatsFaultCodes](docs/VehicleStatsFaultCodes.md)
 - [VehicleStatsFaultCodesIgnitionType](docs/VehicleStatsFaultCodesIgnitionType.md)
 - [VehicleStatsFaultCodesJ1939](docs/VehicleStatsFaultCodesJ1939.md)
 - [VehicleStatsFaultCodesJ1939Lights](docs/VehicleStatsFaultCodesJ1939Lights.md)
 - [VehicleStatsFaultCodesJ1939TroubleCode](docs/VehicleStatsFaultCodesJ1939TroubleCode.md)
 - [VehicleStatsFaultCodesOBDII](docs/VehicleStatsFaultCodesOBDII.md)
 - [VehicleStatsFaultCodesOBDIITroubleCode](docs/VehicleStatsFaultCodesOBDIITroubleCode.md)
 - [VehicleStatsFaultCodesPassengerDtc](docs/VehicleStatsFaultCodesPassengerDtc.md)
 - [VehicleStatsFaultCodesPassengerMonitorStatus](docs/VehicleStatsFaultCodesPassengerMonitorStatus.md)
 - [VehicleStatsFaultCodesPassengerMonitorStatusValue](docs/VehicleStatsFaultCodesPassengerMonitorStatusValue.md)
 - [VehicleStatsFuelPercent](docs/VehicleStatsFuelPercent.md)
 - [VehicleStatsGpsDistanceMeters](docs/VehicleStatsGpsDistanceMeters.md)
 - [VehicleStatsGpsOdometerMeters](docs/VehicleStatsGpsOdometerMeters.md)
 - [VehicleStatsListResponse](docs/VehicleStatsListResponse.md)
 - [VehicleStatsListResponseData](docs/VehicleStatsListResponseData.md)
 - [VehicleStatsListResponseFaultCodes](docs/VehicleStatsListResponseFaultCodes.md)
 - [VehicleStatsListResponseJ1939](docs/VehicleStatsListResponseJ1939.md)
 - [VehicleStatsListResponseJ1939CheckEngineLights](docs/VehicleStatsListResponseJ1939CheckEngineLights.md)
 - [VehicleStatsListResponseJ1939DiagnosticTroubleCodes](docs/VehicleStatsListResponseJ1939DiagnosticTroubleCodes.md)
 - [VehicleStatsListResponseObdii](docs/VehicleStatsListResponseObdii.md)
 - [VehicleStatsListResponseObdiiConfirmedDtcs](docs/VehicleStatsListResponseObdiiConfirmedDtcs.md)
 - [VehicleStatsListResponseObdiiDiagnosticTroubleCodes](docs/VehicleStatsListResponseObdiiDiagnosticTroubleCodes.md)
 - [VehicleStatsListResponseObdiiMonitorStatus](docs/VehicleStatsListResponseObdiiMonitorStatus.md)
 - [VehicleStatsObdEngineSeconds](docs/VehicleStatsObdEngineSeconds.md)
 - [VehicleStatsObdOdometerMeters](docs/VehicleStatsObdOdometerMeters.md)
 - [VehicleStatsResponse](docs/VehicleStatsResponse.md)
 - [VehicleStatsResponseData](docs/VehicleStatsResponseData.md)
 - [VehicleStatsTime](docs/VehicleStatsTime.md)
 - [VehicleStatsTirePressure](docs/VehicleStatsTirePressure.md)
 - [VehicleStatsTirePressures](docs/VehicleStatsTirePressures.md)
 - [VehicleTinyResponse](docs/VehicleTinyResponse.md)


## Documentation For Authorization

  All endpoints do not require authorization.

## Author




