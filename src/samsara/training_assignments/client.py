# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.training_assignments_get_training_assignments_stream_response_body import (
    TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
)
from .raw_client import AsyncRawTrainingAssignmentsClient, RawTrainingAssignmentsClient


class TrainingAssignmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrainingAssignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrainingAssignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrainingAssignmentsClient
        """
        return self._raw_client

    def stream(
        self,
        *,
        start_time: str,
        after: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        learner_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        course_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody:
        """
        Returns all training assignments data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don't include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_time : str
             A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        learner_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`

        course_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

        status : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated values. If status is present, training assignments for the specified status(s) will be returned. Valid values: "notStarted", "inProgress", "completed". Defaults to returning all courses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody
            OK response.

        Examples
        --------
        from samsara import Samsara

        client = Samsara(
            token="YOUR_TOKEN",
        )
        client.training_assignments.stream(
            start_time="startTime",
        )
        """
        _response = self._raw_client.stream(
            start_time=start_time,
            after=after,
            end_time=end_time,
            learner_ids=learner_ids,
            course_ids=course_ids,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncTrainingAssignmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrainingAssignmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrainingAssignmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrainingAssignmentsClient
        """
        return self._raw_client

    async def stream(
        self,
        *,
        start_time: str,
        after: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        learner_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        course_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody:
        """
        Returns all training assignments data that has been created or modified for your organization based on the time parameters passed in. Results are paginated and are sorted by last modified date. If you include an endTime, the endpoint will return data up until that point (exclusive). If you don't include an endTime, you can continue to poll the API real-time with the pagination cursor that gets returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly available. Reach out to your Samsara Representative to have Training APIs enabled for your organization.

         <b>Rate limit:</b> 5 requests/sec (learn more about rate limits <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Training Assignments** under the Training Assignments category when creating or editing an API token. <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn More.</a>


         **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our support team.

        Parameters
        ----------
        start_time : str
             A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        after : typing.Optional[str]
             If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.

        end_time : typing.Optional[str]
             An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

        learner_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated learner IDs. If learner ID is present, training assignments for the specified learner(s) will be returned. Max value for this value is 100 objects. Example: `learnerIds=driver-281474,driver-46282156`

        course_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated course IDs. If course ID is present, training assignments for the specified course ID(s) will be returned. Max value for this value is 100 objects. Defaults to returning all courses. Example: `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

        status : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional string of comma separated values. If status is present, training assignments for the specified status(s) will be returned. Valid values: "notStarted", "inProgress", "completed". Defaults to returning all courses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody
            OK response.

        Examples
        --------
        import asyncio

        from samsara import AsyncSamsara

        client = AsyncSamsara(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.training_assignments.stream(
                start_time="startTime",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stream(
            start_time=start_time,
            after=after,
            end_time=end_time,
            learner_ids=learner_ids,
            course_ids=course_ids,
            status=status,
            request_options=request_options,
        )
        return _response.data
