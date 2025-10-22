# Reference
## V20250611 Addresses
<details><summary><code>client.v_20250611.addresses.<a href="src/samsara/v_20250611/addresses/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all addresses in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.v_20250611.addresses.list(
    limit=1000000,
    after="after",
    created_after_time="createdAfterTime",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` — A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.addresses.<a href="src/samsara/v_20250611/addresses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new address in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import CreateAddressRequestGeofence

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.addresses.create(
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=CreateAddressRequestGeofence(),
    name="Samsara HQ",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**formatted_address:** `str` — The full street address for this address/geofence, as it might be recognized by Google Maps.
    
</dd>
</dl>

<dl>
<dd>

**geofence:** `CreateAddressRequestGeofence` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the address.
    
</dd>
</dl>

<dl>
<dd>

**address_types:** `typing.Optional[typing.Sequence[CreateAddressRequestAddressTypesItem]]` — Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`, `agricultureSource`, `avoidanceZone`, `knownGPSJammingZone`.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of Contact IDs associated with this Address.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` — Latitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` — Longitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the address.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.addresses.<a href="src/samsara/v_20250611/addresses/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.addresses.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.addresses.<a href="src/samsara/v_20250611/addresses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.addresses.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.addresses.<a href="src/samsara/v_20250611/addresses/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific address. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Addresses** under the Addresses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.addresses.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Address. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`
    
</dd>
</dl>

<dl>
<dd>

**address_types:** `typing.Optional[typing.Sequence[UpdateAddressRequestAddressTypesItem]]` — Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`, `agricultureSource`, `avoidanceZone`, `knownGPSJammingZone`.
    
</dd>
</dl>

<dl>
<dd>

**contact_ids:** `typing.Optional[typing.Sequence[str]]` — An array of Contact IDs associated with this Address.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**formatted_address:** `typing.Optional[str]` — The full street address for this address/geofence, as it might be recognized by Google Maps.
    
</dd>
</dl>

<dl>
<dd>

**geofence:** `typing.Optional[UpdateAddressRequestGeofence]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` — Latitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` — Longitude of the address. Will be geocoded from `formattedAddress` if not provided.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the address.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the address.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Alerts
<details><summary><code>client.v_20250611.alerts.<a href="src/samsara/v_20250611/alerts/client.py">get_configurations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get specified Alert Configurations.

The following trigger types are API enabled and will show up in the results:
Vehicle Speed
Ambient Temperature
Fuel Level (Percentage)
Vehicle DEF Level (Percentage)
Vehicle Battery
Gateway Unplugged
Dashcam Disconnected
Camera Connector Disconnected
Asset starts moving
Inside Geofence
Outside Geofence
Unassigned Driving
Driver HOS Violation
Vehicle Engine Idle
Asset Engine On
Asset Engine Off
Harsh Event
Scheduled Maintenance
Scheduled Maintenance by Odometer
Scheduled Maintenance by Engine Hours
Out of Route
GPS Signal Loss
Cell Signal Loss
Fault Code
Tire Faults
Gateway Disconnected
Panic Button
Tampering Detected
Asset Reading
If vehicle is severely speeding (as defined by your organization)
DVIR Submitted for Asset
Driver Document Submitted
Driver App Sign In
Driver App Sign Out
Geofence Entry
Geofence Exit
Route Stop ETA Alert
Driver Recorded
Sudden Fuel Level Rise
Sudden Fuel Level Drop
Scheduled Date And Time
Training Assignment Due Soon
Training Assignment Past Due

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.alerts.get_configurations(
    status="all",
    after="after",
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by the IDs. Returns all if no ids are provided.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetConfigurationsRequestStatus]` — The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.alerts.<a href="src/samsara/v_20250611/alerts/client.py">post_configurations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import (
    ActionObjectRequestBody,
    ScopeObjectRequestBody,
    WorkflowTriggerObjectRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.alerts.post_configurations(
    actions=[
        ActionObjectRequestBody(
            action_type_id=1,
        )
    ],
    is_enabled=True,
    name="My Harsh Event Alert",
    scope=ScopeObjectRequestBody(
        all_=True,
    ),
    triggers=[
        WorkflowTriggerObjectRequestBody(
            trigger_type_id=1000,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**actions:** `typing.Sequence[ActionObjectRequestBody]` — An array of actions.
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `bool` — Whether the alert is enabled or not.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The custom name of the configuration.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `ScopeObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Sequence[WorkflowTriggerObjectRequestBody]` — An array of triggers.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**operational_settings:** `typing.Optional[OperationalSettingsObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.alerts.<a href="src/samsara/v_20250611/alerts/client.py">delete_configurations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.alerts.delete_configurations(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unqiue Samsara id of the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.alerts.<a href="src/samsara/v_20250611/alerts/client.py">patch_configurations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an alert configuration.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.alerts.patch_configurations(
    id="e1c5dffc-c7b7-47b0-a778-6a65de638abf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unqiue Samsara id of the alert configuration.
    
</dd>
</dl>

<dl>
<dd>

**actions:** `typing.Optional[typing.Sequence[ActionObjectRequestBody]]` — An array of actions.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[bool]` — Whether the alert is enabled or not.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The custom name of the configuration.
    
</dd>
</dl>

<dl>
<dd>

**operational_settings:** `typing.Optional[OperationalSettingsObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[ScopeObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Optional[typing.Sequence[WorkflowTriggerObjectRequestBody]]` — An array of triggers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.alerts.<a href="src/samsara/v_20250611/alerts/client.py">get_incidents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Alert Incidents for specific Alert Configurations over a specified period of time.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Alerts** under the Alerts category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.alerts.get_incidents(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp that indicates when to begin receiving data. This will be based on updatedAtTime.
    
</dd>
</dl>

<dl>
<dd>

**configuration_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Required array of alert configuration ids to return incident data for.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not provided. This will be based on updatedAtTime.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assets
<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all assets. Up to 300 assets will be returned per page.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.v_20250611.assets.list(
    type="uncategorized",
    after="after",
    updated_after_time="updatedAfterTime",
    include_external_ids=True,
    include_tags=True,
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    attribute_value_ids="attributeValueIds",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[AssetsListRequestType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` —  A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[bool]` — Optional boolean indicating whether to return tags on supported entities
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of asset IDs and External IDs.
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data to return entities within given range query (only for numeric attributes) separated by a comma. Only entities meeting all the conditions will be returned. At least one bound must be provided. Example: `attributes=Length:range(8,)&attributes=Length:range(10,20)`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">create_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.create_asset()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the asset.
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — The OEM/manufacturer of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The model of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**readings_ingestion_enabled:** `typing.Optional[bool]` — Indicates whether the asset is expected to have data ingested using the Readings API.
    
</dd>
</dl>

<dl>
<dd>

**regulation_mode:** `typing.Optional[AssetsCreateAssetRequestBodyRegulationMode]` — Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[str]` — The serial number of the asset. This can be an internal serial number or used to hold legacy VIN/PIN numbers such as ones of shorter lengths.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AssetsCreateAssetRequestBodyType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The unique 17-digit VIN (Vehicle Identification Number) or PIN (Product Identification Number) of the asset.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — The model year of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">delete_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.delete_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A filter selecting a single asset by id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">update_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.update_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A filter selecting a single asset by id.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the asset.
    
</dd>
</dl>

<dl>
<dd>

**make:** `typing.Optional[str]` — The OEM/manufacturer of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The model of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the asset. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**readings_ingestion_enabled:** `typing.Optional[bool]` — Indicates whether the asset is expected to have data ingested using the Readings API.
    
</dd>
</dl>

<dl>
<dd>

**regulation_mode:** `typing.Optional[AssetsUpdateAssetRequestBodyRegulationMode]` — Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use unregulated asset. Primarily used with vehicles.  Valid values: `mixed`, `regulated`, `unregulated`
    
</dd>
</dl>

<dl>
<dd>

**serial_number:** `typing.Optional[str]` — The serial number of the asset. This can be an internal serial number or used to hold legacy VIN/PIN numbers such as ones of shorter lengths.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AssetsUpdateAssetRequestBodyType]` — The operational context in which the asset interacts with the Samsara system. Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer, flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg: container, dumpster...), or Uncategorized.  Valid values: `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The unique 17-digit VIN (Vehicle Identification Number) or PIN (Product Identification Number) of the asset.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[int]` — The model year of the asset. Updates to this field are restricted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">v_1_get_all_asset_current_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch current locations of all assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.v_1_get_all_asset_current_locations(
    starting_after="startingAfter",
    ending_before="endingBefore",
    limit=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">v_1_get_assets_reefers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetches all reefers and reefer-specific stats. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.v_1_get_assets_reefers(
    start_ms=1000000,
    end_ms=1000000,
    starting_after="startingAfter",
    ending_before="endingBefore",
    limit=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">v_1_get_asset_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

List historical locations for a given asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.v_1_get_asset_location(
    asset_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `int` — ID of the asset. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">v_1_get_asset_reefer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the reefer-specific stats of an asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.v_1_get_asset_reefer(
    asset_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `int` — ID of the asset. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.assets.<a href="src/samsara/v_20250611/assets/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.assets.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beta APIs
<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_assets_inputs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return data collected from the inputs of your organization's assets based on the time parameters passed in. Results are paginated. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. The endpoint will only return data up until the endTime that has been processed by the server at the time of the original request. You will need to request the same [startTime, endTime) range again to receive data for assets processed after the original request time. This endpoint sorts data by time ascending.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assets** under the Assets category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_assets_inputs(
    type="auxInput1",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `GetAssetsInputsRequestType` — Input stat type to query for.  Valid values: `auxInput1`, `auxInput2`, `auxInput3`, `auxInput4`, `auxInput5`, `auxInput6`, `auxInput7`, `auxInput8`, `auxInput9`, `auxInput10`, `auxInput11`, `auxInput12`, `auxInput13`, `analogInput1Voltage`, `analogInput2Voltage`, `analogInput1Current`, `analogInput2Current`, `batteryVoltage`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Limited to 100 ID's for each request.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to never if not provided; if not provided then pagination will not cease, and a valid pagination cursor will always be returned. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_tags:** `typing.Optional[bool]` — Optional boolean indicating whether to return tags on supported entities
    
</dd>
</dl>

<dl>
<dd>

**include_attributes:** `typing.Optional[bool]` — Optional boolean indicating whether to return attributes on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_aemp_equipment_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of equipment following the AEMP ISO 15143-3 standard.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read AEMP** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_aemp_equipment_list(
    page_number="pageNumber",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_number:** `str` — The number corresponding to a specific page of paginated results, defaulting to the first page if not provided. The default page size is 100 records.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_driver_efficiency</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all driver and associated vehicle efficiency data. 

 This is a legacy endpoint, consider using this endpoint [/driver-efficiency/drivers](https://developers.samsara.com/reference/getdriverefficiencybydrivers) instead. The endpoint will continue to function as documented. 

 <b>Rate limit:</b> 50 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_driver_efficiency(
    driver_activation_status="active",
    after="after",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[GetDriverEfficiencyRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Cannot be used with tag filtering or driver status. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters summary to drivers based on this comma-separated list of tag IDs. Data from all the drivers' respective vehicles will be included in the summary, regardless of which tag the vehicle is associated with. Should not be provided in addition to `driverIds`. Example: driverTagIds=1234,5678
    
</dd>
</dl>

<dl>
<dd>

**driver_parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filters like `driverTagIds` but includes descendants of all the given parent tags. Should not be provided in addition to `driverIds`. Example: `driverParentTagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` 

A start time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `startTime` is 2020-03-17T12:06:19Z then the results will include data starting from 2020-03-17T12:00:00Z. The provided start time cannot be in the future. Start time can be at most 31 days before the end time. If the start time is within the last hour, the results will be empty. Default: 24 hours prior to endTime.

Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` 

An end time in RFC 3339 format. The results will be truncated to the hour mark for the provided time. For example, if `endTime` is 2020-03-17T12:06:19Z then the results will include data up until 2020-03-17T12:00:00Z. The provided end time cannot be in the future. End time can be at most 31 days after the start time. Default: The current time truncated to the hour mark.

Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">patch_equipment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an equipment.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.patch_equipment(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTiny]]` — List of attributes associated with the entity
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — When you provide a manual engine hours override, Samsara will begin updating a equipment's engine hours used since this override was set.
    
</dd>
</dl>

<dl>
<dd>

**equipment_serial_number:** `typing.Optional[str]` — The serial number of the equipment.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**equipment_patch_equipment_request_body_id:** `typing.Optional[str]` — The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Equipment. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Equipment. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — When you provide a manual odometer override, Samsara will begin updating a equipment's odometer using GPS distance traveled since this override was set.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this equipment. If your access to the API is scoped by one or more tags, this field is required to pass in. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_hos_eld_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all HOS ELD events in a time range, grouped by driver. Attributes will be populated depending on which ELD Event Type is being returned.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_hos_eld_events(
    start_time="startTime",
    end_time="endTime",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    driver_activation_status="active",
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[GetHosEldEventsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 25 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_trailer_stats_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats of all trailers at the given `time`. If no `time` is specified, the current time is used.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_trailer_stats_snapshot(
    types="types",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
    trailer_ids="trailerIds",
    time="time",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` —  A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 Format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_trailer_stats_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a feed of trailer stats.

The first call to this endpoint will provide the most recent stats for each trailer and an `endCursor`.

Providing the `endCursor` value to the `after` query parameter will fetch all updates since the previous API call.

If `hasNextPage` is false, no new data is immediately available. Please wait a minimum of 5 seconds before making a subsequent request.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_trailer_stats_feed(
    types="types",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
    trailer_ids="trailerIds",
    decorations="decorations",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[str]` 

Decorations add to the primary stats listed in the `types` parameter. For example, if you wish to know the trailer's location whenever the odometer updates, you may set `types=gpsOdometerMeters&decorations=gps`.

You may list **up to 2** types using comma-separated format. If multiple stats are listed in the types parameter, the decorations will be added to each type. For example: `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps` will list GPS decorations for each reeferStateZone1 reading, each reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

Note that decorations may significantly increase the response payload size.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_trailer_stats_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns trailer stats during the given time range for all trailers. This can be optionally filtered by tags or specific trailer IDs.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailer Statistics** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_trailer_stats_history(
    start_time="startTime",
    end_time="endTime",
    types="types",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
    trailer_ids="trailerIds",
    decorations="decorations",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**types:** `str` 

The stat types you want this endpoint to return information on.

You may list **up to 3** types using comma-separated format. For example: `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of trailer IDs and externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[str]` 

Decorations add to the primary stats listed in the `types` parameter. For example, if you wish to know the trailer's location whenever the odometer updates, you may set `types=gpsOdometerMeters&decorations=gps`.

You may list **up to 2** types using comma-separated format. If multiple stats are listed in the types parameter, the decorations will be added to each type. For example: `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps` will list GPS decorations for each reeferStateZone1 reading, each reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

Note that decorations may significantly increase the response payload size.

* `gps`: GPS data including lat/long, heading, speed, and a reverse geocode address.
* `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint or through the [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading). Odometer readings wthat are manually set will update as GPS trip data is gathered.
* `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of the reefer in millidegree Celsius.
* `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run according to onboard diagnostics. Only supported on reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air temperature zone 1 in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferFuelPercent`: The fuel level of the reefer unit in percentage points (e.g. `99`, `50`, etc). Only supported on reefer solutions.
* `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only supported on multizone Carrier reefer solutions.
* `reeferStateZone1`: The state of the reefer in zone 1. For single zone reefers, this applies tot he single zone. Only supported on multizone reefer solutions.
* `reeferStateZone2`: The state of the reefer in zone 2. Only supported on multizone reefer solutions.
* `reeferStateZone3`: The state of the reefer in zone 3. Only supported on multizone reefer solutions.
* `reeferRunMode`: The operational mode of the reefer (`Start/Stop`, `Continuous`)
* `reeferAlarms`: Any alarms that are present on the reefer. Only supported on reefer solutions.
* `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of the reefer in millidegrees Celsius. For single zone reefers, this applies to the single zone. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of the reefer in millidegrees Celsius. Only supported on multizone reefer solutions.
* `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single zone reefers, this applies to the single zone.
* `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only supported on multizone reefer solutions.
* `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only supported on multizone reefer solutions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">update_engine_immobilizer_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the engine immobilizer state of a vehicle. This requires an engine immobilizer to be installed on the vehicle gateway.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Vehicle Immobilization** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import (
    UpdateEngineImmobilizerRelayStateRequestBodyRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.update_engine_immobilizer_state(
    id=1000000,
    relay_states=[
        UpdateEngineImmobilizerRelayStateRequestBodyRequestBody(
            id="relay1",
            is_open=True,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — Vehicle ID
    
</dd>
</dl>

<dl>
<dd>

**relay_states:** `typing.Sequence[UpdateEngineImmobilizerRelayStateRequestBodyRequestBody]` — A list of relay states. If a relay is omitted, its state won't be updated. If the list is empty, a 400 bad request status code will be returned. If there are multiple states for the same relay, a 400 bad request status code will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches jobs based on id/uuid or provided filters.

To use this endpoint, select **Read Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_jobs(
    id="id",
    start_date="startDate",
    end_date="endDate",
    status="active",
    customer_name="customerName",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` —  A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` —  An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**industrial_asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — IndustrialAssetId in STRING format. (Example: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`).
    
</dd>
</dl>

<dl>
<dd>

**fleet_device_ids:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — FleetDeviceId in INTEGER format. (Example: `123456`).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetJobsRequestStatus]` — A job status in STRING format. Job statuses can be one of three (ignores case): `"active", "scheduled", "completed"`  Valid values: `active`, `scheduled`, `completed`
    
</dd>
</dl>

<dl>
<dd>

**customer_name:** `typing.Optional[str]` — Customer name to filter by
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">create_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new job and returns it.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import PostJobObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.create_job(
    job=PostJobObjectRequestBody(
        end_date="2019-06-13T19:08:25Z",
        id="8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
        name="My Job Name",
        start_date="2019-06-13T19:08:25Z",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job:** `PostJobObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">delete_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing job.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.delete_job(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">patch_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing job and returns it.

To use this endpoint, select **Write Jobs** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import PatchJobObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.patch_job(
    id="id",
    job=PatchJobObjectRequestBody(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    
</dd>
</dl>

<dl>
<dd>

**job:** `PatchJobObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**keep_history:** `typing.Optional[bool]` — Defaults to true if user does not want to overwrite entire history for an active job (irrelevant for scheduled/completed jobs)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_detections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return all detections detected by in-vehicle assets and associated metadata. To get core endpoint data, select View Safety Detection Log under the Safety & Cameras category when creating or editing an API token.

If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Detection Log** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_detections(
    inbox_event=True,
    in_cab_alert_played=True,
    include_asset=True,
    include_driver=True,
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime`. (Example: 2024-04-16T19:08:25Z)
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated driver IDs. If driver ID is present, events for the specified driver(s) will be returned. Max for this value is 2000 objects. (Example: 281474982859091,281471982957527)
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated asset IDs. If asset ID is present, events for the specified asset(s) will be returned. Max for this value is 2000 objects. (Example: 281474982859091,281471982957527)
    
</dd>
</dl>

<dl>
<dd>

**detection_behavior_labels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated labels to filter behavior labels. Uses OR semantics for filtering. An empty list allows all values. Valid values: `acceleration`, `braking`, `crash`, `drowsy`, `eatingDrinking`, `edgeRailroadCrossingViolation`, `followingDistance`, `forwardCollisionWarning`, `genericDistraction`, `harshTurn`, `laneDeparture`, `maxSpeed`, `mobileUsage`, `noSeatbelt`, `obstructedCamera`, `passenger`, `policyViolationMask`, `rollingStop`, `rolloverProtection`, `smoking`, `speeding`, `unsafeParking`, `vulnerableRoadUserCollisionWarning`, `yawControl`. (Example: rollingStop,obstructedCamera,noSeatbelt)
    
</dd>
</dl>

<dl>
<dd>

**inbox_filter_reason:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated reasons to filter detections. Uses OR semantics for filtering. An empty list allows all values. Valid values: `overDailyLimit`, `overHourlyLimit`, `overTripLimit`, `belowConfidenceThreshold`, `belowSeverityThreshold`, `overEventRateLimit`, `geofenceFilter`, `belowNudgeThreshold`, `belowSpeedThreshold`, `nighttimeFilter`, `speedingFilter`, `unknown`. (Example: overDailyLimit,overHourlyLimit,belowConfidenceThreshold)
    
</dd>
</dl>

<dl>
<dd>

**inbox_event:** `typing.Optional[bool]` — Indicates whether or not to return detections with an associated Safety Inbox event. An empty entry allows all values. (Example: true)
    
</dd>
</dl>

<dl>
<dd>

**in_cab_alert_played:** `typing.Optional[bool]` — Indicates whether or not to return detections where in-cab alert played. An empty entry allows all values. (Example: true)
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — An optional filter on the data based on this comma-separated list of tag IDs. The filtering is OR inclusive for asset and driver tags. (Example: 1234,5678)
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded data for asset objects. (Example: true)
    
</dd>
</dl>

<dl>
<dd>

**include_driver:** `typing.Optional[bool]` — Indicates whether or not to return expanded data for driver objects. (Example: true)
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes. If endTime is set the same as startTime, the most recent data point before that time will be returned per asset. Value is compared against `updatedAtTime`. (Example: 2024-04-23T19:08:25Z)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_devices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all installed cameras (CM3x), vehicle gateways (VGs), and asset gateways (AGs) and their health information within an organization. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Devices API enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Devices** under the Devices category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_devices(
    include_health=True,
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**models:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated device models. Valid values: `CM31`, `CM32`, `CM33`, `CM34`, `VG34`, `VG34M`, `VG34EU`, `VG34FN`, `VG54NA`, `VG54EU`, `VG55NA`, `VG55EU`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`, `AG52`, `AG52EU`, `AG53`, `AG53EU`
    
</dd>
</dl>

<dl>
<dd>

**health_statuses:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated device health statuses. Valid values: `healthy`, `needsAttention`, `needsReplacement`, `dataPending`.
    
</dd>
</dl>

<dl>
<dd>

**include_health:** `typing.Optional[bool]` — Optional boolean to control whether device health information is returned in the response. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 100 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_driver_trailer_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currently active driver-trailer assignments for driver.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_driver_trailer_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">create_driver_trailer_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new driver-trailer assignment

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.create_driver_trailer_assignment(
    driver_id="494123",
    trailer_id="12345",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**trailer_id:** `str` — ID of the trailer. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — The start time in RFC 3339 format. The time needs to be current or within the past 7 days. Defaults to now if not provided
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">update_driver_trailer_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing driver-trailer assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.update_driver_trailer_assignment(
    id="id",
    end_time="2019-06-13T19:08:25Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara ID for the assignment.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — The end time in RFC 3339 format. The end time should not be in the future
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_engine_immobilizer_states</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the engine immobilizer states of the queried vehicles. If a vehicle has never had an engine immobilizer connected, there won't be any state returned for that vehicle.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicle Immobilization** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_engine_immobilizer_states(
    vehicle_ids="vehicleIds",
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_ids:** `str` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">start_function_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start an asynchronous run for the specified Function. This endpoint allows you to override parameters available at runtime.

 <b>Rate limit:</b> 2 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Functions** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611.beta_ap_is import (
    FunctionsStartFunctionRunRequestBodyParamsOverride,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.start_function_run(
    name="name",
    params_override=FunctionsStartFunctionRunRequestBodyParamsOverride(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the Function to run.
    
</dd>
</dl>

<dl>
<dd>

**params_override:** `FunctionsStartFunctionRunRequestBodyParamsOverride` — Parameter overrides for the Function execution. Can be an empty object but must be provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">update_shipping_docs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the shippingDocs field of an existing assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.update_shipping_docs(
    hos_date="hosDate",
    driver_id="driverID",
    shipping_docs="ShippingID1, ShippingID2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hos_date:** `str` — A start date in yyyy-mm-dd format. Required.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `str` — ID of the driver for whom the duty status is being set.
    
</dd>
</dl>

<dl>
<dd>

**shipping_docs:** `str` — ShippingDocs associated with the driver for the day.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">create_plan_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one or more orders (bulk upsert). Pass an array of order objects; any object whose customerOrderId already exists will be updated, otherwise a new order is created. Functions can return JSON arrays in this Order POST format. Orders are initially created at the plan level but will migrate to hub-level entities, with planId becoming optional in future versions.

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have RoutePlanning APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import OrderInputObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.create_plan_orders(
    data=[
        OrderInputObjectRequestBody(
            customer_order_id="ORDER-2024-001",
            hub_id="550e8400-e29b-41d4-a716-446655440000",
            plan_id="650e8400-e29b-41d4-a716-446655440023",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[OrderInputObjectRequestBody]` — An array of order objects to be created or updated
    
</dd>
</dl>

<dl>
<dd>

**enable_update_existing_orders:** `typing.Optional[bool]` — Enable update of existing orders if an order with the same customerOrderId exists. The input must match the same quantity dimensions as the existing order. If not provided, requests will fail if an order's customerOrderId already exists.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_qualification_records</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns qualification records for the specified list of IDs.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_qualification_records()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 qualification record IDs to filter on. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a query parameter, use the following format: key:value.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — If true, externalIds for qualification record and for the owner entity are returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">post_qualification_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new qualification record.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara
from samsara.v_20250611 import (
    QualificationOwnerRequestObjectRequestBody,
    QualificationRecordRequestFieldInputObjectRequestBody,
    QualificationTypeRequestObjectRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.post_qualification_record(
    fields=[
        QualificationRecordRequestFieldInputObjectRequestBody(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            type="number",
        )
    ],
    issue_date=datetime.datetime.fromisoformat(
        "2025-08-27 10:20:30+00:00",
    ),
    owner=QualificationOwnerRequestObjectRequestBody(
        entity_type="worker",
        id="281474",
    ),
    qualification_type=QualificationTypeRequestObjectRequestBody(
        id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_date:** `dt.datetime` — Issue/effective date. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `QualificationOwnerRequestObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**qualification_type:** `QualificationTypeRequestObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[dt.datetime]` — Expiration date. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[
    typing.Sequence[QualificationRecordRequestFieldInputObjectRequestBody]
]` — Other custom fields in a qualification record.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">delete_qualification_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing qualification record.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.delete_qualification_record(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the qualification record to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">patch_qualification_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing qualification record.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara
from samsara.v_20250611 import QualificationOwnerRequestObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.patch_qualification_record(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    issue_date=datetime.datetime.fromisoformat(
        "2025-08-27 10:20:30+00:00",
    ),
    owner=QualificationOwnerRequestObjectRequestBody(
        entity_type="worker",
        id="281474",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the qualification record to update.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[dt.datetime]` — Expiration date. UTC timestamp in RFC 3339 format. Set to '1970-01-01T00:00:00Z' to clear existing expiration date.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[
    typing.Sequence[QualificationRecordRequestFieldInputObjectRequestBody]
]` — Other custom fields in a qualification record. Only set fields that needs to be updated.
    
</dd>
</dl>

<dl>
<dd>

**issue_date:** `typing.Optional[dt.datetime]` — Issue/effective date. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[QualificationOwnerRequestObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">archive_qualification_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archives an existing qualification record.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.archive_qualification_record(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the qualification record to archive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_qualification_records_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all qualification records that have been created or modified for your organization based on the time parameters passed in. Results are paginated and sorted by last modified time. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_qualification_records_stream(
    entity_type="worker",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    include_deleted=True,
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `GetQualificationRecordsStreamRequestEntityType` — String of entity type.  Valid values: `worker`, `asset`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `dt.datetime` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. Examples: '2019-06-13T19:08:25Z' (basic UTC), '2019-06-13T19:08:25.455Z' (with milliseconds), '2015-09-15T14:00:12-04:00' (with timezone).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — An end time in RFC 3339 format. Optional and defaults to now if not provided. Millisecond precision and timezones are supported. Examples: '2019-06-13T19:08:25Z' (basic UTC), '2019-06-13T19:08:25.455Z' (with milliseconds), '2015-09-15T14:00:12-04:00' (with timezone).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**qualification_type_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional comma-separated list containing up to 100 qualification type IDs to filter on.
    
</dd>
</dl>

<dl>
<dd>

**owner_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional comma-separated list of unique Samsara IDs of workers (if "entityType" is "worker") or assets (if "entityType" is "asset") to filter on. Max value for this field is 100 objects.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted:** `typing.Optional[bool]` — If true, deleted qualification records are returned.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — If true, externalIds for qualification record and for the owner entity are returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">unarchive_qualification_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unarchives an existing qualification record.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.unarchive_qualification_record(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the qualification record to unarchive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_qualification_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of qualification types for the specified list of IDs. If no IDs are provided, all qualification types will be returned.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Qualification Records** under the Qualification Records category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_qualification_types(
    entity_type="worker",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `GetQualificationTypesRequestEntityType` — String of entity type.  Valid values: `worker`, `asset`
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional comma-separated list containing up to 100 qualification type IDs to filter on. If no IDs are provided, all qualification types will be returned.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">post_readings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingest new readings. This endpoint allows the ingestion of batches of readings.

Ingesting readings is only supported for assets created using the POST /assets API endpoint with readingsIngestionEnabled set to true. To see a full list of readings available for ingestion use the GET readings definitions API. When ingesting location data, the readingID 'location' must be used and the value object must contain at least the following fields: 'speed', 'latitude', 'longitude'.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Readings** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import ReadingDatapointRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.post_readings(
    data=[
        ReadingDatapointRequestBody(
            entity_id="123451234512345",
            happened_at_time="2023-10-27T10:00:00Z",
            reading_id="airInletPressure",
            value={"key": "value"},
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[ReadingDatapointRequestBody]` — An array of readings data points to create.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">list_readings_definitions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An introspection endpoint for discovering the set of readings including their name, description, data type, unit, and other metadata.
	Examples:
	Diagnostic/Engine Readings: engineState, engineSpeed, fuelLevelPerc etc.
	Level Monitoring Readings: defLevel, defLevelMilliPercent etc.
	Smart Trailer Readings: reeferState  etc.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Readings** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.list_readings_definitions(
    after="after",
    ids="ids",
    entity_types="entityTypes",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — A String of comma separated reading IDs. Include up to 50 readings IDs. If not set, all readings are returned.
    
</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[str]` — A list of entity type to return readings for. (Examples: asset, sensor)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_readings_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the values of a reading for a set of entities within the specified time range. Returns a paginated response with data for the specified resource IDs where startTime <= happenedAtTime < endTime. End time of null implies endTime is infinite and all known readings are returned.
	Example:
	engineRpm Readings for entityId 212014918105584 between time 2025-01-27T19:22:30Z and 2025-01-27T19:25:00Z
	"data": [
    {
      "entityId": "212014918105584",
      "value": 807,
      "happenedAtTime": "2025-01-27T19:22:30Z"
    },
    {
      "entityId": "212014918105584",
      "value": 811,
      "happenedAtTime": "2025-01-27T19:24:30Z"
    }
  ],

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Readings** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_readings_history(
    after="after",
    reading_id="readingId",
    entity_ids="entityIds",
    entity_type="entityType",
    external_ids="externalIds",
    start_time="startTime",
    end_time="endTime",
    feed=True,
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reading_id:** `str` — The reading ID to retrieve data for. Use /readings/definitions endpoint to get a list of valid reading IDs. (Examples: engineRpm,fuelLevel)
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `str` — A entity type of the entityIds or externalIds to fetch readings for. Use /readings/definitions endpoint to get a list of valid entity types. (Examples: asset, sensor)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of entity IDs or external IDs. If not set, all entities are returned.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of external IDs.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps greater than or equal to this value. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2020-01-27T07:06:25Z)
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. If not set, the time of the request is considered the endTime. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2020-01-27T07:06:25Z)
    
</dd>
</dl>

<dl>
<dd>

**feed:** `typing.Optional[bool]` — Set to true to enable feed mode for continuous reading updates. When enabled, the API always includes an endCursor in the response. If hasNextPage is false, it indicates that no new data is currently available — wait at least 5 seconds before making the next request to avoid unnecessary polling.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_readings_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

An endpoint to get the last value of a reading for a set of entities at the specified time.
	Example:
	engineRpm Readings for entityId 212014918105584 at time 2025-04-16T20:49:19Z
	"data": [
    {
      "readingId": "engineRpm",
      "entityId": "212014918105584",
      "value": 600,
      "happenedAtTime": "2025-04-16T20:49:19Z"
    }
  ],

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Readings** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_readings_snapshot(
    after="after",
    reading_ids="readingIds",
    entity_ids="entityIds",
    external_ids="externalIds",
    as_of_time="asOfTime",
    entity_type="entityType",
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reading_ids:** `str` — A collection of comma separated reading IDs. Include up to 3 readings IDs. Use /readings/definitions endpoint to get a list of valid reading IDs. (Examples: engineRpm,fuelLevel)
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `str` — A entity type of the entityIds or externalIds to fetch readings for. Use /readings/definitions endpoint to get a list of valid entity types. (Examples: asset, sensor)
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of entity IDs or external IDs. If not set, all entities are returned.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of external IDs.
    
</dd>
</dl>

<dl>
<dd>

**as_of_time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2020-01-27T07:06:25Z)
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_safety_events_v_2</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return details for the specified safety events based on the parameters passed in. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_safety_events_v_2()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**safety_event_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Required string of comma separated Safety Event IDs. Unique Samsara IDs (uuid) of the safety event.
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**include_driver:** `typing.Optional[bool]` — Indicates whether or not to return expanded “driver” data
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_safety_events_v_2_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return all safety events associated with your organization based on the parameters passed in. To get core endpoint data, select Read Safety Events & Scores under the Safety & Cameras category when creating or editing an API token. Read Camera Media permissions required to get Safety Event video media via this endpoint. If you include an endTime, the endpoint will return data up until that point. If you do not include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_safety_events_v_2_stream(
    start_time="startTime",
    end_time="endTime",
    include_asset=True,
    include_driver=True,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime` of the events.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — RFC 3339 timestamp which is compared against `updatedAtTime` of the events. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated asset IDs. If asset ID is present, events for the specified asset(s) will be returned. Limit of 2000 asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated driver IDs. If driver ID is present, events for the specified driver(s) will be returned. Limit of 2000 driver IDs.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated tag IDs. If tag ID is present, events for the specified tag(s) will be returned. Limit of 2000 tag IDs.
    
</dd>
</dl>

<dl>
<dd>

**assigned_coaches:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated coach IDs to filter events assigned to a particular coach. Limit of 2000 coach IDs.
    
</dd>
</dl>

<dl>
<dd>

**behavior_labels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated labels to filter behavior labels.  Valid values: `Acceleration`, `AggressiveDriving`, `BluetoothHeadset`, `Braking`, `ContextConstructionOrWorkZone`, `ContextSnowyOrIcy`, `ContextVulnerableRoadUser`, `ContextWet`, `Crash`, `DefensiveDriving`, `DidNotYield`, `Drinking`, `Drowsy`, `Eating`, `EatingDrinking`, `EdgeDistractedDriving`, `EdgeRailroadCrossingViolation`, `FollowingDistance`, `FollowingDistanceModerate`, `FollowingDistanceSevere`, `ForwardCollisionWarning`, `GenericDistraction`, `GenericTailgating`, `HarshTurn`, `HeavySpeeding`, `HosViolation`, `Idling`, `Invalid`, `LaneDeparture`, `LateResponse`, `LeftTurn`, `LightSpeeding`, `MaxSpeed`, `MobileUsage`, `ModerateSpeeding`, `NearCollison`, `NearPedestrianCollision`, `NoSeatbelt`, `ObstructedCamera`, `OtherViolation`, `Passenger`, `PolicyViolationMask`, `ProtectiveEquipment`, `RanRedLight`, `Reversing`, `RollingStop`, `RolloverProtection`, `SevereSpeeding`, `Smoking`, `Speeding`, `UTurn`, `UnsafeManeuver`, `UnsafeParking`, `VulnerableRoadUserCollisionWarning`, `YawControl`
    
</dd>
</dl>

<dl>
<dd>

**event_states:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated values to filter event states.  Valid values: `needsReview`, `reviewed`, `needsCoaching`, `coached`, `dismissed`, `needsRecognition`, `recognized`
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**include_driver:** `typing.Optional[bool]` — Indicates whether or not to return expanded “driver” data
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_driver_safety_scores</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get safety scores and overall risk factors for drivers.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_driver_safety_scores(
    end_time="endTime",
    start_time="startTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of driver IDs to filter by. Include up to 100 IDs. Defaults to all drivers.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_driver_safety_score_trips</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get trips contributing to a driver's safety score, and risk factors in each trip.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_driver_safety_score_trips(
    end_time="endTime",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of driver IDs to fetch trip breakdowns for. Include up to 100 drivers.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_tag_group_safety_scores</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a combined safety score and risk factors for a set of tags.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_tag_group_safety_scores(
    end_time="endTime",
    start_time="startTime",
    score_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**score_type:** `GetTagGroupSafetyScoresRequestScoreType` — Whether to calculate tag score with either all drivers or all vehicles in the tag. Deactivated drivers and unassigned trips are not included when calculating scores for drivers.   Valid values: `driver`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of tag IDs to filter by. Include up to 100 IDs. Defaults to all tags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_tag_safety_scores</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get safety scores and overall risk factors for tags.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_tag_safety_scores(
    end_time="endTime",
    start_time="startTime",
    score_type="driver",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**score_type:** `GetTagSafetyScoresRequestScoreType` — Whether to calculate tag score with either all drivers or all vehicles in the tag. Deactivated drivers and unassigned trips are not included when calculating scores for drivers.   Valid values: `driver`, `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of tag IDs to filter by. Include up to 100 IDs. Defaults to all tags.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_vehicle_safety_scores</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get safety scores and overall risk factors for vehicles.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_vehicle_safety_scores(
    end_time="endTime",
    start_time="startTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of vehicle IDs to filter by. Include up to 100 IDs. Defaults to all vehicles.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_vehicle_safety_score_trips</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get trips contributing to a vehicle's safety score, and risk factors in each trip.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_vehicle_safety_score_trips(
    end_time="endTime",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — End time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — Start time in RFC 3339 format. Millisecond precision and timezones are supported. Includes trips that end after this timestamp. Can be up to 1 year before endTime.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of vehicle IDs to fetch trip breakdowns for. Include up to 100 vehicles.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">post_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create training assignments. Existing assignments will remain unchanged. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.post_training_assignments(
    course_id="courseId",
    due_at_time="dueAtTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**course_id:** `str` — String for the course ID.
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `str` — Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**learner_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">delete_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint supports batch deletion operations. The response does not indicate which specific deletions, if any, have failed. On a successful deletion or partial failure, a ‘204 No Content’ status is returned. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.delete_training_assignments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">patch_training_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update training assignments. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.patch_training_assignments(
    due_at_time="dueAtTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**due_at_time:** `str` — Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_training_assignments_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all training assignments data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don't include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. 

**Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_training_assignments_stream(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**learner_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`
    
</dd>
</dl>

<dl>
<dd>

**course_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated values. If status is present, training assignments for the specified status(s) will be returned. Valid values: "notStarted", "inProgress", "completed". Defaults to returning all courses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_training_courses</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all training courses data. Results are paginated. 
 Courses in the ‘draft’ status are excluded from the data returned by this endpoint.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Training Courses** under the Training Courses category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_training_courses(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**course_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**category_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated course category IDs. If courseCategoryId is present, training courses for the specified course category(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses.  Example: `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated values. If status is present, training courses with the specified status(s) will be returned. Valid values: “published”, “deleted”, “archived”. Defaults to returning all courses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.beta_ap_is.<a href="src/samsara/v_20250611/beta_ap_is/client.py">get_trips</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return trips that have been collected for your organization based on the time parameters passed in. Results are paginated. Reach out to your Samsara Representative to have this API enabled for your organization.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trips** under the Trips category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.beta_ap_is.get_trips(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter.
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**completion_status:** `typing.Optional[GetTripsRequestCompletionStatus]` — Filters trips based on a specific completion status  Valid values: `inProgress`, `completed`, `all`
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[GetTripsRequestQueryBy]` — Decide which timestamp the `startTime` and `endTime` are compared to.  Valid values: `updatedAtTime`, `tripStartTime`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Include up to 50 asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 LocationAndSpeed
<details><summary><code>client.v_20250611.location_and_speed.<a href="src/samsara/v_20250611/location_and_speed/client.py">get_location_and_speed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return asset locations and speed data that has been collected for your organization based on the time parameters passed in. Results are paginated. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call. The endpoint will only return data up until the endTime that has been processed by the server at the time of the original request. You will need to request the same [startTime, endTime) range again to receive data for assets processed after the original request time. This endpoint sorts the time-series data by device.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.location_and_speed.get_location_and_speed(
    after="after",
    limit=1,
    start_time="startTime",
    end_time="endTime",
    include_speed=True,
    include_reverse_geo=True,
    include_geofence_lookup=True,
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to never if not provided; if not provided then pagination will not cease, and a valid pagination cursor will always be returned. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**include_speed:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'speed' object
    
</dd>
</dl>

<dl>
<dd>

**include_reverse_geo:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'address' object
    
</dd>
</dl>

<dl>
<dd>

**include_geofence_lookup:** `typing.Optional[bool]` — Optional boolean indicating whether or not to return the 'geofence' object
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Attributes
<details><summary><code>client.v_20250611.attributes.<a href="src/samsara/v_20250611/attributes/client.py">get_attributes_by_entity_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all attributes in an organization associated with either drivers or assets. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.attributes.get_attributes_by_entity_type(
    entity_type="driver",
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_type:** `GetAttributesByEntityTypeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.attributes.<a href="src/samsara/v_20250611/attributes/client.py">create_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.attributes.create_attribute(
    attribute_type="single-select",
    entity_type="driver",
    name="License Certifications",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_type:** `CreateAttributeRequestAttributeType` — Denotes the data type of the attribute's values. Valid values: `single-select`, `multi-select`, `text`, `freeform-multi-select`.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `CreateAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name
    
</dd>
</dl>

<dl>
<dd>

**entities:** `typing.Optional[typing.Sequence[CreateAttributeRequestEntities]]` — Entities that will be applied to this attribute
    
</dd>
</dl>

<dl>
<dd>

**number_values:** `typing.Optional[typing.Sequence[float]]` — Number values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**string_values:** `typing.Optional[typing.Sequence[str]]` — String values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[CreateAttributeRequestUnit]` — Unit of the attribute (only for Number attributes).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.attributes.<a href="src/samsara/v_20250611/attributes/client.py">get_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.attributes.get_attribute(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `GetAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.attributes.<a href="src/samsara/v_20250611/attributes/client.py">delete_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an attribute by id, including all of its applications. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.attributes.delete_attribute(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `DeleteAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.attributes.<a href="src/samsara/v_20250611/attributes/client.py">update_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an attribute in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Attributes** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.attributes.update_attribute(
    id="id",
    entity_type="driver",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara-provided UUID of the attribute.
    
</dd>
</dl>

<dl>
<dd>

**entity_type:** `UpdateAttributeRequestEntityType` — Denotes the type of entity, driver or asset.
    
</dd>
</dl>

<dl>
<dd>

**attribute_type:** `typing.Optional[UpdateAttributeRequestAttributeType]` — Denotes the data type of the attribute's values. Valid values: `single-select`, `multi-select`, `text`, `freeform-multi-select`.
    
</dd>
</dl>

<dl>
<dd>

**entities:** `typing.Optional[typing.Sequence[CreateAttributeRequestEntities]]` — Entities that will be applied to this attribute
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**number_values:** `typing.Optional[typing.Sequence[float]]` — Number values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**string_values:** `typing.Optional[typing.Sequence[str]]` — String values that can be associated with this attribute
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Media
<details><summary><code>client.v_20250611.media.<a href="src/samsara/v_20250611/media/client.py">list_uploaded_media</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns a list of all uploaded media (video and still images) matching query parameters, with a maximum query range of one day. Additional media can be retrieved with the [Create a media retrieval request](https://developers.samsara.com/reference/postmediaretrieval) endpoint, and they will be included in the list after they are uploaded. Urls provided by this endpoint expire in 8 hours.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Media Retrieval** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.media.list_uploaded_media(
    vehicle_ids="vehicleIds",
    start_time="startTime",
    end_time="endTime",
    available_after_time="availableAfterTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_ids:** `str` — A filter on the data based on this comma-separated list of vehicle IDs and externalIds. You can specify up to 20 vehicles. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. End time cannot be more than 24 hours after startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Optional[
    typing.Union[
        ListUploadedMediaRequestInputsItem,
        typing.Sequence[ListUploadedMediaRequestInputsItem],
    ]
]` — An optional list of desired camera inputs for which to return captured media. If empty, media for all available inputs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**media_types:** `typing.Optional[
    typing.Union[
        ListUploadedMediaRequestMediaTypesItem,
        typing.Sequence[ListUploadedMediaRequestMediaTypesItem],
    ]
]` — An optional list of desired media types for which to return captured media. If empty, media for all available media types will be returned. Possible options include: image, videoHighRes.
    
</dd>
</dl>

<dl>
<dd>

**trigger_reasons:** `typing.Optional[
    typing.Union[
        ListUploadedMediaRequestTriggerReasonsItem,
        typing.Sequence[ListUploadedMediaRequestTriggerReasonsItem],
    ]
]` — An optional list of desired trigger reasons for which to return captured media. If empty, media for all available trigger reasons will be returned. Possible options include: api, panicButton, periodicStill, rfidEvent, safetyEvent, tripEndStill, tripStartStill, videoRetrieval. videoRetrieval represents media captured for a dashboard video retrieval request.
    
</dd>
</dl>

<dl>
<dd>

**available_after_time:** `typing.Optional[str]` — An optional timestamp in RFC 3339 format that can act as a cursor to track which media has previously been retrieved; only media whose availableAtTime comes after this parameter will be returned. Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.media.<a href="src/samsara/v_20250611/media/client.py">get_media_retrieval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint returns media information corresponding to a retrieval ID. Retrieval IDs are associated to prior [media retrieval requests](https://developers.samsara.com/reference/postmediaretrieval). Urls provided by this endpoint expire in 8 hours.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Media Retrieval** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.media.get_media_retrieval(
    retrieval_id="retrievalId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**retrieval_id:** `str` — Retrieval ID associated with this media capture request. Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.media.<a href="src/samsara/v_20250611/media/client.py">post_media_retrieval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint creates an asynchronous request to upload certain media from a device. The closest available media to the requested timestamp is returned. Images and high-res videos are supported; other types of media (e.g. hyperlapse, low-res) are planned to be supported in the future. Currently, only unblurred media is supported. If a device is offline, the requested media will be uploaded once it comes back online. Quota limits are enforced for media retrievals made through the API. The Create a media retrieval request response includes information about the media retrieval quota remaining for the organization. The media retrieval quota for the organization is reset at the beginning of each month.The quota is expressed using seconds of High Resolution video. 10 still images are equivalent to a 1 second of High Resolution footage.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Media Retrieval** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.media.post_media_retrieval(
    end_time="2019-06-13T19:08:55Z",
    inputs=[
        "dashcamRoadFacing",
        "dashcamRoadFacing",
        "dashcamRoadFacing",
        "dashcamRoadFacing",
    ],
    media_type="image",
    start_time="2019-06-13T19:08:25Z",
    vehicle_id="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. If endTime is the same as startTime, an image will be captured at startTime. Must be 1 second or more after startTime and no more than 60 seconds after startTime (Examples: 2019-06-13T19:08:55Z, 2019-06-13T19:08:55.455Z, OR 2015-09-15T14:00:42-04:00).
    
</dd>
</dl>

<dl>
<dd>

**inputs:** `typing.Sequence[MediaRetrievalPostMediaRetrievalRequestBodyInputsItem]` — A list of desired camera inputs for which to capture media. Only media with valid inputs (e.g. device has that input stream and device was recording at the time) will be uploaded. An empty list is invalid.
    
</dd>
</dl>

<dl>
<dd>

**media_type:** `MediaRetrievalPostMediaRetrievalRequestBodyMediaType` — The desired media type. If a video is requested, endTime must be after startTime. If an image is requested, endTime must be the same as startTime. Must be one of: image, videoHighRes. Examples: image, videoHighRes.  Valid values: `image`, `videoHighRes`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — Vehicle ID for which to initiate media capture. Examples: 1234
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Coaching
<details><summary><code>client.v_20250611.coaching.<a href="src/samsara/v_20250611/coaching/client.py">get_driver_coach_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return coach assignments for your organization based on the parameters passed in. Results are paginated.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.coaching.get_driver_coach_assignment(
    include_external_ids=True,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated IDs of the drivers. This can be either a unique Samsara driver ID or an external ID for the driver.
    
</dd>
</dl>

<dl>
<dd>

**coach_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated IDs of the coaches.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.coaching.<a href="src/samsara/v_20250611/coaching/client.py">put_driver_coach_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will update an existing or create a new coach-to-driver assignment for your organization based on the parameters passed in. This endpoint should only be used for existing Coach to Driver assignments. In order to remove a driver-coach-assignment for a given driver, set coachId to null

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.coaching.put_driver_coach_assignment(
    driver_id="driverId",
    coach_id="coachId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — Required string ID of the driver. This is a unique Samsara ID of a driver.
    
</dd>
</dl>

<dl>
<dd>

**coach_id:** `typing.Optional[str]` — Optional string ID of the coach. This is a unique Samsara user ID. If not provided, existing coach assignment will be removed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.coaching.<a href="src/samsara/v_20250611/coaching/client.py">get_coaching_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return coaching sessions for your organization based on the time parameters passed in. Results are paginated by sessions. If you include an endTime, the endpoint will return data up until that point. If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Coaching** under the Coaching category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.coaching.get_coaching_sessions(
    include_coachable_events=True,
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `dt.datetime` — Required RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated driver IDs. If driver ID is present, sessions for the specified driver(s) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**coach_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated user IDs. If coach ID is present, sessions for the specified coach(s) will be returned for either assignedCoach or completedCoach. If both driverId(s) and coachId(s) are present, sessions with specified driver(s) and coach(es) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**session_statuses:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma separated statuses. Valid values:  “upcoming”, “completed”, “deleted”.
    
</dd>
</dl>

<dl>
<dd>

**include_coachable_events:** `typing.Optional[bool]` — Optional boolean to control whether behaviors will include coachableEvents in the response. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes. If endTime is set the same as startTime, the most recent data point before that time will be returned per asset. Value is compared against `updatedAtTime`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.v_20250611.contacts.<a href="src/samsara/v_20250611/contacts/client.py">list_contacts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all contacts in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.contacts.list_contacts(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.contacts.<a href="src/samsara/v_20250611/contacts/client.py">create_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a contact to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.contacts.create_contact()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the contact.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.contacts.<a href="src/samsara/v_20250611/contacts/client.py">get_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific contact's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.contacts.get_contact(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.contacts.<a href="src/samsara/v_20250611/contacts/client.py">delete_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the given contact. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.contacts.delete_contact(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.contacts.<a href="src/samsara/v_20250611/contacts/client.py">update_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific contact's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Alert Contacts** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.contacts.update_contact(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the contact.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the contact.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name of the contact.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Maintenance
<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">get_defect_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get DVIR defect types.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defect Types** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.get_defect_types(
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of defect type IDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">stream_defects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream DVIR defects.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.stream_defects(
    after="after",
    limit=1,
    start_time="startTime",
    end_time="endTime",
    include_external_ids=True,
    is_resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 200 objects.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — Boolean value for whether filter defects by resolved status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">get_defect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single DVIR defect by ID.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.get_defect(
    id="id",
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique ID of the DVIR defect.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">get_dvirs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a history/feed of changed DVIRs by updatedAtTime between startTime and endTime parameters. In case of missing `endTime` parameter it will return a never ending stream of data.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.get_dvirs(
    after="after",
    limit=1,
    include_external_ids=True,
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at `startTime`.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 200 objects.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**safety_status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional list of safety statuses. Valid values: [safe, unsafe, resolved]
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">get_dvir</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single DVIR by ID.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.get_dvir(
    id="id",
    include_external_ids=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**include_external_ids:** `typing.Optional[bool]` — Optional boolean indicating whether to return external IDs on supported entities
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">update_dvir_defect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a given defect. Can be used to resolve a defect by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.update_dvir_defect(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the defect.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — Resolves the defect. Must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the defect.
    
</dd>
</dl>

<dl>
<dd>

**resolved_at_time:** `typing.Optional[str]` — Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**resolved_by:** `typing.Optional[ResolvedBy]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">create_dvir</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new mechanic DVIR in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.create_dvir(
    author_id="11",
    safety_status="safe",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**author_id:** `str` — Samsara user ID of the mechanic creating the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**safety_status:** `CreateDvirRequestSafetyStatus` — Whether or not this vehicle or trailer is safe to drive.
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of this vehicle.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Optional string if your jurisdiction requires a location of the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — The odometer reading in meters.
    
</dd>
</dl>

<dl>
<dd>

**resolved_defect_ids:** `typing.Optional[typing.Sequence[str]]` — Array of ids for defects being resolved with this DVIR.
    
</dd>
</dl>

<dl>
<dd>

**trailer_id:** `typing.Optional[str]` — Id of trailer being inspected. Either vehicleId or trailerId must be provided.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — Id of vehicle being inspected. Either vehicleId or trailerId must be provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">update_dvir</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves a given DVIR by marking its `isResolved` field to `true`. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.update_dvir(
    id="id",
    author_id="11",
    is_resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**author_id:** `str` — The user who is resolving the dvir.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `bool` — Resolves the DVIR. Must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**mechanic_notes:** `typing.Optional[str]` — The mechanics notes on the DVIR.
    
</dd>
</dl>

<dl>
<dd>

**signed_at_time:** `typing.Optional[str]` — Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.maintenance.<a href="src/samsara/v_20250611/maintenance/client.py">v_1_get_fleet_maintenance_list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get list of the vehicles with any engine faults or check light data. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.maintenance.v_1_get_fleet_maintenance_list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 FuelAndEnergy
<details><summary><code>client.v_20250611.fuel_and_energy.<a href="src/samsara/v_20250611/fuel_and_energy/client.py">get_driver_efficiency_by_drivers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return driver efficiency data that has been collected for your organization and grouped by drivers based on the time parameters passed in. Results are paginated. 

**Note:** The data from this endpoint comes from the Driver Efficiency (Eco-Driving) Report. The existing [/fleet/drivers/efficiency](https://developers.samsara.com/reference/getdriverefficiency) endpoint has now been moved to Legacy.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fuel_and_energy.get_driver_efficiency_by_drivers(
    start_time="startTime",
    end_time="endTime",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**data_formats:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.fuel_and_energy.<a href="src/samsara/v_20250611/fuel_and_energy/client.py">get_driver_efficiency_by_vehicles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return driver efficiency data that has been collected for your organization and grouped by vehicle drivers used based on the time parameters passed in. Results are paginated. 

**Note:** The data from this endpoint comes from the Driver Efficiency (Eco-Driving) Report. The existing [/fleet/drivers/efficiency](https://developers.samsara.com/reference/getdriverefficiency) endpoint has now been moved to Legacy.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver Efficiency** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fuel_and_energy.get_driver_efficiency_by_vehicles(
    start_time="startTime",
    end_time="endTime",
    vehicle_ids="vehicleIds",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day before endTime. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Must be in multiple of hours and no later than 3 hours before the current time. Timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**data_formats:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data formats you want to fetch. Valid values: `score`, `raw` and `percentage`. The default data format is `score`. Example: `dataFormats=raw,score`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.fuel_and_energy.<a href="src/samsara/v_20250611/fuel_and_energy/client.py">get_fuel_energy_driver_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get fuel and energy efficiency driver reports for the requested time range.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fuel_and_energy.get_fuel_energy_driver_reports(
    start_date="startDate",
    end_date="endDate",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `str` — A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.fuel_and_energy.<a href="src/samsara/v_20250611/fuel_and_energy/client.py">get_fuel_energy_vehicle_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get fuel and energy efficiency vehicle reports for the requested time range.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fuel_and_energy.get_fuel_energy_vehicle_reports(
    start_date="startDate",
    end_date="endDate",
    vehicle_ids="vehicleIds",
    energy_type="fuel",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `str` — A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `str` — An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**energy_type:** `typing.Optional[GetFuelEnergyVehicleReportsRequestEnergyType]` — The type of energy used by the vehicle.  Valid values: `fuel`, `hybrid`, `electric`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.fuel_and_energy.<a href="src/samsara/v_20250611/fuel_and_energy/client.py">post_fuel_purchase</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a fuel purchase transaction.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import PostFuelPurchaseRequestBodyPriceRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fuel_and_energy.post_fuel_purchase(
    fuel_quantity_liters="676.8",
    transaction_location="350 Rhode Island St, San Francisco, CA 94103",
    transaction_price=PostFuelPurchaseRequestBodyPriceRequestBody(
        amount="640.2",
        currency="usd",
    ),
    transaction_reference="5454534",
    transaction_time="2022-07-13T14:20:50.52-07:00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fuel_quantity_liters:** `str` — The amount of fuel purchased in liters.
    
</dd>
</dl>

<dl>
<dd>

**transaction_location:** `str` — The full street address for the location of the fuel transaction, as it might be recognized by Google Maps. Ideal entries should be in accordance with the format used by the national postal service of the country concerned (example: 1 De Haro St, San Francisco, CA 94107, United States). Alternatively, exact latitude/longitude can be provided (example: 40.748441, -73.985664).
    
</dd>
</dl>

<dl>
<dd>

**transaction_price:** `PostFuelPurchaseRequestBodyPriceRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_reference:** `str` — The fuel transaction reference. This is the transaction identifier. For instance, this can be the Serial Number on the invoice.
    
</dd>
</dl>

<dl>
<dd>

**transaction_time:** `str` — The time of the fuel transaction in RFC 3339 format. Timezone must be specified. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[PostFuelPurchaseRequestBodyDiscountRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[str]` — Samsara ID of the driver that purchased the fuel.
    
</dd>
</dl>

<dl>
<dd>

**fuel_grade:** `typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyFuelGrade]` — The grade of the fuel purchased.  Valid values: `Unknown`, `Regular`, `Premium`
    
</dd>
</dl>

<dl>
<dd>

**ifta_fuel_type:** `typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType]` — The type of fuel purchased supported by IFTA.  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**merchant_name:** `typing.Optional[str]` — Brand name of the fuel station the fuel was purchased at. For example: Shell, Bp, Exxon.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — The integration provider. For example: Customer, Shell Integration
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — Samsara ID of the vehicle that purchased the fuel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 DriverQrCodes
<details><summary><code>client.v_20250611.driver_qr_codes.<a href="src/samsara/v_20250611/driver_qr_codes/client.py">get_drivers_qr_codes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for requested driver(s) QR code, used for driver trip assignment.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_qr_codes.get_drivers_qr_codes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — String of comma separated driver IDs. List of driver - QR codes for specified driver(s) will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.driver_qr_codes.<a href="src/samsara/v_20250611/driver_qr_codes/client.py">create_driver_qr_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign a new QR code for the requested driver. Return error if an active QR code already exists.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_qr_codes.create_driver_qr_code(
    driver_id=494123,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Unique ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.driver_qr_codes.<a href="src/samsara/v_20250611/driver_qr_codes/client.py">delete_driver_qr_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke requested driver's currently active QR code.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_qr_codes.delete_driver_qr_code(
    driver_id=494123,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Unique ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Carrier Proposed Assignments
<details><summary><code>client.v_20250611.carrier_proposed_assignments.<a href="src/samsara/v_20250611/carrier_proposed_assignments/client.py">list_carrier_proposed_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Show the assignments created by the POST fleet/carrier-proposed-assignments. This endpoint will only show the assignments that are active for drivers and currently visible to them in the driver app. Once a proposed assignment has been accepted, the endpoint will not return any data. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.carrier_proposed_assignments.list_carrier_proposed_assignments(
    limit=1000000,
    after="after",
    active_time="activeTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**active_time:** `typing.Optional[str]` — If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.carrier_proposed_assignments.<a href="src/samsara/v_20250611/carrier_proposed_assignments/client.py">create_carrier_proposed_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new assignment that a driver can later use. Each driver can only have one future assignment. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.carrier_proposed_assignments.create_carrier_proposed_assignment(
    driver_id="42",
    vehicle_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**active_time:** `typing.Optional[str]` — Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    
</dd>
</dl>

<dl>
<dd>

**shipping_docs:** `typing.Optional[str]` — Shipping Documents that this assignment will propose to the driver.
    
</dd>
</dl>

<dl>
<dd>

**trailer_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)
    
</dd>
</dl>

<dl>
<dd>

**trailer_names:** `typing.Optional[typing.Sequence[str]]` — Names of trailers to propose. (forbidden if trailerIds is set)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.carrier_proposed_assignments.<a href="src/samsara/v_20250611/carrier_proposed_assignments/client.py">delete_carrier_proposed_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an assignment. You can only delete assignments that are not yet active. To override a currently active assignment, create a new empty one, instead. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.carrier_proposed_assignments.delete_carrier_proposed_assignment(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the assignment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Legacy APIs
<details><summary><code>client.v_20250611.legacy_ap_is.<a href="src/samsara/v_20250611/legacy_ap_is/client.py">get_dvir_defects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/streamdefects) instead. The endpoint will continue to function as documented.** 

Returns a list of DVIR defects in an organization, filtered by creation time. The maximum time period you can query for is 30 days. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Defects** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy_ap_is.get_dvir_defects(
    limit=1000000,
    after="after",
    start_time="startTime",
    end_time="endTime",
    is_resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). *The maximum time period you can query for is 30 days.*
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**is_resolved:** `typing.Optional[bool]` — A filter on the data based on resolution status. Example: `isResolved=true`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.legacy_ap_is.<a href="src/samsara/v_20250611/legacy_ap_is/client.py">get_drivers_vehicle_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments) instead. The endpoint will continue to function as documented.** Get all vehicle assignments for the requested drivers in the requested time range. The only type of assignment supported right now are assignments created through the driver app.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy_ap_is.get_drivers_vehicle_assignments(
    start_time="startTime",
    end_time="endTime",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    driver_activation_status="active",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[GetDriversVehicleAssignmentsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.legacy_ap_is.<a href="src/samsara/v_20250611/legacy_ap_is/client.py">get_dvir_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getdvirs) instead. The endpoint will continue to function as documented.** 

 Returns a list of all DVIRs in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read DVIRs** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy_ap_is.get_dvir_history(
    limit=1000000,
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.legacy_ap_is.<a href="src/samsara/v_20250611/legacy_ap_is/client.py">get_vehicle_idling_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getidlingevents) instead. The endpoint will continue to function as documented.** Get all vehicle idling reports for the requested time duration.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy_ap_is.get_vehicle_idling_reports(
    after="after",
    limit=1,
    start_time="startTime",
    end_time="endTime",
    vehicle_ids="vehicleIds",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    is_pto_active=True,
    min_idling_duration_minutes=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**is_pto_active:** `typing.Optional[bool]` — A filter on the data based on power take-off being active or inactive.
    
</dd>
</dl>

<dl>
<dd>

**min_idling_duration_minutes:** `typing.Optional[int]` — A filter on the data based on a minimum idling duration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.legacy_ap_is.<a href="src/samsara/v_20250611/legacy_ap_is/client.py">get_vehicles_driver_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments) instead. The endpoint will continue to function as documented.** Get all driver assignments for the requested vehicles in the requested time range. The only type of assignment supported right now are assignments created through the driver app.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy_ap_is.get_vehicles_driver_assignments(
    start_time="startTime",
    end_time="endTime",
    vehicle_ids="vehicleIds",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed startTime-endTime range is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">get_document_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the organization document types. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentTypesByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.get_document_types(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">get_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all documents for the given time range. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentsByOrgId).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.get_documents(
    start_time="startTime",
    end_time="endTime",
    after="after",
    document_type_id="documentTypeId",
    query_by="queryBy",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**document_type_id:** `typing.Optional[str]` — ID of the document template type.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[str]` — Query by document creation time (`created`) or updated time (`updated`). Defaults to `created`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">post_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/createDriverDocument).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.post_document(
    document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    driver_id="45646",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_type_id:** `str` — ID for the document type.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[FieldObjectPostRequestBody]]` — The fields associated with this document.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the document.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes on the document.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the route stop.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[DocumentsPostDocumentRequestBodyState]` — The condition of the document created for the driver. Can be either `required` or `submitted`, if no value is specified, `state` defaults to `required`. `required` documents are pre-populated documents for the Driver to fill out in the Driver App.  Valid values: `submitted`, `required`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">generate_document_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request creation of a document PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.generate_document_pdf(
    document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — ID of the document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">get_document_pdf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns generation job status and download URL for a PDF. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.get_document_pdf(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the pdf.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">get_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.get_document(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the document
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.documents.<a href="src/samsara/v_20250611/documents/client.py">delete_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single document. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/deleteDriverDocumentByIdAndDriverId).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Documents** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.documents.delete_document(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the document to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 DriverVehicleAssignments
<details><summary><code>client.v_20250611.driver_vehicle_assignments.<a href="src/samsara/v_20250611/driver_vehicle_assignments/client.py">get_driver_vehicle_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all driver-vehicle assignments for the requested drivers or vehicles in the requested time range. To fetch driver-vehicle assignments out of the vehicle trips' time ranges, assignmentType needs to be specified. Note: this endpoint replaces past endpoints to fetch assignments by driver or by vehicle. Visit [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints) for more information.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_vehicle_assignments.get_driver_vehicle_assignments(
    filter_by="drivers",
    start_time="startTime",
    end_time="endTime",
    driver_tag_ids="driverTagIds",
    vehicle_tag_ids="vehicleTagIds",
    after="after",
    assignment_type="HOS",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_by:** `GetDriverVehicleAssignmentsRequestFilterBy` — Option to filter by drivers or vehicles.  Valid values: `drivers`, `vehicles`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".
    
</dd>
</dl>

<dl>
<dd>

**driver_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**assignment_type:** `typing.Optional[GetDriverVehicleAssignmentsRequestAssignmentType]` — Specifies which assignment type to filter by.  Valid values: `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.driver_vehicle_assignments.<a href="src/samsara/v_20250611/driver_vehicle_assignments/client.py">create_driver_vehicle_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign vehicle drive-time to a driver via API. For a step-by-step instruction on how to leverage this endpoint, see [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_vehicle_assignments.create_driver_vehicle_assignment(
    driver_id="494123",
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` — The time at which the assignment was made in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing assignment) if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Is this driver a passenger? Defaults to false if not provided
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — The start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.driver_vehicle_assignments.<a href="src/samsara/v_20250611/driver_vehicle_assignments/client.py">delete_driver_vehicle_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete driver assignments that were created using the `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in the requested time range.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_vehicle_assignments.delete_driver_vehicle_assignments(
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` —  Assigned at time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Indicates if assigned driver is passenger
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.driver_vehicle_assignments.<a href="src/samsara/v_20250611/driver_vehicle_assignments/client.py">update_driver_vehicle_assignment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update driver assignments that were created using the `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time must match an existing assignment.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.driver_vehicle_assignments.update_driver_vehicle_assignment(
    driver_id="494123",
    start_time="2019-06-13T19:08:25Z",
    vehicle_id="281474978683353",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `str` — The start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `str` — ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**assigned_at_time:** `typing.Optional[str]` — The time at which the assignment was made in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The end time in RFC 3339 format. To make this an ongoing assignment (ie. an assignment with no end time), provide an endTime value of 'null'. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**is_passenger:** `typing.Optional[bool]` — Is this driver a passenger?
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Drivers
<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all drivers in organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.v_20250611.drivers.list(
    driver_activation_status="active",
    limit=1000000,
    after="after",
    updated_after_time="updatedAfterTime",
    created_after_time="createdAfterTime",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[DriversListRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data to return entities having given attributes using name-value pair or range query (only for numeric attributes), separated by semicolon. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributes=ExampleAttributeName:some_value&attributes=SomeOtherAttr:123&attributes=someNumericAttribute:range(10,20)`
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` — A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` — A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a driver to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.drivers.create(
    name="Susan Jones",
    password="aSecurePassword1234",
    username="SusanJones",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Driver's name.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Password that the driver can use to login to the Samsara driver app.
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` — Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[CreateDriverRequestAttributes]]` 
    
</dd>
</dl>

<dl>
<dd>

**carrier_settings:** `typing.Optional[DriverCarrierSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**current_id_card_code:** `typing.Optional[str]` — The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature.
    
</dd>
</dl>

<dl>
<dd>

**eld_adverse_weather_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Adverse Weather exemptions in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_big_day_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Big Day exemption in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_day_start_hour:** `typing.Optional[int]` — `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt:** `typing.Optional[bool]` — Flag indicating this driver is exempt from the Electronic Logging Mandate.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt_reason:** `typing.Optional[str]` — Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).
    
</dd>
</dl>

<dl>
<dd>

**eld_pc_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_ym_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Yard Move duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**has_driving_features_hidden:** `typing.Optional[DriverHasDrivingFeaturesHidden]` 
    
</dd>
</dl>

<dl>
<dd>

**has_vehicle_unpinning_enabled:** `typing.Optional[DriverHasVehicleUnpinningEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**hos_setting:** `typing.Optional[DriverHosSetting]` 
    
</dd>
</dl>

<dl>
<dd>

**license_number:** `typing.Optional[str]` — Driver's state issued license number. The combination of this number and `licenseState` must be unique.
    
</dd>
</dl>

<dl>
<dd>

**license_state:** `typing.Optional[str]` — Abbreviation of US state, Canadian province, or US territory that issued driver's license.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[CreateDriverRequestLocale]` — Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the driver.
    
</dd>
</dl>

<dl>
<dd>

**peer_group_tag_id:** `typing.Optional[str]` — The peer group tag id this driver belong to, used for gamification.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the driver.
    
</dd>
</dl>

<dl>
<dd>

**profile_image_base_64:** `typing.Optional[DriverProfileImageBase64]` 
    
</dd>
</dl>

<dl>
<dd>

**profile_image_url:** `typing.Optional[DriverProfileImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_vehicle_id:** `typing.Optional[str]` — ID of vehicle that the driver is permanently assigned to. (uncommon).
    
</dd>
</dl>

<dl>
<dd>

**tachograph_card_number:** `typing.Optional[str]` — Driver's assigned tachograph card number (Europe specific)
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of tags the driver is associated with. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    
</dd>
</dl>

<dl>
<dd>

**us_driver_ruleset_override:** `typing.Optional[UsDriverRulesetOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle_group_tag_id:** `typing.Optional[str]` — Tag ID which determines which vehicles a driver will see when selecting vehicles.
    
</dd>
</dl>

<dl>
<dd>

**waiting_time_duty_status_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select waiting time duty status in ELD logs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">post_driver_remote_signout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sign out a driver from the Samsara Driver App

To access this endpoint, your organization must have the Samsara Platform Premier license.

Note: Sign out requests made while a logged-in driver does not have internet connection will not log the driver out. A success response will still be provided and the driver will be logged out once they have internet connection.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver Remote Signout** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.drivers.post_driver_remote_signout(
    driver_id="12434",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `str` — ID of the driver.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a driver. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.drivers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.drivers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.drivers.<a href="src/samsara/v_20250611/drivers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific driver's information. This can also be used to activate or de-activate a given driver by setting the driverActivationStatus field. If the driverActivationStatus field is 'deactivated' then the user can also specify the deactivatedAtTime. The deactivatedAtTime cannot be more than 6 months in the past and must not come before the dirver's latest active HOS log. It will be considered an error if deactivatedAtTime is provided with a driverActivationStatus of active. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Drivers** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.drivers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the driver. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[CreateDriverRequestAttributes]]` 
    
</dd>
</dl>

<dl>
<dd>

**carrier_settings:** `typing.Optional[DriverCarrierSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**current_id_card_code:** `typing.Optional[str]` — The ID Card Code on the back of the physical card assigned to the driver.  Contact Samsara if you would like to enable this feature.
    
</dd>
</dl>

<dl>
<dd>

**deactivated_at_time:** `typing.Optional[str]` — The date and time this driver is considered to be deactivated in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[UpdateDriverRequestDriverActivationStatus]` — A value indicating whether the driver is active or deactivated. Valid values: `active`, `deactivated`.
    
</dd>
</dl>

<dl>
<dd>

**eld_adverse_weather_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Adverse Weather exemptions in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_big_day_exemption_enabled:** `typing.Optional[bool]` — Flag indicating this driver may use Big Day exemption in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_day_start_hour:** `typing.Optional[int]` — `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt:** `typing.Optional[bool]` — Flag indicating this driver is exempt from the Electronic Logging Mandate.
    
</dd>
</dl>

<dl>
<dd>

**eld_exempt_reason:** `typing.Optional[str]` — Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).
    
</dd>
</dl>

<dl>
<dd>

**eld_pc_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**eld_ym_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select the Yard Move duty status in ELD logs.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**has_driving_features_hidden:** `typing.Optional[DriverHasDrivingFeaturesHidden]` 
    
</dd>
</dl>

<dl>
<dd>

**has_vehicle_unpinning_enabled:** `typing.Optional[DriverHasVehicleUnpinningEnabled]` 
    
</dd>
</dl>

<dl>
<dd>

**hos_setting:** `typing.Optional[UpdateDriverRequestHosSetting]` 
    
</dd>
</dl>

<dl>
<dd>

**license_number:** `typing.Optional[str]` — Driver's state issued license number. The combination of this number and `licenseState` must be unique.
    
</dd>
</dl>

<dl>
<dd>

**license_state:** `typing.Optional[str]` — Abbreviation of US state, Canadian province, or US territory that issued driver's license.
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[UpdateDriverRequestLocale]` — Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`, `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Driver's name.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the driver.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Password that the driver can use to login to the Samsara driver app.
    
</dd>
</dl>

<dl>
<dd>

**peer_group_tag_id:** `typing.Optional[str]` — The peer group tag id this driver belong to, leave blank to be in group with everyone, used for gamification.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the driver.
    
</dd>
</dl>

<dl>
<dd>

**profile_image_base_64:** `typing.Optional[DriverProfileImageBase64]` 
    
</dd>
</dl>

<dl>
<dd>

**profile_image_url:** `typing.Optional[DriverProfileImageUrl]` 
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_vehicle_id:** `typing.Optional[str]` — ID of vehicle that the driver is permanently assigned to. (uncommon).
    
</dd>
</dl>

<dl>
<dd>

**tachograph_card_number:** `typing.Optional[str]` — Driver's assigned tachograph card number (Europe specific)
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of tags the driver is associated with. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
    
</dd>
</dl>

<dl>
<dd>

**us_driver_ruleset_override:** `typing.Optional[UsDriverRulesetOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_group_tag_id:** `typing.Optional[str]` — Tag ID which determines which vehicles a driver will see when selecting vehicles.
    
</dd>
</dl>

<dl>
<dd>

**waiting_time_duty_status_enabled:** `typing.Optional[bool]` — Flag indicating this driver may select waiting time duty status in ELD logs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tachograph (EU Only)
<details><summary><code>client.v_20250611.tachograph_eu_only.<a href="src/samsara/v_20250611/tachograph_eu_only/client.py">get_driver_tachograph_activity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph activity for all specified drivers in the time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tachograph_eu_only.get_driver_tachograph_activity(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. It can't be more than 30 days past startTime. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tachograph_eu_only.<a href="src/samsara/v_20250611/tachograph_eu_only/client.py">get_driver_tachograph_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph files for all specified drivers in the time range. 

 <b>Rate limit:</b> 50 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tachograph_eu_only.get_driver_tachograph_files(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tachograph_eu_only.<a href="src/samsara/v_20250611/tachograph_eu_only/client.py">get_vehicle_tachograph_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known tachograph files for all specified vehicles in the time range. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tachograph_eu_only.get_vehicle_tachograph_files(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Equipment
<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">list_equipment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all equipment in an organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.list_equipment(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns last known locations for all equipment. This can be optionally filtered by tags or specific equipment IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_locations(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_locations_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all equipment locations.

Your first call to this endpoint will provide you with the most recent location for each unit of equipment and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment location updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_locations_feed(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_locations_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical equipment locations during the given time range. This can be optionally filtered by tags or specific equipment IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_locations_history(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_stats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats for all equipment. This can be optionally filtered by tags or specific equipment IDs. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetEquipmentStatsRequestTypesItem,
        typing.Sequence[GetEquipmentStatsRequestTypesItem],
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 4 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running as reported directly from on-board diagnostics. This is supported with the following hardware configurations: AG24/AG26 + AOPEN/A9PIN/ACT9/ACT14.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address. 
- `engineTotalIdleTimeMinutes`: Total time in minutes that the engine has been idling.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_stats_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all equipment stats.

Your first call to this endpoint will provide you with the most recent stats for each unit of equipment and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to subsequent calls via the `after` parameter. The response will contain any equipment stats updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. Each stat type has a different refresh rate, but in general we'd suggest waiting a minimum of 5 seconds before requesting updates. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_stats_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetEquipmentStatsFeedRequestTypesItem,
        typing.Sequence[GetEquipmentStatsFeedRequestTypesItem],
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 4 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running as reported directly from on-board diagnostics. This is supported with the following hardware configurations: AG24/AG26 + AOPEN/A9PIN/ACT9/ACT14.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address. 
- `engineTotalIdleTimeMinutes`: Total time in minutes that the engine has been idling.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment_stats_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical equipment status during the given time range. This can be optionally filtered by tags or specific equipment IDs. 

 <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment_stats_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**equipment_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetEquipmentStatsHistoryRequestTypesItem,
        typing.Sequence[GetEquipmentStatsHistoryRequestTypesItem],
    ]
]` 

The types of equipment stats you want to query. Currently, you may submit up to 4 types.

- `engineRpm`: The revolutions per minute of the engine.
- `fuelPercents`: The percent of fuel in the unit of equipment.
- `obdEngineSeconds`: The number of seconds the engine has been running as reported directly from on-board diagnostics. This is supported with the following hardware configurations: AG24/AG26 + AOPEN/A9PIN/ACT9/ACT14.
- `gatewayEngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the asset gateway has been receiving power with an offset provided manually through the Samsara cloud dashboard. This is supported with the following hardware configurations: 
  - AG24/AG26/AG46P + APWR cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required) 
  - AG52 + BPWR/BEQP cable ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d) required). 
- `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power via J1939/CAT cable and an offset provided manually through the Samsara cloud dashboard.
- `obdEngineStates`: The state of the engine read from on-board diagnostics. Can be `Off`, `On`, or `Idle`.
- `gatewayEngineStates`: An approximation of engine state based on readings the AG26 receives from the aux/digio cable. Can be `Off` or `On`.
- `gpsOdometerMeters`: An approximation of odometer reading based on GPS calculations since the AG26 was activated, and a manual odometer offset provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address. 
- `engineTotalIdleTimeMinutes`: Total time in minutes that the engine has been idling.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.equipment.<a href="src/samsara/v_20250611/equipment/client.py">get_equipment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the unit of equipment with the given Samsara ID. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.equipment.get_equipment(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Samsara ID of the Equipment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Hours of Service
<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">get_hos_clocks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogsSummary). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.get_hos_clocks(
    after="after",
    limit=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">get_hos_daily_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get summarized daily Hours of Service charts for the specified drivers.

The time range for a log is defined by the `driver`'s `eldDayStartHour`. This value is configurable per driver.

The `startDate` and `endDate` parameters indicate the date range you'd like to retrieve daily logs for. A daily log will be returned if its `startTime` is on any of the days within in this date range (inclusive of `startDate` and `endDate`).

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded.

If you are using the legacy version of this endpoint and looking for its documentation, you can find it [here](https://www.samsara.com/api-legacy#operation/getFleetDriversHosDailyLogs).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.get_hos_daily_logs(
    start_date="startDate",
    end_date="endDate",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    driver_activation_status="active",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` —  A start date in YYYY-MM-DD. This is a date only without an associated time. Example: `2019-06-13`. This is a required field
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` —  An end date in YYYY-MM-DD. This is a date only without an associated time. Must be greater than or equal to the start date. Example: `2019-07-21`. This is a required field
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_activation_status:** `typing.Optional[GetHosDailyLogsRequestDriverActivationStatus]` — If value is `deactivated`, only drivers that are deactivated will appear in the response. This parameter will default to `active` if not provided (fetching only active drivers).  Valid values: `active`, `deactivated`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["vehicle"]]` 

Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

Valid value: `vehicle`  Valid values: `vehicle`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">get_hos_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns HOS logs between a given `startTime` and `endTime`. The logs can be further filtered using tags or by providing a list of driver IDs (including external IDs). The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogs).

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded. 

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.get_hos_logs(
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of driver IDs. Example: `driverIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` — A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">get_hos_violations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get active Hours of Service violations for the specified drivers.

The day object time range for a violation is defined by the `driver`'s `eldDayStartHour`. This value is configurable per driver.

The `startTime` and `endTime` parameters indicate the datetime range you'd like to retrieve violations for. A violation will be returned if its `violationStartTime` falls within this datetime range (inclusive of `startTime` and `endTime`) 

**Note:** The following are all the violation types with a short explanation about what each of them means: `californiaMealbreakMissed` (Missed California Meal Break), `cycleHoursOn` (Cycle Limit), `cycleOffHoursAfterOnDutyHours` (Cycle 2 Limit), `dailyDrivingHours` (Daily Driving Limit), `dailyOffDutyDeferralAddToDay2Consecutive` (Daily Off-Duty Deferral: Add To Day2 Consecutive), `dailyOffDutyDeferralNotPartMandatory` (Daily Off-Duty Deferral: Not Part Of Mandatory), `dailyOffDutyDeferralTwoDayDrivingLimit` (Daily Off-Duty Deferral: 2 Day Driving Limit), `dailyOffDutyDeferralTwoDayOffDuty` (Daily Off-Duty Deferral: 2 Day Off Duty), `dailyOffDutyNonResetHours` (Daily Off-Duty Time: Non-Reset), `dailyOffDutyTotalHours` (Daily Off-Duty Time), `dailyOnDutyHours` (Daily On-Duty Limit), `mandatory24HoursOffDuty` (24 Hours of Off Duty required), `restbreakMissed` (Missed Rest Break), `shiftDrivingHours` (Shift Driving Limit), `shiftHours` (Shift Duty Limit), `shiftOnDutyHours` (Shift On-Duty Limit), `unsubmittedLogs` (Missing Driver Certification)

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.get_hos_violations(
    start_time="startTime",
    end_time="endTime",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` —  A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on violations data based on the violation type enum. Supported types: `NONE, californiaMealbreakMissed, cycleHoursOn, cycleOffHoursAfterOnDutyHours, dailyDrivingHours, dailyOffDutyDeferralAddToDay2Consecutive, dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit, dailyOffDutyDeferralTwoDayOffDuty, dailyOffDutyNonResetHours, dailyOffDutyTotalHours, dailyOnDutyHours, mandatory24HoursOffDuty, restbreakMissed, shiftDrivingHours, shiftHours, shiftOnDutyHours, unsubmittedLogs`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">set_current_duty_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Set an individual driver’s current duty status to 'On Duty' or 'Off Duty'.

 To ensure compliance with the ELD Mandate, only  authenticated drivers can make direct duty status changes on their own logbook. Any system external to the Samsara Driver App using this endpoint to trigger duty status changes must ensure that such changes are only triggered directly by the driver in question and that the driver has been properly authenticated. This endpoint should not be used to algorithmically trigger duty status changes nor should it be used by personnel besides the driver to trigger duty status changes on the driver’s behalf. Carriers and their drivers are ultimately responsible for maintaining accurate logs and should confirm that their use of the endpoint is compliant with the ELD Mandate. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.set_current_duty_status(
    driver_id=1000000,
    duty_status="ON_DUTY",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — ID of the driver for whom the duty status is being set.
    
</dd>
</dl>

<dl>
<dd>

**duty_status:** `str` — Duty status to set the driver to. The only supported values are 'ON_DUTY' and 'OFF_DUTY'.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Location to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**remark:** `typing.Optional[str]` — Remark to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**status_change_at_ms:** `typing.Optional[int]` — Timestamp that the duty status will begin at specified in milliseconds UNIX time. Defaults to the current time if left blank. This can only be set to up to 8 hours in the past.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[int]` — Vehicle ID to associate the duty status change with.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hours_of_service.<a href="src/samsara/v_20250611/hours_of_service/client.py">v_1_get_fleet_hos_authentication_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.

**Note:** If data is still being uploaded from the Samsara Driver App, it may not be completely reflected in the response from this endpoint. The best practice is to wait a couple of days before querying this endpoint to make sure that all data from the Samsara Driver App has been uploaded. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read ELD Hours of Service (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hours_of_service.v_1_get_fleet_hos_authentication_logs(
    driver_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — Driver ID to query.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Ifta
<details><summary><code>client.v_20250611.ifta.<a href="src/samsara/v_20250611/ifta/client.py">get_ifta_jurisdiction_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all jurisdiction IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

**Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.ifta.get_ifta_jurisdiction_reports(
    year=1,
    month="January",
    quarter="Q1",
    jurisdictions="jurisdictions",
    fuel_type="Unspecified",
    vehicle_ids="vehicleIds",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**year:** `int` —  The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[GetIftaJurisdictionReportsRequestMonth]` —  The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`
    
</dd>
</dl>

<dl>
<dd>

**quarter:** `typing.Optional[GetIftaJurisdictionReportsRequestQuarter]` —  The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`
    
</dd>
</dl>

<dl>
<dd>

**jurisdictions:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`
    
</dd>
</dl>

<dl>
<dd>

**fuel_type:** `typing.Optional[GetIftaJurisdictionReportsRequestFuelType]` —  A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.ifta.<a href="src/samsara/v_20250611/ifta/client.py">get_ifta_vehicle_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all vehicle IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

**Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.ifta.get_ifta_vehicle_reports(
    year=1,
    month="January",
    quarter="Q1",
    jurisdictions="jurisdictions",
    fuel_type="Unspecified",
    vehicle_ids="vehicleIds",
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**year:** `int` —  The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`
    
</dd>
</dl>

<dl>
<dd>

**month:** `typing.Optional[GetIftaVehicleReportsRequestMonth]` —  The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`
    
</dd>
</dl>

<dl>
<dd>

**quarter:** `typing.Optional[GetIftaVehicleReportsRequestQuarter]` —  The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`
    
</dd>
</dl>

<dl>
<dd>

**jurisdictions:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`
    
</dd>
</dl>

<dl>
<dd>

**fuel_type:** `typing.Optional[GetIftaVehicleReportsRequestFuelType]` —  A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.ifta.<a href="src/samsara/v_20250611/ifta/client.py">create_ifta_detail_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a job to generate csv files of IFTA mileage segments.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.ifta.create_ifta_detail_job(
    end_hour="2019-06-13T19:00:00Z",
    start_hour="2019-06-13T19:00:00Z",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_hour:** `str` —  An end time in RFC 3339 format. Hour precision and timezones are supported. Any minutes or seconds will be truncated down to the nearest hour. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. The maximum request duration is 1 month. Limit the number of vehicles to 1000 when requesting more than 24 hours of data. (Examples: 2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**start_hour:** `str` —  A start time in RFC 3339 format. Hour precision and timezones are supported. Any minutes or seconds will be truncated down to the nearest hour. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. The maximum request duration is 1 month. Limit the number of vehicles to 1000 when requesting more than 24 hours of data. (Examples: 2019-06-13T19:00:00Z, 2019-06-13T19:00:00.000Z, OR 2015-09-15T14:00:00-04:00).
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of vehicle IDs and external IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleIds: '1234,5678,samsara.vin:1HGBH41JXMN109186'`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle parent tag IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleParentTagIds: '1234,5678'`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of vehicle tag IDs. The number of vehicles requested per job shouldn't exceed 5000. Example: `vehicleTagIds: '1234,5678'`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.ifta.<a href="src/samsara/v_20250611/ifta/client.py">get_ifta_detail_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an existing IFTA detail job.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.ifta.get_ifta_detail_job(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the requested job.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Routes
<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">fetch_routes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns multiple routes. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/fetchAllDispatchRoutes).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.fetch_routes(
    start_time="startTime",
    end_time="endTime",
    limit=1,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">create_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a route. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/createDispatchRoute).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import CreateRoutesStopRequestObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.create_route(
    name="Bid 123",
    stops=[CreateRoutesStopRequestObjectRequestBody()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name for the route
    
</dd>
</dl>

<dl>
<dd>

**stops:** `typing.Sequence[CreateRoutesStopRequestObjectRequestBody]` — List of stops along the route. For each stop, exactly one of `addressId` and `singleUseLocation` are required. Depending on the `settings` on your route, either a `scheduledArrivalTime` or `scheduledDepartureTime` must be specified for the first job.
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[str]` — ID of the driver. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the route.
    
</dd>
</dl>

<dl>
<dd>

**recompute_scheduled_times:** `typing.Optional[bool]` — This optional boolean parameter controls whether route schedule arrival and departure times are recalculated. When set to true, the system will automatically recompute the scheduledArrivalTime and scheduledDepartureTime for each stop along the route during route creation. This process overrides any manually provided values, with the exception of the first stop, which retains its user-defined schedule.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RouteSettingsRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this route.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">get_routes_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Subscribes to a feed of immutable, append-only updates for routes. The initial request to this feed endpoint returns a cursor, which can be used on the next request to fetch updated routes that have had state changes since that request.

The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/fetchAllRouteJobUpdates).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.get_routes_feed(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["route"]]` 

Expands the specified value(s) in the response object. Expansion populates additional fields in an object, if supported. Unsupported fields are ignored. To expand multiple fields, input a comma-separated list.

Valid value: `route`  Valid values: `route`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">fetch_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single route. The legacy version of this endpoint can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getDispatchRouteById).

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.fetch_route(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">delete_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a dispatch route and its associated stops.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.delete_route(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">patch_route</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a route.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array.

The legacy version of this endpoint (which uses PUT instead of PATCH) can be found at [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/updateDispatchRouteById).

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.patch_route(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**driver_id:** `typing.Optional[str]` — ID of the driver. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for the route
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Notes about the route.
    
</dd>
</dl>

<dl>
<dd>

**recompute_scheduled_times:** `typing.Optional[bool]` — This optional boolean parameter controls whether route schedule arrival and departure times are recalculated. When set to true, the system will automatically recompute the scheduledArrivalTime and scheduledDepartureTime for each stop along the route during route creation. This process overrides any manually provided values, with the exception of the first stop, which retains its user-defined schedule.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[RouteSettingsRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**stops:** `typing.Optional[typing.Sequence[UpdateRoutesStopRequestObjectRequestBody]]` — List of stops along the route. If a valid `id` of a stop is provided, that stop will be updated. If no `id` is provided for a passed in stop, that stop will be created. If `id` value are passed in for some stops and not for others, those with `id` value specified will be retained and updated in the original route, those without `id` value specified in the body will be created, and those without `id` value specified that already existed on the route will be deleted. For each new stop, exactly one of `addressId` and `singleUseLocation` are required. Depending on the `settings` on your route, either a `scheduledArrivalTime` or `scheduledDepartureTime` must be specified for the first job, if a new first job is being added.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this route.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_id:** `typing.Optional[str]` — ID of the vehicle. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">list_hub_plan_routes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve routes for a specific plan.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.list_hub_plan_routes(
    plan_id="planId",
    route_ids="routeIds",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plan_id:** `str` — The plan identifier
    
</dd>
</dl>

<dl>
<dd>

**route_ids:** `typing.Optional[str]` — Comma-separated list of route IDs for filtering.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Time filter of when the route was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Time filter of when the route was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.routes.<a href="src/samsara/v_20250611/routes/client.py">v_1_delete_dispatch_route_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Delete a dispatch route and its associated jobs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.routes.v_1_delete_dispatch_route_by_id(
    route_id_or_external_id="route_id_or_external_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**route_id_or_external_id:** `str` — ID of the route. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `payrollId:ABFS18600`
    
</dd>
</dl>

<dl>
<dd>

**apply_to_future_routes:** `typing.Optional[bool]` — This is only for a recurring route.  If set to true, delete all following runs of the route.  If set to false, only delete the current route.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Safety
<details><summary><code>client.v_20250611.safety.<a href="src/samsara/v_20250611/safety/client.py">get_safety_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch safety events for the organization in a given time period. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.safety.get_safety_events(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.safety.<a href="src/samsara/v_20250611/safety/client.py">get_safety_activity_event_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get continuous safety events. The safety activity event feed offers a change-log for safety events. Use this endpoint to subscribe to safety event changes. See documentation below for all supported change-log types.

| ActivityType      | Description |
| ----------- | ----------- |
| CreateSafetyEventActivityType | a new safety event is processed by Samsara      |
| BehaviorLabelActivityType     | a label is added or removed from a safety event |
| CoachingStateActivityType     | a safety event coaching state is updated        |

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.safety.get_safety_activity_event_feed(
    after="after",
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[str]` —  A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.safety.<a href="src/samsara/v_20250611/safety/client.py">v_1_get_driver_safety_score</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the driver.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.safety.v_1_get_driver_safety_score(
    driver_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_id:** `int` — ID of the driver. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.safety.<a href="src/samsara/v_20250611/safety/client.py">v_1_get_vehicle_harsh_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch harsh event details for a vehicle. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.safety.v_1_get_vehicle_harsh_event(
    vehicle_id=1000000,
    timestamp=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — ID of the vehicle. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `int` — Timestamp in milliseconds representing the timestamp of a harsh event.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.safety.<a href="src/samsara/v_20250611/safety/client.py">v_1_get_vehicle_safety_score</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch the safety score for the vehicle. 

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.safety.v_1_get_vehicle_safety_score(
    vehicle_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — ID of the vehicle. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Settings
<details><summary><code>client.v_20250611.settings.<a href="src/samsara/v_20250611/settings/client.py">get_compliance_settings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.settings.get_compliance_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.settings.<a href="src/samsara/v_20250611/settings/client.py">patch_compliance_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update organization's compliance settings, including carrier name, office address, and DOT number

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write ELD Compliance Settings (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.settings.patch_compliance_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**allow_unregulated_vehicles_enabled:** `typing.Optional[bool]` — [deprecated] Allow Unregulated Vehicles. This setting is deprecated as all organizations can now mark vehicles as unregulated.
    
</dd>
</dl>

<dl>
<dd>

**canada_hos_enabled:** `typing.Optional[bool]` — Enable Canada HOS
    
</dd>
</dl>

<dl>
<dd>

**carrier_name:** `typing.Optional[str]` — Carrier Name / Principal Place of Business Name
    
</dd>
</dl>

<dl>
<dd>

**dot_number:** `typing.Optional[int]` — Carrier US DOT Number
    
</dd>
</dl>

<dl>
<dd>

**driver_auto_duty_enabled:** `typing.Optional[bool]` — Enable Driver Auto-Duty
    
</dd>
</dl>

<dl>
<dd>

**edit_certified_logs_enabled:** `typing.Optional[bool]` — Drivers Can Edit Certified Log
    
</dd>
</dl>

<dl>
<dd>

**force_manual_location_for_duty_status_changes_enabled:** `typing.Optional[bool]` — Force Manual Location For Duty Status Changes
    
</dd>
</dl>

<dl>
<dd>

**force_review_unassigned_hos_enabled:** `typing.Optional[bool]` — Force Review of Unassigned HOS
    
</dd>
</dl>

<dl>
<dd>

**main_office_formatted_address:** `typing.Optional[str]` — Main Office Address / Principal Place of Businesss Address
    
</dd>
</dl>

<dl>
<dd>

**persistent_duty_status_enabled:** `typing.Optional[bool]` — Persistent Duty Status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.settings.<a href="src/samsara/v_20250611/settings/client.py">get_driver_app_settings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get driver app settings.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.settings.get_driver_app_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.settings.<a href="src/samsara/v_20250611/settings/client.py">patch_driver_app_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update driver app settings.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver App Settings** under the Drivers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.settings.patch_driver_app_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_fleet_id:** `typing.Optional[str]` — Global login user name for the fleet driver app
    
</dd>
</dl>

<dl>
<dd>

**gamification:** `typing.Optional[bool]` — Driver gamification feature. Enabling this will turn on the feature for all drivers using the mobile app. Drivers can be configured into peer groups within the Drivers Page. Unconfigured drivers will be grouped on an organization level.
    
</dd>
</dl>

<dl>
<dd>

**gamification_config:** `typing.Optional[DriverAppSettingsGamificationConfigTinyObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**org_vehicle_search:** `typing.Optional[bool]` — Allow drivers to search for vehicles outside of their selection tag when connected to the internet.
    
</dd>
</dl>

<dl>
<dd>

**trailer_selection:** `typing.Optional[bool]` — Allow drivers to see and select trailers in the Samsara Driver app. 
    
</dd>
</dl>

<dl>
<dd>

**trailer_selection_config:** `typing.Optional[DriverAppSettingsTrailerSelectionConfigTinyObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.settings.<a href="src/samsara/v_20250611/settings/client.py">get_safety_settings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get safety settings

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Safety Events & Scores** under the Safety & Cameras category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.settings.get_safety_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Trailers
<details><summary><code>client.v_20250611.trailers.<a href="src/samsara/v_20250611/trailers/client.py">list_trailers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all trailers.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailers.list_trailers(
    tag_ids="tagIds",
    parent_tag_ids="parentTagIds",
    limit=1,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.trailers.<a href="src/samsara/v_20250611/trailers/client.py">create_trailer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new trailer asset.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailers.create_trailer(
    name="Trailer-123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTinyRequestBody]]` — A list of attributes to assign to the trailer.
    
</dd>
</dl>

<dl>
<dd>

**enabled_for_mobile:** `typing.Optional[bool]` — Indicates if the trailer is visible on the Samsara mobile apps.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this trailer. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**trailer_serial_number:** `typing.Optional[str]` — The serial number of the trailer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.trailers.<a href="src/samsara/v_20250611/trailers/client.py">get_trailer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a trailer with given ID.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailers.get_trailer(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the trailer. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.trailers.<a href="src/samsara/v_20250611/trailers/client.py">delete_trailer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a trailer with the given ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailers.delete_trailer(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the trailer to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.trailers.<a href="src/samsara/v_20250611/trailers/client.py">update_trailer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a trailer.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Trailers** under the Trailers category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailers.update_trailer(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the trailer. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[GoaAttributeTinyRequestBody]]` — A list of attributes to assign to the trailer.
    
</dd>
</dl>

<dl>
<dd>

**enabled_for_mobile:** `typing.Optional[bool]` — Indicates if the trailer is visible on the Samsara mobile apps.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Trailer. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Trailer. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Trailer. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — When you provide a manual odometer override, Samsara will begin updating a trailer's odometer using GPS distance traveled since this override was set. Only applies to trailers installed with Samsara gateways.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this trailer. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**trailer_serial_number:** `typing.Optional[str]` — The serial number of the trailer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Vehicles
<details><summary><code>client.v_20250611.vehicles.<a href="src/samsara/v_20250611/vehicles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all vehicles.

 <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
response = client.v_20250611.vehicles.list(
    limit=1,
    after="after",
    parent_tag_ids="parentTagIds",
    tag_ids="tagIds",
    attribute_value_ids="attributeValueIds",
    updated_after_time="updatedAfterTime",
    created_after_time="createdAfterTime",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**attribute_value_ids:** `typing.Optional[str]` — A filter on the data based on this comma-separated list of attribute value IDs. Only entities associated with ALL of the referenced values will be returned (i.e. the intersection of the sets of entities with each value). Example: `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data to return entities having given attributes using either name-value pair, or range query (only for numeric attributes) separated by a comma. Only entities meeting all the conditions will be returned. Example: `attributes=ExampleAttributeName:some_value&attributes=SomeOtherAttr:123&attributes=Length:range(10,20)`
    
</dd>
</dl>

<dl>
<dd>

**updated_after_time:** `typing.Optional[str]` —  A filter on data to have an updated at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**created_after_time:** `typing.Optional[str]` —  A filter on data to have a created at time after or equal to this specified time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicles.<a href="src/samsara/v_20250611/vehicles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific vehicle. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicles.<a href="src/samsara/v_20250611/vehicles/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the given Vehicle object.

**Note:** Vehicle objects are automatically created when Samsara Vehicle Gateways are installed. You cannot create a Vehicle object via API.

You are able to *update* many of the fields of a Vehicle.

**Note**: There are no required fields in the request body, and you only need to provide the fields you wish to update. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Vehicles** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Sequence[AttributeTiny]]` 
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_1:** `typing.Optional[UpdateVehicleRequestAuxInputType1]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_10:** `typing.Optional[UpdateVehicleRequestAuxInputType10]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_11:** `typing.Optional[UpdateVehicleRequestAuxInputType11]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_12:** `typing.Optional[UpdateVehicleRequestAuxInputType12]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_13:** `typing.Optional[UpdateVehicleRequestAuxInputType13]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_2:** `typing.Optional[UpdateVehicleRequestAuxInputType2]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_3:** `typing.Optional[UpdateVehicleRequestAuxInputType3]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_4:** `typing.Optional[UpdateVehicleRequestAuxInputType4]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_5:** `typing.Optional[UpdateVehicleRequestAuxInputType5]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_6:** `typing.Optional[UpdateVehicleRequestAuxInputType6]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_7:** `typing.Optional[UpdateVehicleRequestAuxInputType7]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_8:** `typing.Optional[UpdateVehicleRequestAuxInputType8]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**aux_input_type_9:** `typing.Optional[UpdateVehicleRequestAuxInputType9]` — The type of <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. Valid values: `None`, `Emergency Lights`, `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`, `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`, `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`, `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — A manual override for the vehicle's engine hours. You may only override a vehicle's engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle's engine hours based on when the Samsara Vehicle Gateway is recieving power or not. Setting the value to 0 will unset the manual engine hours.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given object.
    
</dd>
</dl>

<dl>
<dd>

**gateway_serial:** `typing.Optional[UserIdentifierSerial]` 
    
</dd>
</dl>

<dl>
<dd>

**gross_vehicle_weight:** `typing.Optional[GrossVehicleWeight]` 
    
</dd>
</dl>

<dl>
<dd>

**harsh_acceleration_setting_type:** `typing.Optional[UpdateVehicleRequestHarshAccelerationSettingType]` — The harsh acceleration setting type. This setting influences the acceleration sensitivity from which a <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh event</a> is triggered. **By default**, this setting is inferred by the Samsara Vehicle Gateway from the engine computer, but it may be set or updated through the Samsara Dashboard or the API at any time. If set to `off`, then no acceleration based harsh events are triggered for the vehicle. Valid values: `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.
    
</dd>
</dl>

<dl>
<dd>

**license_plate:** `typing.Optional[str]` — The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — A manual override for the vehicle's odometer. You may only override a vehicle's odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle's odometer using GPS distance traveled since this override was set. See <a href="https://kb.samsara.com/hc/en-us/articles/115005273667" target="_blank">here</a> for more details.
    
</dd>
</dl>

<dl>
<dd>

**static_assigned_driver_id:** `typing.Optional[str]` — ID for the static assigned driver of the vehicle. Setting the value to 0 will unassign the current driver.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — An array of IDs of tags to associate with this vehicle. If your access to the API is scoped by one or more tags, this field is required to pass in.
    
</dd>
</dl>

<dl>
<dd>

**vehicle_regulation_mode:** `typing.Optional[VehicleRegulationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle_type:** `typing.Optional[VehicleType]` 
    
</dd>
</dl>

<dl>
<dd>

**vin:** `typing.Optional[str]` — The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicle Locations
<details><summary><code>client.v_20250611.vehicle_locations.<a href="src/samsara/v_20250611/vehicle_locations/client.py">get_vehicle_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestats) instead.***

Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_locations.get_vehicle_locations(
    after="after",
    time="time",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicle_locations.<a href="src/samsara/v_20250611/vehicle_locations/client.py">get_vehicle_locations_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatsfeed) instead.***

Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`. 

If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_locations.get_vehicle_locations_feed(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicle_locations.<a href="src/samsara/v_20250611/vehicle_locations/client.py">get_vehicle_locations_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatshistory) instead.***

Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_locations.get_vehicle_locations_history(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vehicle Stats
<details><summary><code>client.v_20250611.vehicle_stats.<a href="src/samsara/v_20250611/vehicle_stats/client.py">get_vehicle_stats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the last known stats of all vehicles at the given `time`. If no `time` is specified, the current time is used.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_stats.get_vehicle_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetVehicleStatsRequestTypesItem,
        typing.Sequence[GetVehicleStatsRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `fuelConsumedMilliliters`: The cumulative fuel consumption in milliliters for vehicles. Cumulative values always increase. This includes all fuel consumption reported by vehicles without filtering of invalid data points. For filtered fuel consumption that matches the Fuel & Energy Report, please use <a href="https://developers.samsara.com/reference/getfuelenergyvehiclereports" target="_blank">the Fuel and Energy API</a>.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `idlingDurationMilliseconds`: The cumulative idling duration in milliseconds. Cumulative values always increase. For filtering of idling duration please use [the Idling Events API](https://developers.samsara.com/reference/getvehicleidlingreports).
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. When onboard diagnostic data is unavailable, ignition-based engine data (for ELD vehicles) will be used as a proxy to accumulate engine hours.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: The cumulative number of seconds the engine has run estimated based on when the engine is running. Please note that this method <a href="https://kb.samsara.com/hc/en-us/articles/360043552511-Synthetic-Engine-Hours" target="_blank">requires the addition of a baseline</a> to trigger accumulation.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses: unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
- `tellTales`: Tell tales status as read from the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicle_stats.<a href="src/samsara/v_20250611/vehicle_stats/client.py">get_vehicle_stats_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a feed of vehicle stats. 

Your first call to this endpoint will provide you with the most recent stats for each vehicle and an `endCursor`.

You can the provide the `endCursor` value to the `after` query parameter to get all updates since the last call you made.

If `hasNextPage` is `false`, no new data is immediately available. You should wait a minimum of 5 seconds making a subsequent request.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_stats.get_vehicle_stats_feed()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetVehicleStatsFeedRequestTypesItem,
        typing.Sequence[GetVehicleStatsFeedRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `fuelConsumedMilliliters`: The cumulative fuel consumption in milliliters for vehicles. Cumulative values always increase. This includes all fuel consumption reported by vehicles without filtering of invalid data points. For filtered fuel consumption that matches the Fuel & Energy Report, please use <a href="https://developers.samsara.com/reference/getfuelenergyvehiclereports" target="_blank">the Fuel and Energy API</a>.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `idlingDurationMilliseconds`: The cumulative idling duration in milliseconds. Cumulative values always increase. For filtering of idling duration please use [the Idling Events API](https://developers.samsara.com/reference/getvehicleidlingreports).
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. When onboard diagnostic data is unavailable, ignition-based engine data (for ELD vehicles) will be used as a proxy to accumulate engine hours.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: The cumulative number of seconds the engine has run estimated based on when the engine is running. Please note that this method <a href="https://kb.samsara.com/hc/en-us/articles/360043552511-Synthetic-Engine-Hours" target="_blank">requires the addition of a baseline</a> to trigger accumulation.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses: unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
- `tellTales`: Tell tales status as read from the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[
    typing.Union[
        GetVehicleStatsFeedRequestDecorationsItem,
        typing.Sequence[GetVehicleStatsFeedRequestDecorationsItem],
    ]
]` 

Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.

You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

Note that decorations may significantly increase the response payload size.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `fuelConsumedMilliliters`: The cumulative fuel consumption in milliliters for vehicles. Cumulative values always increase. This includes all fuel consumption reported by vehicles without filtering of invalid data points. For filtered fuel consumption that matches the Fuel & Energy Report, please use <a href="https://developers.samsara.com/reference/getfuelenergyvehiclereports" target="_blank">the Fuel and Energy API</a>.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `idlingDurationMilliseconds`: The cumulative idling duration in milliseconds. Cumulative values always increase. For filtering of idling duration please use <a href="https://developers.samsara.com/reference/getvehicleidlingreports" target="_blank">the Idling Events API</a>.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. When onboard diagnostic data is unavailable, ignition-based engine data (for ELD vehicles) will be used as a proxy to accumulate engine hours.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: The cumulative number of seconds the engine has run estimated based on when the engine is running. Please note that this method <a href="https://kb.samsara.com/hc/en-us/articles/360043552511-Synthetic-Engine-Hours" target="_blank">requires the addition of a baseline</a> to trigger accumulation.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses: unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in 'blast mode'.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
- `tellTales`: Tell tales status as read from the vehicle. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.vehicle_stats.<a href="src/samsara/v_20250611/vehicle_stats/client.py">get_vehicle_stats_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns vehicle stats during the given time range for all vehicles. This can be optionally filtered by tags or specific vehicle IDs.

Related guide: <a href="/docs/telematics" target="_blank">Telematics</a>. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.vehicle_stats.get_vehicle_stats_history(
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**vehicle_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[
    typing.Union[
        GetVehicleStatsHistoryRequestTypesItem,
        typing.Sequence[GetVehicleStatsHistoryRequestTypesItem],
    ]
]` 

The stat types you want this endpoint to return information on. See also the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

You may list ***up to 3*** types using comma-separated format. For example: `types=gps,engineStates,obdOdometerMeters`.

*Note:* `auxInput3`-`auxInput10` count as a single type against the limit of 3. For example, you could list `types=engineStates,obdOdometerMeters,auxInput3,auxInput4` because `auxInput3` and `auxInput4` count as a single stat type. `auxInput1` and `auxInput2` still count as their own individual types.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `defLevelMilliPercent`: The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc).
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `fuelConsumedMilliliters`: The cumulative fuel consumption in milliliters for vehicles. Cumulative values always increase. This includes all fuel consumption reported by vehicles without filtering of invalid data points. For filtered fuel consumption that matches the Fuel & Energy Report, please use <a href="https://developers.samsara.com/reference/getfuelenergyvehiclereports" target="_blank">the Fuel and Energy API</a>.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `gpsOdometerMeters`: Odometer reading provided by GPS calculations when OBD odometer cannot be pulled automatically. You must provide a manual odometer reading before this value is updated. Manual odometer readings can be provided via the [PATCH /fleet/vehicles/{id}](ref:updatevehicle) endpoint or through the <a href="https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading" target="_blank">cloud dasbhoard</a>. Odometer readings that are manually set will update as GPS trip data is gathered. Try combining with `obdOdometerMeters`.
- `idlingDurationMilliseconds`: The cumulative idling duration in milliseconds. Cumulative values always increase. For filtering of idling duration please use [the Idling Events API](https://developers.samsara.com/reference/getvehicleidlingreports).
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. When onboard diagnostic data is unavailable, ignition-based engine data (for ELD vehicles) will be used as a proxy to accumulate engine hours.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: The cumulative number of seconds the engine has run estimated based on when the engine is running. Please note that this method <a href="https://kb.samsara.com/hc/en-us/articles/360043552511-Synthetic-Engine-Hours" target="_blank">requires the addition of a baseline</a> to trigger accumulation.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses: unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in ‘blast mode’.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
- `tellTales`: Tell tales status as read from the vehicle.
    
</dd>
</dl>

<dl>
<dd>

**decorations:** `typing.Optional[
    typing.Union[
        GetVehicleStatsHistoryRequestDecorationsItem,
        typing.Sequence[GetVehicleStatsHistoryRequestDecorationsItem],
    ]
]` 

Decorations to add to the primary stats listed in the `types` parameter. For example, if you wish to know the vehicle's location whenever the engine changes state, you may set `types=engineStates&decorations=gps`.

You may list ***up to 2*** decorations using comma-separated format. If multiple stats are listed in the `types` parameter, the decorations will be added to each one. For example: `types=engineStates,obdOdometerMeters,faultCodes&decorations=gps,fuelPercents` will list GPS and fuel decorations for each engine state change, each odometer reading, and each fault code. See the <a href="/docs/telematics#query-parameters" target="_blank">Telematics</a> guide for more details.

Note that decorations may significantly increase the response payload size.

- `ambientAirTemperatureMilliC`: The ambient air temperature reading in millidegree Celsius.
- `auxInput1`-`auxInput13`: Stat events from the <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary inputs</a> for the vehicle.
- `batteryMilliVolts`: The vehicle battery voltage reading.
- `barometricPressurePa`: The barometric pressure reading in pascals.
- `ecuSpeedMph`: The speed of the engine in miles per hour according to the ECU.
- `engineCoolantTemperatureMilliC`: The engine coolant temperature reading in millidegree Celsius.
- `engineImmobilizer`: The state of the engine immobilizer - Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only return states of our first Engine Immobilizer Hardware (ACC-EI). Please use <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get engine immobilizer states</a> to get states for both Engine Immobilizer Hardware versions (incl. HW-EI21).
- `engineOilPressureKPa`: The engine oil pressure reading in kilopascals.
- `engineLoadPercent`: The engine load in percentage points (e.g. `99`, `50`, etc).
- `engineRpm`: The revolutions per minute of the engine.
- `engineStates`: The state of the engine (`Off`, `On`, `Idle`).
- `faultCodes`: The diagnostic fault codes for the vehicle.
- `fuelPercents`: The engine fuel level in percentage points (e.g. `99`, `50`, etc).
- `fuelConsumedMilliliters`: The cumulative fuel consumption in milliliters for vehicles. Cumulative values always increase. This includes all fuel consumption reported by vehicles without filtering of invalid data points. For filtered fuel consumption that matches the Fuel & Energy Report, please use <a href="https://developers.samsara.com/reference/getfuelenergyvehiclereports" target="_blank">the Fuel and Energy API</a>.
- `gps`: GPS data including lat/long, heading, speed, address book entry (if exists), and a reverse geocoded address.
- `gpsDistanceMeters`: The distance the vehicle has traveled since the gateway was installed based on GPS calculations.
- `idlingDurationMilliseconds`: The cumulative idling duration in milliseconds. Cumulative values always increase. For filtering of idling duration please use <a href="https://developers.samsara.com/reference/getvehicleidlingreports" target="_blank">the Idling Events API</a>.
- `intakeManifoldTemperatureMilliC`: The intake manifold temperature reading in millidegree Celsius.
- `nfcCardScans`: ID card scans.
- `obdEngineSeconds`: The cumulative number of seconds the engine has run according to onboard diagnostics. When onboard diagnostic data is unavailable, ignition-based engine data (for ELD vehicles) will be used as a proxy to accumulate engine hours.
- `obdOdometerMeters`: The odometer reading according to onboard diagnostics. If Samsara does not have diagnostic coverage for a particular vehicle, the value for this stat type will be omitted.
- `syntheticEngineSeconds`: The cumulative number of seconds the engine has run estimated based on when the engine is running. Please note that this method <a href="https://kb.samsara.com/hc/en-us/articles/360043552511-Synthetic-Engine-Hours" target="_blank">requires the addition of a baseline</a> to trigger accumulation.
- `evStateOfChargeMilliPercent`: Milli percent State of Charge for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evChargingStatus`: Charging status for electric and hybrid vehicles. Not all EV and HEVs may report this field. Statuses: unknown - 0, not charging - 1, charging - 2.
- `evChargingEnergyMicroWh`: Charging energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evChargingVoltageMilliVolt`: Charging voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evChargingCurrentMilliAmp`: Charging current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evConsumedEnergyMicroWh`: Consumed energy (including regenerated) for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evRegeneratedEnergyMicroWh`: Regenerated energy for electric and hybrid vehicles in microwatt hours. Not all EV and HEVs may report this field.
- `evBatteryVoltageMilliVolt`: Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field.
- `evBatteryCurrentMilliAmp`: Battery current for electric and hybrid vehicles in milli amps. Not all EV and HEVs may report this field.
- `evBatteryStateOfHealthMilliPercent`: Milli percent battery state of health for electric and hybrid vehicles. Not all EV and HEVs may report this field.
- `evAverageBatteryTemperatureMilliCelsius`: Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
- `evDistanceDrivenMeters`: Electric distance driven for electric and hybrid vehicles in meters. Not all EV and HEVs may report this field.
- `spreaderLiquidRate`: Liquid spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderGranularRate`: Granular spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderPrewetRate`: Prewet spread rate reading in milliliters per meter, read from the material spreader. Unfiltered live stats are supplied as-read from the Material Spreader unit. Readings do not consider total spread rate(s) over time or distance.
- `spreaderAirTemp`: Air (ambient) temperature in milli celsius reading from material spreader.
- `spreaderRoadTemp`: Road temperature reading in milli celsius from material spreader.
- `spreaderOnState`: Whether vehicle spreader is enabled.
- `spreaderActive`: Whether vehicle is actively spreading any material.
- `spreaderBlastState`: Whether vehicle is actively spreading material in 'blast mode'.
- `spreaderGranularName`: Name of most recent type of granular material spread, read from the material spreader.
- `spreaderPrewetName`: Name of most recent type of prewet material spread, read from the material spreader.
- `spreaderLiquidName`: Name of most recent type of liquid material spread, read from the material spreader.
- `spreaderPlowStatus`: Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
- `seatbeltDriver`: Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`. (Beta only)
- `tellTales`: Tell tales status as read from the vehicle. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Forms
<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">get_form_submissions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all form submissions data for the specified list of IDs.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.get_form_submissions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 form submission IDs to filter on. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the form submission.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of strings indicating whether to return additional information. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">post_form_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a form submission and assigns it to an individual worker. This endpoint can be used to create an empty or partially complete form submission and assign it to a worker.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import FormTemplateRequestObjectRequestBody

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.post_form_submission(
    form_template=FormTemplateRequestObjectRequestBody(
        id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        revision_id="1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**form_template:** `FormTemplateRequestObjectRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[FormSubmissionRequestAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — Due date of the form submission. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[
    typing.Sequence[FormSubmissionRequestFieldInputObjectRequestBody]
]` — List of field inputs in a form submission.
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — Indicates whether the worker is required to complete this form or not at a specific route stop. Defaults to `true` if the form is assigned to a user or driver. When true, the worker cannot depart the route stop until this form submission is `submitted`.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop the form submission is assigned to. Must be a unique Samsara ID.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">patch_form_submission</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an instance of a form submission.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.patch_form_submission(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac8",
    status="notStarted",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**approval_details:** `typing.Optional[FormSubmissionRequestApprovalDetailsRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[FormSubmissionRequestAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — Due date of the form submission. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**is_required:** `typing.Optional[bool]` — Indicates whether the worker is required to complete this form or not at a specific route stop. Defaults to `true` if the form is assigned to a user or driver. When true, the worker cannot depart the route stop until this form submission is `submitted`.
    
</dd>
</dl>

<dl>
<dd>

**route_stop_id:** `typing.Optional[str]` — ID of the route stop the form submission is assigned to. Must be a unique Samsara ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[FormSubmissionsPatchFormSubmissionRequestBodyStatus]` — Status of the form submission.  Valid values: `notStarted`, `archived`, `inProgress`, `changesRequested`, `approved`
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title of the form submission.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">get_form_submissions_pdf_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a PDF export that has already been generated for a form submission.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.get_form_submissions_pdf_exports(
    pdf_id="pdfId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pdf_id:** `str` — ID of the form submission PDF export.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">post_form_submissions_pdf_exports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a PDF export for an existing form submission.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.post_form_submissions_pdf_exports(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the form submission to create a PDF export from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">get_form_submissions_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all form submissions data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.get_form_submissions_stream(
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. Value is compared against `updatedAtTime`. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Value is compared against `updatedAtTime`. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**form_template_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 template IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 user IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**driver_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 user IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of strings indicating whether to return additional information. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**assigned_to_route_stop_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 route stop IDs to filter data to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.forms.<a href="src/samsara/v_20250611/forms/client.py">get_form_templates</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of the organization's form templates for the specified list of IDs. If no IDs are provided, all form templates for the organization will be returned.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.forms.get_form_templates(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 template IDs to filter on.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Gateways
<details><summary><code>client.v_20250611.gateways.<a href="src/samsara/v_20250611/gateways/client.py">get_gateways</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all gateways

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.gateways.get_gateways(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**models:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by a comma separated list of gateway models.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.gateways.<a href="src/samsara/v_20250611/gateways/client.py">post_gateway</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate a new gateway. To activate a device and associate it with your organization, enter its serial number. Each device's serial number can also be found on its label or packaging, or from your order confirmation email. A Not Found error could mean that the serial was not found or it has already been activated

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.gateways.post_gateway(
    serial="GFRV-43N-VGX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**serial:** `str` — Gateway serial number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.gateways.<a href="src/samsara/v_20250611/gateways/client.py">delete_gateway</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate a gateway

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Gateways** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.gateways.delete_gateway(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Gateway serial number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Hubs
<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">list_hub_capacities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve capacity types for a specific hub.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.list_hub_capacities(
    hub_id="hubId",
    capacity_ids="capacityIds",
    capacity_names="capacityNames",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_id:** `str` — The hub identifier
    
</dd>
</dl>

<dl>
<dd>

**capacity_ids:** `typing.Optional[str]` — Comma-separated list of capacity IDs for filtering.
    
</dd>
</dl>

<dl>
<dd>

**capacity_names:** `typing.Optional[str]` — Comma-separated list of capacity names for filtering.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Time filter of when the capacity was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Time filter of when the capacity was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">update_hub_location</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update existing location by ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import (
    HubLocationServiceWindowInputRequestBody,
    UpdateHubLocationRequestBodyRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.update_hub_location(
    id="id",
    data=UpdateHubLocationRequestBodyRequestBody(
        address="123 Industrial Blvd, Los Angeles, CA 90210, US",
        customer_location_id="LOC-123",
        driver_instructions="sample instructions",
        is_depot=False,
        latitude=34.0522,
        longitude=-118.2437,
        name="Customer ABC Warehouse",
        planner_notes="sample note",
        service_time_seconds=1800,
        service_windows=[
            HubLocationServiceWindowInputRequestBody(
                days_of_week=[
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday",
                    "friday",
                ],
                end_time="17:00:00",
                start_time="08:00:00",
            )
        ],
        skills_required=["650e8400-e29b-41d4-a716-446655440001"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique Samsara ID of the hub location to update
    
</dd>
</dl>

<dl>
<dd>

**data:** `UpdateHubLocationRequestBodyRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">list_hub_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve locations for a specific hub.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.list_hub_locations(
    hub_id="hubId",
    location_ids="locationIds",
    customer_location_ids="customerLocationIds",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_id:** `str` — The hub identifier
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[str]` — A comma-separated list of location IDs that can be used for filtering
    
</dd>
</dl>

<dl>
<dd>

**customer_location_ids:** `typing.Optional[str]` — A comma-separated list of customer provided location IDs that can be used for filtering
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Time filter of when the location was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Time filter of when the location was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">create_hub_locations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new locations.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import (
    HubLocationInputObjectRequestBody,
    HubLocationServiceWindowInputRequestBody,
)

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.create_hub_locations(
    data=[
        HubLocationInputObjectRequestBody(
            address="123 Industrial Blvd, Los Angeles, CA 90210, US",
            customer_location_id="LOC-123",
            driver_instructions="sample instructions",
            hub_id="550e8400-e29b-41d4-a716-446655440000",
            is_depot=False,
            latitude=34.0522,
            longitude=-118.2437,
            name="Customer ABC Warehouse",
            planner_notes="sample note",
            service_time_seconds=1800,
            service_windows=[
                HubLocationServiceWindowInputRequestBody(
                    days_of_week=[
                        "monday",
                        "tuesday",
                        "wednesday",
                        "thursday",
                        "friday",
                    ],
                    end_time="17:00:00",
                    start_time="08:00:00",
                )
            ],
            skills_required=["650e8400-e29b-41d4-a716-446655440001"],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[HubLocationInputObjectRequestBody]` — An array of location objects to be created or updated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">list_hub_skills</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve skills for a specific hub.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.list_hub_skills(
    hub_id="hubId",
    skill_ids="skillIds",
    skill_names="skillNames",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_id:** `str` — The hub identifier
    
</dd>
</dl>

<dl>
<dd>

**skill_ids:** `typing.Optional[str]` — A comma-separated list of skill IDs that can be used for filtering.
    
</dd>
</dl>

<dl>
<dd>

**skill_names:** `typing.Optional[str]` — A comma-separated list of skill namess that can be used for filtering.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Time filter of when the skill was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Time filter of when the skill was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.hubs.<a href="src/samsara/v_20250611/hubs/client.py">list_hubs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all hubs (planners) in the organization. This endpoint supports pagination and filtering based on hub IDs and update times.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.hubs.list_hubs(
    hub_ids="hubIds",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_ids:** `typing.Optional[str]` — A comma-separated list of hub IDs for filtering results.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Returns hubs updated after the specified time in UTC
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Returns hubs updated before the specified time in UTC
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Plans
<details><summary><code>client.v_20250611.plans.<a href="src/samsara/v_20250611/plans/client.py">create_hub_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new plan.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.plans.create_hub_plan(
    hub_id="550e8400-e29b-41d4-a716-446655440000",
    name="Weekly Plan - Week 15",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_id:** `str` — The ID of the hub the plan belongs to
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the plan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.plans.<a href="src/samsara/v_20250611/plans/client.py">list_hub_plans</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all plans for a specific hub.

 <b>Rate limit:</b> 10 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Routes** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.plans.list_hub_plans(
    hub_id="hubId",
    plan_ids="planIds",
    start_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_time=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**hub_id:** `str` — The hub identifier
    
</dd>
</dl>

<dl>
<dd>

**plan_ids:** `typing.Optional[str]` — Comma-separated list of plan IDs for filtering.
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[dt.datetime]` — Time filter of when the plan was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[dt.datetime]` — Time filter of when the plan was updated, in RFC 3339 format
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, should be the endCursor from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of objects to return. Default and maximum is 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Idling
<details><summary><code>client.v_20250611.idling.<a href="src/samsara/v_20250611/idling/client.py">get_idling_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get idling events for the requested time duration.

**Note:** The data from this endpoint comes from the new Advanced Idling Report, which provides additional data fields for each idling event such as air temperature, geofence, PTO state and minimum idle time. This endpoint includes data from January 1, 2024. If you require additional historical data, you can access it via the [vehicle idling reports API](https://developers.samsara.com/reference/getvehicleidlingreports).

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Idling** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.idling.get_idling_events(
    start_time="startTime",
    end_time="endTime",
    pto_state="active",
    min_air_temperature_millicelsius=1,
    max_air_temperature_millicelsius=1,
    exclude_events_with_unknown_air_temperature=True,
    min_duration_milliseconds=1,
    max_duration_milliseconds=1,
    after="after",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — The start of the time range for filtering idling events in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00). Returns events that begin at or after this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — The end of the time range for filtering idling events in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00). Returns events that begin before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of asset IDs. Asset IDs only include vehicle IDs at this time.
    
</dd>
</dl>

<dl>
<dd>

**operator_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of operator IDs. Operator IDs only include driver IDs at this time.
    
</dd>
</dl>

<dl>
<dd>

**pto_state:** `typing.Optional[GetIdlingEventsRequestPtoState]` — A filter on the data on this PTO (Power Take-Off) state. If no specific state is provided, data including any state will be included.  Valid values: `active`, `inactive`
    
</dd>
</dl>

<dl>
<dd>

**min_air_temperature_millicelsius:** `typing.Optional[int]` — A filter on the data based on the minimum value of air temperature in millicelsius. The acceptable range for this value is between -20,000 and 50,000 millicelsius.
    
</dd>
</dl>

<dl>
<dd>

**max_air_temperature_millicelsius:** `typing.Optional[int]` — A filter on the data based on the maximum value of air temperature in millicelsius. The acceptable range for this value is between -20,000 and 50,000 millicelsius.
    
</dd>
</dl>

<dl>
<dd>

**exclude_events_with_unknown_air_temperature:** `typing.Optional[bool]` — A filter on the data based on unknown air temperature value.
    
</dd>
</dl>

<dl>
<dd>

**min_duration_milliseconds:** `typing.Optional[int]` — A filter on the data based on the minimum value of Idling duration in milliseconds. The acceptable range for this value is between 2 minutes and 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**max_duration_milliseconds:** `typing.Optional[int]` — A filter on the data based on the maximum value of Idling duration in milliseconds. The acceptable range for this value is between 2 minutes and 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Tag IDs only include vehicle IDs at this time.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs. Parent tag IDs only include vehicle IDs at this time.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 200 objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Industrial
<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_industrial_assets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all assets in the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_industrial_assets(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">create_industrial_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an asset with optional configuration parameters. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.create_industrial_asset(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `AssetName` 
    
</dd>
</dl>

<dl>
<dd>

**custom_metadata:** `typing.Optional[CustomMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[AssetLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**location_data_input_id:** `typing.Optional[str]` — Required if locationType is "dataInput". Specifies the id of a location data input which will determine the asset's location. **The data input will be moved to the new asset.**
    
</dd>
</dl>

<dl>
<dd>

**location_type:** `typing.Optional[LocationType]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[ParentId]` 
    
</dd>
</dl>

<dl>
<dd>

**running_status_data_input_id:** `typing.Optional[str]` — The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. **The data input will be moved to the new asset.**
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[TagIds]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">delete_industrial_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete asset. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.delete_industrial_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the asset to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">patch_industrial_asset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing asset. Only the provided fields will be updated. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.patch_industrial_asset(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the asset to be updated
    
</dd>
</dl>

<dl>
<dd>

**custom_metadata:** `typing.Optional[CustomMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[AssetLocation]` 
    
</dd>
</dl>

<dl>
<dd>

**location_data_input_id:** `typing.Optional[str]` — Required if locationType is "dataInput". Specifies the id of a location data input which will determine the asset's location. The data input must be in the asset.
    
</dd>
</dl>

<dl>
<dd>

**location_type:** `typing.Optional[LocationType]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[AssetName]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent asset that the asset belongs to. Pass in an empty string to remove the child from the parent.
    
</dd>
</dl>

<dl>
<dd>

**running_status_data_input_id:** `typing.Optional[str]` — The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. The data input must be in the asset.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[TagIds]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">patch_asset_data_outputs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Writes values to multiple data outputs on an asset simultaneously. Only the provided data outputs will be updated.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.patch_asset_data_outputs(
    id="id",
    values={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Asset ID
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Dict[str, typing.Optional[typing.Any]]` — A map of data output IDs to values. All data outputs must belong to the same asset. Only the specified IDs will be written to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_data_inputs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all data inputs, optionally filtered by tags or asset ids. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_data_inputs(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_data_input_data_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns last known data points for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_data_input_data_snapshot(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_data_input_data_feed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follow a continuous feed of all data input data points.

Your first call to this endpoint will provide you with the most recent data points for each data input and a `pagination` object that contains an `endCursor`.

You can provide the `endCursor` to the `after` parameter of this endpoint to get data point updates since that `endCursor`.

If `hasNextPage` is `false`, no updates are readily available yet. We suggest waiting a minimum of 5 seconds before requesting updates. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_data_input_data_feed(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_data_input_data_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all known data points during the given time range for all data inputs. This can be filtered by optional tags, specific data input IDs or asset IDs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment Statistics** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_data_input_data_history(
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `str` — An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**data_input_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of industrial asset UUIDs. Example: `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_cameras</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch all cameras. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_cameras()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_vision_programs_by_camera</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch configured programs on the camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_vision_programs_by_camera(
    camera_id=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_vision_latest_run_camera</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch the latest run for a camera or program by default. If startedAtMs is supplied, fetch the specific run that corresponds to that start time. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_vision_latest_run_camera(
    camera_id=1000000,
    program_id=1000000,
    started_at_ms=1000000,
    include="include",
    limit=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[int]` — The configured program's ID on the camera.
    
</dd>
</dl>

<dl>
<dd>

**started_at_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit is an integer value from 1 to 1,000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_vision_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_vision_runs(
    duration_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**duration_ms:** `int` — DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">get_vision_runs_by_camera</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.get_vision_runs_by_camera(
    camera_id=1000000,
    duration_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**duration_ms:** `int` — DurationMs is a required param. This works with the EndMs parameter. Indicates the duration in which the visionRuns will be fetched
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — EndMs is an optional param. It will default to the current time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_vision_runs_by_camera_and_program</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch runs by camera and program. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_vision_runs_by_camera_and_program(
    camera_id=1000000,
    program_id=1000000,
    started_at_ms=1000000,
    include="include",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `int` — The camera_id should be valid for the given accessToken.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `int` — The configured program's ID on the camera.
    
</dd>
</dl>

<dl>
<dd>

**started_at_ms:** `int` — Started_at_ms is a required param. Indicates the start time of the run to be fetched.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_machines_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical data for machine objects. This method returns a set of historical data for all machines. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_machines_history(
    end_ms=1462881998034,
    start_ms=1462878398034,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.industrial.<a href="src/samsara/v_20250611/industrial/client.py">v_1_get_machines</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get machine objects. This method returns a list of the machine objects in the Samsara Cloud and information about them. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Industrial** under the Industrial category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.industrial.v_1_get_machines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Issues
<details><summary><code>client.v_20250611.issues.<a href="src/samsara/v_20250611/issues/client.py">get_issues</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all issues data for the specified IDs.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Issues** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.issues.get_issues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 100 issue IDs to filter on. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of additional fields to include on requested objects. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.issues.<a href="src/samsara/v_20250611/issues/client.py">patch_issue</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an instance of an issue.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Issues** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.issues.patch_issue(
    id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the issue. Can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    
</dd>
</dl>

<dl>
<dd>

**assigned_to:** `typing.Optional[PatchIssueRequestBodyAssignedToRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[dt.datetime]` — Due date of the issue. UTC timestamp in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — A map of external ids
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IssuesPatchIssueRequestBodyStatus]` — Status of the issue.  Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.issues.<a href="src/samsara/v_20250611/issues/client.py">get_issues_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all issues data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don’t include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Issues** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.issues.get_issues_stream(
    start_time="startTime",
    end_time="endTime",
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. Value is compared against `updatedAtTime`. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Value is compared against `updatedAtTime`. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing status values to filter issues on. Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 asset IDs to filter issues on. Issues with untracked assets can also be included by passing the value: 'untracked'.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma separated list of additional fields to include on requested objects. Valid values: `externalIds`
    
</dd>
</dl>

<dl>
<dd>

**assigned_to_route_stop_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list containing up to 50 route stop IDs to filter data on.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 LiveSharingLinks
<details><summary><code>client.v_20250611.live_sharing_links.<a href="src/samsara/v_20250611/live_sharing_links/client.py">get_live_sharing_links</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all non-expired Live Sharing Links.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.live_sharing_links.get_live_sharing_links(
    type="all",
    limit=1,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A filter on the data based on this comma-separated list of Live Share Link IDs
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetLiveSharingLinksRequestType]` — A filter on the data based on the Live Sharing Link type.  Valid values: `all`, `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 100 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.live_sharing_links.<a href="src/samsara/v_20250611/live_sharing_links/client.py">create_live_sharing_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.live_sharing_links.create_live_sharing_link(
    name="Example Live Sharing Link name",
    type="assetsLocation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**type:** `LiveSharingLinksCreateLiveSharingLinkRequestBodyType` — Type of the Live Sharing Link. This field specifies which one of '<type>LinkConfig' objects will be used to configure the sharing link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    
</dd>
</dl>

<dl>
<dd>

**assets_location_link_config:** `typing.Optional[AssetsLocationLinkRequestConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_near_location_link_config:** `typing.Optional[AssetsNearLocationLinkConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_on_route_link_config:** `typing.Optional[AssetsOnRouteLinkConfigObject]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    
</dd>
</dl>

<dl>
<dd>

**expires_at_time:** `typing.Optional[str]` — Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.live_sharing_links.<a href="src/samsara/v_20250611/live_sharing_links/client.py">delete_live_sharing_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.live_sharing_links.delete_live_sharing_link(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.live_sharing_links.<a href="src/samsara/v_20250611/live_sharing_links/client.py">update_live_sharing_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Live Sharing Link.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Live Sharing Links** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.live_sharing_links.update_live_sharing_link(
    id="id",
    name="Example Live Sharing Link name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the Live Sharing Link.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    
</dd>
</dl>

<dl>
<dd>

**expires_at_time:** `typing.Optional[str]` — Date that this link expires in RFC 3339 format. Can't be set in the past. If not provided then link will never expire.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 WorkOrders
<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">get_service_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets service tasks.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.get_service_tasks(
    include_archived=True,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by the IDs. If not provided, won't filter by id.
    
</dd>
</dl>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` — Include archived service task definitions.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">get_work_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets work orders.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.get_work_orders(
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by the IDs. Up to 100 ids. Returns all if no ids are provided.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">post_work_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a work order.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.post_work_orders(
    asset_id="12443",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the asset.
    
</dd>
</dl>

<dl>
<dd>

**assigned_user_id:** `typing.Optional[str]` — The ID of the assigned mechanic.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[WorkOrdersPostWorkOrdersRequestBodyCategory]` — The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of what needs to be fixed.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[WorkOrderDiscountObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — The due date of the work order in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — The engine hours at the time of the work order. Will default to current asset reading if unset.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]` — Items related to the work order.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — The odometer reading at the time of the work order. Will default to current asset reading if unset.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[WorkOrdersPostWorkOrdersRequestBodyPriority]` — The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`
    
</dd>
</dl>

<dl>
<dd>

**service_task_instances:** `typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]` — Service Tasks for the work order.
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[WorkOrderTaxCreateObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">delete_work_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a work order.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.delete_work_orders(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique id of the work order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">patch_work_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a work order.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.patch_work_orders(
    id="5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique id of the work order.
    
</dd>
</dl>

<dl>
<dd>

**assigned_user_id:** `typing.Optional[str]` — The ID of the assigned mechanic.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyCategory]` — The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`
    
</dd>
</dl>

<dl>
<dd>

**closing_notes:** `typing.Optional[str]` — Notes on the work order.
    
</dd>
</dl>

<dl>
<dd>

**completed_at_time:** `typing.Optional[dt.datetime]` — The time the work order was completed in RFC 3339 format. Is automatically set when the status changes and this field is not provided.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of what needs to be fixed.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[WorkOrderDiscountObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**due_at_time:** `typing.Optional[dt.datetime]` — The due date of the work order in RFC 3339 format.
    
</dd>
</dl>

<dl>
<dd>

**engine_hours:** `typing.Optional[int]` — The engine hours at the time of the work order. Will default to current asset reading if unset.
    
</dd>
</dl>

<dl>
<dd>

**invoice_number:** `typing.Optional[str]` — The invoice number for the work order.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]` — Items related to the work order.
    
</dd>
</dl>

<dl>
<dd>

**odometer_meters:** `typing.Optional[int]` — The odometer reading at the time of the work order. Will default to current asset reading if unset.
    
</dd>
</dl>

<dl>
<dd>

**po_number:** `typing.Optional[str]` — The purchase order number for the work order.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyPriority]` — The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`
    
</dd>
</dl>

<dl>
<dd>

**service_task_instances:** `typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]` — Service Tasks for the work order.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyStatus]` — The status of the work order  Valid values: `Assigned`, `Cancelled`, `Closed`, `Completed`, `In Progress`, `On Hold`, `Open`, `Pending Approval`, `Pending Parts`
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[WorkOrderTaxObjectRequestBody]` 
    
</dd>
</dl>

<dl>
<dd>

**vendor_uuid:** `typing.Optional[str]` — The vendor UUID for the work order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.work_orders.<a href="src/samsara/v_20250611/work_orders/client.py">stream_work_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream work orders.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Work Orders** under the Work Orders category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.work_orders.stream_work_orders(
    after="after",
    start_time="startTime",
    end_time="endTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` —  An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    
</dd>
</dl>

<dl>
<dd>

**work_order_statuses:** `typing.Optional[
    typing.Union[
        StreamWorkOrdersRequestWorkOrderStatusesItem,
        typing.Sequence[StreamWorkOrdersRequestWorkOrderStatusesItem],
    ]
]` — Work Order status filter.
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Work Order asset id filter. Up to 50 ids.
    
</dd>
</dl>

<dl>
<dd>

**assigned_user_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Work Order assigned user id filter. Up to 50 ids.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Info
<details><summary><code>client.v_20250611.organization_info.<a href="src/samsara/v_20250611/organization_info/client.py">get_organization_info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about your organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Org Information** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.organization_info.get_organization_info()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Preview APIs
<details><summary><code>client.v_20250611.preview_ap_is.<a href="src/samsara/v_20250611/preview_ap_is/client.py">create_driver_auth_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a short-lived auth token for a driver.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Driver Auth Token** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.preview_ap_is.create_driver_auth_token(
    code="dp[gZc1wAigz4uGa0Hh",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` — Required. Random 12+ character string, used with the auth token to help secure the client from intercepted tokens.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — Optional. External ID of the driver, in the format `key:value` (e.g., `payrollId:ABFS18600`). One of `id`, `externalId`, or `username` is required.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[int]` — Optional. Samsara ID of the driver. One of `id`, `externalId`, or `username` is required.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Optional. Username of the driver. This is the login identifier configured when the driver is created. One of `id`, `externalId`, or `username` is required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.preview_ap_is.<a href="src/samsara/v_20250611/preview_ap_is/client.py">lock_vehicle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lock a vehicle. This requires a vehicle gateway with locking capabilities.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Vehicle Lock/Unlock** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.preview_ap_is.lock_vehicle(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the vehicle to lock or unlock. This can be a Samsara internal ID or an external ID in the format `samsara.vin:{VIN}`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.preview_ap_is.<a href="src/samsara/v_20250611/preview_ap_is/client.py">unlock_vehicle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlock a vehicle.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Vehicle Lock/Unlock** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

Endpoints in this section are in Preview. These APIs are not functional and are instead for soliciting feedback from our API users on the intended design of this API. Additionally, it is not guaranteed that we will be releasing an endpoint included in this section to production. This means that developers should **NOT** rely on these APIs to build business critical applications

- Samsara may change the structure of a preview API's interface without versioning or any notice to API users.

- When an endpoint becomes generally available, it will be announced in the API [changelog](https://developers.samsara.com/changelog).
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.preview_ap_is.unlock_vehicle(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the vehicle to lock or unlock. This can be a Samsara internal ID or an external ID in the format `samsara.vin:{VIN}`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 SpeedingIntervals
<details><summary><code>client.v_20250611.speeding_intervals.<a href="src/samsara/v_20250611/speeding_intervals/client.py">get_speeding_intervals</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint will return all speeding intervals associated with all trips that have been collected for your organization based on the time parameters passed in. Only completed trips are included. Trips with no speeding intervals detected will be returned with an empty list of intervals. Results are paginated.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Speeding Intervals** under the Speeding Intervals category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.speeding_intervals.get_speeding_intervals(
    start_time="startTime",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `str` — RFC 3339 timestamp that indicates when to begin receiving data. Value is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter.
    
</dd>
</dl>

<dl>
<dd>

**asset_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of asset IDs. Include up to 50 asset IDs.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime` depending on the queryBy parameter. If not provided then the endpoint behaves as an unending feed of changes.
    
</dd>
</dl>

<dl>
<dd>

**query_by:** `typing.Optional[GetSpeedingIntervalsRequestQueryBy]` — Decide which timestamp the `startTime` and `endTime` are compared to.  Valid values: `updatedAtTime`, `tripStartTime`
    
</dd>
</dl>

<dl>
<dd>

**include_asset:** `typing.Optional[bool]` — Indicates whether or not to return expanded “asset” data
    
</dd>
</dl>

<dl>
<dd>

**include_driver_id:** `typing.Optional[bool]` — Indicates whether or not to return trip's driver id
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**severity_levels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional string of comma-separated severity levels to filter speeding intervals by. Valid values:  “light”, ”moderate”, ”heavy”, “severe”. This filter does not exclude trips that have no speeding intervals.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">list_tags</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all of the tags for an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.list_tags(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">create_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tag for the organization. This may include up to 20,000 tagged entities. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.create_tag(
    name="California",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">get_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a tag by id. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.get_tag(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">replace_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a tag with a new name and new members. This API call would replace all old members of a tag with new members specified in the request body. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.replace_tag(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">delete_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a tag. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.delete_tag(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.tags.<a href="src/samsara/v_20250611/tags/client.py">patch_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tag. **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard. 

 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource. 

 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Tags** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.tags.patch_tag(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`.
    
</dd>
</dl>

<dl>
<dd>

**addresses:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The addresses that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The trailers, unpowered, and powered assets that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**drivers:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The drivers that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Dict[str, str]]` — The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    
</dd>
</dl>

<dl>
<dd>

**machines:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The machines that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of this tag.
    
</dd>
</dl>

<dl>
<dd>

**parent_tag_id:** `typing.Optional[str]` — If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The sensors that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**vehicles:** `typing.Optional[typing.Sequence[TaggedObjectId]]` — The vehicles that belong to this tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">list_user_roles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all user roles in an organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.list_user_roles(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">list_users</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all users in an organization. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.list_users(
    limit=1000000,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">create_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a user to the organization. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import CreateUserRequestRoles

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.create_user(
    auth_type="default",
    email="user@company.com",
    name="Bob Smith",
    roles=[
        CreateUserRequestRoles(
            role_id="8a9371af-82d1-4158-bf91-4ecc8d3a114c",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_type:** `CreateUserRequestAuthType` — The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The email address of this user.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The first and last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Sequence[CreateUserRequestRoles]` — The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag.
    
</dd>
</dl>

<dl>
<dd>

**expire_at:** `typing.Optional[str]` — For users with temporary access, this is the expiration datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">get_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific user's information. Users that have expired access will not be returned. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.get_user(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">delete_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the given user. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.delete_user(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.users.<a href="src/samsara/v_20250611/users/client.py">update_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific user's information. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Users** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.users.update_user(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[UpdateUserRequestAuthType]` — The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`.
    
</dd>
</dl>

<dl>
<dd>

**expire_at:** `typing.Optional[str]` — For users with temporary access, this is the expiration datetime in RFC3339 format
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The first and last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[CreateUserRequestRoles]]` — The list of roles that applies to this user. A user may have "organizational" roles, which apply to the user at the organizational level, and "tag-specific" roles, which apply to the user for a given tag.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Legacy
<details><summary><code>client.v_20250611.legacy.<a href="src/samsara/v_20250611/legacy/client.py">v_1_get_all_assets</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Note: This is a legacy endpoint, consider using [this endpoint](https://developers.samsara.com/reference/listassets) instead. The endpoint will continue to function as documented.** 

 Fetch all powered and unpowered equipment. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Equipment** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.legacy.v_1_get_all_assets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.v_20250611.messages.<a href="src/samsara/v_20250611/messages/client.py">v_1_get_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get all messages. 

 <b>Rate limit:</b> 75 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.messages.v_1_get_messages(
    end_ms=1000000,
    duration_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**duration_ms:** `typing.Optional[int]` — Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.messages.<a href="src/samsara/v_20250611/messages/client.py">v_1_create_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Send a message to a list of driver ids. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.messages.v_1_create_messages(
    driver_ids=[111, 222, 333],
    text="This is a message.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**driver_ids:** `typing.Sequence[int]` — IDs of the drivers for whom the messages are sent to.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text sent in the message. Max 2500 characters allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trailer Assignments
<details><summary><code>client.v_20250611.trailer_assignments.<a href="src/samsara/v_20250611/trailer_assignments/client.py">v_1_get_all_trailer_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for all trailers in your organization. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailer_assignments.v_1_get_all_trailer_assignments(
    start_ms=1000000,
    end_ms=1000000,
    limit=1000000,
    starting_after="startingAfter",
    ending_before="endingBefore",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_ms:** `typing.Optional[int]` — Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[str]` — Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.trailer_assignments.<a href="src/samsara/v_20250611/trailer_assignments/client.py">v_1_get_fleet_trailer_assignments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Fetch trailer assignment data for a single trailer. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trailer_assignments.v_1_get_fleet_trailer_assignments(
    trailer_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**trailer_id:** `int` — ID of trailer. Must contain only digits 0-9.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `typing.Optional[int]` — Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `typing.Optional[int]` — Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trips
<details><summary><code>client.v_20250611.trips.<a href="src/samsara/v_20250611/trips/client.py">v_1_get_fleet_trips</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical trips data for specified vehicle. This method returns a set of historical trips data for the specified vehicle in the specified time range. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Read Vehicle Trips** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.trips.v_1_get_fleet_trips(
    vehicle_id=1000000,
    start_ms=1000000,
    end_ms=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vehicle_id:** `int` — Vehicle ID to query.
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time. Limited to a 90 day window with respect to startMs and endMs
    
</dd>
</dl>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sensors
<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors_cargo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get cargo monitor status (empty / full) for requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors_cargo(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors_door</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get door monitor status (closed / open) for requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors_door(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get historical data for specified sensors. This method returns a set of historical data for the specified sensors in the specified time range and at the specified time resolution. 

 <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>). 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara
from samsara.v_20250611 import V1SensorsHistorySeries

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors_history(
    end_ms=1462881998034,
    series=[
        V1SensorsHistorySeries(
            field="ambientTemperature",
            widget_id=1,
        )
    ],
    start_ms=1462878398034,
    step_ms=3600000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_ms:** `int` — End of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**series:** `typing.Sequence[V1SensorsHistorySeries]` 
    
</dd>
</dl>

<dl>
<dd>

**start_ms:** `int` — Beginning of the time range, specified in milliseconds UNIX time.
    
</dd>
</dl>

<dl>
<dd>

**step_ms:** `int` — Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.
    
</dd>
</dl>

<dl>
<dd>

**fill_missing:** `typing.Optional[InlineObject6FillMissing]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors_humidity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get humidity for requested sensors. This method returns the current relative humidity for the requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors_humidity(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get sensor objects. This method returns a list of the sensor objects in the Samsara Cloud and information about them. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.sensors.<a href="src/samsara/v_20250611/sensors/client.py">v_1_get_sensors_temperature</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<n class="warning">
<nh>
<i class="fa fa-exclamation-circle"></i>
This endpoint is still on our legacy API.
</nh>
</n>

Get temperature for requested sensors. This method returns the current ambient temperature (and probe temperature if applicable) for the requested sensors. 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

To use this endpoint, select **Write Sensors** under the Equipment category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.sensors.v_1_get_sensors_temperature(
    sensors=[122],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensors:** `typing.Sequence[int]` — List of sensor IDs to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Webhooks
<details><summary><code>client.v_20250611.webhooks.<a href="src/samsara/v_20250611/webhooks/client.py">list_webhooks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all webhooks belonging to a specific org.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.webhooks.list_webhooks(
    ids="ids",
    limit=1,
    after="after",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ids:** `typing.Optional[str]` —  A filter on the data based on this comma-separated list of webhook IDs. Example: `ids=49412323223,49412329928`
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The limit for how many objects will be in the response. Default and max for this value is 512 objects.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` —  If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.webhooks.<a href="src/samsara/v_20250611/webhooks/client.py">post_webhooks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.webhooks.post_webhooks(
    name="Webhook-123",
    url="https://www.Webhook-123.com/webhook/listener",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**custom_headers:** `typing.Optional[typing.Sequence[CustomHeadersObjectRequestBody]]` — The list of custom headers that users can include with their request
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[WebhooksPostWebhooksRequestBodyEventTypesItem]]` — [beta] The list of event types associated with a particular event type
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[WebhooksPostWebhooksRequestBodyVersion]` — The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.webhooks.<a href="src/samsara/v_20250611/webhooks/client.py">get_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a webhook with given ID.

 <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Read Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.webhooks.get_webhook(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the webhook. This is the Samsara-specified ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.webhooks.<a href="src/samsara/v_20250611/webhooks/client.py">delete_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook with the given ID.

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.webhooks.delete_webhook(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v_20250611.webhooks.<a href="src/samsara/v_20250611/webhooks/client.py">patch_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific webhook's information.  **Note** this implementation of patch uses [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
 This means that any fields included in the patch request will _overwrite_ fields which exist on the target resource.
 For arrays, this means any array included in the request will _replace_ the array that exists at the specified path, it will not _add_ to the existing array

 <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

To use this endpoint, select **Write Webhooks** under the Setup & Administration category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>
 

 **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.webhooks.patch_webhook(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_headers:** `typing.Optional[typing.Sequence[CustomHeadersObjectRequestBody]]` — The list of custom headers that users can include with their request
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The  name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[WebhooksPatchWebhookRequestBodyVersion]` — The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V20250611 Fleet Attributes
<details><summary><code>client.v_20250611.fleet.attributes.<a href="src/samsara/v_20250611/fleet/attributes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from samsara import Samsara

client = Samsara(
    token="YOUR_TOKEN",
)
client.v_20250611.fleet.attributes.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

