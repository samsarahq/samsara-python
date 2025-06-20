# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...types.tachograph_vehicle_files_response import TachographVehicleFilesResponse


class RawVehiclesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def files(
        self,
        *,
        start_time: str,
        end_time: str,
        after: typing.Optional[str] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TachographVehicleFilesResponse]:
        """
        Returns all known tachograph files for all specified vehicles in the time range.

         <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : str
            An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TachographVehicleFilesResponse]
            List of all vehicle tachograph files in a specified time range.
        """
        _response = self._client_wrapper.httpx_client.request(
            "fleet/vehicles/tachograph-files/history",
            method="GET",
            params={
                "after": after,
                "startTime": start_time,
                "endTime": end_time,
                "vehicleIds": vehicle_ids,
                "parentTagIds": parent_tag_ids,
                "tagIds": tag_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TachographVehicleFilesResponse,
                    parse_obj_as(
                        type_=TachographVehicleFilesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVehiclesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def files(
        self,
        *,
        start_time: str,
        end_time: str,
        after: typing.Optional[str] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TachographVehicleFilesResponse]:
        """
        Returns all known tachograph files for all specified vehicles in the time range.

         <b>Rate limit:</b> 150 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Tachograph (EU)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : str
            An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TachographVehicleFilesResponse]
            List of all vehicle tachograph files in a specified time range.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fleet/vehicles/tachograph-files/history",
            method="GET",
            params={
                "after": after,
                "startTime": start_time,
                "endTime": end_time,
                "vehicleIds": vehicle_ids,
                "parentTagIds": parent_tag_ids,
                "tagIds": tag_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TachographVehicleFilesResponse,
                    parse_obj_as(
                        type_=TachographVehicleFilesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
