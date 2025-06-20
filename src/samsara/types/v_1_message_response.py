# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v_1_message_sender import V1MessageSender


class V1MessageResponse(UniversalBaseModel):
    driver_id: typing_extensions.Annotated[int, FieldMetadata(alias="driverId")] = pydantic.Field()
    """
    ID of the driver for whom the message is sent to or sent by.
    """

    is_read: typing_extensions.Annotated[bool, FieldMetadata(alias="isRead")] = pydantic.Field()
    """
    True if the message was read by the recipient.
    """

    sender: V1MessageSender
    sent_at_ms: typing_extensions.Annotated[int, FieldMetadata(alias="sentAtMs")] = pydantic.Field()
    """
    The time in Unix epoch milliseconds that the message is sent to the recipient.
    """

    text: str = pydantic.Field()
    """
    The text sent in the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
