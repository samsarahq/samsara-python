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
from samsara.models.vehicle_stats_list_response_data import VehicleStatsListResponseData  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsListResponseData(unittest.TestCase):
    """VehicleStatsListResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsListResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_list_response_data.VehicleStatsListResponseData()  # noqa: E501
        if include_optional :
            return VehicleStatsListResponseData(
                aux_input1 = [
                    samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                        name = 'boom', 
                        time = '2020-01-27T07:06:25Z', 
                        value = True, )
                    ], 
                aux_input2 = [
                    samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                        name = 'boom', 
                        time = '2020-01-27T07:06:25Z', 
                        value = True, )
                    ], 
                engine_states = [
                    samsara.models.vehicle_stats_engine_state.VehicleStatsEngineState(
                        time = '2020-01-27T07:06:25Z', 
                        value = 'On', )
                    ], 
                fuel_percents = [
                    samsara.models.vehicle_stats_fuel_percent.VehicleStatsFuelPercent(
                        time = '2020-01-27T07:06:25Z', 
                        value = 54, )
                    ], 
                gps_distance_meters = [
                    samsara.models.vehicle_stats_gps_distance_meters.VehicleStatsGpsDistanceMeters(
                        time = '2020-01-27T07:06:25Z', 
                        value = 81029.591434899, )
                    ], 
                gps_odometer_meters = [
                    samsara.models.vehicle_stats_gps_odometer_meters.VehicleStatsGpsOdometerMeters(
                        time = '2020-01-27T07:06:25Z', 
                        value = 14010293, )
                    ], 
                id = '112', 
                name = 'Truck A7', 
                obd_engine_seconds = [
                    samsara.models.vehicle_stats_obd_engine_seconds.VehicleStatsObdEngineSeconds(
                        time = '2020-01-27T07:06:25Z', 
                        value = 9723103, )
                    ], 
                obd_odometer_meters = [
                    samsara.models.vehicle_stats_obd_odometer_meters.VehicleStatsObdOdometerMeters(
                        time = '2020-01-27T07:06:25Z', 
                        value = 14010293, )
                    ]
            )
        else :
            return VehicleStatsListResponseData(
                id = '112',
                name = 'Truck A7',
        )

    def testVehicleStatsListResponseData(self):
        """Test VehicleStatsListResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
