# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SuddenFuelLevelRiseTriggerDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Sudden Fuel Level Rise
    """

    min_fuel_level_change_in_percents: typing_extensions.Annotated[
        int, FieldMetadata(alias="minFuelLevelChangeInPercents")
    ] = pydantic.Field()
    """
    The minimum fuel level change in percents to trigger on. Need to be between 5 to 100.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
