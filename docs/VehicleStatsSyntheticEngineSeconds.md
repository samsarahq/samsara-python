# VehicleStatsSyntheticEngineSeconds

Data for the synthetic engine seconds for the vehicle
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decorations** | [**VehicleStatsDecorations**](VehicleStatsDecorations.md) |  | [optional] 
**time** | **str** | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 
**value** | **int** | Stats for the number of seconds the vehicle&#39;s engine has been on, calculated based on a manually-specified engine seconds reading and the number of seconds the vehicle has been on according to the engine state changes reported to the vehicle gateway since that reading was set. This stat will not be present for any vehicle that does not have the engine seconds reading set. The engine seconds reading can be set from the UI on the vehicle details page. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


