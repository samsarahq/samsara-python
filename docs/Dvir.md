# Dvir

Information about a DVIR.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_signature** | [**DvirAuthorSignature**](DvirAuthorSignature.md) |  | [optional] 
**end_time** | **str** | Time when driver signed and completed this DVIR. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**id** | **str** | Unique Samsara ID for the DVIR. | 
**license_plate** | **str** | The license plate of this vehicle. | [optional] 
**location** | **str** | Optional string if your jurisdiction requires a location of the DVIR. | [optional] 
**mechanic_notes** | **str** | The mechanics notes on the DVIR. | [optional] 
**odometer_meters** | **int** | The odometer reading in meters. | [optional] 
**safety_status** | **str** | The condition of vehicle on which DVIR was done. | [optional] [default to 'unsafe']
**second_signature** | [**DvirSecondSignature**](DvirSecondSignature.md) |  | [optional] 
**start_time** | **str** | Time when driver began filling out this DVIR. UTC timestamp in RFC 3339 format. Example: &#x60;2020-01-27T07:06:25Z&#x60;. | [optional] 
**third_signature** | [**DvirThirdSignature**](DvirThirdSignature.md) |  | [optional] 
**trailer** | [**DvirTrailer**](DvirTrailer.md) |  | [optional] 
**trailer_defects** | [**list[DvirTrailerDefectsItems]**](DvirTrailerDefectsItems.md) | Defects registered for the trailer which was part of the DVIR. | [optional] 
**trailer_name** | **str** | The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs. | [optional] 
**type** | **str** | Inspection type of the DVIR. | [optional] [default to 'unspecified']
**vehicle** | [**DvirVehicle**](DvirVehicle.md) |  | [optional] 
**vehicle_defects** | [**list[DvirTrailerDefectsItems]**](DvirTrailerDefectsItems.md) | Defects registered for the vehicle which was part of the DVIR. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


