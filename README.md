# samsara-python

Python SDK for the Samsara REST API.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

To install directly from Github:

```sh
pip install git+https://github.com/samsarahq/samsara-python.git
```
(Note that you may need to run `pip` with root permission).

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Getting Started

* Install the samsara Python package: [installation procedure](#installation--usage).

* Get your Samsara API access token.

The access token authenticates requests. It is tied to your organization and can be found on the
API Tokens tab on your Organization Settings page in Samsara Cloud (click on the user drop-down in
the upper-right of the Dashboard).

All API calls require the access token.

* Get the Group IDs for the groups you want to access.

The API Tokens tab lists all your organization's Groups and their associated IDs ("groupId").

Certain API calls require this value.

* Check out the examples in the `examples/` directory to see how to use the Python client.


## Documentation for API Endpoints

All URIs are relative to *https://api.samsara.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_fleet_address**](docs/DefaultApi.md#add_fleet_address) | **POST** /fleet/add_address | This method adds an address book entry to the specified group.
*DefaultApi* | [**create_fleet_dispatch_jobs**](docs/DefaultApi.md#create_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/create | Create dispatch jobs in the specified group.
*DefaultApi* | [**get_fleet**](docs/DefaultApi.md#get_fleet) | **POST** /fleet/list | This method returns a list of the vehicles in the Samsara Cloud and information about them.
*DefaultApi* | [**get_fleet_dispatch_jobs**](docs/DefaultApi.md#get_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs | Get the dispatch jobs for the specified group.
*DefaultApi* | [**get_fleet_drivers**](docs/DefaultApi.md#get_fleet_drivers) | **POST** /fleet/drivers | Get all the drivers for the specified group.
*DefaultApi* | [**get_fleet_drivers_summary**](docs/DefaultApi.md#get_fleet_drivers_summary) | **POST** /fleet/drivers/summary | Get the activity summary for each driver in the specified org.
*DefaultApi* | [**get_fleet_hos_logs**](docs/DefaultApi.md#get_fleet_hos_logs) | **POST** /fleet/hos_logs | Get the HOS (hours of service) logs for the specified driver.
*DefaultApi* | [**get_fleet_locations**](docs/DefaultApi.md#get_fleet_locations) | **POST** /fleet/locations | This method returns the current location in latitude and longitude of all vehicles in a requested group.
*DefaultApi* | [**get_fleet_trips**](docs/DefaultApi.md#get_fleet_trips) | **POST** /fleet/trips | This method returns a set of historical trips data for the specified vehicle in the specified time range.
*DefaultApi* | [**get_sensors**](docs/DefaultApi.md#get_sensors) | **POST** /sensors/list | This method returns a list of the sensor objects in the Samsara Cloud and information about them.
*DefaultApi* | [**get_sensors_history**](docs/DefaultApi.md#get_sensors_history) | **POST** /sensors/history | This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution.
*DefaultApi* | [**get_sensors_humidity**](docs/DefaultApi.md#get_sensors_humidity) | **POST** /sensors/humidity | This method returns the current relative humidity for the requested sensors.
*DefaultApi* | [**get_sensors_temperature**](docs/DefaultApi.md#get_sensors_temperature) | **POST** /sensors/temperature | This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors.
*DefaultApi* | [**update_fleet_dispatch_jobs**](docs/DefaultApi.md#update_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/update | Update dispatch jobs specified group.
*DefaultApi* | [**update_vehicles**](docs/DefaultApi.md#update_vehicles) | **POST** /fleet/set_data | This method enables the mutation of metadata for vehicles in the Samsara Cloud.


## Documentation For Models

 - [AddressParam](docs/AddressParam.md)
 - [CreateDispatchJobsParam](docs/CreateDispatchJobsParam.md)
 - [DispatchJobsResponse](docs/DispatchJobsResponse.md)
 - [DispatchJobsResponseDispatchJobs](docs/DispatchJobsResponseDispatchJobs.md)
 - [DriversRespose](docs/DriversRespose.md)
 - [DriversResposeDrivers](docs/DriversResposeDrivers.md)
 - [DriversSummaryParam](docs/DriversSummaryParam.md)
 - [DriversSummaryResponse](docs/DriversSummaryResponse.md)
 - [DriversSummaryResponseSummaries](docs/DriverSummaryResponseSummaries.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FleetdispatchJobscreateDispatchJobs](docs/FleetdispatchJobscreateDispatchJobs.md)
 - [FleetdispatchJobsupdateDispatchJobs](docs/FleetdispatchJobsupdateDispatchJobs.md)
 - [GetDispatchJobsParam](docs/GetDispatchJobsParam.md)
 - [GroupDriversParam](docs/GroupDriversParam.md)
 - [GroupParam](docs/GroupParam.md)
 - [HistoryParam](docs/HistoryParam.md)
 - [HosLogsParam](docs/HosLogsParam.md)
 - [HosLogsResponse](docs/HosLogsResponse.md)
 - [HosLogsResponseLogs](docs/HosLogsResponseLogs.md)
 - [HumidityResponse](docs/HumidityResponse.md)
 - [HumidityResponseSensors](docs/HumidityResponseSensors.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [Sensor](docs/Sensor.md)
 - [SensorHistoryResponse](docs/SensorHistoryResponse.md)
 - [SensorHistoryResponseResults](docs/SensorHistoryResponseResults.md)
 - [SensorParam](docs/SensorParam.md)
 - [SensorshistorySeries](docs/SensorshistorySeries.md)
 - [TemperatureResponse](docs/TemperatureResponse.md)
 - [TemperatureResponseSensors](docs/TemperatureResponseSensors.md)
 - [TripResponse](docs/TripResponse.md)
 - [TripResponseEndCoordinates](docs/TripResponseEndCoordinates.md)
 - [TripResponseStartCoordinates](docs/TripResponseStartCoordinates.md)
 - [TripResponseTrips](docs/TripResponseTrips.md)
 - [TripsParam](docs/TripsParam.md)
 - [UpdateDispatchJobsParam](docs/UpdateDispatchJobsParam.md)
 - [Vehicle](docs/Vehicle.md)
 - [VehicleLocation](docs/VehicleLocation.md)
 - [VehicleUpdateParam](docs/VehicleUpdateParam.md)


## Footnotes

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build date: 2016-08-17T12:10:56.786-07:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen
