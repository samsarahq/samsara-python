# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fuel_purchase_post_fuel_purchase_response_body import FuelPurchasePostFuelPurchaseResponseBody
from ..types.post_fuel_purchase_request_body_price_request_body import PostFuelPurchaseRequestBodyPriceRequestBody
from .raw_client import AsyncRawFuelPurchasesClient, RawFuelPurchasesClient
from .types.fuel_purchase_post_fuel_purchase_request_body_ifta_fuel_type import (
    FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType,
)

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FuelPurchasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFuelPurchasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFuelPurchasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFuelPurchasesClient
        """
        return self._raw_client

    def create(
        self,
        *,
        fuel_quantity_liters: str,
        transaction_location: str,
        transaction_price: PostFuelPurchaseRequestBodyPriceRequestBody,
        transaction_reference: str,
        transaction_time: str,
        ifta_fuel_type: typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType] = OMIT,
        vehicle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FuelPurchasePostFuelPurchaseResponseBody:
        """
        Create a fuel purchase transaction.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        fuel_quantity_liters : str
            The amount of fuel purchased in liters.

        transaction_location : str
            The full street address for the location of the fuel transaction, as it might be recognized by Google Maps. Ideal entries should be in accordance with the format used by the national postal service of the country concerned (example: 1 De Haro St, San Francisco, CA 94107, United States). Alternatively, exact latitude/longitude can be provided (example: 40.748441, -73.985664).

        transaction_price : PostFuelPurchaseRequestBodyPriceRequestBody

        transaction_reference : str
            The fuel transaction reference. This is the transaction identifier. For instance, this can be the Serial Number on the invoice.

        transaction_time : str
            The time of the fuel transaction in RFC 3339 format. Timezone must be specified. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        ifta_fuel_type : typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType]
            The type of fuel purchased supported by IFTA.  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`

        vehicle_id : typing.Optional[str]
            Samsara ID of the vehicle that purchased the fuel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FuelPurchasePostFuelPurchaseResponseBody
            OK response.

        Examples
        --------
        from samsara import PostFuelPurchaseRequestBodyPriceRequestBody, Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.fuel_purchases.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price=PostFuelPurchaseRequestBodyPriceRequestBody(
                amount="640.2",
                currency="usd",
            ),
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        )
        """
        _response = self._raw_client.create(
            fuel_quantity_liters=fuel_quantity_liters,
            transaction_location=transaction_location,
            transaction_price=transaction_price,
            transaction_reference=transaction_reference,
            transaction_time=transaction_time,
            ifta_fuel_type=ifta_fuel_type,
            vehicle_id=vehicle_id,
            request_options=request_options,
        )
        return _response.data


class AsyncFuelPurchasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFuelPurchasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFuelPurchasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFuelPurchasesClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        fuel_quantity_liters: str,
        transaction_location: str,
        transaction_price: PostFuelPurchaseRequestBodyPriceRequestBody,
        transaction_reference: str,
        transaction_time: str,
        ifta_fuel_type: typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType] = OMIT,
        vehicle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FuelPurchasePostFuelPurchaseResponseBody:
        """
        Create a fuel purchase transaction.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        fuel_quantity_liters : str
            The amount of fuel purchased in liters.

        transaction_location : str
            The full street address for the location of the fuel transaction, as it might be recognized by Google Maps. Ideal entries should be in accordance with the format used by the national postal service of the country concerned (example: 1 De Haro St, San Francisco, CA 94107, United States). Alternatively, exact latitude/longitude can be provided (example: 40.748441, -73.985664).

        transaction_price : PostFuelPurchaseRequestBodyPriceRequestBody

        transaction_reference : str
            The fuel transaction reference. This is the transaction identifier. For instance, this can be the Serial Number on the invoice.

        transaction_time : str
            The time of the fuel transaction in RFC 3339 format. Timezone must be specified. For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

        ifta_fuel_type : typing.Optional[FuelPurchasePostFuelPurchaseRequestBodyIftaFuelType]
            The type of fuel purchased supported by IFTA.  Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`

        vehicle_id : typing.Optional[str]
            Samsara ID of the vehicle that purchased the fuel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FuelPurchasePostFuelPurchaseResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara, PostFuelPurchaseRequestBodyPriceRequestBody

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.fuel_purchases.create(
                fuel_quantity_liters="676.8",
                transaction_location="350 Rhode Island St, San Francisco, CA 94103",
                transaction_price=PostFuelPurchaseRequestBodyPriceRequestBody(
                    amount="640.2",
                    currency="usd",
                ),
                transaction_reference="5454534",
                transaction_time="2022-07-13T14:20:50.52-07:00",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            fuel_quantity_liters=fuel_quantity_liters,
            transaction_location=transaction_location,
            transaction_price=transaction_price,
            transaction_reference=transaction_reference,
            transaction_time=transaction_time,
            ifta_fuel_type=ifta_fuel_type,
            vehicle_id=vehicle_id,
            request_options=request_options,
        )
        return _response.data
