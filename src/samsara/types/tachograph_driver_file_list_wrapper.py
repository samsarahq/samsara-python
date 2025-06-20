# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .driver_tiny_response import DriverTinyResponse
from .tachograph_driver_file_list import TachographDriverFileList


class TachographDriverFileListWrapper(UniversalBaseModel):
    driver: typing.Optional[DriverTinyResponse] = None
    files: typing.Optional[TachographDriverFileList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
