# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pagination import AsyncPager, BaseHttpResponse, SyncPager
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.carrier_proposed_assignment import CarrierProposedAssignment
from ..types.carrier_proposed_assignment_response import CarrierProposedAssignmentResponse
from ..types.list_carrier_proposed_assignment_response import ListCarrierProposedAssignmentResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCarrierProposedAssignmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        active_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[CarrierProposedAssignment]:
        """
        Show the assignments created by the POST fleet/carrier-proposed-assignments. This endpoint will only show the assignments that are active for drivers and currently visible to them in the driver app. Once a proposed assignment has been accepted, the endpoint will not return any data.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        limit : typing.Optional[int]
            The limit for how many objects will be in the response. Default and max for this value is 512 objects.

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        active_time : typing.Optional[str]
            If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[CarrierProposedAssignment]
            Returns the assignments that drivers would see in the future, if any.
        """
        _response = self._client_wrapper.httpx_client.request(
            "fleet/carrier-proposed-assignments",
            method="GET",
            params={
                "limit": limit,
                "after": after,
                "driverIds": driver_ids,
                "activeTime": active_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCarrierProposedAssignmentResponse,
                    parse_obj_as(
                        type_=ListCarrierProposedAssignmentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.end_cursor
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        limit=limit,
                        after=_parsed_next,
                        driver_ids=driver_ids,
                        active_time=active_time,
                        request_options=request_options,
                    )
                return SyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        active_time: typing.Optional[str] = OMIT,
        shipping_docs: typing.Optional[str] = OMIT,
        trailer_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        trailer_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CarrierProposedAssignmentResponse]:
        """
        Creates a new assignment that a driver can later use. Each driver can only have one future assignment.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        driver_id : str
            ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver.

        vehicle_id : str
            ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle.

        active_time : typing.Optional[str]
            Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.

        shipping_docs : typing.Optional[str]
            Shipping Documents that this assignment will propose to the driver.

        trailer_ids : typing.Optional[typing.Sequence[str]]
            IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)

        trailer_names : typing.Optional[typing.Sequence[str]]
            Names of trailers to propose. (forbidden if trailerIds is set)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CarrierProposedAssignmentResponse]
            Return the created assignment
        """
        _response = self._client_wrapper.httpx_client.request(
            "fleet/carrier-proposed-assignments",
            method="POST",
            json={
                "activeTime": active_time,
                "driverId": driver_id,
                "shippingDocs": shipping_docs,
                "trailerIds": trailer_ids,
                "trailerNames": trailer_names,
                "vehicleId": vehicle_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CarrierProposedAssignmentResponse,
                    parse_obj_as(
                        type_=CarrierProposedAssignmentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Permanently delete an assignment. You can only delete assignments that are not yet active. To override a currently active assignment, create a new empty one, instead.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        id : str
            ID of the assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            A successful DELETE response is a 204 with no content.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleet/carrier-proposed-assignments/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCarrierProposedAssignmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        active_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[CarrierProposedAssignment]:
        """
        Show the assignments created by the POST fleet/carrier-proposed-assignments. This endpoint will only show the assignments that are active for drivers and currently visible to them in the driver app. Once a proposed assignment has been accepted, the endpoint will not return any data.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        limit : typing.Optional[int]
            The limit for how many objects will be in the response. Default and max for this value is 512 objects.

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        active_time : typing.Optional[str]
            If specified, shows assignments that will be active at this time. Defaults to now, which would show current active assignments. In RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[CarrierProposedAssignment]
            Returns the assignments that drivers would see in the future, if any.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fleet/carrier-proposed-assignments",
            method="GET",
            params={
                "limit": limit,
                "after": after,
                "driverIds": driver_ids,
                "activeTime": active_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListCarrierProposedAssignmentResponse,
                    parse_obj_as(
                        type_=ListCarrierProposedAssignmentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.end_cursor
                    _has_next = _parsed_next is not None and _parsed_next != ""

                    async def _get_next():
                        return await self.list(
                            limit=limit,
                            after=_parsed_next,
                            driver_ids=driver_ids,
                            active_time=active_time,
                            request_options=request_options,
                        )

                return AsyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        active_time: typing.Optional[str] = OMIT,
        shipping_docs: typing.Optional[str] = OMIT,
        trailer_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        trailer_names: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CarrierProposedAssignmentResponse]:
        """
        Creates a new assignment that a driver can later use. Each driver can only have one future assignment.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        driver_id : str
            ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver.

        vehicle_id : str
            ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle.

        active_time : typing.Optional[str]
            Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.

        shipping_docs : typing.Optional[str]
            Shipping Documents that this assignment will propose to the driver.

        trailer_ids : typing.Optional[typing.Sequence[str]]
            IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)

        trailer_names : typing.Optional[typing.Sequence[str]]
            Names of trailers to propose. (forbidden if trailerIds is set)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CarrierProposedAssignmentResponse]
            Return the created assignment
        """
        _response = await self._client_wrapper.httpx_client.request(
            "fleet/carrier-proposed-assignments",
            method="POST",
            json={
                "activeTime": active_time,
                "driverId": driver_id,
                "shippingDocs": shipping_docs,
                "trailerIds": trailer_ids,
                "trailerNames": trailer_names,
                "vehicleId": vehicle_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CarrierProposedAssignmentResponse,
                    parse_obj_as(
                        type_=CarrierProposedAssignmentResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Permanently delete an assignment. You can only delete assignments that are not yet active. To override a currently active assignment, create a new empty one, instead.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        id : str
            ID of the assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            A successful DELETE response is a 204 with no content.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleet/carrier-proposed-assignments/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
