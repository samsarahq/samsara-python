# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .forms_single_approval_config_object_response_body import FormsSingleApprovalConfigObjectResponseBody


class FormsApprovalConfigObjectResponseBody(UniversalBaseModel):
    """
    Form Template approval configuration object.
    """

    single_approval_config: typing_extensions.Annotated[
        typing.Optional[FormsSingleApprovalConfigObjectResponseBody], FieldMetadata(alias="singleApprovalConfig")
    ] = None
    type: typing.Literal["singleApproval"] = pydantic.Field(default="singleApproval")
    """
    Type of approval.  Valid values: `singleApproval`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
