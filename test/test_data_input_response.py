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
from samsara.models.data_input_response import DataInputResponse  # noqa: E501
from samsara.rest import ApiException

class TestDataInputResponse(unittest.TestCase):
    """DataInputResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DataInputResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.data_input_response.DataInputResponse()  # noqa: E501
        if include_optional :
            return DataInputResponse(
                asset_id = '74771078-5edb-4733-88f2-7242f520d1f1', 
                data_group = 'Flow', 
                id = '0', 
                name = 'Pump Flow', 
                units = 'Gallons Per Minute', 
                fft_spectra_points = [
                    samsara.models.fft_spectra_data_point.FftSpectraDataPoint(
                        fft_spectra = samsara.models.fft_spectra_data_point_fft_spectra.FftSpectraDataPoint_fftSpectra(
                            frequencies = [
                                1.337
                                ], 
                            x = [
                                1.337
                                ], 
                            y = [
                                1.337
                                ], 
                            z = [
                                1.337
                                ], ), 
                        time = '2020-01-27T07:06:25Z', )
                    ], 
                j1939_d1_status_points = [
                    samsara.models.j1939_d1_status_data_point.J1939D1StatusDataPoint(
                        time = '2020-01-27T07:06:25Z', 
                        value = [
                            samsara.models.j1939_d1_status_data_point_value.J1939D1StatusDataPoint_value(
                                amber_lamp_status = 1.337, 
                                fmi = 1.337, 
                                mil_status = 1.337, 
                                occurance_count = 1.337, 
                                protect_lamp_status = 1.337, 
                                red_lamp_status = 1.337, 
                                spn = 1.337, 
                                tx_id = 1.337, )
                            ], )
                    ], 
                location_points = [
                    samsara.models.location_data_point.LocationDataPoint(
                        gps_location = samsara.models.location_data_point_gps_location.LocationDataPoint_gpsLocation(
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
                                street = 'Rhode Island', ), ), 
                        time = '2020-01-27T07:06:25Z', )
                    ], 
                number_points = [
                    samsara.models.number_data_point.NumberDataPoint(
                        time = '2020-01-27T07:06:25Z', 
                        value = 1992.0506, )
                    ], 
                string_points = [
                    samsara.models.string_data_point.StringDataPoint(
                        time = '2020-01-27T07:06:25Z', 
                        value = 'On', )
                    ]
            )
        else :
            return DataInputResponse(
        )

    def testDataInputResponse(self):
        """Test DataInputResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
