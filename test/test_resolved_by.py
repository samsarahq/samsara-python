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
from samsara.models.resolved_by import ResolvedBy  # noqa: E501
from samsara.rest import ApiException

class TestResolvedBy(unittest.TestCase):
    """ResolvedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResolvedBy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.resolved_by.ResolvedBy()  # noqa: E501
        if include_optional :
            return ResolvedBy(
                id = '11', 
                type = 'mechanic'
            )
        else :
            return ResolvedBy(
                id = '11',
                type = 'mechanic',
        )

    def testResolvedBy(self):
        """Test ResolvedBy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
