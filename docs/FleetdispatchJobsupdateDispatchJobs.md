# FleetdispatchJobsupdateDispatchJobs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Samsara dispatch job to be updated. | [optional] 
**external_identifier** | **str** | New&#x3D; string that can be used to map jobs in the Samsara database to jobs in an external database. | [optional] 
**driver_id** | **int** | New ID of the driver assigned to the dispatch job. | [optional] 
**vehicle_id** | **int** | New ID of the vehicle used for the dispatch job. | [optional] 
**job_state** | **str** | The current state of the dispatch job. | [optional] 
**scheduled_arrival_time_ms** | **int** | The time at which the assigned driver is scheduled to arrive at the job destination. | [optional] 
**started_at_ms** | **int** | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). | [optional] 
**completed_at_ms** | **int** | The time at which the job was marked complete. | [optional] 
**cancelled_at_ms** | **int** | The time at which the job was marked cancelled. | [optional] 
**notes** | **str** | Notes regarding the details of this job. | [optional] 
**destination_name** | **str** | The name of the job destination. | [optional] 
**destination_address** | **str** | The address of the job destination, as it would be recognized if provided to maps.google.com | [optional] 
**destination_lat** | **float** | Latitude of the destination in decimal degrees. | [optional] 
**destination_lng** | **float** | Latitude of the destination in decimal degrees. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


