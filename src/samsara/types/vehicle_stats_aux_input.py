# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vehicle_aux_input_name import VehicleAuxInputName
from .vehicle_stats_aux_input_time import VehicleStatsAuxInputTime


class VehicleStatsAuxInput(UniversalBaseModel):
    """
    Data for auxiliary digio equipment.
    """

    name: typing.Optional[VehicleAuxInputName] = None
    time: typing.Optional[VehicleStatsAuxInputTime] = None
    value: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean indicating the state of the auxiliary equipment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
