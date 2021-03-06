# DefectPatch

Information about resolving a defect. If resolving a defect, must specify `isResolved` as `true` and `resolvedBy`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_resolved** | **bool** | Resolves the defect. Must be &#x60;true&#x60;. | [optional] 
**mechanic_notes** | **str** | The mechanics notes on the defect. | [optional] 
**resolved_at_time** | **str** | Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**resolved_by** | [**ResolvedBy**](ResolvedBy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


