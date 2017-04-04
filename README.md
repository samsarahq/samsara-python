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
*DefaultApi* | [**add_fleet_address**](docs/DefaultApi.md#add_fleet_address) | **POST** /fleet/add_address | /fleet/add_address
*DefaultApi* | [**create_fleet_dispatch_jobs**](docs/DefaultApi.md#create_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/create | /fleet/dispatch_jobs/create
*DefaultApi* | [**get_fleet**](docs/DefaultApi.md#get_fleet) | **POST** /fleet/list | /fleet/list
*DefaultApi* | [**get_fleet_dispatch_jobs**](docs/DefaultApi.md#get_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs | /fleet/dispatch_jobs
*DefaultApi* | [**get_fleet_drivers**](docs/DefaultApi.md#get_fleet_drivers) | **POST** /fleet/drivers | /fleet/drivers
*DefaultApi* | [**get_fleet_drivers_summary**](docs/DefaultApi.md#get_fleet_drivers_summary) | **POST** /fleet/drivers/summary | /fleet/drivers/summary
*DefaultApi* | [**get_fleet_hos_authentication_logs**](docs/DefaultApi.md#get_fleet_hos_authentication_logs) | **POST** /fleet/hos_authentication_logs | /fleet/hos_authentication_logs
*DefaultApi* | [**get_fleet_hos_logs**](docs/DefaultApi.md#get_fleet_hos_logs) | **POST** /fleet/hos_logs | /fleet/hos_logs
*DefaultApi* | [**get_fleet_locations**](docs/DefaultApi.md#get_fleet_locations) | **POST** /fleet/locations | /fleet/locations
*DefaultApi* | [**get_fleet_maintenance_list**](docs/DefaultApi.md#get_fleet_maintenance_list) | **POST** /fleet/maintenance/list | /fleet/maintenance/list
*DefaultApi* | [**get_fleet_trips**](docs/DefaultApi.md#get_fleet_trips) | **POST** /fleet/trips | /fleet/trips
*DefaultApi* | [**get_sensors**](docs/DefaultApi.md#get_sensors) | **POST** /sensors/list | /sensors/list
*DefaultApi* | [**get_sensors_history**](docs/DefaultApi.md#get_sensors_history) | **POST** /sensors/history | /sensors/history
*DefaultApi* | [**get_sensors_humidity**](docs/DefaultApi.md#get_sensors_humidity) | **POST** /sensors/humidity | /sensors/humidity
*DefaultApi* | [**get_sensors_temperature**](docs/DefaultApi.md#get_sensors_temperature) | **POST** /sensors/temperature | /sensors/temperature
*DefaultApi* | [**update_fleet_dispatch_jobs**](docs/DefaultApi.md#update_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/update | /fleet/dispatch_jobs/update
*DefaultApi* | [**update_vehicles**](docs/DefaultApi.md#update_vehicles) | **POST** /fleet/set_data | /fleet/set_data
*FleetApi* | [**add_fleet_address**](docs/FleetApi.md#add_fleet_address) | **POST** /fleet/add_address | /fleet/add_address
*FleetApi* | [**create_fleet_dispatch_jobs**](docs/FleetApi.md#create_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/create | /fleet/dispatch_jobs/create
*FleetApi* | [**get_fleet**](docs/FleetApi.md#get_fleet) | **POST** /fleet/list | /fleet/list
*FleetApi* | [**get_fleet_dispatch_jobs**](docs/FleetApi.md#get_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs | /fleet/dispatch_jobs
*FleetApi* | [**get_fleet_drivers**](docs/FleetApi.md#get_fleet_drivers) | **POST** /fleet/drivers | /fleet/drivers
*FleetApi* | [**get_fleet_drivers_summary**](docs/FleetApi.md#get_fleet_drivers_summary) | **POST** /fleet/drivers/summary | /fleet/drivers/summary
*FleetApi* | [**get_fleet_hos_authentication_logs**](docs/FleetApi.md#get_fleet_hos_authentication_logs) | **POST** /fleet/hos_authentication_logs | /fleet/hos_authentication_logs
*FleetApi* | [**get_fleet_hos_logs**](docs/FleetApi.md#get_fleet_hos_logs) | **POST** /fleet/hos_logs | /fleet/hos_logs
*FleetApi* | [**get_fleet_locations**](docs/FleetApi.md#get_fleet_locations) | **POST** /fleet/locations | /fleet/locations
*FleetApi* | [**get_fleet_maintenance_list**](docs/FleetApi.md#get_fleet_maintenance_list) | **POST** /fleet/maintenance/list | /fleet/maintenance/list
*FleetApi* | [**get_fleet_trips**](docs/FleetApi.md#get_fleet_trips) | **POST** /fleet/trips | /fleet/trips
*FleetApi* | [**update_fleet_dispatch_jobs**](docs/FleetApi.md#update_fleet_dispatch_jobs) | **POST** /fleet/dispatch_jobs/update | /fleet/dispatch_jobs/update
*FleetApi* | [**update_vehicles**](docs/FleetApi.md#update_vehicles) | **POST** /fleet/set_data | /fleet/set_data
*SensorsApi* | [**get_sensors**](docs/SensorsApi.md#get_sensors) | **POST** /sensors/list | /sensors/list
*SensorsApi* | [**get_sensors_history**](docs/SensorsApi.md#get_sensors_history) | **POST** /sensors/history | /sensors/history
*SensorsApi* | [**get_sensors_humidity**](docs/SensorsApi.md#get_sensors_humidity) | **POST** /sensors/humidity | /sensors/humidity
*SensorsApi* | [**get_sensors_temperature**](docs/SensorsApi.md#get_sensors_temperature) | **POST** /sensors/temperature | /sensors/temperature


## Documentation For Models

 - [AddressParam](docs/AddressParam.md)
 - [CreateDispatchJobsParam](docs/CreateDispatchJobsParam.md)
 - [DispatchJobsResponse](docs/DispatchJobsResponse.md)
 - [DispatchJobsResponseDispatchJobs](docs/DispatchJobsResponseDispatchJobs.md)
 - [DriversRespose](docs/DriversRespose.md)
 - [DriversResposeDrivers](docs/DriversResposeDrivers.md)
 - [DriversSummaryParam](docs/DriversSummaryParam.md)
 - [DriversSummaryResponse](docs/DriversSummaryResponse.md)
 - [DriversSummaryResponseSummaries](docs/DriversSummaryResponseSummaries.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FleetdispatchJobscreateDispatchJobs](docs/FleetdispatchJobscreateDispatchJobs.md)
 - [FleetdispatchJobsupdateDispatchJobs](docs/FleetdispatchJobsupdateDispatchJobs.md)
 - [GetDispatchJobsParam](docs/GetDispatchJobsParam.md)
 - [GroupDriversParam](docs/GroupDriversParam.md)
 - [GroupParam](docs/GroupParam.md)
 - [HistoryParam](docs/HistoryParam.md)
 - [HosAuthenticationLogsParam](docs/HosAuthenticationLogsParam.md)
 - [HosAuthenticationLogsResponse](docs/HosAuthenticationLogsResponse.md)
 - [HosAuthenticationLogsResponseAuthenticationLogs](docs/HosAuthenticationLogsResponseAuthenticationLogs.md)
 - [HosLogsParam](docs/HosLogsParam.md)
 - [HosLogsResponse](docs/HosLogsResponse.md)
 - [HosLogsResponseLogs](docs/HosLogsResponseLogs.md)
 - [HumidityResponse](docs/HumidityResponse.md)
 - [HumidityResponseSensors](docs/HumidityResponseSensors.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
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
 - [VehicleMaintenance](docs/VehicleMaintenance.md)
 - [VehicleMaintenanceJ1939](docs/VehicleMaintenanceJ1939.md)
 - [VehicleMaintenanceJ1939CheckEngineLight](docs/VehicleMaintenanceJ1939CheckEngineLight.md)
 - [VehicleMaintenanceJ1939DiagnosticTroubleCodes](docs/VehicleMaintenanceJ1939DiagnosticTroubleCodes.md)
 - [VehicleMaintenancePassenger](docs/VehicleMaintenancePassenger.md)
 - [VehicleMaintenancePassengerCheckEngineLight](docs/VehicleMaintenancePassengerCheckEngineLight.md)
 - [VehicleMaintenancePassengerDiagnosticTroubleCodes](docs/VehicleMaintenancePassengerDiagnosticTroubleCodes.md)
 - [VehicleUpdateParam](docs/VehicleUpdateParam.md)


## Footnotes

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build date: 2016-08-17T12:10:56.786-07:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen
