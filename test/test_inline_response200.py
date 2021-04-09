# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.inline_response200 import InlineResponse200  # noqa: E501
from samsara.rest import ApiException

class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.inline_response200.InlineResponse200()  # noqa: E501
        if include_optional :
            return InlineResponse200(
                data = samsara.models.asset_response.AssetResponse(
                    custom_metadata = {manufacturer=Samsara, serialNumber=123ABC}, 
                    data_outputs = [
                        samsara.models.asset_data_output.AssetDataOutput(
                            data_group = 'Control Pressure', 
                            data_input = samsara.models.asset_data_input.AssetDataInput(
                                data_group = 'Pressure', 
                                id = '123456', 
                                last_point = samsara.models.asset_data_input_last_point.AssetDataInput_lastPoint(
                                    time = '2020-01-27T07:06:25Z', 
                                    value = 1992.0506, ), 
                                name = 'Digital Input 1', 
                                units = 'PSI', ), 
                            device_id = '123', 
                            id = '3fa85f64-5717-4562-b3fc-2c963f66afa6', 
                            name = 'Digital Output 1', )
                        ], 
                    id = '123abcde-4567-8910-1112-fghi1314jklm', 
                    is_running = True, 
                    location = samsara.models.asset_location.AssetLocation(
                        formatted_address = '350 Rhode Island St, San Francisco CA, 94103', 
                        latitude = 37.765363, 
                        longitude = -122.403098, ), 
                    location_data_input = samsara.models.asset_response_location_data_input.AssetResponse_locationDataInput(
                        id = '0', ), 
                    location_type = 'point', 
                    name = '0', 
                    parent_asset = samsara.models.asset_response_parent_asset.AssetResponse_parentAsset(
                        id = '123abcde-4567-8910-1112-fghi1314jklm', 
                        name = '0', ), 
                    running_status_data_input = samsara.models.asset_response_running_status_data_input.AssetResponse_runningStatusDataInput(
                        id = '12345', ), 
                    tags = [
                        samsara.models.tag_tiny_response.tagTinyResponse(
                            parent_tag_id = '4815', )
                        ], )
            )
        else :
            return InlineResponse200(
        )

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
