# HosCycle

Remaining durations and start time for the HOS driving cycle.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_remaining_duration_ms** | **float** | Remaining on duty or driving time the driver has in the current cycle in milliseconds. For property-carrying drivers, this is the amount of time the driver can be on duty or driving before hitting the 60/70-hour limit in 7/8 days. | [optional] 
**cycle_started_at_time** | **str** | UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**cycle_tomorrow_duration_ms** | **float** | Remaining on duty or driving time the driver has available tomorrow in milliseconds. For property-carrying drivers this is calculated based on the 60/70-hour limit in 7/8 days rule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


