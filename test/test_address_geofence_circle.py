# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.address_geofence_circle import AddressGeofenceCircle  # noqa: E501
from samsara.rest import ApiException

class TestAddressGeofenceCircle(unittest.TestCase):
    """AddressGeofenceCircle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressGeofenceCircle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.address_geofence_circle.AddressGeofenceCircle()  # noqa: E501
        if include_optional :
            return AddressGeofenceCircle(
                latitude = 37.765363, 
                longitude = -122.4029238, 
                radius_meters = 25
            )
        else :
            return AddressGeofenceCircle(
                radius_meters = 25,
        )

    def testAddressGeofenceCircle(self):
        """Test AddressGeofenceCircle"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
