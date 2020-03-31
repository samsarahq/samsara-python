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
from samsara.models.equipment_obd_engine_seconds import EquipmentObdEngineSeconds  # noqa: E501
from samsara.rest import ApiException

class TestEquipmentObdEngineSeconds(unittest.TestCase):
    """EquipmentObdEngineSeconds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EquipmentObdEngineSeconds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.equipment_obd_engine_seconds.EquipmentObdEngineSeconds()  # noqa: E501
        if include_optional :
            return EquipmentObdEngineSeconds(
                time = '2019-05-03T04:30:31Z', 
                value = 22374000
            )
        else :
            return EquipmentObdEngineSeconds(
                time = '2019-05-03T04:30:31Z',
                value = 22374000,
        )

    def testEquipmentObdEngineSeconds(self):
        """Test EquipmentObdEngineSeconds"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()