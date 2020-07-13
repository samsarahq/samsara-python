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
from samsara.models.j1939_d1_status_data_point_value import J1939D1StatusDataPointValue  # noqa: E501
from samsara.rest import ApiException

class TestJ1939D1StatusDataPointValue(unittest.TestCase):
    """J1939D1StatusDataPointValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test J1939D1StatusDataPointValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.j1939_d1_status_data_point_value.J1939D1StatusDataPointValue()  # noqa: E501
        if include_optional :
            return J1939D1StatusDataPointValue(
                amber_lamp_status = 1.337, 
                fmi = 1.337, 
                mil_status = 1.337, 
                occurance_count = 1.337, 
                protect_lamp_status = 1.337, 
                red_lamp_status = 1.337, 
                spn = 1.337, 
                tx_id = 1.337
            )
        else :
            return J1939D1StatusDataPointValue(
        )

    def testJ1939D1StatusDataPointValue(self):
        """Test J1939D1StatusDataPointValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
