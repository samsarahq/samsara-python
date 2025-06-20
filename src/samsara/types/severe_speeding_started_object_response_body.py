# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vehicle_response_response_body import VehicleResponseResponseBody


class SevereSpeedingStartedObjectResponseBody(UniversalBaseModel):
    """
    The start of a severe speeding event
    """

    start_time: typing_extensions.Annotated[str, FieldMetadata(alias="startTime")] = pydantic.Field()
    """
    The speeding start time in RFC 3339 format (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    trip_start_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tripStartTime")] = (
        pydantic.Field(default=None)
    )
    """
    The trip start time in RFC 3339 format (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    vehicle: VehicleResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
