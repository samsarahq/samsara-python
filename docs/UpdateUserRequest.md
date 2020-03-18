# UpdateUserRequest

The user update arguments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**UserAuthType**](UserAuthType.md) |  | [optional] 
**name** | **str** | The first and last name of the user. | [optional] 
**roles** | [**list[UserRoleAssignmentRequest]**](UserRoleAssignmentRequest.md) | The list of roles that applies to this user. A user may have \&quot;organizational\&quot; roles, which apply to the user at the organizational level, and \&quot;tag-specific\&quot; roles, which apply to the user for a given tag. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


