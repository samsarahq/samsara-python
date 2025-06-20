# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DriverAssignmentMetadataTinyObjectResponseBody(UniversalBaseModel):
    """
    Metadata object for external assignment source data.
    """

    source_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sourceName")] = pydantic.Field(
        default=None
    )
    """
    Assigned source name from an external source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
