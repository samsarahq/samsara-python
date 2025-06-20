# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FormsMultipleChoiceValueObjectResponseBody(UniversalBaseModel):
    """
    The value of a multiple choice form input field.
    """

    value: str = pydantic.Field()
    """
    Selected option.
    """

    value_id: typing_extensions.Annotated[str, FieldMetadata(alias="valueId")] = pydantic.Field()
    """
    ID of the selected option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
