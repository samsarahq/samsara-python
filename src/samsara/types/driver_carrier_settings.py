# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .driver_home_terminal_address import DriverHomeTerminalAddress
from .driver_home_terminal_name import DriverHomeTerminalName


class DriverCarrierSettings(UniversalBaseModel):
    """
    Carrier for a given driver. If the driver's carrier differs from the general organization's carrier settings, the override value is used. Updating this value only updates the override setting for this driver.
    """

    carrier_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="carrierName")] = (
        pydantic.Field(default=None)
    )
    """
    Carrier for a given driver.
    """

    dot_number: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="dotNumber")] = pydantic.Field(
        default=None
    )
    """
    Carrier US DOT Number. If this differs from the general organization's settings, the override value is used. Updating this value only updates the override setting for this driver.
    """

    home_terminal_address: typing_extensions.Annotated[
        typing.Optional[DriverHomeTerminalAddress], FieldMetadata(alias="homeTerminalAddress")
    ] = None
    home_terminal_name: typing_extensions.Annotated[
        typing.Optional[DriverHomeTerminalName], FieldMetadata(alias="homeTerminalName")
    ] = None
    main_office_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mainOfficeAddress")] = (
        pydantic.Field(default=None)
    )
    """
    Main office address for a given driver. If this differs from the general organization's settings, the override value is used. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
