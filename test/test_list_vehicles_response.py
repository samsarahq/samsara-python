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
from samsara.models.list_vehicles_response import ListVehiclesResponse  # noqa: E501
from samsara.rest import ApiException

class TestListVehiclesResponse(unittest.TestCase):
    """ListVehiclesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListVehiclesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.list_vehicles_response.ListVehiclesResponse()  # noqa: E501
        if include_optional :
            return ListVehiclesResponse(
                data = [
                    samsara.models.vehicle.Vehicle(
                        aux_input_type1 = 'boom', 
                        aux_input_type2 = 'boom', 
                        external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                        harsh_acceleration_setting_type = 'off', 
                        id = '112', 
                        license_plate = 'XHK1234', 
                        make = 'Ford', 
                        model = 'F150', 
                        name = 'Truck A7', 
                        notes = '0', 
                        static_assigned_driver = samsara.models.driver_tiny_response.driverTinyResponse(), 
                        tags = [
                            samsara.models.tag_tiny_response.tagTinyResponse(
                                parent_tag_id = '4815', )
                            ], 
                        vin = '1FUJA6BD31LJ09646', 
                        year = '2008', )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return ListVehiclesResponse(
                data = [
                    samsara.models.vehicle.Vehicle(
                        aux_input_type1 = 'boom', 
                        aux_input_type2 = 'boom', 
                        external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                        harsh_acceleration_setting_type = 'off', 
                        id = '112', 
                        license_plate = 'XHK1234', 
                        make = 'Ford', 
                        model = 'F150', 
                        name = 'Truck A7', 
                        notes = '0', 
                        static_assigned_driver = samsara.models.driver_tiny_response.driverTinyResponse(), 
                        tags = [
                            samsara.models.tag_tiny_response.tagTinyResponse(
                                parent_tag_id = '4815', )
                            ], 
                        vin = '1FUJA6BD31LJ09646', 
                        year = '2008', )
                    ],
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, ),
        )

    def testListVehiclesResponse(self):
        """Test ListVehiclesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
