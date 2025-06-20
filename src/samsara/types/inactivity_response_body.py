# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_object_onvif_camera_stream_response_body import AlertObjectOnvifCameraStreamResponseBody


class InactivityResponseBody(UniversalBaseModel):
    """
    Details specific to Inactivity.
    """

    camera_stream: typing_extensions.Annotated[
        typing.Optional[AlertObjectOnvifCameraStreamResponseBody], FieldMetadata(alias="cameraStream")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
