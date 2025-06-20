# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .work_order_attachment_object_response_body_processing_status import (
    WorkOrderAttachmentObjectResponseBodyProcessingStatus,
)


class WorkOrderAttachmentObjectResponseBody(UniversalBaseModel):
    """
    Work Order Attachment object.
    """

    id: str = pydantic.Field()
    """
    ID of the media record.
    """

    processing_status: typing_extensions.Annotated[
        WorkOrderAttachmentObjectResponseBodyProcessingStatus, FieldMetadata(alias="processingStatus")
    ] = pydantic.Field()
    """
    Status of the media record.  Valid values: `unknown`, `processing`, `finished`
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL containing a link to associated media content. Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="urlExpiresAt")] = (
        pydantic.Field(default=None)
    )
    """
    Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
