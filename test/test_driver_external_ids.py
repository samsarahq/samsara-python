# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.driver_external_ids import DriverExternalIds  # noqa: E501
from samsara.rest import ApiException

class TestDriverExternalIds(unittest.TestCase):
    """DriverExternalIds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DriverExternalIds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.driver_external_ids.DriverExternalIds()  # noqa: E501
        if include_optional :
            return DriverExternalIds(
            )
        else :
            return DriverExternalIds(
        )

    def testDriverExternalIds(self):
        """Test DriverExternalIds"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
