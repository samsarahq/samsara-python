# Defect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment on the defect. | [optional] 
**created_at_time** | **str** | Time when the defect was created. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**defect_type** | **str** | The type of DVIR defect. | [optional] 
**id** | **str** | ID of the defect. | 
**is_resolved** | **bool** | Signifies if this defect is resolved. | 
**mechanic_notes** | **str** | The mechanics notes on the defect. | [optional] 
**mechanic_notes_updated_at_time** | **str** | Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**resolved_at_time** | **str** | Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**resolved_by** | [**DefectResolvedBy**](DefectResolvedBy.md) |  | [optional] 
**trailer** | **object** |  | [optional] 
**vehicle** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


