# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .reading_trigger_continuous_value_object_response_body_operation import (
    ReadingTriggerContinuousValueObjectResponseBodyOperation,
)
from .reading_trigger_continuous_value_object_response_body_unit import (
    ReadingTriggerContinuousValueObjectResponseBodyUnit,
)


class ReadingTriggerContinuousValueObjectResponseBody(UniversalBaseModel):
    """
    Threshold to alert on if reading is continuous, either enum or continuous threshold may be set.
    """

    operation: ReadingTriggerContinuousValueObjectResponseBodyOperation = pydantic.Field()
    """
    The operation to use when comparing the value to the threshold.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    threshold: int = pydantic.Field()
    """
    The lower threshold of criticality.
    """

    unit: typing.Optional[ReadingTriggerContinuousValueObjectResponseBodyUnit] = pydantic.Field(default=None)
    """
    The unit of the threshold defined by reading type. If not provided base unit of the reading will be used.  Valid values: `bar`, `celsius`, `fahrenheit`, `foot`, `gallon`, `galpermi`, `gforce`, `gperliter`, `gperm`, `hour`, `impgallon`, `impgalpermi`, `inch`, `kelvin`, `kgper100kmgaseousfuel`, `kgpergallon`, `kgperkm`, `kgperliter`, `kgpermi`, `kilogram`, `kilogramgaseousfuel`, `kilometer`, `kilopascal`, `kilowatthour`, `kmperhr`, `lbpermi`, `liter`, `litergaseousfuel`, `lper100km`, `lper100kmgaseousfuel`, `lperkm`, `lperm`, `meter`, `meterspersec`, `mile`, `milliknot`, `millisecond`, `millivolt`, `mipergal`, `miperhr`, `miperimpgal`, `mpgusgalgaseousfuel`, `mpkggaseousfuel`, `percent`, `pound`, `poundsPerSquareInch`, `poundspergallon`, `poundsperliter`, `second`, `usd`, `usgallongaseousfuel`, `volt`, `watthour`
    """

    upper_threshold: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="upperThreshold")] = (
        pydantic.Field(default=None)
    )
    """
    The upper threshold of criticality. Required for RANGE operations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
