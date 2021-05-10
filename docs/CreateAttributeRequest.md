# CreateAttributeRequest

A request body to create an Attribute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_type** | **str** | Denotes the data type of the attribute&#39;s values. | [default to 'string']
**attribute_value_quantity** | **str** | Defines whether or not this attribute can be used on the same entity many times (with different values). | [default to 'multi']
**entities** | [**list[CreateAttributeRequestEntities]**](CreateAttributeRequestEntities.md) | Entities that will be applied to this attribute | [optional] 
**entity_type** | **str** | Denotes the type of entity, driver or asset. | 
**name** | **str** | Name | 
**number_values** | **list[float]** | Number values that can be associated with this attribute | [optional] 
**string_values** | **list[str]** | String values that can be associated with this attribute | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


