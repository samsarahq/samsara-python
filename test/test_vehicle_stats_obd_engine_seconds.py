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
from samsara.models.vehicle_stats_obd_engine_seconds import VehicleStatsObdEngineSeconds  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsObdEngineSeconds(unittest.TestCase):
    """VehicleStatsObdEngineSeconds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsObdEngineSeconds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_obd_engine_seconds.VehicleStatsObdEngineSeconds()  # noqa: E501
        if include_optional :
            return VehicleStatsObdEngineSeconds(
                time = '2020-01-27T07:06:25Z', 
                value = 9723103
            )
        else :
            return VehicleStatsObdEngineSeconds(
                time = '2020-01-27T07:06:25Z',
                value = 9723103,
        )

    def testVehicleStatsObdEngineSeconds(self):
        """Test VehicleStatsObdEngineSeconds"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
