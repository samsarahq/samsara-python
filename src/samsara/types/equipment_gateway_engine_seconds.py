# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .equipment_time import EquipmentTime


class EquipmentGatewayEngineSeconds(UniversalBaseModel):
    """
    Engine seconds reading from the aux/digio cable.
    """

    time: EquipmentTime
    value: int = pydantic.Field()
    """
    The number of seconds an engine has been running as detected via engine state. Used in combination with an offset provided manually through the Samsara cloud dashboard. Useful for when assets do not report engine hours over the J1939 network. The Engine Speed SPN must be available from the ECU for this parameter to properly calculate seconds. This is supported with the following hardware configurations: AG24/AG26 + AOPEN/A9PIN/ACT9/ACT14.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
