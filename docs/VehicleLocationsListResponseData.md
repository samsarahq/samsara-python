# VehicleLocationsListResponseData

A vehicle and its list of location events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**locations** | [**list[VehicleLocation]**](VehicleLocation.md) | A list of location events for the given vehicle. | 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


