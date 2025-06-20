# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .driver_with_external_id_object_response_body import DriverWithExternalIdObjectResponseBody


class CoachAssignmentWithDriverExternalIdsResponseResponseBody(UniversalBaseModel):
    """
    Driver coach assignment object.
    """

    coach_id: typing_extensions.Annotated[str, FieldMetadata(alias="coachId")] = pydantic.Field()
    """
    Coach ID associated with coach assignment. Always returned.
    """

    created_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Time coach assignment was created in UTC. Always returned.
    """

    driver: DriverWithExternalIdObjectResponseBody
    updated_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Time coaching assignment was updated in UTC. Always returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
