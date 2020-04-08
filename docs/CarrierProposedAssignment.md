# CarrierProposedAssignment

A carrier proposed assignment object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_time** | **str** | Time when the driver accepted this assignment in the mobile app. Will be omitted if the driver hasn&#39;t accepted this assignment. RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
**active_time** | **str** | Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | 
**driver** | [**CarrierProposedAssignmentDriver**](CarrierProposedAssignmentDriver.md) |  | [optional] 
**first_seen_time** | **str** | Time when the driver first saw this assignment in the mobile app. Will be omitted if the driver hasn&#39;t seen this assignment yet. RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
**id** | **str** | Samsara ID for the assignment. | 
**rejected_time** | **str** | Time when the driver rejected this assignment in the mobile app. Will be omitted if the driver hasn&#39;t rejected this assignment. RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). | [optional] 
**shipping_docs** | **str** | Shipping Documents that this assignment will propose to the driver. | [optional] 
**trailers** | [**list[TrailerNameOnlyResponse]**](TrailerNameOnlyResponse.md) | Trailers that this assignment will propose to the driver. | [optional] 
**vehicle** | [**CarrierProposedAssignmentVehicle**](CarrierProposedAssignmentVehicle.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


