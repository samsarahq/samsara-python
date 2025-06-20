# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.inline_response_2005 import InlineResponse2005
from ..types.inline_response_2006 import InlineResponse2006
from .raw_client import AsyncRawV1MessagesClient, RawV1MessagesClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1MessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1MessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1MessagesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        end_ms: typing.Optional[int] = None,
        duration_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2005:
        """
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

        Parameters
        ----------
        end_ms : typing.Optional[int]
            Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.

        duration_ms : typing.Optional[int]
            Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2005
            Returns the fetched messages from most recently sent to least recently sent.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.v_1_messages.list()
        """
        _response = self._raw_client.list(end_ms=end_ms, duration_ms=duration_ms, request_options=request_options)
        return _response.data

    def create(
        self, *, driver_ids: typing.Sequence[int], text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InlineResponse2006:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Send a message to a list of driver ids.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        driver_ids : typing.Sequence[int]
            IDs of the drivers for whom the messages are sent to.

        text : str
            The text sent in the message. Max 2500 characters allowed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2006
            Returns the created messages.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.v_1_messages.create(
            driver_ids=[111, 222, 333],
            text="This is a message.",
        )
        """
        _response = self._raw_client.create(driver_ids=driver_ids, text=text, request_options=request_options)
        return _response.data


class AsyncV1MessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1MessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1MessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1MessagesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        end_ms: typing.Optional[int] = None,
        duration_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InlineResponse2005:
        """
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

        Parameters
        ----------
        end_ms : typing.Optional[int]
            Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.

        duration_ms : typing.Optional[int]
            Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2005
            Returns the fetched messages from most recently sent to least recently sent.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.v_1_messages.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(end_ms=end_ms, duration_ms=duration_ms, request_options=request_options)
        return _response.data

    async def create(
        self, *, driver_ids: typing.Sequence[int], text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InlineResponse2006:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Send a message to a list of driver ids.

         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>

        Parameters
        ----------
        driver_ids : typing.Sequence[int]
            IDs of the drivers for whom the messages are sent to.

        text : str
            The text sent in the message. Max 2500 characters allowed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InlineResponse2006
            Returns the created messages.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.v_1_messages.create(
                driver_ids=[111, 222, 333],
                text="This is a message.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(driver_ids=driver_ids, text=text, request_options=request_options)
        return _response.data
