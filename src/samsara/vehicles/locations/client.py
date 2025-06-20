# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.request_options import RequestOptions
from ...types.vehicle_locations_list_response_data import VehicleLocationsListResponseData
from ...types.vehicle_locations_response_data import VehicleLocationsResponseData
from .raw_client import AsyncRawLocationsClient, RawLocationsClient


class LocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        after: typing.Optional[str] = None,
        time: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[VehicleLocationsResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestats) instead.***

        Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        time : typing.Optional[str]
            A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[VehicleLocationsResponseData]
            List of the most recent locations for the specified vehicles.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.vehicles.locations.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            after=after,
            time=time,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )

    def feed(
        self,
        *,
        after: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[VehicleLocationsListResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatsfeed) instead.***

        Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

        Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[VehicleLocationsListResponseData]
            List of locations events for the specified vehicles.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.vehicles.locations.feed()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.feed(
            after=after,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )

    def history(
        self,
        *,
        start_time: str,
        end_time: str,
        after: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[VehicleLocationsListResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatshistory) instead.***

        Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : str
            An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[VehicleLocationsListResponseData]
            List of all locations for the specified vehicles and time range.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.vehicles.locations.history(
            start_time="startTime",
            end_time="endTime",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.history(
            start_time=start_time,
            end_time=end_time,
            after=after,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )


class AsyncLocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        after: typing.Optional[str] = None,
        time: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[VehicleLocationsResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestats) instead.***

        Returns the last known location of all vehicles at the given `time`. If no `time` is specified, the current time is used. This can be optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicles category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        time : typing.Optional[str]
            A filter on the data that returns the last known data points with timestamps less than or equal to this value. Defaults to now if not provided. Must be a string in RFC 3339 format. Millisecond precision and timezones are supported. (Example: `2020-01-27T07:06:25Z`).

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[VehicleLocationsResponseData]
            List of the most recent locations for the specified vehicles.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.vehicles.locations.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            after=after,
            time=time,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )

    async def feed(
        self,
        *,
        after: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[VehicleLocationsListResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatsfeed) instead.***

        Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

        Your first call to this endpoint will provide you with the most recent location for each vehicle and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get location updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest waiting a minimum of 5 seconds before requesting updates.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[VehicleLocationsListResponseData]
            List of locations events for the specified vehicles.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.vehicles.locations.feed()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.feed(
            after=after,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )

    async def history(
        self,
        *,
        start_time: str,
        end_time: str,
        after: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        vehicle_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[VehicleLocationsListResponseData]:
        """
        ***NOTE: The Vehicle Locations API is an older API that does not combine GPS data with onboard diagnostics. Try our new [Vehicle Stats API](ref:getvehiclestatshistory) instead.***

        Returns all known vehicle locations during the given time range. This can be optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle Locations</a>.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        end_time : str
            An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
            If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        parent_tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        tag_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        vehicle_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[VehicleLocationsListResponseData]
            List of all locations for the specified vehicles and time range.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.vehicles.locations.history(
                start_time="startTime",
                end_time="endTime",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.history(
            start_time=start_time,
            end_time=end_time,
            after=after,
            parent_tag_ids=parent_tag_ids,
            tag_ids=tag_ids,
            vehicle_ids=vehicle_ids,
            request_options=request_options,
        )
