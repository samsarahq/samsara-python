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
from samsara.models.user_auth_type import UserAuthType  # noqa: E501
from samsara.rest import ApiException

class TestUserAuthType(unittest.TestCase):
    """UserAuthType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserAuthType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.user_auth_type.UserAuthType()  # noqa: E501
        if include_optional :
            return UserAuthType(
            )
        else :
            return UserAuthType(
        )

    def testUserAuthType(self):
        """Test UserAuthType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
