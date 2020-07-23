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
from samsara.models.driver_efficiencies_response import DriverEfficienciesResponse  # noqa: E501
from samsara.rest import ApiException

class TestDriverEfficienciesResponse(unittest.TestCase):
    """DriverEfficienciesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DriverEfficienciesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.driver_efficiencies_response.DriverEfficienciesResponse()  # noqa: E501
        if include_optional :
            return DriverEfficienciesResponse(
                data = samsara.models.driver_efficiencies_response_data.DriverEfficienciesResponse_data(
                    driver_summaries = [
                        samsara.models.driver_efficiency.DriverEfficiency(
                            driver = samsara.models.extended_driver_tiny_response.ExtendedDriverTinyResponse(
                                external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                                id = '88668', 
                                name = 'Susan Bob', 
                                username = 'susanbob', ), 
                            total_distance_driven_meters = 1.337, 
                            total_drive_time_duration_ms = 1.337, 
                            total_fuel_consumed_ml = 1.337, 
                            total_idle_time_duration_ms = 1.337, 
                            total_power_take_off_duration_ms = 1.337, 
                            vehicle_summaries = [
                                samsara.models.vehicle_summary.VehicleSummary(
                                    distance_driven_meters = 1.337, 
                                    drive_time_duration_ms = 1.337, 
                                    fuel_consumed_ml = 1.337, 
                                    idle_time_duration_ms = 1.337, 
                                    power_take_off_duration_ms = 1.337, 
                                    vehicle = samsara.models.vehicle_tiny_response.vehicleTinyResponse(
                                        id = '123456789', 
                                        name = 'Midwest Truck #4', ), )
                                ], )
                        ], 
                    summary_end_time = '2020-03-16T16:00Z', 
                    summary_start_time = '2020-03-15T16:00Z', ), 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return DriverEfficienciesResponse(
        )

    def testDriverEfficienciesResponse(self):
        """Test DriverEfficienciesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
