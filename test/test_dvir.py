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
from samsara.models.dvir import Dvir  # noqa: E501
from samsara.rest import ApiException

class TestDvir(unittest.TestCase):
    """Dvir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Dvir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.dvir.Dvir()  # noqa: E501
        if include_optional :
            return Dvir(
                author_signature = null, 
                end_time = '2020-01-27T07:06:25Z', 
                id = '7107471', 
                license_plate = 'XHK1234', 
                location = '350 Rhode Island St Ste. 400S, San Francisco, CA 94103', 
                mechanic_notes = 'Replaced headlight on passenger side.', 
                odometer_meters = 14010293, 
                safety_status = 'unsafe', 
                second_signature = null, 
                start_time = '2020-01-27T07:06:25Z', 
                third_signature = null, 
                trailer = null, 
                trailer_defects = [
                    samsara.models.dvir_trailer_defects_items.dvirTrailerDefectsItems(
                        comment = 'Air Compressor not working', 
                        created_at_time = '2020-01-27T07:06:25Z', 
                        defect_type = 'Air Compressor', 
                        id = '18', 
                        is_resolved = True, 
                        mechanic_notes = 'Extremely large oddly shaped hole in passenger side window.', 
                        mechanic_notes_updated_at_time = '2020-01-27T07:06:25Z', 
                        resolved_at_time = '2020-01-27T07:06:25Z', 
                        resolved_by = samsara.models.defect_resolved_by.Defect_resolvedBy(
                            id = '0', 
                            name = '0', 
                            type = 'driver', ), 
                        trailer = samsara.models.trailer.trailer(), 
                        vehicle = samsara.models.vehicle.vehicle(), )
                    ], 
                trailer_name = 'Midwest Trailer #5', 
                type = 'unspecified', 
                vehicle = null, 
                vehicle_defects = [
                    samsara.models.dvir_trailer_defects_items.dvirTrailerDefectsItems(
                        comment = 'Air Compressor not working', 
                        created_at_time = '2020-01-27T07:06:25Z', 
                        defect_type = 'Air Compressor', 
                        id = '18', 
                        is_resolved = True, 
                        mechanic_notes = 'Extremely large oddly shaped hole in passenger side window.', 
                        mechanic_notes_updated_at_time = '2020-01-27T07:06:25Z', 
                        resolved_at_time = '2020-01-27T07:06:25Z', 
                        resolved_by = samsara.models.defect_resolved_by.Defect_resolvedBy(
                            id = '0', 
                            name = '0', 
                            type = 'driver', ), 
                        trailer = samsara.models.trailer.trailer(), 
                        vehicle = samsara.models.vehicle.vehicle(), )
                    ]
            )
        else :
            return Dvir(
                id = '7107471',
        )

    def testDvir(self):
        """Test Dvir"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
