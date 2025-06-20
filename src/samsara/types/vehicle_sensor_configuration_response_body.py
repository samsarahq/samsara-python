# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vehicle_sensor_configuration_area_response_body import VehicleSensorConfigurationAreaResponseBody
from .vehicle_sensor_configuration_door_response_body import VehicleSensorConfigurationDoorResponseBody


class VehicleSensorConfigurationResponseBody(UniversalBaseModel):
    """
    The sensors configured on a vehicle
    """

    areas: typing.Optional[typing.List[VehicleSensorConfigurationAreaResponseBody]] = pydantic.Field(default=None)
    """
    Configured sensor areas on the vehicle with its associated sensors
    """

    doors: typing.Optional[typing.List[VehicleSensorConfigurationDoorResponseBody]] = pydantic.Field(default=None)
    """
    Configured door monitors on the vehicle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
