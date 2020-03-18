# UserRoleAssignment

A role that applies to a user. If the role has a `tag`, then the role applies for that tag. If there is no `tag`, then the role applies at the organizational level. A user may have many tag-specific roles, but may only have one organizational level role. If the organizational level role has higher privileges than a tag-specific role, then the organizational role privileges will take precedence.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**tag** | [**UserRoleAssignmentTag**](UserRoleAssignmentTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


