# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vehicle_stats_fault_codes_value_oem_diagnostic_trouble_codes import (
    VehicleStatsFaultCodesValueOemDiagnosticTroubleCodes,
)


class VehicleStatsFaultCodesValueOem(UniversalBaseModel):
    """
    Vehicle fault codes for OEM vehicles.
    """

    diagnostic_trouble_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[VehicleStatsFaultCodesValueOemDiagnosticTroubleCodes]],
        FieldMetadata(alias="diagnosticTroubleCodes"),
    ] = pydantic.Field(default=None)
    """
    Proprietary diagnostic trouble codes for OEM vehicles.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
