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
from samsara.models.vehicle_stats_response import VehicleStatsResponse  # noqa: E501
from samsara.rest import ApiException

class TestVehicleStatsResponse(unittest.TestCase):
    """VehicleStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleStatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_stats_response.VehicleStatsResponse()  # noqa: E501
        if include_optional :
            return VehicleStatsResponse(
                data = [
                    samsara.models.vehicle_stats_response_data.VehicleStatsResponse_data(
                        ambient_air_temperature_milli_c = samsara.models.vehicle_stats_ambient_air_temp_milli_c.VehicleStatsAmbientAirTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 31110, ), 
                        aux_input1 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            name = 'boom', 
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input10 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input2 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input3 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input4 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input5 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input6 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input7 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input8 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input9 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        barometric_pressure_pa = samsara.models.vehicle_stats_barometric_pressure_pa.VehicleStatsBarometricPressurePa(
                            time = '2020-01-27T07:06:25Z', 
                            value = 99000, ), 
                        battery_milli_volts = samsara.models.vehicle_stats_battery_voltage.VehicleStatsBatteryVoltage(
                            time = '2020-01-27T07:06:25Z', 
                            value = 7991, ), 
                        def_level_milli_percent = samsara.models.vehicle_stats_def_level_milli_percent.VehicleStatsDefLevelMilliPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54200, ), 
                        ecu_speed_mph = samsara.models.vehicle_stats_ecu_speed_mph.VehicleStatsEcuSpeedMph(
                            time = '2020-01-27T07:06:25Z', 
                            value = 32.1, ), 
                        engine_coolant_temperature_milli_c = samsara.models.vehicle_stats_engine_coolant_temp_milli_c.VehicleStatsEngineCoolantTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 31110, ), 
                        engine_immobilizer = samsara.models.vehicle_stats_engine_immobilizer.VehicleStatsEngineImmobilizer(
                            connected = False, 
                            state = 'ignition_disabled', 
                            time = '2020-01-27T07:06:25Z', ), 
                        engine_load_percent = samsara.models.vehicle_stats_engine_load_percent.VehicleStatsEngineLoadPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54, ), 
                        engine_oil_pressure_k_pa = samsara.models.vehicle_stats_engine_oil_pressure_k_pa.VehicleStatsEngineOilPressureKPa(
                            time = '2020-01-27T07:06:25Z', 
                            value = 100, ), 
                        engine_rpm = samsara.models.vehicle_stats_engine_rpm.VehicleStatsEngineRpm(
                            time = '2020-01-27T07:06:25Z', 
                            value = 1000, ), 
                        engine_state = samsara.models.vehicle_stats_engine_state.VehicleStatsEngineState(
                            time = '2020-01-27T07:06:25Z', 
                            value = 'On', ), 
                        fault_codes = samsara.models.vehicle_stats_fault_codes.VehicleStatsFaultCodes(
                            can_bus_type = 'CANBUS_J1939_500', 
                            j1939 = samsara.models.vehicle_stats_fault_codes_j1939.VehicleStatsFaultCodesJ1939(
                                check_engine_lights = samsara.models.vehicle_stats_fault_codes_j1939_lights.VehicleStatsFaultCodesJ1939Lights(
                                    emissions_is_on = True, 
                                    protect_is_on = False, 
                                    stop_is_on = False, 
                                    warning_is_on = False, ), 
                                diagnostic_trouble_codes = [
                                    samsara.models.vehicle_stats_fault_codes_j1939_trouble_code.VehicleStatsFaultCodesJ1939TroubleCode(
                                        fmi_description = 'Voltage Below Normal', 
                                        fmi_id = 9, 
                                        mil_status = 1, 
                                        occurrence_count = 1, 
                                        source_address_name = 'Engine #1', 
                                        spn_description = 'System Diagnostic Code #1', 
                                        spn_id = 3031, 
                                        tx_id = 0, 
                                        vendor_specific_fields = samsara.models.vehicle_stats_fault_codes_vendor_specific_fields.VehicleStatsFaultCodesVendorSpecificFields(
                                            dtc_description = 'false', 
                                            repair_instructions_url = 'false', ), )
                                    ], ), 
                            obdii = samsara.models.vehicle_stats_fault_codes_obdii.VehicleStatsFaultCodesOBDII(
                                check_engine_light_is_on = True, 
                                diagnostic_trouble_codes = [
                                    samsara.models.vehicle_stats_fault_codes_obdii_trouble_code.VehicleStatsFaultCodesOBDIITroubleCode(
                                        confirmed_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        ignition_type = 'spark', 
                                        mil_status = True, 
                                        monitor_status = samsara.models.vehicle_stats_fault_codes_passenger_monitor_status.VehicleStatsFaultCodesPassengerMonitorStatus(
                                            catalyst = 'N', 
                                            comprehensive = 'N', 
                                            egr = 'N', 
                                            evap_system = 'N', 
                                            fuel = 'N', 
                                            heated_catalyst = 'N', 
                                            heated_o2_sensor = 'N', 
                                            iso_sae_reserved = 'N', 
                                            misfire = 'N', 
                                            not_ready_count = 56, 
                                            o2_sensor = 'N', 
                                            secondary_air = 'N', ), 
                                        pending_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        permanent_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        tx_id = 0, )
                                    ], ), 
                            time = '2020-01-27T07:06:25Z', ), 
                        fuel_percent = samsara.models.vehicle_stats_fuel_percent.VehicleStatsFuelPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54, ), 
                        gps = samsara.models.vehicle_stats_gps.VehicleStatsGps(
                            heading_degrees = 120, 
                            latitude = 122.142, 
                            longitude = -93.343, 
                            reverse_geo = samsara.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                                formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                            speed_miles_per_hour = 48.3, 
                            time = '2020-01-27T07:06:25Z', ), 
                        gps_distance_meters = samsara.models.vehicle_stats_gps_distance_meters.VehicleStatsGpsDistanceMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 81029.591434899, ), 
                        gps_odometer_meters = samsara.models.vehicle_stats_gps_odometer_meters.VehicleStatsGpsOdometerMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), 
                        id = '112', 
                        intake_manifold_temperature_milli_c = samsara.models.vehicle_stats_intake_manifold_temp_milli_c.VehicleStatsIntakeManifoldTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 88000, ), 
                        name = 'Truck A7', 
                        nfc_card_scan = samsara.models.vehicle_stats_nfc_card_scan.VehicleStatsNfcCardScan(
                            card = samsara.models.vehicle_stats_nfc_card_scan_card.VehicleStatsNfcCardScan_card(), 
                            time = '2020-01-27T07:06:25Z', ), 
                        obd_engine_seconds = samsara.models.vehicle_stats_obd_engine_seconds.VehicleStatsObdEngineSeconds(
                            time = '2020-01-27T07:06:25Z', 
                            value = 9723103, ), 
                        obd_odometer_meters = samsara.models.vehicle_stats_obd_odometer_meters.VehicleStatsObdOdometerMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), 
                        synthetic_engine_seconds = samsara.models.vehicle_stats_synthetic_engine_seconds.VehicleStatsSyntheticEngineSeconds(
                            decorations = samsara.models.vehicle_stats_decorations.VehicleStatsDecorations(
                                engine_states = samsara.models.vehicle_stats_decorations_engine_states.VehicleStatsDecorations_engineStates(
                                    value = 'On', ), 
                                fuel_percents = samsara.models.vehicle_stats_decorations_fuel_percents.VehicleStatsDecorations_fuelPercents(
                                    value = 54, ), 
                                tire_pressure = samsara.models.vehicle_stats_tire_pressures.VehicleStatsTirePressures(
                                    back_left_tire_pressure_k_pa = 200, 
                                    back_right_tire_pressure_k_pa = 200, 
                                    front_left_tire_pressure_k_pa = 200, 
                                    front_right_tire_pressure_k_pa = 200, ), ), 
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), )
                    ], 
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return VehicleStatsResponse(
                data = [
                    samsara.models.vehicle_stats_response_data.VehicleStatsResponse_data(
                        ambient_air_temperature_milli_c = samsara.models.vehicle_stats_ambient_air_temp_milli_c.VehicleStatsAmbientAirTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 31110, ), 
                        aux_input1 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            name = 'boom', 
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input10 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input2 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input3 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input4 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input5 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input6 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input7 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input8 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        aux_input9 = samsara.models.vehicle_stats_aux_input.VehicleStatsAuxInput(
                            time = '2020-01-27T07:06:25Z', 
                            value = True, ), 
                        barometric_pressure_pa = samsara.models.vehicle_stats_barometric_pressure_pa.VehicleStatsBarometricPressurePa(
                            time = '2020-01-27T07:06:25Z', 
                            value = 99000, ), 
                        battery_milli_volts = samsara.models.vehicle_stats_battery_voltage.VehicleStatsBatteryVoltage(
                            time = '2020-01-27T07:06:25Z', 
                            value = 7991, ), 
                        def_level_milli_percent = samsara.models.vehicle_stats_def_level_milli_percent.VehicleStatsDefLevelMilliPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54200, ), 
                        ecu_speed_mph = samsara.models.vehicle_stats_ecu_speed_mph.VehicleStatsEcuSpeedMph(
                            time = '2020-01-27T07:06:25Z', 
                            value = 32.1, ), 
                        engine_coolant_temperature_milli_c = samsara.models.vehicle_stats_engine_coolant_temp_milli_c.VehicleStatsEngineCoolantTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 31110, ), 
                        engine_immobilizer = samsara.models.vehicle_stats_engine_immobilizer.VehicleStatsEngineImmobilizer(
                            connected = False, 
                            state = 'ignition_disabled', 
                            time = '2020-01-27T07:06:25Z', ), 
                        engine_load_percent = samsara.models.vehicle_stats_engine_load_percent.VehicleStatsEngineLoadPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54, ), 
                        engine_oil_pressure_k_pa = samsara.models.vehicle_stats_engine_oil_pressure_k_pa.VehicleStatsEngineOilPressureKPa(
                            time = '2020-01-27T07:06:25Z', 
                            value = 100, ), 
                        engine_rpm = samsara.models.vehicle_stats_engine_rpm.VehicleStatsEngineRpm(
                            time = '2020-01-27T07:06:25Z', 
                            value = 1000, ), 
                        engine_state = samsara.models.vehicle_stats_engine_state.VehicleStatsEngineState(
                            time = '2020-01-27T07:06:25Z', 
                            value = 'On', ), 
                        fault_codes = samsara.models.vehicle_stats_fault_codes.VehicleStatsFaultCodes(
                            can_bus_type = 'CANBUS_J1939_500', 
                            j1939 = samsara.models.vehicle_stats_fault_codes_j1939.VehicleStatsFaultCodesJ1939(
                                check_engine_lights = samsara.models.vehicle_stats_fault_codes_j1939_lights.VehicleStatsFaultCodesJ1939Lights(
                                    emissions_is_on = True, 
                                    protect_is_on = False, 
                                    stop_is_on = False, 
                                    warning_is_on = False, ), 
                                diagnostic_trouble_codes = [
                                    samsara.models.vehicle_stats_fault_codes_j1939_trouble_code.VehicleStatsFaultCodesJ1939TroubleCode(
                                        fmi_description = 'Voltage Below Normal', 
                                        fmi_id = 9, 
                                        mil_status = 1, 
                                        occurrence_count = 1, 
                                        source_address_name = 'Engine #1', 
                                        spn_description = 'System Diagnostic Code #1', 
                                        spn_id = 3031, 
                                        tx_id = 0, 
                                        vendor_specific_fields = samsara.models.vehicle_stats_fault_codes_vendor_specific_fields.VehicleStatsFaultCodesVendorSpecificFields(
                                            dtc_description = 'false', 
                                            repair_instructions_url = 'false', ), )
                                    ], ), 
                            obdii = samsara.models.vehicle_stats_fault_codes_obdii.VehicleStatsFaultCodesOBDII(
                                check_engine_light_is_on = True, 
                                diagnostic_trouble_codes = [
                                    samsara.models.vehicle_stats_fault_codes_obdii_trouble_code.VehicleStatsFaultCodesOBDIITroubleCode(
                                        confirmed_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        ignition_type = 'spark', 
                                        mil_status = True, 
                                        monitor_status = samsara.models.vehicle_stats_fault_codes_passenger_monitor_status.VehicleStatsFaultCodesPassengerMonitorStatus(
                                            catalyst = 'N', 
                                            comprehensive = 'N', 
                                            egr = 'N', 
                                            evap_system = 'N', 
                                            fuel = 'N', 
                                            heated_catalyst = 'N', 
                                            heated_o2_sensor = 'N', 
                                            iso_sae_reserved = 'N', 
                                            misfire = 'N', 
                                            not_ready_count = 56, 
                                            o2_sensor = 'N', 
                                            secondary_air = 'N', ), 
                                        pending_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        permanent_dtcs = [
                                            samsara.models.vehicle_stats_fault_codes_passenger_dtc.VehicleStatsFaultCodesPassengerDtc(
                                                dtc_description = 'Fuel Rail/System Pressure - Too Low Bank 1', 
                                                dtc_id = 135, 
                                                dtc_short_code = 'P0087', )
                                            ], 
                                        tx_id = 0, )
                                    ], ), 
                            time = '2020-01-27T07:06:25Z', ), 
                        fuel_percent = samsara.models.vehicle_stats_fuel_percent.VehicleStatsFuelPercent(
                            time = '2020-01-27T07:06:25Z', 
                            value = 54, ), 
                        gps = samsara.models.vehicle_stats_gps.VehicleStatsGps(
                            heading_degrees = 120, 
                            latitude = 122.142, 
                            longitude = -93.343, 
                            reverse_geo = samsara.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                                formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                            speed_miles_per_hour = 48.3, 
                            time = '2020-01-27T07:06:25Z', ), 
                        gps_distance_meters = samsara.models.vehicle_stats_gps_distance_meters.VehicleStatsGpsDistanceMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 81029.591434899, ), 
                        gps_odometer_meters = samsara.models.vehicle_stats_gps_odometer_meters.VehicleStatsGpsOdometerMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), 
                        id = '112', 
                        intake_manifold_temperature_milli_c = samsara.models.vehicle_stats_intake_manifold_temp_milli_c.VehicleStatsIntakeManifoldTempMilliC(
                            time = '2020-01-27T07:06:25Z', 
                            value = 88000, ), 
                        name = 'Truck A7', 
                        nfc_card_scan = samsara.models.vehicle_stats_nfc_card_scan.VehicleStatsNfcCardScan(
                            card = samsara.models.vehicle_stats_nfc_card_scan_card.VehicleStatsNfcCardScan_card(), 
                            time = '2020-01-27T07:06:25Z', ), 
                        obd_engine_seconds = samsara.models.vehicle_stats_obd_engine_seconds.VehicleStatsObdEngineSeconds(
                            time = '2020-01-27T07:06:25Z', 
                            value = 9723103, ), 
                        obd_odometer_meters = samsara.models.vehicle_stats_obd_odometer_meters.VehicleStatsObdOdometerMeters(
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), 
                        synthetic_engine_seconds = samsara.models.vehicle_stats_synthetic_engine_seconds.VehicleStatsSyntheticEngineSeconds(
                            decorations = samsara.models.vehicle_stats_decorations.VehicleStatsDecorations(
                                engine_states = samsara.models.vehicle_stats_decorations_engine_states.VehicleStatsDecorations_engineStates(
                                    value = 'On', ), 
                                fuel_percents = samsara.models.vehicle_stats_decorations_fuel_percents.VehicleStatsDecorations_fuelPercents(
                                    value = 54, ), 
                                tire_pressure = samsara.models.vehicle_stats_tire_pressures.VehicleStatsTirePressures(
                                    back_left_tire_pressure_k_pa = 200, 
                                    back_right_tire_pressure_k_pa = 200, 
                                    front_left_tire_pressure_k_pa = 200, 
                                    front_right_tire_pressure_k_pa = 200, ), ), 
                            time = '2020-01-27T07:06:25Z', 
                            value = 14010293, ), )
                    ],
                pagination = samsara.models.pagination_response.paginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, ),
        )

    def testVehicleStatsResponse(self):
        """Test VehicleStatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
