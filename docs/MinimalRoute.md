# MinimalRoute

A single route. Only the fields that have changed are present in the response. All other fields, including the route id, will not be present in the response. For now, only routeStops are included since only Route Tracking updates are supported.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_stops** | [**list[MinimalRouteStop]**](MinimalRouteStop.md) | The route stops in the route. Only stops that have been updated will be included in the response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


