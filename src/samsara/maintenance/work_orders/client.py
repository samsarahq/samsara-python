# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.request_options import RequestOptions
from ...types.patch_work_orders_response_body import PatchWorkOrdersResponseBody
from ...types.post_work_orders_response_body import PostWorkOrdersResponseBody
from ...types.service_task_instance_input_object_request_body import ServiceTaskInstanceInputObjectRequestBody
from ...types.work_order_discount_object_request_body import WorkOrderDiscountObjectRequestBody
from ...types.work_order_item_object_request_body import WorkOrderItemObjectRequestBody
from ...types.work_order_object_response_body import WorkOrderObjectResponseBody
from ...types.work_order_tax_object_request_body import WorkOrderTaxObjectRequestBody
from .raw_client import AsyncRawWorkOrdersClient, RawWorkOrdersClient
from .types.work_orders_patch_work_orders_request_body_category import WorkOrdersPatchWorkOrdersRequestBodyCategory
from .types.work_orders_patch_work_orders_request_body_priority import WorkOrdersPatchWorkOrdersRequestBodyPriority
from .types.work_orders_patch_work_orders_request_body_status import WorkOrdersPatchWorkOrdersRequestBodyStatus
from .types.work_orders_post_work_orders_request_body_category import WorkOrdersPostWorkOrdersRequestBodyCategory
from .types.work_orders_post_work_orders_request_body_priority import WorkOrdersPostWorkOrdersRequestBodyPriority
from .types.work_orders_stream_request_work_order_statuses_item import WorkOrdersStreamRequestWorkOrderStatusesItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkOrdersClient
        """
        return self._raw_client

    def list(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[WorkOrderObjectResponseBody]:
        """
        Gets work orders.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by the IDs. Up to 100 ids. Returns all if no ids are provided.

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[WorkOrderObjectResponseBody]
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.maintenance.work_orders.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(ids=ids, after=after, request_options=request_options)

    def create(
        self,
        *,
        asset_id: str,
        assigned_user_id: typing.Optional[str] = OMIT,
        category: typing.Optional[WorkOrdersPostWorkOrdersRequestBodyCategory] = OMIT,
        created_by_user_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        discount: typing.Optional[WorkOrderDiscountObjectRequestBody] = OMIT,
        due_at_time: typing.Optional[dt.datetime] = OMIT,
        engine_hours: typing.Optional[int] = OMIT,
        items: typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]] = OMIT,
        odometer_meters: typing.Optional[int] = OMIT,
        priority: typing.Optional[WorkOrdersPostWorkOrdersRequestBodyPriority] = OMIT,
        service_task_instances: typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]] = OMIT,
        tax: typing.Optional[WorkOrderTaxObjectRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWorkOrdersResponseBody:
        """
        Creates a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        asset_id : str
            The ID of the asset.

        assigned_user_id : typing.Optional[str]
            The ID of the assigned mechanic.

        category : typing.Optional[WorkOrdersPostWorkOrdersRequestBodyCategory]
            The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`

        created_by_user_id : typing.Optional[str]
            The ID of the creator of the work order.

        description : typing.Optional[str]
            A description of what needs to be fixed.

        discount : typing.Optional[WorkOrderDiscountObjectRequestBody]

        due_at_time : typing.Optional[dt.datetime]
            The due date of the work order in RFC 3339 format.

        engine_hours : typing.Optional[int]
            The engine hours at the time of the work order. Will default to current asset reading if unset.

        items : typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]
            Items related to the work order.

        odometer_meters : typing.Optional[int]
            The odometer reading at the time of the work order. Will default to current asset reading if unset.

        priority : typing.Optional[WorkOrdersPostWorkOrdersRequestBodyPriority]
            The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`

        service_task_instances : typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]
            Service Tasks for the work order.

        tax : typing.Optional[WorkOrderTaxObjectRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkOrdersResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.maintenance.work_orders.create(
            asset_id="12443",
        )
        """
        _response = self._raw_client.create(
            asset_id=asset_id,
            assigned_user_id=assigned_user_id,
            category=category,
            created_by_user_id=created_by_user_id,
            description=description,
            discount=discount,
            due_at_time=due_at_time,
            engine_hours=engine_hours,
            items=items,
            odometer_meters=odometer_meters,
            priority=priority,
            service_task_instances=service_task_instances,
            tax=tax,
            request_options=request_options,
        )
        return _response.data

    def delete(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        id : str
            The unique id of the work order.

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
        client.maintenance.work_orders.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id=id, request_options=request_options)
        return _response.data

    def update(
        self,
        *,
        id: str,
        assigned_user_id: typing.Optional[str] = OMIT,
        category: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyCategory] = OMIT,
        closing_notes: typing.Optional[str] = OMIT,
        completed_at_time: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        discount: typing.Optional[WorkOrderDiscountObjectRequestBody] = OMIT,
        due_at_time: typing.Optional[dt.datetime] = OMIT,
        engine_hours: typing.Optional[int] = OMIT,
        items: typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]] = OMIT,
        odometer_meters: typing.Optional[int] = OMIT,
        priority: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyPriority] = OMIT,
        service_task_instances: typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]] = OMIT,
        status: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyStatus] = OMIT,
        tax: typing.Optional[WorkOrderTaxObjectRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWorkOrdersResponseBody:
        """
        Updates a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        id : str
            The unique id of the work order.

        assigned_user_id : typing.Optional[str]
            The ID of the assigned mechanic.

        category : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyCategory]
            The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`

        closing_notes : typing.Optional[str]
            Notes on the work order.

        completed_at_time : typing.Optional[dt.datetime]
            The time the work order was completed in RFC 3339 format. Is automatically set when the status changes and this field is not provided.

        description : typing.Optional[str]
            A description of what needs to be fixed.

        discount : typing.Optional[WorkOrderDiscountObjectRequestBody]

        due_at_time : typing.Optional[dt.datetime]
            The due date of the work order in RFC 3339 format.

        engine_hours : typing.Optional[int]
            The engine hours at the time of the work order. Will default to current asset reading if unset.

        items : typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]
            Items related to the work order.

        odometer_meters : typing.Optional[int]
            The odometer reading at the time of the work order. Will default to current asset reading if unset.

        priority : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyPriority]
            The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`

        service_task_instances : typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]
            Service Tasks for the work order.

        status : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyStatus]
            The status of the work order  Valid values: `Assigned`, `Cancelled`, `Closed`, `Completed`, `In Progress`, `On Hold`, `Open`, `Pending Approval`, `Pending Parts`

        tax : typing.Optional[WorkOrderTaxObjectRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWorkOrdersResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.maintenance.work_orders.update(
            id="5",
        )
        """
        _response = self._raw_client.update(
            id=id,
            assigned_user_id=assigned_user_id,
            category=category,
            closing_notes=closing_notes,
            completed_at_time=completed_at_time,
            description=description,
            discount=discount,
            due_at_time=due_at_time,
            engine_hours=engine_hours,
            items=items,
            odometer_meters=odometer_meters,
            priority=priority,
            service_task_instances=service_task_instances,
            status=status,
            tax=tax,
            request_options=request_options,
        )
        return _response.data

    def stream(
        self,
        *,
        start_time: str,
        after: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        work_order_statuses: typing.Optional[
            typing.Union[
                WorkOrdersStreamRequestWorkOrderStatusesItem,
                typing.Sequence[WorkOrdersStreamRequestWorkOrderStatusesItem],
            ]
        ] = None,
        asset_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        assigned_user_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[WorkOrderObjectResponseBody]:
        """
        Stream work orders.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        work_order_statuses : typing.Optional[typing.Union[WorkOrdersStreamRequestWorkOrderStatusesItem, typing.Sequence[WorkOrdersStreamRequestWorkOrderStatusesItem]]]
            Work Order status filter.

        asset_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Work Order asset id filter. Up to 50 ids.

        assigned_user_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Work Order assigned user id filter. Up to 50 ids.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[WorkOrderObjectResponseBody]
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        response = client.maintenance.work_orders.stream(
            start_time="startTime",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.stream(
            start_time=start_time,
            after=after,
            end_time=end_time,
            work_order_statuses=work_order_statuses,
            asset_ids=asset_ids,
            assigned_user_ids=assigned_user_ids,
            request_options=request_options,
        )


class AsyncWorkOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkOrdersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkOrdersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkOrdersClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[WorkOrderObjectResponseBody]:
        """
        Gets work orders.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by the IDs. Up to 100 ids. Returns all if no ids are provided.

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[WorkOrderObjectResponseBody]
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.maintenance.work_orders.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(ids=ids, after=after, request_options=request_options)

    async def create(
        self,
        *,
        asset_id: str,
        assigned_user_id: typing.Optional[str] = OMIT,
        category: typing.Optional[WorkOrdersPostWorkOrdersRequestBodyCategory] = OMIT,
        created_by_user_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        discount: typing.Optional[WorkOrderDiscountObjectRequestBody] = OMIT,
        due_at_time: typing.Optional[dt.datetime] = OMIT,
        engine_hours: typing.Optional[int] = OMIT,
        items: typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]] = OMIT,
        odometer_meters: typing.Optional[int] = OMIT,
        priority: typing.Optional[WorkOrdersPostWorkOrdersRequestBodyPriority] = OMIT,
        service_task_instances: typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]] = OMIT,
        tax: typing.Optional[WorkOrderTaxObjectRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWorkOrdersResponseBody:
        """
        Creates a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        asset_id : str
            The ID of the asset.

        assigned_user_id : typing.Optional[str]
            The ID of the assigned mechanic.

        category : typing.Optional[WorkOrdersPostWorkOrdersRequestBodyCategory]
            The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`

        created_by_user_id : typing.Optional[str]
            The ID of the creator of the work order.

        description : typing.Optional[str]
            A description of what needs to be fixed.

        discount : typing.Optional[WorkOrderDiscountObjectRequestBody]

        due_at_time : typing.Optional[dt.datetime]
            The due date of the work order in RFC 3339 format.

        engine_hours : typing.Optional[int]
            The engine hours at the time of the work order. Will default to current asset reading if unset.

        items : typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]
            Items related to the work order.

        odometer_meters : typing.Optional[int]
            The odometer reading at the time of the work order. Will default to current asset reading if unset.

        priority : typing.Optional[WorkOrdersPostWorkOrdersRequestBodyPriority]
            The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`

        service_task_instances : typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]
            Service Tasks for the work order.

        tax : typing.Optional[WorkOrderTaxObjectRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkOrdersResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.maintenance.work_orders.create(
                asset_id="12443",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            asset_id=asset_id,
            assigned_user_id=assigned_user_id,
            category=category,
            created_by_user_id=created_by_user_id,
            description=description,
            discount=discount,
            due_at_time=due_at_time,
            engine_hours=engine_hours,
            items=items,
            odometer_meters=odometer_meters,
            priority=priority,
            service_task_instances=service_task_instances,
            tax=tax,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        id : str
            The unique id of the work order.

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
            await client.maintenance.work_orders.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id=id, request_options=request_options)
        return _response.data

    async def update(
        self,
        *,
        id: str,
        assigned_user_id: typing.Optional[str] = OMIT,
        category: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyCategory] = OMIT,
        closing_notes: typing.Optional[str] = OMIT,
        completed_at_time: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        discount: typing.Optional[WorkOrderDiscountObjectRequestBody] = OMIT,
        due_at_time: typing.Optional[dt.datetime] = OMIT,
        engine_hours: typing.Optional[int] = OMIT,
        items: typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]] = OMIT,
        odometer_meters: typing.Optional[int] = OMIT,
        priority: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyPriority] = OMIT,
        service_task_instances: typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]] = OMIT,
        status: typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyStatus] = OMIT,
        tax: typing.Optional[WorkOrderTaxObjectRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchWorkOrdersResponseBody:
        """
        Updates a work order.

         <b>Rate limit:</b> 100 requests/min (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        id : str
            The unique id of the work order.

        assigned_user_id : typing.Optional[str]
            The ID of the assigned mechanic.

        category : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyCategory]
            The category of the work order  Valid values: `Annual`, `Corrective`, `Damage Repair`, `Preventive`, `Recall`, `Unspecified`

        closing_notes : typing.Optional[str]
            Notes on the work order.

        completed_at_time : typing.Optional[dt.datetime]
            The time the work order was completed in RFC 3339 format. Is automatically set when the status changes and this field is not provided.

        description : typing.Optional[str]
            A description of what needs to be fixed.

        discount : typing.Optional[WorkOrderDiscountObjectRequestBody]

        due_at_time : typing.Optional[dt.datetime]
            The due date of the work order in RFC 3339 format.

        engine_hours : typing.Optional[int]
            The engine hours at the time of the work order. Will default to current asset reading if unset.

        items : typing.Optional[typing.Sequence[WorkOrderItemObjectRequestBody]]
            Items related to the work order.

        odometer_meters : typing.Optional[int]
            The odometer reading at the time of the work order. Will default to current asset reading if unset.

        priority : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyPriority]
            The priority of the work order  Valid values: `High`, `Low`, `Medium`, `Urgent`

        service_task_instances : typing.Optional[typing.Sequence[ServiceTaskInstanceInputObjectRequestBody]]
            Service Tasks for the work order.

        status : typing.Optional[WorkOrdersPatchWorkOrdersRequestBodyStatus]
            The status of the work order  Valid values: `Assigned`, `Cancelled`, `Closed`, `Completed`, `In Progress`, `On Hold`, `Open`, `Pending Approval`, `Pending Parts`

        tax : typing.Optional[WorkOrderTaxObjectRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWorkOrdersResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.maintenance.work_orders.update(
                id="5",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id=id,
            assigned_user_id=assigned_user_id,
            category=category,
            closing_notes=closing_notes,
            completed_at_time=completed_at_time,
            description=description,
            discount=discount,
            due_at_time=due_at_time,
            engine_hours=engine_hours,
            items=items,
            odometer_meters=odometer_meters,
            priority=priority,
            service_task_instances=service_task_instances,
            status=status,
            tax=tax,
            request_options=request_options,
        )
        return _response.data

    async def stream(
        self,
        *,
        start_time: str,
        after: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        work_order_statuses: typing.Optional[
            typing.Union[
                WorkOrdersStreamRequestWorkOrderStatusesItem,
                typing.Sequence[WorkOrdersStreamRequestWorkOrderStatusesItem],
            ]
        ] = None,
        asset_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        assigned_user_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[WorkOrderObjectResponseBody]:
        """
        Stream work orders.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Work Orders** under the Closed Beta category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_time : str
            A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        work_order_statuses : typing.Optional[typing.Union[WorkOrdersStreamRequestWorkOrderStatusesItem, typing.Sequence[WorkOrdersStreamRequestWorkOrderStatusesItem]]]
            Work Order status filter.

        asset_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Work Order asset id filter. Up to 50 ids.

        assigned_user_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Work Order assigned user id filter. Up to 50 ids.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[WorkOrderObjectResponseBody]
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.maintenance.work_orders.stream(
                start_time="startTime",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.stream(
            start_time=start_time,
            after=after,
            end_time=end_time,
            work_order_statuses=work_order_statuses,
            asset_ids=asset_ids,
            assigned_user_ids=assigned_user_ids,
            request_options=request_options,
        )
