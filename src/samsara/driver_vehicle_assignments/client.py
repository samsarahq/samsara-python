# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.driver_vehicle_assignments_v_2_create_driver_vehicle_assignment_response_body import (
    DriverVehicleAssignmentsV2CreateDriverVehicleAssignmentResponseBody,
)
from ..types.driver_vehicle_assignments_v_2_get_driver_vehicle_assignments_response_body import (
    DriverVehicleAssignmentsV2GetDriverVehicleAssignmentsResponseBody,
)
from ..types.driver_vehicle_assignments_v_2_update_driver_vehicle_assignment_response_body import (
    DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody,
)
from ..types.patch_driver_vehicle_assignments_v_2_request_body_metadata_request_body import (
    PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody,
)
from ..types.post_driver_vehicle_assignments_v_2_request_body_metadata_request_body import (
    PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody,
)
from .raw_client import AsyncRawDriverVehicleAssignmentsClient, RawDriverVehicleAssignmentsClient
from .types.driver_vehicle_assignments_get_request_assignment_type import (
    DriverVehicleAssignmentsGetRequestAssignmentType,
)
from .types.driver_vehicle_assignments_get_request_filter_by import DriverVehicleAssignmentsGetRequestFilterBy

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DriverVehicleAssignmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDriverVehicleAssignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDriverVehicleAssignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDriverVehicleAssignmentsClient
        """
        return self._raw_client

    def get(
        self,
        *,
        filter_by: DriverVehicleAssignmentsGetRequestFilterBy,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        driver_tag_ids: typing.Optional[str] = None,
        vehicle_tag_ids: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        assignment_type: typing.Optional[DriverVehicleAssignmentsGetRequestAssignmentType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2GetDriverVehicleAssignmentsResponseBody:
        """
        Get all driver-vehicle assignments for the requested drivers or vehicles in the requested time range. To fetch driver-vehicle assignments out of the vehicle trips' time ranges, assignmentType needs to be specified. Note: this endpoint replaces past endpoints to fetch assignments by driver or by vehicle. Visit [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints) for more information.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        filter_by : DriverVehicleAssignmentsGetRequestFilterBy
            Option to filter by drivers or vehicles.  Valid values: `drivers`, `vehicles`

        start_time : typing.Optional[str]
             A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
             A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".

        driver_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`

        vehicle_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of vehicle tag IDs. Example: `tagIds=1234,5678`

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        assignment_type : typing.Optional[DriverVehicleAssignmentsGetRequestAssignmentType]
            Specifies which assignment type to filter by.  Valid values: `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2GetDriverVehicleAssignmentsResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.driver_vehicle_assignments.get(
            filter_by="drivers",
        )
        """
        _response = self._raw_client.get(
            filter_by=filter_by,
            start_time=start_time,
            end_time=end_time,
            driver_ids=driver_ids,
            vehicle_ids=vehicle_ids,
            driver_tag_ids=driver_tag_ids,
            vehicle_tag_ids=vehicle_tag_ids,
            after=after,
            assignment_type=assignment_type,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2CreateDriverVehicleAssignmentResponseBody:
        """
        Assign vehicle drive-time to a driver via API. For a step-by-step instruction on how to leverage this endpoint, see [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        driver_id : str
            ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
            The time at which the assignment was made in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
            The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing assignment) if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Is this driver a passenger? Defaults to false if not provided

        metadata : typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]

        start_time : typing.Optional[str]
            The start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2CreateDriverVehicleAssignmentResponseBody
            Created response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.driver_vehicle_assignments.create(
            driver_id="494123",
            vehicle_id="281474978683353",
        )
        """
        _response = self._raw_client.create(
            driver_id=driver_id,
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            metadata=metadata,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        *,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete driver assignments that were created using the `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in the requested time range.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
             Assigned at time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Indicates if assigned driver is passenger

        start_time : typing.Optional[str]
             A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.driver_vehicle_assignments.delete(
            vehicle_id="281474978683353",
        )
        """
        _response = self._raw_client.delete(
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    def update(
        self,
        *,
        driver_id: str,
        start_time: str,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody:
        """
        Update driver assignments that were created using the `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time must match an existing assignment.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        driver_id : str
            ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

        start_time : str
            The start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
            The time at which the assignment was made in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
            The end time in RFC 3339 format. To make this an ongoing assignment (ie. an assignment with no end time), provide an endTime value of 'null'. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Is this driver a passenger?

        metadata : typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody
            Accepted response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.driver_vehicle_assignments.update(
            driver_id="494123",
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="281474978683353",
        )
        """
        _response = self._raw_client.update(
            driver_id=driver_id,
            start_time=start_time,
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data


class AsyncDriverVehicleAssignmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDriverVehicleAssignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDriverVehicleAssignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDriverVehicleAssignmentsClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        filter_by: DriverVehicleAssignmentsGetRequestFilterBy,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        driver_tag_ids: typing.Optional[str] = None,
        vehicle_tag_ids: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        assignment_type: typing.Optional[DriverVehicleAssignmentsGetRequestAssignmentType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2GetDriverVehicleAssignmentsResponseBody:
        """
        Get all driver-vehicle assignments for the requested drivers or vehicles in the requested time range. To fetch driver-vehicle assignments out of the vehicle trips' time ranges, assignmentType needs to be specified. Note: this endpoint replaces past endpoints to fetch assignments by driver or by vehicle. Visit [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints) for more information.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        filter_by : DriverVehicleAssignmentsGetRequestFilterBy
            Option to filter by drivers or vehicles.  Valid values: `drivers`, `vehicles`

        start_time : typing.Optional[str]
             A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
             A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: "key:value". For example, "maintenanceId:250020".

        driver_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of driver tag IDs. Example: `tagIds=1234,5678`

        vehicle_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of vehicle tag IDs. Example: `tagIds=1234,5678`

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        assignment_type : typing.Optional[DriverVehicleAssignmentsGetRequestAssignmentType]
            Specifies which assignment type to filter by.  Valid values: `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2GetDriverVehicleAssignmentsResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.driver_vehicle_assignments.get(
                filter_by="drivers",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            filter_by=filter_by,
            start_time=start_time,
            end_time=end_time,
            driver_ids=driver_ids,
            vehicle_ids=vehicle_ids,
            driver_tag_ids=driver_tag_ids,
            vehicle_tag_ids=vehicle_tag_ids,
            after=after,
            assignment_type=assignment_type,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2CreateDriverVehicleAssignmentResponseBody:
        """
        Assign vehicle drive-time to a driver via API. For a step-by-step instruction on how to leverage this endpoint, see [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        driver_id : str
            ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
            The time at which the assignment was made in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
            The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing assignment) if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Is this driver a passenger? Defaults to false if not provided

        metadata : typing.Optional[PostDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]

        start_time : typing.Optional[str]
            The start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2CreateDriverVehicleAssignmentResponseBody
            Created response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.driver_vehicle_assignments.create(
                driver_id="494123",
                vehicle_id="281474978683353",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            driver_id=driver_id,
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            metadata=metadata,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        *,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete driver assignments that were created using the `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in the requested time range.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
             Assigned at time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Indicates if assigned driver is passenger

        start_time : typing.Optional[str]
             A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.driver_vehicle_assignments.delete(
                vehicle_id="281474978683353",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    async def update(
        self,
        *,
        driver_id: str,
        start_time: str,
        vehicle_id: str,
        assigned_at_time: typing.Optional[str] = OMIT,
        end_time: typing.Optional[str] = OMIT,
        is_passenger: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody:
        """
        Update driver assignments that were created using the `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time must match an existing assignment.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        driver_id : str
            ID of the driver. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

        start_time : str
            The start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        vehicle_id : str
            ID of the vehicle. This can be either a unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

        assigned_at_time : typing.Optional[str]
            The time at which the assignment was made in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : typing.Optional[str]
            The end time in RFC 3339 format. To make this an ongoing assignment (ie. an assignment with no end time), provide an endTime value of 'null'. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        is_passenger : typing.Optional[bool]
            Is this driver a passenger?

        metadata : typing.Optional[PatchDriverVehicleAssignmentsV2RequestBodyMetadataRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody
            Accepted response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.driver_vehicle_assignments.update(
                driver_id="494123",
                start_time="2019-06-13T19:08:25Z",
                vehicle_id="281474978683353",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            driver_id=driver_id,
            start_time=start_time,
            vehicle_id=vehicle_id,
            assigned_at_time=assigned_at_time,
            end_time=end_time,
            is_passenger=is_passenger,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data
