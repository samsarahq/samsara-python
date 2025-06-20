# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .equipment_time import EquipmentTime


class EquipmentObdEngineSeconds(UniversalBaseModel):
    """
    Engine seconds reading from on-board diagnostics.
    """

    time: EquipmentTime
    value: int = pydantic.Field()
    """
    The number of seconds the engine has been running as reported directly from on-board diagnostics. This is supported with the following hardware configurations: AG24/AG26 + AOPEN/A9PIN/ACT9/ACT14
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
