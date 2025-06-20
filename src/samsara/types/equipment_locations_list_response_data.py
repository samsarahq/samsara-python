# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .equipment_id import EquipmentId
from .equipment_location import EquipmentLocation
from .equipment_name import EquipmentName


class EquipmentLocationsListResponseData(UniversalBaseModel):
    """
    A unit of equipment and its time-series of location events.
    """

    id: EquipmentId
    locations: typing.List[EquipmentLocation] = pydantic.Field()
    """
    A time-series of location events for the given unit of equipment.
    """

    name: EquipmentName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
