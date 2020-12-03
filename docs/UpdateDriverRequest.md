# UpdateDriverRequest

Driver that should be updated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**list[CreateDriverRequestAttributes]**](CreateDriverRequestAttributes.md) |  | [optional] 
**carrier_settings** | [**CreateDriverRequestCarrierSettings**](CreateDriverRequestCarrierSettings.md) |  | [optional] 
**current_id_card_code** | **str** | The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature. | [optional] 
**deactivated_at_time** | **str** | The date and time this driver is considered to be deactivated in RFC 3339 format. | [optional] 
**driver_activation_status** | **str** | A value indicating whether the driver is active or deactivated. | [optional] 
**eld_adverse_weather_exemption_enabled** | **bool** | Flag indicating this driver may use Adverse Weather exemptions in ELD logs. | [optional] 
**eld_big_day_exemption_enabled** | **bool** | Flag indicating this driver may use Big Day exemption in ELD logs. | [optional] 
**eld_day_start_hour** | **int** | &#x60;0&#x60; indicating midnight-to-midnight ELD driving hours, &#x60;12&#x60; to indicate noon-to-noon driving hours. | [optional] 
**eld_exempt** | **bool** | Flag indicating this driver is exempt from the Electronic Logging Mandate. | [optional] 
**eld_exempt_reason** | **str** | Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt). | [optional] 
**eld_pc_enabled** | **bool** | Flag indicating this driver may select the Personal Conveyance duty status in ELD logs. | [optional] 
**eld_ym_enabled** | **bool** | Flag indicating this driver may select the Yard Move duty status in ELD logs. | [optional] 
**external_ids** | **dict(str, str)** | The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object. | [optional] 
**license_number** | **str** | Driver&#39;s state issued license number. The combination of this number and &#x60;licenseState&#x60; must be unique. | [optional] 
**license_state** | **str** | Abbreviation of US state, Canadian province, or US territory that issued driver&#39;s license. | [optional] 
**locale** | **str** | Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. | [optional] 
**name** | **str** | Driver&#39;s name. | [optional] 
**notes** | **str** | Notes about the driver. | [optional] 
**password** | **str** | Password that the driver can use to login to the Samsara driver app. | [optional] 
**phone** | **str** | Phone number of the driver. | [optional] 
**static_assigned_vehicle_id** | **str** | ID of vehicle that the driver is permanently assigned to. (uncommon). | [optional] 
**tachograph_card_number** | **str** | Driver&#39;s assigned tachograph card number (Europe specific) | [optional] 
**tag_ids** | **list[str]** | IDs of tags the driver is associated with. | [optional] 
**timezone** | **str** | Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. &#x60;America/Los_Angeles&#x60;, &#x60;America/New_York&#x60;, &#x60;Europe/London&#x60;, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html). | [optional] 
**username** | **str** | Driver&#39;s login username into the driver app. The username may not contain spaces or the &#39;@&#39; symbol. The username must be unique. | [optional] 
**vehicle_group_tag_id** | **str** | Tag ID which determines which vehicles a driver will see when selecting vehicles. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


