# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .single_approval_requirements_object_response_body import SingleApprovalRequirementsObjectResponseBody


class FormsSingleApprovalConfigObjectResponseBody(UniversalBaseModel):
    """
    Single approval configuration object.
    """

    allow_manual_approver_selection: typing_extensions.Annotated[
        bool, FieldMetadata(alias="allowManualApproverSelection")
    ] = pydantic.Field()
    """
    Indicates whether approver can be manually selected. True by default.
    """

    requirements: SingleApprovalRequirementsObjectResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
