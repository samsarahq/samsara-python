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
from samsara.models.update_vehicle_request import UpdateVehicleRequest  # noqa: E501
from samsara.rest import ApiException

class TestUpdateVehicleRequest(unittest.TestCase):
    """UpdateVehicleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateVehicleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.update_vehicle_request.UpdateVehicleRequest()  # noqa: E501
        if include_optional :
            return UpdateVehicleRequest(
                aux_input_type1 = 'boom', 
                aux_input_type10 = 'boom', 
                aux_input_type2 = 'boom', 
                aux_input_type3 = 'boom', 
                aux_input_type4 = 'boom', 
                aux_input_type5 = 'boom', 
                aux_input_type6 = 'boom', 
                aux_input_type7 = 'boom', 
                aux_input_type8 = 'boom', 
                aux_input_type9 = 'boom', 
                engine_hours = 10943, 
                external_ids = {"maintenanceId":"250020","payrollId":"ABFS18600"}, 
                gateway_serial = 'ABCD-123-XYZ', 
                harsh_acceleration_setting_type = 'off', 
                license_plate = 'XHK1234', 
                name = 'Truck A7', 
                notes = 'These are notes about this given vehicle.', 
                odometer_meters = 9182, 
                static_assigned_driver_id = '123', 
                tag_ids = [
                    '321'
                    ], 
                vin = '1FUJA6BD31LJ09646'
            )
        else :
            return UpdateVehicleRequest(
        )

    def testUpdateVehicleRequest(self):
        """Test UpdateVehicleRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
