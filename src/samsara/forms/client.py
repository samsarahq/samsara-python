# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.form_templates_get_form_templates_response_body import FormTemplatesGetFormTemplatesResponseBody
from .raw_client import AsyncRawFormsClient, RawFormsClient


class FormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormsClient
        """
        return self._raw_client

    def get_form_templates(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormTemplatesGetFormTemplatesResponseBody:
        """
        Returns a list of the organization's form templates for the specified list of IDs. If no IDs are provided, all form templates for the organization will be returned.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list containing up to 100 template IDs to filter on.

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormTemplatesGetFormTemplatesResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.forms.get_form_templates()
        """
        _response = self._raw_client.get_form_templates(ids=ids, after=after, request_options=request_options)
        return _response.data


class AsyncFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormsClient
        """
        return self._raw_client

    async def get_form_templates(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormTemplatesGetFormTemplatesResponseBody:
        """
        Returns a list of the organization's form templates for the specified list of IDs. If no IDs are provided, all form templates for the organization will be returned.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Forms category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list containing up to 100 template IDs to filter on.

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormTemplatesGetFormTemplatesResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forms.get_form_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_templates(ids=ids, after=after, request_options=request_options)
        return _response.data
