# Address

An Address object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**contacts** | [**list[ContactTinyResponse]**](ContactTinyResponse.md) | An array Contact mini-objects that are associated the Address. | [optional] 
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**id** | **str** | ID of the Address. | 
**latitude** | **float** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**longitude** | **float** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**name** | **str** | Name of the address. | 
**notes** | **str** | Notes about the address. | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | An array of all tag mini-objects that are associated with the given address entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


