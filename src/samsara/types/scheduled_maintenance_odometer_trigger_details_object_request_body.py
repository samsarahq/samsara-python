# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScheduledMaintenanceOdometerTriggerDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Scheduled Maintenance by Odometer
    """

    due_in_meters: typing_extensions.Annotated[int, FieldMetadata(alias="dueInMeters")] = pydantic.Field()
    """
    Alert when vehicle odometer has this many meters left until maintenance is due.
    """

    schedule_id: typing_extensions.Annotated[str, FieldMetadata(alias="scheduleId")] = pydantic.Field()
    """
    The id of the maintenance schedule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
