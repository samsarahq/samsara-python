# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SpeedResponseResponseBody(UniversalBaseModel):
    """
    Speed object.
    """

    ecu_speed_meters_per_second: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="ecuSpeedMetersPerSecond")
    ] = pydantic.Field(default=None)
    """
    Speed of asset based on ECU data.
    """

    gps_speed_meters_per_second: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="gpsSpeedMetersPerSecond")
    ] = pydantic.Field(default=None)
    """
    Speed of asset based on GPS data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
