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
from samsara.models.create_address_request_geofence import CreateAddressRequestGeofence  # noqa: E501
from samsara.rest import ApiException

class TestCreateAddressRequestGeofence(unittest.TestCase):
    """CreateAddressRequestGeofence unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAddressRequestGeofence
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.create_address_request_geofence.CreateAddressRequestGeofence()  # noqa: E501
        if include_optional :
            return CreateAddressRequestGeofence(
                circle = samsara.models.address_geofence_circle.AddressGeofence_circle(
                    latitude = 37.765363, 
                    longitude = -122.4029238, 
                    radius_meters = 25, ), 
                polygon = samsara.models.address_geofence_polygon.AddressGeofence_polygon(
                    vertices = [{latitude=37.765363, longitude=-122.403098}, {latitude=38.765363, longitude=-122.403098}, {latitude=37.765363, longitude=-123.403098}], )
            )
        else :
            return CreateAddressRequestGeofence(
        )

    def testCreateAddressRequestGeofence(self):
        """Test CreateAddressRequestGeofence"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()