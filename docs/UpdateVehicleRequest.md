# UpdateVehicleRequest

All the editable portions of the vehicle object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input_type1** | [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**aux_input_type2** | [**VehicleAuxInputType**](VehicleAuxInputType.md) |  | [optional] 
**engine_hours** | **int** | A manual override for the vehicle&#39;s engine hours. You may only override a vehicle&#39;s engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle&#39;s engine hours based on when the Samsara Vehicle Gateway is recieving power or not. | [optional] 
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**harsh_acceleration_setting_type** | [**VehicleHarshAccelerationSettingType**](VehicleHarshAccelerationSettingType.md) |  | [optional] 
**license_plate** | **str** | The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | [optional] 
**notes** | **str** | These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] [default to '']
**odometer_meters** | **int** | A manual override for the vehicle&#39;s odometer. You may only override a vehicle&#39;s odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle&#39;s odometer using GPS distance traveled since this override was set. See [here](https://kb.samsara.com/hc/en-us/articles/115005273667) for more details. | [optional] 
**static_assigned_driver_id** | **str** | ID for the static assigned driver of the vehicle. | [optional] 
**tag_ids** | **list[str]** | An array of IDs of tags to associate with this vehicle. | [optional] 
**vin** | **str** | The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


