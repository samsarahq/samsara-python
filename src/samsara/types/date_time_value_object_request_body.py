# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DateTimeValueObjectRequestBody(UniversalBaseModel):
    """
    The value of a date time field. Only present for date time fields.
    """

    date_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="dateTime")] = (
        pydantic.Field(default=None)
    )
    """
    Date time value inin RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
