# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .recipient_object_request_body_notification_types_item import RecipientObjectRequestBodyNotificationTypesItem
from .recipient_object_request_body_type import RecipientObjectRequestBodyType


class RecipientObjectRequestBody(UniversalBaseModel):
    """
    Recipient of an Action. One of userId contactId or roleId needs to be set.
    """

    contact_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="contactId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the contact.
    """

    notification_types: typing_extensions.Annotated[
        typing.Optional[typing.List[RecipientObjectRequestBodyNotificationTypesItem]],
        FieldMetadata(alias="notificationTypes"),
    ] = pydantic.Field(default=None)
    """
    How the user/contact/role should be notified.
    """

    role_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="roleId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the role.
    """

    type: RecipientObjectRequestBodyType = pydantic.Field()
    """
    The type of recipients  Valid values: `user`, `contact`, `role`
    """

    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
