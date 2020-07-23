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
from samsara.models.vehicle_stats_obd_odometer_meters_with_decoration import VehicleStatsObdOdometerMetersWithDecoration  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsObdOdometerMetersWithDecoration(unittest.TestCase):
    """VehicleStatsObdOdometerMetersWithDecoration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsObdOdometerMetersWithDecoration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_obd_odometer_meters_with_decoration.VehicleStatsObdOdometerMetersWithDecoration()  # noqa: E501
        if include_optional :
            return VehicleStatsObdOdometerMetersWithDecoration(
                decorations = samsara.models.vehicle_stats_decorations.VehicleStatsDecorations(
                    aux_input1 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input10 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input2 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input3 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input4 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input5 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input6 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input7 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input8 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    aux_input9 = samsara.models.vehicle_stats_aux_input_decoration.VehicleStatsAuxInputDecoration(
                        name = 'boom', 
                        value = True, ), 
                    battery_milli_volts = samsara.models.vehicle_stats_decorations_battery_milli_volts.VehicleStatsDecorations_batteryMilliVolts(
                        value = 7991, ), 
                    ecu_speed_mph = samsara.models.vehicle_stats_decorations_ecu_speed_mph.VehicleStatsDecorations_ecuSpeedMph(
                        value = 58.3, ), 
                    engine_rpm = samsara.models.vehicle_stats_decorations_engine_rpm.VehicleStatsDecorations_engineRpm(
                        value = 1000, ), 
                    engine_states = samsara.models.vehicle_stats_decorations_engine_states.VehicleStatsDecorations_engineStates(
                        value = 'On', ), 
                    fault_codes = samsara.models.vehicle_stats_fault_codes_value.VehicleStatsFaultCodesValue(
                        can_bus_type = 'CANBUS_J1939_500', 
                        j1939 = samsara.models.vehicle_stats_fault_codes_value_j1939.VehicleStatsFaultCodesValue_j1939(
                            check_engine_lights = samsara.models.vehicle_stats_fault_codes_value_j1939_check_engine_lights.VehicleStatsFaultCodesValue_j1939_checkEngineLights(
                                emissions_is_on = True, 
                                protect_is_on = False, 
                                stop_is_on = False, 
                                warning_is_on = False, ), 
                            diagnostic_trouble_codes = [
                                samsara.models.vehicle_stats_fault_codes_value_j1939_diagnostic_trouble_codes.VehicleStatsFaultCodesValue_j1939_diagnosticTroubleCodes(
                                    fmi_description = 'Voltage Below Normal', 
                                    fmi_id = 9, 
                                    mil_status = 1, 
                                    occurrence_count = 1, 
                                    source_address_name = 'Engine #1', 
                                    spn_description = 'System Diagnostic Code #1', 
                                    spn_id = 3031, 
                                    tx_id = 0, )
                                ], ), 
                        obdii = samsara.models.vehicle_stats_fault_codes_value_obdii.VehicleStatsFaultCodesValue_obdii(
                            check_engine_light_is_on = True, ), ), 
                    fuel_percents = samsara.models.vehicle_stats_decorations_fuel_percents.VehicleStatsDecorations_fuelPercents(
                        value = 54, ), 
                    gps = samsara.models.vehicle_stats_decorations_gps.VehicleStatsDecorations_gps(
                        heading_degrees = 120, 
                        latitude = 122.142, 
                        longitude = -93.343, 
                        reverse_geo = samsara.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                            formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                        speed_miles_per_hour = 48.3, ), 
                    gps_distance_meters = samsara.models.vehicle_stats_decorations_gps_distance_meters.VehicleStatsDecorations_gpsDistanceMeters(
                        value = 81029.591434899, ), 
                    gps_odometer_meters = samsara.models.vehicle_stats_decorations_gps_odometer_meters.VehicleStatsDecorations_gpsOdometerMeters(
                        value = 14010293, ), 
                    obd_engine_seconds = samsara.models.vehicle_stats_decorations_obd_engine_seconds.VehicleStatsDecorations_obdEngineSeconds(
                        value = 9723103, ), 
                    obd_odometer_meters = samsara.models.vehicle_stats_decorations_obd_odometer_meters.VehicleStatsDecorations_obdOdometerMeters(
                        value = 14010293, ), 
                    tire_pressure = samsara.models.vehicle_stats_tire_pressures.VehicleStatsTirePressures(
                        back_left_tire_pressure_k_pa = 200, 
                        back_right_tire_pressure_k_pa = 200, 
                        front_left_tire_pressure_k_pa = 200, 
                        front_right_tire_pressure_k_pa = 200, ), ), 
                time = '2020-01-27T07:06:25Z', 
                value = 14010293
            )
        else :
            return VehicleStatsObdOdometerMetersWithDecoration(
                time = '2020-01-27T07:06:25Z',
                value = 14010293,
        )

    def testVehicleStatsObdOdometerMetersWithDecoration(self):
        """Test VehicleStatsObdOdometerMetersWithDecoration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()