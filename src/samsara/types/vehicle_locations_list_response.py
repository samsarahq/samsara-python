# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_response import PaginationResponse
from .vehicle_locations_list_response_data import VehicleLocationsListResponseData


class VehicleLocationsListResponse(UniversalBaseModel):
    """
    List of vehicle location events and pagination info.
    """

    data: typing.List[VehicleLocationsListResponseData] = pydantic.Field()
    """
    A list of vehicles and an array of location events for each vehicle.
    """

    pagination: PaginationResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
