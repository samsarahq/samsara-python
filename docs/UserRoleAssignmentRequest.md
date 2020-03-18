# UserRoleAssignmentRequest

A role that applies to a user. If the role has a `tagId`, then the role applies for that tag. If there is no `tagId`, then the role applies at the organizational level. A user may have many tag-specific roles, but may only have one organizational role. If the organizational level role has higher privileges than a tag-specific role, then the organizational role privileges will take precedence.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The unique ID for the role. | [optional] 
**tag_id** | **str** | ID of the tag this role applies to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


