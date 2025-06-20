# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .equipment_stats_response_data import EquipmentStatsResponseData
from .pagination_response import PaginationResponse


class EquipmentStatsResponse(UniversalBaseModel):
    """
    The most recent equipment stats and pagination information
    """

    data: typing.List[EquipmentStatsResponseData] = pydantic.Field()
    """
    List of the most recent stats for the specified units of equipment and stat types.
    """

    pagination: PaginationResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
