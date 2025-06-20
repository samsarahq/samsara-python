# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dvir_resolved_by_object_response_body import DvirResolvedByObjectResponseBody
from .goa_trailer_tiny_response_response_body import GoaTrailerTinyResponseResponseBody
from .vehicle_with_gateway_tiny_response_response_body import VehicleWithGatewayTinyResponseResponseBody


class DvirDefectsObjectV20220913ResponseBody(UniversalBaseModel):
    """
    A description of a DVIR defect
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comment on the defect.
    """

    created_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Time when the defect was created. UTC timestamp in RFC 3339 format.
    """

    defect_type: typing_extensions.Annotated[str, FieldMetadata(alias="defectType")] = pydantic.Field()
    """
    The type of DVIR defect.
    """

    id: str = pydantic.Field()
    """
    The ID of the defect.
    """

    is_resolved: typing_extensions.Annotated[bool, FieldMetadata(alias="isResolved")] = pydantic.Field()
    """
    Signifies if this defect is resolved.
    """

    mechanic_notes: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mechanicNotes")] = (
        pydantic.Field(default=None)
    )
    """
    The mechanic notes on this defect.
    """

    mechanic_notes_updated_at_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mechanicNotesUpdatedAtTime")
    ] = pydantic.Field(default=None)
    """
    Time when mechanic notes were last updated. UTC timestamp in RFC 3339 format.
    """

    resolved_at_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="resolvedAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format.
    """

    resolved_by: typing_extensions.Annotated[
        typing.Optional[DvirResolvedByObjectResponseBody], FieldMetadata(alias="resolvedBy")
    ] = None
    trailer: typing.Optional[GoaTrailerTinyResponseResponseBody] = None
    vehicle: typing.Optional[VehicleWithGatewayTinyResponseResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
