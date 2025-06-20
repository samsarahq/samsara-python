# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assets_inputs_response_response_body import AssetsInputsResponseResponseBody
from .goa_pagination_response_response_body import GoaPaginationResponseResponseBody


class AssetsInputsGetAssetsInputsResponseBody(UniversalBaseModel):
    data: typing.List[AssetsInputsResponseResponseBody] = pydantic.Field()
    """
    Array of assets inputs objects.
    """

    pagination: GoaPaginationResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
