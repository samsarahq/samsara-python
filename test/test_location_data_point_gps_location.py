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
from samsara.models.location_data_point_gps_location import LocationDataPointGpsLocation  # noqa: E501
from samsara.rest import ApiException

class TestLocationDataPointGpsLocation(unittest.TestCase):
    """LocationDataPointGpsLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocationDataPointGpsLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.location_data_point_gps_location.LocationDataPointGpsLocation()  # noqa: E501
        if include_optional :
            return LocationDataPointGpsLocation(
                formatted_address = '350 Rhode Island St, San Francisco CA, 94103', 
                gps_meters_per_second = 35.5, 
                heading_degrees = 91.2, 
                latitude = 42.44817, 
                longitude = -71.224716, 
                place = samsara.models.location_data_point_gps_location_place.LocationDataPoint_gpsLocation_place(
                    city = 'San Francisco', 
                    house_number = '350', 
                    neighborhood = 'Castro', 
                    poi = '400', 
                    postcode = '94103', 
                    state = 'CA', 
                    street = 'Rhode Island', )
            )
        else :
            return LocationDataPointGpsLocation(
        )

    def testLocationDataPointGpsLocation(self):
        """Test LocationDataPointGpsLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()