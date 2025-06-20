# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.defect_types_response_data_response_body import DefectTypesResponseDataResponseBody
from .raw_client import AsyncRawDefectTypesClient, RawDefectTypesClient


class DefectTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDefectTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDefectTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDefectTypesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[DefectTypesResponseDataResponseBody]:
        """
        Get DVIR defect types.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Defect Types** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        limit : typing.Optional[int]
            The limit for how many objects will be in the response. Default and max for this value is 512 objects.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of defect type IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[DefectTypesResponseDataResponseBody]
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.defect_types.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(after=after, limit=limit, ids=ids, request_options=request_options)


class AsyncDefectTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDefectTypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDefectTypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDefectTypesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[DefectTypesResponseDataResponseBody]:
        """
        Get DVIR defect types.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Defect Types** under the Maintenance category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        limit : typing.Optional[int]
            The limit for how many objects will be in the response. Default and max for this value is 512 objects.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A filter on the data based on this comma-separated list of defect type IDs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[DefectTypesResponseDataResponseBody]
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.defect_types.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(after=after, limit=limit, ids=ids, request_options=request_options)
