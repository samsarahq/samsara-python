# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .form_template_section_object_response_body import FormTemplateSectionObjectResponseBody
from .forms_approval_config_object_response_body import FormsApprovalConfigObjectResponseBody
from .forms_field_definition_object_response_body import FormsFieldDefinitionObjectResponseBody
from .forms_polymorphic_user_object_response_body import FormsPolymorphicUserObjectResponseBody


class FormTemplateResponseObjectResponseBody(UniversalBaseModel):
    """
    Form Template response object.
    """

    approval_config: typing_extensions.Annotated[
        typing.Optional[FormsApprovalConfigObjectResponseBody], FieldMetadata(alias="approvalConfig")
    ] = None
    created_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Creation time of the form template. UTC timestamp in RFC 3339 format.
    """

    created_by: typing_extensions.Annotated[FormsPolymorphicUserObjectResponseBody, FieldMetadata(alias="createdBy")]
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the form template. Sometimes returned if the template has a description.
    """

    fields: typing.List[FormsFieldDefinitionObjectResponseBody] = pydantic.Field()
    """
    List of fields in the form template.
    """

    id: str = pydantic.Field()
    """
    Unique identifier of the form template.
    """

    revision_id: typing_extensions.Annotated[str, FieldMetadata(alias="revisionId")] = pydantic.Field()
    """
    Unique identifier of the form template revision.
    """

    sections: typing.List[FormTemplateSectionObjectResponseBody] = pydantic.Field()
    """
    List of sections in the form template.
    """

    title: str = pydantic.Field()
    """
    Title of the form template.
    """

    updated_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Update time of the form template. UTC timestamp in RFC 3339 format.
    """

    updated_by: typing_extensions.Annotated[FormsPolymorphicUserObjectResponseBody, FieldMetadata(alias="updatedBy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
