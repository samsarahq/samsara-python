# AssetResponse

Asset
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_metadata** | **dict(str, str)** | The custom fields of an asset. | [optional] 
**data_outputs** | [**list[AssetDataOutput]**](AssetDataOutput.md) | The list of data outputs configured on the asset. | [optional] 
**id** | **str** | The id of the asset | 
**is_running** | **bool** | The running status of the asset. Returns True for On, and False for Off. | 
**location** | [**AssetLocation**](AssetLocation.md) |  | [optional] 
**location_data_input** | [**AssetResponseLocationDataInput**](AssetResponseLocationDataInput.md) |  | [optional] 
**location_type** | [**LocationType**](LocationType.md) |  | [optional] 
**name** | **str** | The name of the asset. | 
**parent_asset** | [**AssetResponseParentAsset**](AssetResponseParentAsset.md) |  | [optional] 
**running_status_data_input** | [**AssetResponseRunningStatusDataInput**](AssetResponseRunningStatusDataInput.md) |  | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Industrial Asset. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


