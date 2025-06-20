# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .camera_details_response_response_body import CameraDetailsResponseResponseBody
from .gateway_details_response_response_body import GatewayDetailsResponseResponseBody


class HealthDetailsResponseResponseBody(UniversalBaseModel):
    """
    Detailed health related metadata for the device.
    """

    camera_details: typing_extensions.Annotated[
        typing.Optional[CameraDetailsResponseResponseBody], FieldMetadata(alias="cameraDetails")
    ] = None
    gateway_details: typing_extensions.Annotated[
        typing.Optional[GatewayDetailsResponseResponseBody], FieldMetadata(alias="gatewayDetails")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
