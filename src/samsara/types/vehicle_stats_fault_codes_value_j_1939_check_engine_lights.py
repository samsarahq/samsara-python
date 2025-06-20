# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VehicleStatsFaultCodesValueJ1939CheckEngineLights(UniversalBaseModel):
    """
    Status of engine lights on J1939 vehicles.
    """

    emissions_is_on: typing_extensions.Annotated[bool, FieldMetadata(alias="emissionsIsOn")] = pydantic.Field()
    """
    True if the MIL status is nonzero.
    """

    protect_is_on: typing_extensions.Annotated[bool, FieldMetadata(alias="protectIsOn")] = pydantic.Field()
    """
    True if the engine protect lamp status is nonzero.
    """

    stop_is_on: typing_extensions.Annotated[bool, FieldMetadata(alias="stopIsOn")] = pydantic.Field()
    """
    True if the red lamp status is nonzero.
    """

    warning_is_on: typing_extensions.Annotated[bool, FieldMetadata(alias="warningIsOn")] = pydantic.Field()
    """
    True if the amber lamp status is nonzero.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
