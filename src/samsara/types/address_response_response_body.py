# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AddressResponseResponseBody(UniversalBaseModel):
    """
    Closest address that the GPS latitude and longitude match to.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the city
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country
    """

    neighborhood: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the neighborhood if one exists
    """

    point_of_interest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pointOfInterest")] = (
        pydantic.Field(default=None)
    )
    """
    Point that may be of interest to the user
    """

    postal_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="postalCode")] = pydantic.Field(
        default=None
    )
    """
    The zip code
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the state
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street name
    """

    street_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="streetNumber")] = (
        pydantic.Field(default=None)
    )
    """
    Street number of the address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
