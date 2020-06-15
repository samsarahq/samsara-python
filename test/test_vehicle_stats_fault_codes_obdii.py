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
from samsara.models.vehicle_stats_fault_codes_obdii import VehicleStatsFaultCodesOBDII  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsFaultCodesOBDII(unittest.TestCase):
    """VehicleStatsFaultCodesOBDII unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsFaultCodesOBDII
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_fault_codes_obdii.VehicleStatsFaultCodesOBDII()  # noqa: E501
        if include_optional :
            return VehicleStatsFaultCodesOBDII(
                check_engine_light_is_on = True, 
                diagnostic_trouble_codes = [
                    samsara.models.vehicle_stats_fault_codes_obdii_trouble_code.VehicleStatsFaultCodesOBDIITroubleCode(
                        confirmed_dtcs = [
                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                dtc_id = 135, 
                                dtc_short_code = 'P0087', )
                            ], 
                        ignition_type = 'spark', 
                        mil_status = True, 
                        monitor_status = samsara.models.vehicle_stats_fault_codes_passenger_monitor_status.VehicleStatsFaultCodesPassengerMonitorStatus(
                            catalyst = 'N', 
                            comprehensive = 'N', 
                            egr = 'N', 
                            evap_system = 'N', 
                            fuel = 'N', 
                            heated_catalyst = 'N', 
                            heated_o2_sensor = 'N', 
                            iso_sae_reserved = 'N', 
                            misfire = 'N', 
                            not_ready_count = 56, 
                            o2_sensor = 'N', 
                            secondary_air = 'N', ), 
                        pending_dtcs = [
                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                dtc_id = 135, 
                                dtc_short_code = 'P0087', )
                            ], 
                        permanent_dtcs = [
                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                dtc_id = 135, 
                                dtc_short_code = 'P0087', )
                            ], 
                        tx_id = 0, )
                    ]
            )
        else :
            return VehicleStatsFaultCodesOBDII(
        )

    def testVehicleStatsFaultCodesOBDII(self):
        """Test VehicleStatsFaultCodesOBDII"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
