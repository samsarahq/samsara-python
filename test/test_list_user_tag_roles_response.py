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
from samsara.models.list_user_tag_roles_response import ListUserTagRolesResponse  # noqa: E501
from samsara.rest import ApiException

class TestListUserTagRolesResponse(unittest.TestCase):
    """ListUserTagRolesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUserTagRolesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.list_user_tag_roles_response.ListUserTagRolesResponse()  # noqa: E501
        if include_optional :
            return ListUserTagRolesResponse(
                data = [
                    samsara.models.user_role_tiny_response.userRoleTinyResponse(
                        id = '8a9371af-82d1-4158-bf91-4ecc8d3a114c', 
                        name = 'Full Admin', )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return ListUserTagRolesResponse(
        )

    def testListUserTagRolesResponse(self):
        """Test ListUserTagRolesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()