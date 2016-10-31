# samsara.DefaultApi

All URIs are relative to *https://api.samsara.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fleet_address**](DefaultApi.md#add_fleet_address) | **POST** /fleet/add_address | This method adds an address book entry to the specified group.
[**create_fleet_dispatch_jobs**](DefaultApi.md#create_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/create | Create dispatch jobs in the specified group.
[**get_fleet**](DefaultApi.md#get_fleet) | **POST** /fleet/list | This method returns a list of the vehicles in the Samsara Cloud and information about them.
[**get_fleet_dispatch_jobs**](DefaultApi.md#get_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs | Get the dispatch jobs for the specified group.
[**get_fleet_drivers**](DefaultApi.md#get_fleet_drivers) | **POST** /fleet/drivers | Get all the drivers for the specified group.
[**get_fleet_hos_logs**](DefaultApi.md#get_fleet_hos_logs) | **POST** /fleet/hos_logs | Get the HOS (hours of service) logs for the specified driver.
[**get_fleet_locations**](DefaultApi.md#get_fleet_locations) | **POST** /fleet/locations | This method returns the current location in latitude and longitude of all vehicles in a requested group.
[**get_fleet_trips**](DefaultApi.md#get_fleet_trips) | **POST** /fleet/trips | This method returns a set of historical trips data for the specified vehicle in the specified time range.
[**get_sensors**](DefaultApi.md#get_sensors) | **POST** /sensors/list | This method returns a list of the sensor objects in the Samsara Cloud and information about them.
[**get_sensors_history**](DefaultApi.md#get_sensors_history) | **POST** /sensors/history | This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.
[**get_sensors_humidity**](DefaultApi.md#get_sensors_humidity) | **POST** /sensors/humidity | This method returns the current relative humidity for the requested sensors.
[**get_sensors_temperature**](DefaultApi.md#get_sensors_temperature) | **POST** /sensors/temperature | This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.
[**update_fleet_dispatch_jobs**](DefaultApi.md#update_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/update | Update dispatch jobs specified group.
[**update_vehicles**](DefaultApi.md#update_vehicles) | **POST** /fleet/set_data | This method enables the mutation of metadata for vehicles in the Samsara Cloud.


# **add_fleet_address**
> add_fleet_address(access_token, address_param)

This method adds an address book entry to the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
address_param = samsara.AddressParam() # AddressParam | 

try: 
    # This method adds an address book entry to the specified group.
    api_instance.add_fleet_address(access_token, address_param)
except ApiException as e:
    print "Exception when calling DefaultApi->add_fleet_address: %s\n" % e
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

Create dispatch jobs in the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
create_dispatch_jobs_param = samsara.CreateDispatchJobsParam() # CreateDispatchJobsParam | 

try: 
    # Create dispatch jobs in the specified group.
    api_response = api_instance.create_fleet_dispatch_jobs(access_token, create_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_fleet_dispatch_jobs: %s\n" % e
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

This method returns a list of the vehicles in the Samsara Cloud and information about them.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # This method returns a list of the vehicles in the Samsara Cloud and information about them.
    api_response = api_instance.get_fleet(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet: %s\n" % e
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

Get the dispatch jobs for the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
get_dispatch_jobs_param = samsara.GetDispatchJobsParam() # GetDispatchJobsParam | 

try: 
    # Get the dispatch jobs for the specified group.
    api_response = api_instance.get_fleet_dispatch_jobs(access_token, get_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_dispatch_jobs: %s\n" % e
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

Get all the drivers for the specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_drivers_param = samsara.GroupDriversParam() # GroupDriversParam | 

try: 
    # Get all the drivers for the specified group.
    api_response = api_instance.get_fleet_drivers(access_token, group_drivers_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_drivers: %s\n" % e
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

# **get_fleet_hos_logs**
> HosLogsResponse get_fleet_hos_logs(access_token, hos_logs_param)

Get the HOS (hours of service) logs for the specified driver.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
hos_logs_param = samsara.HosLogsParam() # HosLogsParam | 

try: 
    # Get the HOS (hours of service) logs for the specified driver.
    api_response = api_instance.get_fleet_hos_logs(access_token, hos_logs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_hos_logs: %s\n" % e
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

This method returns the current location in latitude and longitude of all vehicles in a requested group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # This method returns the current location in latitude and longitude of all vehicles in a requested group.
    api_response = api_instance.get_fleet_locations(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_locations: %s\n" % e
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

This method returns a set of historical trips data for the specified vehicle in the specified time range.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
trips_param = samsara.TripsParam() # TripsParam | Group ID, vehicle ID and time range to query.

try: 
    # This method returns a set of historical trips data for the specified vehicle in the specified time range.
    api_response = api_instance.get_fleet_trips(access_token, trips_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_trips: %s\n" % e
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

# **get_sensors**
> InlineResponse2002 get_sensors(access_token, group_param)

This method returns a list of the sensor objects in the Samsara Cloud and information about them.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # This method returns a list of the sensor objects in the Samsara Cloud and information about them.
    api_response = api_instance.get_sensors(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **group_param** | [**GroupParam**](GroupParam.md)| Group ID to query. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_history**
> SensorHistoryResponse get_sensors_history(access_token, history_param)

This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
history_param = samsara.HistoryParam() # HistoryParam | Group ID, time range and resolution, and list of sensor ID, field pairs to query.

try: 
    # This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.
    api_response = api_instance.get_sensors_history(access_token, history_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **history_param** | [**HistoryParam**](HistoryParam.md)| Group ID, time range and resolution, and list of sensor ID, field pairs to query. | 

### Return type

[**SensorHistoryResponse**](SensorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_humidity**
> HumidityResponse get_sensors_humidity(access_token, sensor_param)

This method returns the current relative humidity for the requested sensors.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
sensor_param = samsara.SensorParam() # SensorParam | Group ID and list of sensor IDs to query.

try: 
    # This method returns the current relative humidity for the requested sensors.
    api_response = api_instance.get_sensors_humidity(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_humidity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **sensor_param** | [**SensorParam**](SensorParam.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**HumidityResponse**](HumidityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_temperature**
> TemperatureResponse get_sensors_temperature(access_token, sensor_param)

This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
sensor_param = samsara.SensorParam() # SensorParam | Group ID and list of sensor IDs to query.

try: 
    # This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.
    api_response = api_instance.get_sensors_temperature(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_temperature: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Samsara API access token. | 
 **sensor_param** | [**SensorParam**](SensorParam.md)| Group ID and list of sensor IDs to query. | 

### Return type

[**TemperatureResponse**](TemperatureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fleet_dispatch_jobs**
> DispatchJobsResponse update_fleet_dispatch_jobs(access_token, update_dispatch_jobs_param)

Update dispatch jobs specified group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
update_dispatch_jobs_param = samsara.UpdateDispatchJobsParam() # UpdateDispatchJobsParam | 

try: 
    # Update dispatch jobs specified group.
    api_response = api_instance.update_fleet_dispatch_jobs(access_token, update_dispatch_jobs_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->update_fleet_dispatch_jobs: %s\n" % e
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

This method enables the mutation of metadata for vehicles in the Samsara Cloud.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | Samsara API access token.
vehicle_update_param = samsara.VehicleUpdateParam() # VehicleUpdateParam | 

try: 
    # This method enables the mutation of metadata for vehicles in the Samsara Cloud.
    api_instance.update_vehicles(access_token, vehicle_update_param)
except ApiException as e:
    print "Exception when calling DefaultApi->update_vehicles: %s\n" % e
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

