# Driver

A driver object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_settings** | [**DriverCarrierSettings**](DriverCarrierSettings.md) |  | [optional] 
**created_at_time** | **datetime** | The date and time this driver was created in RFC 3339 format. | [optional] 
**driver_activation_status** | [**DriverActivationStatus**](DriverActivationStatus.md) |  | [optional] 
**eld_adverse_weather_exemption_enabled** | **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] [default to False]
**eld_big_day_exemption_enabled** | **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] [default to False]
**eld_day_start_hour** | **int** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] [default to 0]
**eld_exempt** | **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] [default to False]
**eld_exempt_reason** | **str** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**eld_pc_enabled** | **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] [default to False]
**eld_ym_enabled** | **bool** | Flag indicating this driver may select the Yard Move duty status in ELD logs. | [optional] [default to False]
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**id** | **str** | Samsara ID for the driver. | [optional] 
**is_deactivated** | **bool** | [DEPRECATED] A boolean indicating whether or not the driver is deactivated. Use &#x60;driverActivationStatus&#x60; instead. | [optional] 
**license_number** | **str** | Driver&#39;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**license_state** | **str** | Abbreviation of state that issued driver&#39;s license. | [optional] 
**locale** | [**DriverLocale**](DriverLocale.md) |  | [optional] 
**name** | **str** | Driver&#39;s name. | [optional] 
**notes** | **str** | Notes about the driver. | [optional] 
**phone** | **str** | Phone number of the driver. | [optional] 
**static_assigned_vehicle** | [**DriverStaticAssignedVehicle**](DriverStaticAssignedVehicle.md) |  | [optional] 
**tachograph_card_number** | **str** | Driver&#39;s assigned tachograph card number (Europe specific) | [optional] 
**tags** | [**list[TagTinyResponse]**](TagTinyResponse.md) | The tags this driver belongs to. | [optional] 
**timezone** | **str** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. &#x60;America/Los_Angeles&#x60;, &#x60;America/New_York&#x60;, &#x60;Europe/London&#x60;, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html). | [optional] 
**updated_at_time** | **datetime** | The date and time this driver was last updated in RFC 3339 format. | [optional] 
**username** | **str** | Driver&#39;s login username into the driver app. The username may not contain spaces or the &#39;@&#39; symbol. The username must be unique. | [optional] 
**vehicle_group_tag** | [**DriverVehicleGroupTag**](DriverVehicleGroupTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


