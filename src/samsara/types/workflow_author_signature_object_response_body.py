# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_author_signature_object_response_body_type import WorkflowAuthorSignatureObjectResponseBodyType
from .workflow_signatory_user_object_response_body import WorkflowSignatoryUserObjectResponseBody


class WorkflowAuthorSignatureObjectResponseBody(UniversalBaseModel):
    """
    An author signature for DVIRs with a signed time.
    """

    signatory_user: typing_extensions.Annotated[
        WorkflowSignatoryUserObjectResponseBody, FieldMetadata(alias="signatoryUser")
    ]
    signed_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="signedAtTime")] = pydantic.Field()
    """
    The time when the DVIR was signed. UTC timestamp in RFC 3339 format.
    """

    type: WorkflowAuthorSignatureObjectResponseBodyType = pydantic.Field()
    """
    Whether the DVIR was submitted by a driver or mechanic.  Valid values: `driver`, `mechanic`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
