# CreateUserRequest

The user creation arguments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**UserAuthType**](UserAuthType.md) |  | 
**email** | **str** | The email address of this user. | 
**name** | **str** | The first and last name of the user. | 
**roles** | [**list[UserTagRoleRequest]**](UserTagRoleRequest.md) | The roles for this user. Users must have at least a single role to be a part of an organization. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


