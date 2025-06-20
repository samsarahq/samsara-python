# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Sensor(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    ID of the sensor
    """

    mac: str = pydantic.Field()
    """
    MAC address of the sensor
    """

    name: str = pydantic.Field()
    """
    Name of the sensor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
