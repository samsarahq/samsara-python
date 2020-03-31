# VehicleStatsListResponseData

A vehicle and its list of stat events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aux_input1** | [**list[VehicleStatsAuxInput]**](VehicleStatsAuxInput.md) | A list of auxiliary equipment states. | [optional] 
**aux_input2** | [**list[VehicleStatsAuxInput]**](VehicleStatsAuxInput.md) | A list of auxiliary equipment states. | [optional] 
**engine_states** | [**list[VehicleStatsEngineState]**](VehicleStatsEngineState.md) | A list of engine state events for the given vehicle. | [optional] 
**fuel_percent** | [**list[VehicleStatsFuelPercent]**](VehicleStatsFuelPercent.md) | A list of fuel percentage readings for the given vehicle. | [optional] 
**gps_distance_meters** | [**list[VehicleStatsGpsDistanceMeters]**](VehicleStatsGpsDistanceMeters.md) | A list of GPS distance events for the given vehicle. | [optional] 
**gps_odometer_meters** | [**list[VehicleStatsGpsOdometerMeters]**](VehicleStatsGpsOdometerMeters.md) | A list of GPS odometer events for the given vehicle. | [optional] 
**id** | **str** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 
**obd_engine_seconds** | [**list[VehicleStatsObdEngineSeconds]**](VehicleStatsObdEngineSeconds.md) | A list of OBD engine seconds readings for the given vehicle. | [optional] 
**obd_odometer_meters** | [**list[VehicleStatsObdOdometerMeters]**](VehicleStatsObdOdometerMeters.md) | A list of OBD odometer readings for the given vehicle. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


