# CreateDvirRequest

DVIR creation body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | Samsara user ID of the mechanic creating the DVIR. | 
**license_plate** | **str** | The license plate of this vehicle. | [optional] 
**location** | **str** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**mechanic_notes** | **str** | The mechanics notes on the DVIR. | [optional] 
**odometer_meters** | **int** | The odometer reading in meters. | [optional] 
**resolved_defect_ids** | **list[str]** | Array of ids for defects being resolved with this DVIR. | [optional] 
**safety_status** | **str** | Whether or not this vehicle or trailer is safe to drive. | 
**trailer_id** | **str** | Id of trailer being inspected. Either vehicleId or trailerId must be provided. | [optional] 
**type** | **str** | Only type &#39;mechanic&#39; is currently accepted. | 
**vehicle_id** | **str** | Id of vehicle being inspected. Either vehicleId or trailerId must be provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


