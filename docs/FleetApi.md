# samsara.FleetApi

All URIs are relative to *https://api.samsara.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fleet_address**](FleetApi.md#add_fleet_address) | **POST** /fleet/add_address | /fleet/add_address
[**create_fleet_dispatch_jobs**](FleetApi.md#create_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/create | /fleet/dispatch_jobs/create
[**get_fleet**](FleetApi.md#get_fleet) | **POST** /fleet/list | /fleet/list
[**get_fleet_dispatch_jobs**](FleetApi.md#get_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs | /fleet/dispatch_jobs
[**get_fleet_drivers**](FleetApi.md#get_fleet_drivers) | **POST** /fleet/drivers | /fleet/drivers
[**get_fleet_drivers_summary**](FleetApi.md#get_fleet_drivers_summary) | **POST** /fleet/drivers/summary | /fleet/drivers/summary
[**get_fleet_hos_logs**](FleetApi.md#get_fleet_hos_logs) | **POST** /fleet/hos_logs | /fleet/hos_logs
[**get_fleet_locations**](FleetApi.md#get_fleet_locations) | **POST** /fleet/locations | /fleet/locations
[**get_fleet_trips**](FleetApi.md#get_fleet_trips) | **POST** /fleet/trips | /fleet/trips
[**update_fleet_dispatch_jobs**](FleetApi.md#update_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/update | /fleet/dispatch_jobs/update
[**update_vehicles**](FleetApi.md#update_vehicles) | **POST** /fleet/set_data | /fleet/set_data


# **add_fleet_address**
> add_fleet_address(access_token, address_param)

/fleet/add_address

This method adds an address book entry to the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
address_param = samsara.AddressParam() # AddressParam | 

try: 
    # /fleet/add_address
    api_instance.add_fleet_address(access_token, address_param)
except ApiException as e:
    print "Exception when calling FleetApi->add_fleet_address: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **address_param** | [**AddressParam**](AddressParam.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fleet_dispatch_jobs**
> DispatchJobsResponse create_fleet_dispatch_jobs(access_token, create_dispatch_jobs_param)

/fleet/dispatch_jobs/create

Create dispatch jobs in the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
create_dispatch_jobs_param = samsara.CreateDispatchJobsParam() # CreateDispatchJobsParam | 

try: 
    # /fleet/dispatch_jobs/create
    api_response = api_instance.create_fleet_dispatch_jobs(access_token, create_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->create_fleet_dispatch_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **create_dispatch_jobs_param** | [**CreateDispatchJobsParam**](CreateDispatchJobsParam.md)|  | 

### Return type

[**DispatchJobsResponse**](DispatchJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet**
> InlineResponse200 get_fleet(access_token, group_param)

/fleet/list

Get list of the vehicles. This method returns a list of the vehicles in the Samsara Cloud and information about them.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # /fleet/list
    api_response = api_instance.get_fleet(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **group_param** | [**GroupParam**](GroupParam.md)| Group ID to query. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_dispatch_jobs**
> DispatchJobsResponse get_fleet_dispatch_jobs(access_token, get_dispatch_jobs_param)

/fleet/dispatch_jobs

Get the dispatch jobs for the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
get_dispatch_jobs_param = samsara.GetDispatchJobsParam() # GetDispatchJobsParam | 

try: 
    # /fleet/dispatch_jobs
    api_response = api_instance.get_fleet_dispatch_jobs(access_token, get_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_dispatch_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **get_dispatch_jobs_param** | [**GetDispatchJobsParam**](GetDispatchJobsParam.md)|  | 

### Return type

[**DispatchJobsResponse**](DispatchJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_drivers**
> DriversRespose get_fleet_drivers(access_token, group_drivers_param)

/fleet/drivers

Get all the drivers for the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_drivers_param = samsara.GroupDriversParam() # GroupDriversParam | 

try: 
    # /fleet/drivers
    api_response = api_instance.get_fleet_drivers(access_token, group_drivers_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_drivers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **group_drivers_param** | [**GroupDriversParam**](GroupDriversParam.md)|  | 

### Return type

[**DriversRespose**](DriversRespose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_drivers_summary**
> DriversSummaryResponse get_fleet_drivers_summary(access_token, drivers_summary_param)

/fleet/drivers/summary

Get the distance and time each driver in an organization has driven in a given time period.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
drivers_summary_param = samsara.DriversSummaryParam() # DriversSummaryParam | Org ID and time range to query.

try: 
    # /fleet/drivers/summary
    api_response = api_instance.get_fleet_drivers_summary(access_token, drivers_summary_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_drivers_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **drivers_summary_param** | [**DriversSummaryParam**](DriversSummaryParam.md)| Org ID and time range to query. | 

### Return type

[**DriversSummaryResponse**](DriversSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_hos_logs**
> HosLogsResponse get_fleet_hos_logs(access_token, hos_logs_param)

/fleet/hos_logs

Get the HOS (hours of service) logs for the specified driver.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
hos_logs_param = samsara.HosLogsParam() # HosLogsParam | 

try: 
    # /fleet/hos_logs
    api_response = api_instance.get_fleet_hos_logs(access_token, hos_logs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_hos_logs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **hos_logs_param** | [**HosLogsParam**](HosLogsParam.md)|  | 

### Return type

[**HosLogsResponse**](HosLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_locations**
> InlineResponse2001 get_fleet_locations(access_token, group_param)

/fleet/locations

Get current location of vehicles in a group. This method returns the current location in latitude and longitude of all vehicles in a requested group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # /fleet/locations
    api_response = api_instance.get_fleet_locations(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_locations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **group_param** | [**GroupParam**](GroupParam.md)| Group ID to query. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_trips**
> TripResponse get_fleet_trips(access_token, trips_param)

/fleet/trips

Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
trips_param = samsara.TripsParam() # TripsParam | Group ID, vehicle ID and time range to query.

try: 
    # /fleet/trips
    api_response = api_instance.get_fleet_trips(access_token, trips_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->get_fleet_trips: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **trips_param** | [**TripsParam**](TripsParam.md)| Group ID, vehicle ID and time range to query. | 

### Return type

[**TripResponse**](TripResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fleet_dispatch_jobs**
> DispatchJobsResponse update_fleet_dispatch_jobs(access_token, update_dispatch_jobs_param)

/fleet/dispatch_jobs/update

Update dispatch jobs in the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
update_dispatch_jobs_param = samsara.UpdateDispatchJobsParam() # UpdateDispatchJobsParam | 

try: 
    # /fleet/dispatch_jobs/update
    api_response = api_instance.update_fleet_dispatch_jobs(access_token, update_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FleetApi->update_fleet_dispatch_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **update_dispatch_jobs_param** | [**UpdateDispatchJobsParam**](UpdateDispatchJobsParam.md)|  | 

### Return type

[**DispatchJobsResponse**](DispatchJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicles**
> update_vehicles(access_token, vehicle_update_param)

/fleet/set_data

This method enables the mutation of metadata for vehicles in the Samsara Cloud.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.FleetApi()
access_token = 'access_token_example' # str | Samsara API access token.
vehicle_update_param = samsara.VehicleUpdateParam() # VehicleUpdateParam | 

try: 
    # /fleet/set_data
    api_instance.update_vehicles(access_token, vehicle_update_param)
except ApiException as e:
    print "Exception when calling FleetApi->update_vehicles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **vehicle_update_param** | [**VehicleUpdateParam**](VehicleUpdateParam.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

