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
from samsara.models.asset_data_output import AssetDataOutput  # noqa: E501
from samsara.rest import ApiException

class TestAssetDataOutput(unittest.TestCase):
    """AssetDataOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AssetDataOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.asset_data_output.AssetDataOutput()  # noqa: E501
        if include_optional :
            return AssetDataOutput(
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
                name = 'Digital Output 1'
            )
        else :
            return AssetDataOutput(
        )

    def testAssetDataOutput(self):
        """Test AssetDataOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
