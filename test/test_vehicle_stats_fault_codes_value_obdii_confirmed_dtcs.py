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
from samsara.models.vehicle_stats_fault_codes_value_obdii_confirmed_dtcs import VehicleStatsFaultCodesValueObdiiConfirmedDtcs  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsFaultCodesValueObdiiConfirmedDtcs(unittest.TestCase):
    """VehicleStatsFaultCodesValueObdiiConfirmedDtcs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsFaultCodesValueObdiiConfirmedDtcs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_fault_codes_value_obdii_confirmed_dtcs.VehicleStatsFaultCodesValueObdiiConfirmedDtcs()  # noqa: E501
        if include_optional :
            return VehicleStatsFaultCodesValueObdiiConfirmedDtcs(
                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                dtc_id = 135, 
                dtc_short_code = 'P0087'
            )
        else :
            return VehicleStatsFaultCodesValueObdiiConfirmedDtcs(
                dtc_id = 135,
        )

    def testVehicleStatsFaultCodesValueObdiiConfirmedDtcs(self):
        """Test VehicleStatsFaultCodesValueObdiiConfirmedDtcs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()