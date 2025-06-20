# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .coach_assignment_without_driver_external_ids_response_response_body import (
    CoachAssignmentWithoutDriverExternalIdsResponseResponseBody,
)


class DriverCoachAssignmentsPutDriverCoachAssignmentResponseBody(UniversalBaseModel):
    data: CoachAssignmentWithoutDriverExternalIdsResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
