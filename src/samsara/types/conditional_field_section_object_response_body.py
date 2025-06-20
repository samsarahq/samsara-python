# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConditionalFieldSectionObjectResponseBody(UniversalBaseModel):
    conditional_field_first_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="conditionalFieldFirstIndex")
    ] = pydantic.Field(default=None)
    """
    The index of the first conditional field associated with the triggeringFieldValue in the fieldTypes list.
    """

    conditional_field_last_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="conditionalFieldLastIndex")
    ] = pydantic.Field(default=None)
    """
    The index of the last conditional field associated with the triggeringFieldValue in the fieldTypes list.
    """

    triggering_field_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="triggeringFieldIndex")
    ] = pydantic.Field(default=None)
    """
    The index of the multiple choice field in the fieldTypes list that triggers one or more conditional fields.
    """

    triggering_field_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="triggeringFieldValue")
    ] = pydantic.Field(default=None)
    """
    The multiple choice option value that triggers the conditional fields.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
