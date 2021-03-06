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
from samsara.models.equipment_locations_list_response import EquipmentLocationsListResponse  # noqa: E501
from samsara.rest import ApiException

class TestEquipmentLocationsListResponse(unittest.TestCase):
    """EquipmentLocationsListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EquipmentLocationsListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.equipment_locations_list_response.EquipmentLocationsListResponse()  # noqa: E501
        if include_optional :
            return EquipmentLocationsListResponse(
                data = [
                    samsara.models.equipment_locations_list_response_data.EquipmentLocationsListResponse_data(
                        id = '112', 
                        locations = [
                            samsara.models.equipment_location.EquipmentLocation(
                                heading = 120.0, 
                                latitude = 122.142, 
                                longitude = -93.343, 
                                speed = 48.3, 
                                time = '2020-01-27T07:06:25Z', )
                            ], 
                        name = 'Crane A7', )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return EquipmentLocationsListResponse(
                data = [
                    samsara.models.equipment_locations_list_response_data.EquipmentLocationsListResponse_data(
                        id = '112', 
                        locations = [
                            samsara.models.equipment_location.EquipmentLocation(
                                heading = 120.0, 
                                latitude = 122.142, 
                                longitude = -93.343, 
                                speed = 48.3, 
                                time = '2020-01-27T07:06:25Z', )
                            ], 
                        name = 'Crane A7', )
                    ],
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, ),
        )

    def testEquipmentLocationsListResponse(self):
        """Test EquipmentLocationsListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
