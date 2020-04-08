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
from samsara.models.vehicle_stats_tire_pressure import VehicleStatsTirePressure  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsTirePressure(unittest.TestCase):
    """VehicleStatsTirePressure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsTirePressure
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_tire_pressure.VehicleStatsTirePressure()  # noqa: E501
        if include_optional :
            return VehicleStatsTirePressure(
                time = '2020-01-27T07:06:25Z', 
                value = samsara.models.vehicle_stats_tire_pressures.VehicleStatsTirePressures(
                    back_left_tire_pressure_k_pa = 200, 
                    back_right_tire_pressure_k_pa = 200, 
                    front_left_tire_pressure_k_pa = 200, 
                    front_right_tire_pressure_k_pa = 200, )
            )
        else :
            return VehicleStatsTirePressure(
        )

    def testVehicleStatsTirePressure(self):
        """Test VehicleStatsTirePressure"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
