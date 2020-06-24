# SafetyEvent

A safety event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior_labels** | [**list[SafetyEventBehaviorLabel]**](SafetyEventBehaviorLabel.md) | The most up-to-date behavior labels associated with the safety event. These labels can be updated by the Safety Report Admin. | [optional] 
**coaching_state** | [**SafetyEventCoachingState**](SafetyEventCoachingState.md) |  | [optional] 
**download_forward_video_url** | **str** | URL to download the forward video. | [optional] 
**download_inward_video_url** | **str** | URL to download the inward video. | [optional] 
**download_tracked_inward_video_url** | **str** | URL to download the tracked inward video. | [optional] 
**driver** | [**DriverTinyResponse**](DriverTinyResponse.md) |  | [optional] 
**id** | **str** | The unique Samsara ID of the safety event. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**max_acceleration_g_force** | **float** | The maximum acceleration value as a multiplier on the force of gravity (g). | [optional] 
**time** | **str** | The time the safety event occurred in RFC 3339 milliseconds format. | [optional] 
**vehicle** | [**VehicleTinyResponse**](VehicleTinyResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


