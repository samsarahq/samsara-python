# EquipmentStatsListResponseData

A unit of equipment and its time-series of stats events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine_rpm** | [**list[EquipmentEngineRpm]**](EquipmentEngineRpm.md) | A time-series of engine RPM readings for the given unit of equipment. | [optional] 
**engine_seconds** | [**list[EquipmentEngineSeconds]**](EquipmentEngineSeconds.md) | [DEPRECATED] Please use either &#x60;gatewayEngineSeconds&#x60; or &#x60;obdEngineSeconds&#x60;. | [optional] 
**engine_states** | [**list[EquipmentEngineState]**](EquipmentEngineState.md) | [DEPRECATED] Please use either &#x60;gatewayEngineStates&#x60; or &#x60;obdEngineStates&#x60;. | [optional] 
**fuel_percent** | [**list[EquipmentFuelPercent]**](EquipmentFuelPercent.md) | A time-series of fuel percent level changes for the given unit of equipment. | [optional] 
**gateway_engine_seconds** | [**list[EquipmentGatewayEngineSeconds]**](EquipmentGatewayEngineSeconds.md) | A time-series of engine seconds readings for the given unit of equipment. (An approximate based on readings from the AG24&#39;s aux/digio cable.) | [optional] 
**gateway_engine_state** | [**list[EquipmentGatewayEngineState]**](EquipmentGatewayEngineState.md) | A time-series of engine state changes (as read from the AG24&#39;s aux/digio cable) for the given unit of equipment. | [optional] 
**gps_odometer_meters** | [**list[EquipmentGpsOdometerMeters]**](EquipmentGpsOdometerMeters.md) | A time-series of GPS odometer readings for the given unit of equipment. | [optional] 
**id** | **str** | Unique Samsara ID for the equipment. | 
**name** | **str** | Name of the equipment. | 
**obd_engine_seconds** | [**list[EquipmentObdEngineSeconds]**](EquipmentObdEngineSeconds.md) | A time-series of engine state changes for the given unit of equipment. (As directly from on-board diagnostics.) | [optional] 
**obd_engine_state** | [**list[EquipmentObdEngineState]**](EquipmentObdEngineState.md) | A time-series of engine state changes (as read from on-board diagnostics) for the given unit of equipment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


