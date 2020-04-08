# CreateCarrierProposedAssignmentRequest

New assignment for a driver.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_time** | **str** | Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**driver_id** | **str** | Samsara ID for the driver that this assignment is for. | 
**shipping_docs** | **str** | Shipping Documents that this assignment will propose to the driver. | [optional] 
**trailer_names** | **list[str]** | Names of trailers to propose. | [optional] 
**vehicle_id** | **str** | Samsara ID for the vehicle to propose. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


