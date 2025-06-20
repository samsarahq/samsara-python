# This file was auto-generated by Fern from our API Definition.

import typing

from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.request_options import RequestOptions
from ....types.ifta_get_ifta_jurisdiction_reports_response_body import IftaGetIftaJurisdictionReportsResponseBody
from .raw_client import AsyncRawJurisdictionClient, RawJurisdictionClient
from .types.jurisdiction_get_request_fuel_type import JurisdictionGetRequestFuelType
from .types.jurisdiction_get_request_month import JurisdictionGetRequestMonth
from .types.jurisdiction_get_request_quarter import JurisdictionGetRequestQuarter


class JurisdictionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJurisdictionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJurisdictionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJurisdictionClient
        """
        return self._raw_client

    def get(
        self,
        *,
        year: int,
        month: typing.Optional[JurisdictionGetRequestMonth] = None,
        quarter: typing.Optional[JurisdictionGetRequestQuarter] = None,
        jurisdictions: typing.Optional[str] = None,
        fuel_type: typing.Optional[JurisdictionGetRequestFuelType] = None,
        vehicle_ids: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IftaGetIftaJurisdictionReportsResponseBody:
        """
        Get all jurisdiction IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

        **Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        year : int
             The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`

        month : typing.Optional[JurisdictionGetRequestMonth]
             The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`

        quarter : typing.Optional[JurisdictionGetRequestQuarter]
             The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`

        jurisdictions : typing.Optional[str]
             A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`

        fuel_type : typing.Optional[JurisdictionGetRequestFuelType]
             A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`

        vehicle_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

        tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        parent_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IftaGetIftaJurisdictionReportsResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.reports.ifta.jurisdiction.get(
            year=1,
        )
        """
        _response = self._raw_client.get(
            year=year,
            month=month,
            quarter=quarter,
            jurisdictions=jurisdictions,
            fuel_type=fuel_type,
            vehicle_ids=vehicle_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            request_options=request_options,
        )
        return _response.data


class AsyncJurisdictionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJurisdictionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJurisdictionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJurisdictionClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        year: int,
        month: typing.Optional[JurisdictionGetRequestMonth] = None,
        quarter: typing.Optional[JurisdictionGetRequestQuarter] = None,
        jurisdictions: typing.Optional[str] = None,
        fuel_type: typing.Optional[JurisdictionGetRequestFuelType] = None,
        vehicle_ids: typing.Optional[str] = None,
        tag_ids: typing.Optional[str] = None,
        parent_tag_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IftaGetIftaJurisdictionReportsResponseBody:
        """
        Get all jurisdiction IFTA reports for the requested time duration. Data is returned in your organization's defined timezone.

        **Note:** The most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        year : int
             The year of the requested IFTA report summary. Must be provided with a month or quarter param. Example: `year=2021`

        month : typing.Optional[JurisdictionGetRequestMonth]
             The month of the requested IFTA report summary. Can not be provided with the quarter param. Example: `month=January`  Valid values: `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`

        quarter : typing.Optional[JurisdictionGetRequestQuarter]
             The quarter of the requested IFTA report summary. Can not be provided with the month param. Q1: January, February, March. Q2: April, May, June. Q3: July, August, September. Q4: October, November, December. Example: `quarter=Q1`  Valid values: `Q1`, `Q2`, `Q3`, `Q4`

        jurisdictions : typing.Optional[str]
             A filter on the data based on this comma-separated list of jurisdictions. Example: `jurisdictions=GA`

        fuel_type : typing.Optional[JurisdictionGetRequestFuelType]
             A filter on the data based on this comma-separated list of IFTA fuel types. Example: `fuelType=Diesel`  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`

        vehicle_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

        tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`

        parent_tag_ids : typing.Optional[str]
             A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IftaGetIftaJurisdictionReportsResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.ifta.jurisdiction.get(
                year=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            year=year,
            month=month,
            quarter=quarter,
            jurisdictions=jurisdictions,
            fuel_type=fuel_type,
            vehicle_ids=vehicle_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            request_options=request_options,
        )
        return _response.data
