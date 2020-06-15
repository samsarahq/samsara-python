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
from samsara.models.equipment import Equipment  # noqa: E501
from samsara.rest import ApiException

class TestEquipment(unittest.TestCase):
    """Equipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Equipment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.equipment.Equipment()  # noqa: E501
        if include_optional :
            return Equipment(
                asset_serial = '1FUJA6BD31LJ09646', 
                id = '112', 
                name = 'Crane A7', 
                notes = 'These are notes about this given equipment.', 
                tags = [
                    samsara.models.tag_tiny_response.tagTinyResponse(
                        id = '3914', 
                        name = 'East Coast', 
                        parent_tag_id = '4815', )
                    ]
            )
        else :
            return Equipment(
                id = '112',
        )

    def testEquipment(self):
        """Test Equipment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
