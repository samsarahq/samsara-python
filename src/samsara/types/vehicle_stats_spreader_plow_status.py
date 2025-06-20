# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .time import Time
from .vehicle_stats_spreader_plow_status_value import VehicleStatsSpreaderPlowStatusValue


class VehicleStatsSpreaderPlowStatus(UniversalBaseModel):
    """
    Snow plow status (`Up` or `Down`), as read from the material spreader. Note: this is separate from plow status defined via auxInput.
    """

    time: Time
    value: VehicleStatsSpreaderPlowStatusValue = pydantic.Field()
    """
    Snow plow status, as read from the material spreader
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
