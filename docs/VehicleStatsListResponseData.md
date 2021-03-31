# VehicleStatsListResponseData

A vehicle and its list of stat events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ambient_air_temperature_milli_c** | [**list[VehicleStatsAmbientAirTempMilliCWithDecoration]**](VehicleStatsAmbientAirTempMilliCWithDecoration.md) | A list of ambient air temperature readings in millidegree Celsius for the given vehicle. | [optional] 
**aux_input1** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input10** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input2** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input3** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input4** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input5** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input6** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input7** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input8** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**aux_input9** | [**list[VehicleStatsAuxInputWithDecoration]**](VehicleStatsAuxInputWithDecoration.md) | A list of auxiliary equipment states. | [optional] 
**barometric_pressure_pa** | [**list[VehicleStatsBarometricPressurePaWithDecoration]**](VehicleStatsBarometricPressurePaWithDecoration.md) | A list of barometric pressure readings in pascals for the given vehicle. | [optional] 
**battery_milli_volts** | [**list[VehicleStatsBatteryVoltageWithDecoration]**](VehicleStatsBatteryVoltageWithDecoration.md) | A list of battery levels in milliVolts for the given vehicle. | [optional] 
**def_level_milli_percent** | [**list[VehicleStatsDefLevelMilliPercentWithDecoration]**](VehicleStatsDefLevelMilliPercentWithDecoration.md) | A list of DEF level milli percentage readings for the given vehicle. | [optional] 
**ecu_speed_mph** | [**list[VehicleStatsEcuSpeedMphWithDecoration]**](VehicleStatsEcuSpeedMphWithDecoration.md) | A list of the speeds of the vehicle in miles per hour, as reported by the ECU. | [optional] 
**engine_coolant_temperature_milli_c** | [**list[VehicleStatsEngineCoolantTempMilliCWithDecoration]**](VehicleStatsEngineCoolantTempMilliCWithDecoration.md) | A list of engine coolant temperature readings in millidegree Celsius for the given vehicle. | [optional] 
**engine_immobilizer** | [**list[VehicleStatsEngineImmobilizerWithDecoration]**](VehicleStatsEngineImmobilizerWithDecoration.md) | A list of engine immobilizer data for the given vehicle. | [optional] 
**engine_load_percent** | [**list[VehicleStatsEngineLoadPercentWithDecoration]**](VehicleStatsEngineLoadPercentWithDecoration.md) | A list of engine load percentage readings for the given vehicle. | [optional] 
**engine_oil_pressure_k_pa** | [**list[VehicleStatsEngineOilPressureKPaWithDecoration]**](VehicleStatsEngineOilPressureKPaWithDecoration.md) | A list of engine oil pressure readings in kilopascals for the given vehicle. | [optional] 
**engine_rpm** | [**list[VehicleStatsEngineRpmWithDecoration]**](VehicleStatsEngineRpmWithDecoration.md) | A list engine RPM values for the given vehicle. | [optional] 
**engine_states** | [**list[VehicleStatsEngineStateWithDecoration]**](VehicleStatsEngineStateWithDecoration.md) | A list of engine state events for the given vehicle. | [optional] 
**fault_codes** | [**list[VehicleStatsFaultCodesWithDecoration]**](VehicleStatsFaultCodesWithDecoration.md) | A list of engine fault codes. | [optional] 
**fuel_percents** | [**list[VehicleStatsFuelPercentWithDecoration]**](VehicleStatsFuelPercentWithDecoration.md) | A list of fuel percentage readings for the given vehicle. | [optional] 
**gps** | [**list[VehicleStatsListGps]**](VehicleStatsListGps.md) | A list of GPS location events for the given vehicles. | [optional] 
**gps_distance_meters** | [**list[VehicleStatsGpsDistanceMetersWithDecoration]**](VehicleStatsGpsDistanceMetersWithDecoration.md) | A list of GPS distance events for the given vehicle. | [optional] 
**gps_odometer_meters** | [**list[VehicleStatsGpsOdometerMetersWithDecoration]**](VehicleStatsGpsOdometerMetersWithDecoration.md) | A list of GPS odometer events for the given vehicle. | [optional] 
**id** | **str** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | [optional] 
**intake_manifold_temperature_milli_c** | [**list[VehicleStatsIntakeManifoldTempMilliCWithDecoration]**](VehicleStatsIntakeManifoldTempMilliCWithDecoration.md) | A list of intake manifold temperature readings in millidegree Celsius for the given vehicle. | [optional] 
**name** | **str** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | [optional] 
**nfc_card_scans** | [**list[VehicleStatsNfcCardScanWithDecoration]**](VehicleStatsNfcCardScanWithDecoration.md) | A list of NFC cards that were scanned for the given vehicles. | [optional] 
**obd_engine_seconds** | [**list[VehicleStatsObdEngineSecondsWithDecoration]**](VehicleStatsObdEngineSecondsWithDecoration.md) | A list of OBD engine seconds readings for the given vehicle. | [optional] 
**obd_odometer_meters** | [**list[VehicleStatsObdOdometerMetersWithDecoration]**](VehicleStatsObdOdometerMetersWithDecoration.md) | A list of OBD odometer readings for the given vehicle. | [optional] 
**synthetic_engine_seconds** | [**list[VehicleStatsListSyntheticEngineSeconds]**](VehicleStatsListSyntheticEngineSeconds.md) | A list of synthetic engine seconds values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


