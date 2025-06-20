# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateUserRequestRoles(UniversalBaseModel):
    """
    A role that applies to a user. If the role has a `tagId`, then the role applies for that tag. If there is no `tagId`, then the role applies at the organizational level. A user may have many tag-specific roles, but may only have one organizational role. If the organizational level role has higher privileges than a tag-specific role, then the organizational role privileges will take precedence.
    """

    role_id: typing_extensions.Annotated[str, FieldMetadata(alias="roleId")] = pydantic.Field()
    """
    The unique ID for the role.
    """

    tag_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tagId")] = pydantic.Field(
        default=None
    )
    """
    ID of the tag this role applies to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
