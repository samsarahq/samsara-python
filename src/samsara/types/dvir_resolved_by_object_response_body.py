# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dvir_resolved_by_object_response_body_type import DvirResolvedByObjectResponseBodyType


class DvirResolvedByObjectResponseBody(UniversalBaseModel):
    """
    The person who resolved this defect.
    """

    id: str = pydantic.Field()
    """
    ID of the entity that resolved this defect. If the defect was resolved by a driver, this will be a Samsara Driver ID. If the defect was resolved by a mechanic, this will be the Samsara Dashboard User ID of the mechanic.
    """

    name: str = pydantic.Field()
    """
    Name of the person who resolved this defect.
    """

    type: DvirResolvedByObjectResponseBodyType = pydantic.Field()
    """
    Indicates whether this defect was resolved by a driver or a mechanic.  Valid values: `driver`, `mechanic`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
