# Vehicle

The vehicle object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input_type1** | [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**aux_input_type2** | [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**harsh_acceleration_setting_type** | [**VehicleHarshAccelerationSettingType**](VehicleHarshAccelerationSettingType.md) |  | [optional] 
**id** | **str** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**license_plate** | **str** | The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**make** | **str** | The Vehicle’s manufacturing make. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 
**model** | **str** | The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | [optional] 
**notes** | **str** | These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] [default to '']
**static_assigned_driver** | [**DriverTinyResponse**](DriverTinyResponse.md) |  | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**vin** | **str** | The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**year** | **str** | The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


