# TachographVehicleFile

Tachograph vehicle file
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_time** | **str** | Creation time of files in RFC 3339 format. This is either the download time from the tachograph itself (for files downloaded via Samsara VG) or upload time (for files manually uploaded via Samsara UI). | [optional] 
**id** | **str** | ID of the file. | [optional] 
**url** | **str** | A temporary URL which can be used to download the file. The link can be used multiple times and expires after an hour. | [optional] 
**vehicle_identification_number** | **str** | VIN associated with the vehicle file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


