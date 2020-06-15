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
from samsara.models.driver_tachograph_activity_response import DriverTachographActivityResponse  # noqa: E501
from samsara.rest import ApiException

class TestDriverTachographActivityResponse(unittest.TestCase):
    """DriverTachographActivityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DriverTachographActivityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.driver_tachograph_activity_response.DriverTachographActivityResponse()  # noqa: E501
        if include_optional :
            return DriverTachographActivityResponse(
                data = [
                    samsara.models.tachograph_activity_list_wrapper.TachographActivityListWrapper(
                        activity = [
                            samsara.models.tachograph_activity.TachographActivity(
                                end_time = '2020-01-03T16:04:05Z07:00', 
                                is_manual_entry = False, 
                                start_time = '2020-01-02T15:04:05Z07:00', 
                                state = 'BREAK/REST', )
                            ], 
                        driver = samsara.models.driver_tiny_response.driverTinyResponse(
                            id = '88668', 
                            name = 'Susan Bob', ), )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return DriverTachographActivityResponse(
        )

    def testDriverTachographActivityResponse(self):
        """Test DriverTachographActivityResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
