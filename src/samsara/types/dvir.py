# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dvir_author_signature import DvirAuthorSignature
from .dvir_license_plate import DvirLicensePlate
from .dvir_location import DvirLocation
from .dvir_mechanic_notes import DvirMechanicNotes
from .dvir_odometer_meters import DvirOdometerMeters
from .dvir_safety_status import DvirSafetyStatus
from .dvir_second_signature import DvirSecondSignature
from .dvir_third_signature import DvirThirdSignature
from .dvir_trailer import DvirTrailer
from .dvir_trailer_defects import DvirTrailerDefects
from .dvir_type import DvirType
from .dvir_vehicle import DvirVehicle
from .dvir_vehicle_defects import DvirVehicleDefects


class Dvir(UniversalBaseModel):
    """
    Information about a DVIR.
    """

    author_signature: typing_extensions.Annotated[
        typing.Optional[DvirAuthorSignature], FieldMetadata(alias="authorSignature")
    ] = None
    end_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="endTime")] = pydantic.Field(
        default=None
    )
    """
    Time when driver signed and completed this DVIR. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    id: str = pydantic.Field()
    """
    Unique Samsara ID for the DVIR.
    """

    license_plate: typing_extensions.Annotated[
        typing.Optional[DvirLicensePlate], FieldMetadata(alias="licensePlate")
    ] = None
    location: typing.Optional[DvirLocation] = None
    mechanic_notes: typing_extensions.Annotated[
        typing.Optional[DvirMechanicNotes], FieldMetadata(alias="mechanicNotes")
    ] = None
    odometer_meters: typing_extensions.Annotated[
        typing.Optional[DvirOdometerMeters], FieldMetadata(alias="odometerMeters")
    ] = None
    safety_status: typing_extensions.Annotated[
        typing.Optional[DvirSafetyStatus], FieldMetadata(alias="safetyStatus")
    ] = pydantic.Field(default=None)
    """
    The condition of vehicle on which DVIR was done. Valid values: `safe`, `unsafe`, `resolved`.
    """

    second_signature: typing_extensions.Annotated[
        typing.Optional[DvirSecondSignature], FieldMetadata(alias="secondSignature")
    ] = None
    start_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="startTime")] = pydantic.Field(
        default=None
    )
    """
    Time when driver began filling out this DVIR. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    third_signature: typing_extensions.Annotated[
        typing.Optional[DvirThirdSignature], FieldMetadata(alias="thirdSignature")
    ] = None
    trailer: typing.Optional[DvirTrailer] = None
    trailer_defects: typing_extensions.Annotated[
        typing.Optional[DvirTrailerDefects], FieldMetadata(alias="trailerDefects")
    ] = None
    trailer_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="trailerName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the trailer the DVIR was submitted for.  Only included for tractor+trailer DVIRs.
    """

    type: typing.Optional[DvirType] = pydantic.Field(default=None)
    """
    Inspection type of the DVIR. Valid values: `preTrip`, `postTrip`, `mechanic`, `unspecified`.
    """

    vehicle: typing.Optional[DvirVehicle] = None
    vehicle_defects: typing_extensions.Annotated[
        typing.Optional[DvirVehicleDefects], FieldMetadata(alias="vehicleDefects")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
