# HistoryParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Group ID to query. | 
**start_ms** | **int** | Beginning of the time range, specified in milliseconds UNIX time. | 
**end_ms** | **int** | End of the time range, specified in milliseconds UNIX time. | 
**step_ms** | **int** | Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals. | 
**series** | [**list[SensorshistorySeries]**](SensorshistorySeries.md) |  | 
**fill_missing** | **str** |  | [optional] [default to 'withNull']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


