# samsara.SensorsApi

All URIs are relative to *https://api.samsara.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sensors**](SensorsApi.md#get_sensors) | **POST** /sensors/list | /sensors/list
[**get_sensors_history**](SensorsApi.md#get_sensors_history) | **POST** /sensors/history | /sensors/history
[**get_sensors_humidity**](SensorsApi.md#get_sensors_humidity) | **POST** /sensors/humidity | /sensors/humidity
[**get_sensors_temperature**](SensorsApi.md#get_sensors_temperature) | **POST** /sensors/temperature | /sensors/temperature


# **get_sensors**
> InlineResponse200 get_sensors(access_token, group_param)

/sensors/list

Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them.

### Example 
```python
from __future__ import print_statement
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.SensorsApi()
access_token = 'access_token_example' # str | Samsara API access token.
group_param = samsara.GroupParam() # GroupParam | Group ID to query.

try: 
    # /sensors/list
    api_response = api_instance.get_sensors(access_token, group_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors: %s\n" % e)
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

# **get_sensors_history**
> SensorHistoryResponse get_sensors_history(access_token, history_param)

/sensors/history

Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.

### Example 
```python
from __future__ import print_statement
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.SensorsApi()
access_token = 'access_token_example' # str | Samsara API access token.
history_param = samsara.HistoryParam() # HistoryParam | Group ID, time range and resolution, and list of sensor ID, field pairs to query.

try: 
    # /sensors/history
    api_response = api_instance.get_sensors_history(access_token, history_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_history: %s\n" % e)
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

/sensors/humidity

Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors.

### Example 
```python
from __future__ import print_statement
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.SensorsApi()
access_token = 'access_token_example' # str | Samsara API access token.
sensor_param = samsara.SensorParam() # SensorParam | Group ID and list of sensor IDs to query.

try: 
    # /sensors/humidity
    api_response = api_instance.get_sensors_humidity(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_humidity: %s\n" % e)
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

/sensors/temperature

Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.

### Example 
```python
from __future__ import print_statement
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = samsara.SensorsApi()
access_token = 'access_token_example' # str | Samsara API access token.
sensor_param = samsara.SensorParam() # SensorParam | Group ID and list of sensor IDs to query.

try: 
    # /sensors/temperature
    api_response = api_instance.get_sensors_temperature(access_token, sensor_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_temperature: %s\n" % e)
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

