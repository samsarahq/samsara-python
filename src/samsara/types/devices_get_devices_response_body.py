# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_response_response_body import DeviceResponseResponseBody
from .goa_pagination_response_response_body import GoaPaginationResponseResponseBody


class DevicesGetDevicesResponseBody(UniversalBaseModel):
    data: typing.List[DeviceResponseResponseBody] = pydantic.Field()
    """
    List of device objects.
    """

    pagination: GoaPaginationResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
