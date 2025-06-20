# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .circle_response_body import CircleResponseBody
from .location_object_response_body_address_types_item import LocationObjectResponseBodyAddressTypesItem
from .polygon_response_body import PolygonResponseBody


class LocationObjectResponseBody(UniversalBaseModel):
    """
    A location. Polygon and Circle is deprecated, but may be set for old Alerts. At least one location must be selected.
    """

    address_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="addressIds")] = (
        pydantic.Field(default=None)
    )
    """
    All locations with selected address IDs will trigger.
    """

    address_types: typing_extensions.Annotated[
        typing.Optional[typing.List[LocationObjectResponseBodyAddressTypesItem]], FieldMetadata(alias="addressTypes")
    ] = pydantic.Field(default=None)
    """
    All locations with the selected address types will trigger.
    """

    circle: typing.Optional[CircleResponseBody] = None
    polygon: typing.Optional[PolygonResponseBody] = None
    tag_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="tagIds")] = (
        pydantic.Field(default=None)
    )
    """
    All locations with selected tag will trigger.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
