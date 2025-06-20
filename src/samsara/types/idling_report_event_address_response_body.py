# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IdlingReportEventAddressResponseBody(UniversalBaseModel):
    """
    Address where the idling event took place.
    """

    formatted: str = pydantic.Field()
    """
    The formatted address of the idling location.
    """

    latitude: float = pydantic.Field()
    """
    The latitude of the idling location.
    """

    longitude: float = pydantic.Field()
    """
    The longitude of the idling location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
