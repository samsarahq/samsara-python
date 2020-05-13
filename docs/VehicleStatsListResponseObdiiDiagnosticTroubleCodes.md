# VehicleStatsListResponseObdiiDiagnosticTroubleCodes

Diagnostic trouble code for passenger vehicles.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_dtcs** | [**list[VehicleStatsListResponseObdiiConfirmedDtcs]**](VehicleStatsListResponseObdiiConfirmedDtcs.md) | Confirmed DTC codes. | [optional] 
**ignition_type** | **str** | The ignition type of this passenger vehicle. Valid values are \&quot;spark\&quot; and \&quot;compression\&quot; | [optional] 
**mil_status** | **bool** | The MIL status, indicating a check engine light. | [optional] 
**monitor_status** | [**VehicleStatsListResponseObdiiMonitorStatus**](VehicleStatsListResponseObdiiMonitorStatus.md) |  | [optional] 
**pending_dtcs** | [**list[VehicleStatsListResponseObdiiConfirmedDtcs]**](VehicleStatsListResponseObdiiConfirmedDtcs.md) | Pending DTC codes. | [optional] 
**permanent_dtcs** | [**list[VehicleStatsListResponseObdiiConfirmedDtcs]**](VehicleStatsListResponseObdiiConfirmedDtcs.md) | Permanent DTC codes. | [optional] 
**tx_id** | **int** | The TX identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


