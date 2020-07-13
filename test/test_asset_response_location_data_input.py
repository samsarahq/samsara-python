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
from samsara.models.asset_response_location_data_input import AssetResponseLocationDataInput  # noqa: E501
from samsara.rest import ApiException

class TestAssetResponseLocationDataInput(unittest.TestCase):
    """AssetResponseLocationDataInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AssetResponseLocationDataInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.asset_response_location_data_input.AssetResponseLocationDataInput()  # noqa: E501
        if include_optional :
            return AssetResponseLocationDataInput(
                id = '0'
            )
        else :
            return AssetResponseLocationDataInput(
                id = '0',
        )

    def testAssetResponseLocationDataInput(self):
        """Test AssetResponseLocationDataInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
