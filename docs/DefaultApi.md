# samsara.DefaultApi

All URIs are relative to *https://api.samsara.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fleet_locations**](DefaultApi.md#get_fleet_locations) | **POST** /fleet/locations | Get the GPS locations for all vehicles in the group.
[**get_fleet_trips**](DefaultApi.md#get_fleet_trips) | **POST** /fleet/trips | Get the trips for the specified vehicle.
[**get_sensors**](DefaultApi.md#get_sensors) | **POST** /sensors/list | Get the sensors for a group.
[**get_sensors_history**](DefaultApi.md#get_sensors_history) | **POST** /sensors/history | Get the historical data for the sensors.
[**get_sensors_humidity**](DefaultApi.md#get_sensors_humidity) | **POST** /sensors/humidity | Get the current humidity readings for the specified sensors.
[**get_sensors_temperature**](DefaultApi.md#get_sensors_temperature) | **POST** /sensors/temperature | Get the current temperature readings for the specified sensors.


# **get_fleet_locations**
> InlineResponse200 get_fleet_locations(access_token, group_param)

Get the GPS locations for all vehicles in the group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
group_param = samsara.GroupParam() # GroupParam | 

try: 
    # Get the GPS locations for all vehicles in the group.
    api_response = api_instance.get_fleet_locations(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_locations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **group_param** | [**GroupParam**](GroupParam.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_trips**
> TripResponse get_fleet_trips(access_token, trips_param)

Get the trips for the specified vehicle.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
trips_param = samsara.TripsParam() # TripsParam | 

try: 
    # Get the trips for the specified vehicle.
    api_response = api_instance.get_fleet_trips(access_token, trips_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_fleet_trips: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **trips_param** | [**TripsParam**](TripsParam.md)|  | 

### Return type

[**TripResponse**](TripResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors**
> InlineResponse2001 get_sensors(access_token, group_param)

Get the sensors for a group.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
group_param = samsara.GroupParam() # GroupParam | 

try: 
    # Get the sensors for a group.
    api_response = api_instance.get_sensors(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **group_param** | [**GroupParam**](GroupParam.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_history**
> SensorHistoryResponse get_sensors_history(access_token, history_param)

Get the historical data for the sensors.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
history_param = samsara.HistoryParam() # HistoryParam | 

try: 
    # Get the historical data for the sensors.
    api_response = api_instance.get_sensors_history(access_token, history_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **history_param** | [**HistoryParam**](HistoryParam.md)|  | 

### Return type

[**SensorHistoryResponse**](SensorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_humidity**
> HumidityResponse get_sensors_humidity(access_token, sensor_param)

Get the current humidity readings for the specified sensors.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
sensor_param = samsara.SensorParam() # SensorParam | 

try: 
    # Get the current humidity readings for the specified sensors.
    api_response = api_instance.get_sensors_humidity(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_humidity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **sensor_param** | [**SensorParam**](SensorParam.md)|  | 

### Return type

[**HumidityResponse**](HumidityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_temperature**
> TemperatureResponse get_sensors_temperature(access_token, sensor_param)

Get the current temperature readings for the specified sensors.

### Example 
```python
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.DefaultApi()
access_token = 'access_token_example' # str | 
sensor_param = samsara.SensorParam() # SensorParam | 

try: 
    # Get the current temperature readings for the specified sensors.
    api_response = api_instance.get_sensors_temperature(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_sensors_temperature: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **sensor_param** | [**SensorParam**](SensorParam.md)|  | 

### Return type

[**TemperatureResponse**](TemperatureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

