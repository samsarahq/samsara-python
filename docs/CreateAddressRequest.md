# CreateAddressRequest

A request body to create an Address.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_types** | **list[str]** | Reporting location type associated with the address (used for ELD reporting purposes). | [optional] 
**contact_ids** | **list[str]** | An array of Contact IDs associated with this Address. | [optional] 
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**formatted_address** | **str** | The full street address for this address/geofence, as it might be recognized by Google Maps. | 
**geofence** | [**AddressGeofence**](AddressGeofence.md) |  | 
**latitude** | **float** | Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**longitude** | **float** | Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided. | [optional] 
**name** | **str** | Name of the address. | 
**notes** | **str** | Notes about the address. | [optional] 
**tag_ids** | **list[str]** | An array of IDs of tags to associate with this address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


