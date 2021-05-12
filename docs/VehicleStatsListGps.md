# VehicleStatsListGps

GPS location data for the vehicle.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**VehicleLocationAddress**](VehicleLocationAddress.md) |  | [optional] 
**decorations** | [**VehicleStatsDecorations**](VehicleStatsDecorations.md) |  | [optional] 
**heading_degrees** | **float** | Heading of the vehicle in degrees. | [optional] 
**is_ecu_speed** | **bool** | True if the speed value is reported from the ECU. Speed value is reported from GPS otherwise. | [optional] 
**latitude** | **float** | GPS latitude represented in degrees | 
**longitude** | **float** | GPS longitude represented in degrees | 
**reverse_geo** | [**VehicleLocationReverseGeo**](VehicleLocationReverseGeo.md) |  | [optional] 
**speed_miles_per_hour** | **float** | GPS speed of the vehicle in miles per hour. See &#x60;isEcuSpeed&#x60; to determine speed data source. | [optional] 
**time** | **str** | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


