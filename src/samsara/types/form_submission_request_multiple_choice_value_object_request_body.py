# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FormSubmissionRequestMultipleChoiceValueObjectRequestBody(UniversalBaseModel):
    """
    The value of a multiple choice form input field. Only valid for multiple choice form input fields.
    """

    value_id: typing_extensions.Annotated[str, FieldMetadata(alias="valueId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
