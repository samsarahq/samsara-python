# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .behavior_response_body_coachable_behavior_type import BehaviorResponseBodyCoachableBehaviorType
from .coachable_event_response_body import CoachableEventResponseBody


class BehaviorResponseBody(UniversalBaseModel):
    """
    Object reference for the behavior within the session.
    """

    coachable_behavior_type: typing_extensions.Annotated[
        BehaviorResponseBodyCoachableBehaviorType, FieldMetadata(alias="coachableBehaviorType")
    ] = pydantic.Field()
    """
    Coachable behavior type for the behavior in the coaching session.  Valid values: `acceleration`, `braking`, `cameraObstruction`, `crash`, `defensiveDriving`, `didNotYield`, `drinkPolicy`, `drowsy`, `eatingDrinking`, `event`, `falsePositive`, `foodPolicy`, `forwardCollisionWarning`, `genericDistraction`, `harshTurn`, `hosViolation`, `idling`, `laneDeparture`, `lateResponse`, `maskPolicy`, `maxSpeed`, `mobileUsage`, `nearCollison`, `noSeatbelt`, `obstructedCamera`, `outwardObstruction`, `passengerPolicy`, `ranRedLight`, `rollingRailroadCrossing`, `rollingStop`, `rollingStop`, `rollover`, `rolloverProtection`, `rolloverProtectionBrakeControlActivated`, `rolloverProtectionEngineControlActivated`, `severeSpeeding`, `smoking`, `speeding`, `tailgating`, `unknown`, `yawControl`, `yawControlBrakeControlActivated`, `yawControlEngineControlActivated`
    """

    coachable_events: typing_extensions.Annotated[
        typing.Optional[typing.List[CoachableEventResponseBody]], FieldMetadata(alias="coachableEvents")
    ] = pydantic.Field(default=None)
    """
    Object references for the coachableEvents within the behavior. Returned when includeCoachableEvents is 'true'. Capped at 100 coachable events per Coaching session. For sessions where coachable events exceed 100, please visit the Samsara dashboard to address this coaching session. Corresponds to the following unique identifiers: Non-Speeding Safety events - unique Samsara ID of the safety event as 'vehicleId - eventMS'. Speeding events - unique UUID of the event. Day of HOS Violations - unique Samsara ID of the day of violations as '{driverId},{date}'. Idling events - unique UUID of the event.
    """

    id: str = pydantic.Field()
    """
    Unique ID for the coaching behavior.
    """

    last_coached_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="lastCoachedTime")] = (
        pydantic.Field()
    )
    """
    Time of last coached date for the same behavior label.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Associated note for the coaching behavior. Returned when present.
    """

    updated_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Time of coaching behavior update in UTC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
