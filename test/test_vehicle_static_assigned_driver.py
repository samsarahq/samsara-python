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
from samsara.models.vehicle_static_assigned_driver import VehicleStaticAssignedDriver  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStaticAssignedDriver(unittest.TestCase):
    """VehicleStaticAssignedDriver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStaticAssignedDriver
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_static_assigned_driver.VehicleStaticAssignedDriver()  # noqa: E501
        if include_optional :
            return VehicleStaticAssignedDriver(
            )
        else :
            return VehicleStaticAssignedDriver(
        )

    def testVehicleStaticAssignedDriver(self):
        """Test VehicleStaticAssignedDriver"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
