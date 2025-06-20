# This file was auto-generated by Fern from our API Definition.

import typing

from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.request_options import RequestOptions
from ....types.fuel_energy_get_fuel_energy_driver_reports_response_body import (
    FuelEnergyGetFuelEnergyDriverReportsResponseBody,
)
from .raw_client import AsyncRawFuelEnergyClient, RawFuelEnergyClient


class FuelEnergyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFuelEnergyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFuelEnergyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFuelEnergyClient
        """
        return self._raw_client

    def list(
        self,
        *,
        start_date: str,
        end_date: str,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FuelEnergyGetFuelEnergyDriverReportsResponseBody:
        """
        Get fuel and energy efficiency driver reports for the requested time range.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_date : str
            A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        end_date : str
            An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
             A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        parent_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FuelEnergyGetFuelEnergyDriverReportsResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.reports.drivers.fuel_energy.list(
            start_date="startDate",
            end_date="endDate",
        )
        """
        _response = self._raw_client.list(
            start_date=start_date,
            end_date=end_date,
            driver_ids=driver_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            after=after,
            request_options=request_options,
        )
        return _response.data


class AsyncFuelEnergyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFuelEnergyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFuelEnergyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFuelEnergyClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        start_date: str,
        end_date: str,
        driver_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag_ids: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FuelEnergyGetFuelEnergyDriverReportsResponseBody:
        """
        Get fuel and energy efficiency driver reports for the requested time range.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_date : str
            A start date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        end_date : str
            An end date in RFC 3339 format. This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time zone is passed in, then the UTC time zone will be used. This parameter is inclusive, so data on the date specified will be considered. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        driver_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
             A filter on the data based on this comma-separated list of driver IDs and externalIds. Example: `driverIds=1234,5678,payroll:4841`

        tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        parent_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FuelEnergyGetFuelEnergyDriverReportsResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.drivers.fuel_energy.list(
                start_date="startDate",
                end_date="endDate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            start_date=start_date,
            end_date=end_date,
            driver_ids=driver_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            after=after,
            request_options=request_options,
        )
        return _response.data
