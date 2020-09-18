# AttributeExpanded

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_type** | **str** | Denotes the data type of the attribute&#39;s values. | [optional] [default to 'string']
**attribute_value_quantity** | **str** | Defines whether or not this attribute can be used on the same entity many times (with different values). | [optional] [default to 'multi']
**entity_type** | **str** | Denotes the type of entity, driver or vehicle. | [optional] 
**id** | **str** | The samsara id of the attribute object. | [optional] 
**name** | **str** | Name of attribute. | [optional] 
**number_values** | **list[float]** | Number values that can be associated with this attribute | [optional] 
**string_values** | **list[str]** | String values that can be associated with this attribute | [optional] 
**entities** | [**list[AttributeEntity]**](AttributeEntity.md) | Entities that this attribute is applied onto | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


