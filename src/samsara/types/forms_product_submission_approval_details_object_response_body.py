# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FormsProductSubmissionApprovalDetailsObjectResponseBody(UniversalBaseModel):
    """
    The value of the approval details for a forms product submission.
    """

    comment: str = pydantic.Field()
    """
    Comment from the approver when requesting changes or approving the submission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
