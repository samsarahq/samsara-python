# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2020-06-15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class VehicleStatsDecorations(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ambient_air_temperature_milli_c': 'VehicleStatsDecorationsAmbientAirTemperatureMilliC',
        'aux_input1': 'VehicleStatsAuxInputDecoration',
        'aux_input10': 'VehicleStatsAuxInputDecoration',
        'aux_input2': 'VehicleStatsAuxInputDecoration',
        'aux_input3': 'VehicleStatsAuxInputDecoration',
        'aux_input4': 'VehicleStatsAuxInputDecoration',
        'aux_input5': 'VehicleStatsAuxInputDecoration',
        'aux_input6': 'VehicleStatsAuxInputDecoration',
        'aux_input7': 'VehicleStatsAuxInputDecoration',
        'aux_input8': 'VehicleStatsAuxInputDecoration',
        'aux_input9': 'VehicleStatsAuxInputDecoration',
        'barometric_pressure_pa': 'VehicleStatsDecorationsBarometricPressurePa',
        'battery_milli_volts': 'VehicleStatsDecorationsBatteryMilliVolts',
        'def_level_milli_percent': 'VehicleStatsDecorationsDefLevelMilliPercent',
        'ecu_speed_mph': 'VehicleStatsDecorationsEcuSpeedMph',
        'engine_coolant_temperature_milli_c': 'VehicleStatsDecorationsEngineCoolantTemperatureMilliC',
        'engine_load_percent': 'VehicleStatsDecorationsEngineLoadPercent',
        'engine_oil_pressure_k_pa': 'VehicleStatsDecorationsEngineOilPressureKPa',
        'engine_rpm': 'VehicleStatsDecorationsEngineRpm',
        'engine_states': 'VehicleStatsDecorationsEngineStates',
        'fault_codes': 'VehicleStatsFaultCodesValue',
        'fuel_percents': 'VehicleStatsDecorationsFuelPercents',
        'gps': 'VehicleStatsDecorationsGps',
        'gps_distance_meters': 'VehicleStatsDecorationsGpsDistanceMeters',
        'gps_odometer_meters': 'VehicleStatsDecorationsGpsOdometerMeters',
        'intake_manifold_temperature_milli_c': 'VehicleStatsDecorationsIntakeManifoldTemperatureMilliC',
        'obd_engine_seconds': 'VehicleStatsDecorationsObdEngineSeconds',
        'obd_odometer_meters': 'VehicleStatsDecorationsObdOdometerMeters',
        'tire_pressure': 'VehicleStatsTirePressures'
    }

    attribute_map = {
        'ambient_air_temperature_milli_c': 'ambientAirTemperatureMilliC',
        'aux_input1': 'auxInput1',
        'aux_input10': 'auxInput10',
        'aux_input2': 'auxInput2',
        'aux_input3': 'auxInput3',
        'aux_input4': 'auxInput4',
        'aux_input5': 'auxInput5',
        'aux_input6': 'auxInput6',
        'aux_input7': 'auxInput7',
        'aux_input8': 'auxInput8',
        'aux_input9': 'auxInput9',
        'barometric_pressure_pa': 'barometricPressurePa',
        'battery_milli_volts': 'batteryMilliVolts',
        'def_level_milli_percent': 'defLevelMilliPercent',
        'ecu_speed_mph': 'ecuSpeedMph',
        'engine_coolant_temperature_milli_c': 'engineCoolantTemperatureMilliC',
        'engine_load_percent': 'engineLoadPercent',
        'engine_oil_pressure_k_pa': 'engineOilPressureKPa',
        'engine_rpm': 'engineRpm',
        'engine_states': 'engineStates',
        'fault_codes': 'faultCodes',
        'fuel_percents': 'fuelPercents',
        'gps': 'gps',
        'gps_distance_meters': 'gpsDistanceMeters',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'intake_manifold_temperature_milli_c': 'intakeManifoldTemperatureMilliC',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_odometer_meters': 'obdOdometerMeters',
        'tire_pressure': 'tirePressure'
    }

    def __init__(self, ambient_air_temperature_milli_c=None, aux_input1=None, aux_input10=None, aux_input2=None, aux_input3=None, aux_input4=None, aux_input5=None, aux_input6=None, aux_input7=None, aux_input8=None, aux_input9=None, barometric_pressure_pa=None, battery_milli_volts=None, def_level_milli_percent=None, ecu_speed_mph=None, engine_coolant_temperature_milli_c=None, engine_load_percent=None, engine_oil_pressure_k_pa=None, engine_rpm=None, engine_states=None, fault_codes=None, fuel_percents=None, gps=None, gps_distance_meters=None, gps_odometer_meters=None, intake_manifold_temperature_milli_c=None, obd_engine_seconds=None, obd_odometer_meters=None, tire_pressure=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsDecorations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ambient_air_temperature_milli_c = None
        self._aux_input1 = None
        self._aux_input10 = None
        self._aux_input2 = None
        self._aux_input3 = None
        self._aux_input4 = None
        self._aux_input5 = None
        self._aux_input6 = None
        self._aux_input7 = None
        self._aux_input8 = None
        self._aux_input9 = None
        self._barometric_pressure_pa = None
        self._battery_milli_volts = None
        self._def_level_milli_percent = None
        self._ecu_speed_mph = None
        self._engine_coolant_temperature_milli_c = None
        self._engine_load_percent = None
        self._engine_oil_pressure_k_pa = None
        self._engine_rpm = None
        self._engine_states = None
        self._fault_codes = None
        self._fuel_percents = None
        self._gps = None
        self._gps_distance_meters = None
        self._gps_odometer_meters = None
        self._intake_manifold_temperature_milli_c = None
        self._obd_engine_seconds = None
        self._obd_odometer_meters = None
        self._tire_pressure = None
        self.discriminator = None

        if ambient_air_temperature_milli_c is not None:
            self.ambient_air_temperature_milli_c = ambient_air_temperature_milli_c
        if aux_input1 is not None:
            self.aux_input1 = aux_input1
        if aux_input10 is not None:
            self.aux_input10 = aux_input10
        if aux_input2 is not None:
            self.aux_input2 = aux_input2
        if aux_input3 is not None:
            self.aux_input3 = aux_input3
        if aux_input4 is not None:
            self.aux_input4 = aux_input4
        if aux_input5 is not None:
            self.aux_input5 = aux_input5
        if aux_input6 is not None:
            self.aux_input6 = aux_input6
        if aux_input7 is not None:
            self.aux_input7 = aux_input7
        if aux_input8 is not None:
            self.aux_input8 = aux_input8
        if aux_input9 is not None:
            self.aux_input9 = aux_input9
        if barometric_pressure_pa is not None:
            self.barometric_pressure_pa = barometric_pressure_pa
        if battery_milli_volts is not None:
            self.battery_milli_volts = battery_milli_volts
        if def_level_milli_percent is not None:
            self.def_level_milli_percent = def_level_milli_percent
        if ecu_speed_mph is not None:
            self.ecu_speed_mph = ecu_speed_mph
        if engine_coolant_temperature_milli_c is not None:
            self.engine_coolant_temperature_milli_c = engine_coolant_temperature_milli_c
        if engine_load_percent is not None:
            self.engine_load_percent = engine_load_percent
        if engine_oil_pressure_k_pa is not None:
            self.engine_oil_pressure_k_pa = engine_oil_pressure_k_pa
        if engine_rpm is not None:
            self.engine_rpm = engine_rpm
        if engine_states is not None:
            self.engine_states = engine_states
        if fault_codes is not None:
            self.fault_codes = fault_codes
        if fuel_percents is not None:
            self.fuel_percents = fuel_percents
        if gps is not None:
            self.gps = gps
        if gps_distance_meters is not None:
            self.gps_distance_meters = gps_distance_meters
        if gps_odometer_meters is not None:
            self.gps_odometer_meters = gps_odometer_meters
        if intake_manifold_temperature_milli_c is not None:
            self.intake_manifold_temperature_milli_c = intake_manifold_temperature_milli_c
        if obd_engine_seconds is not None:
            self.obd_engine_seconds = obd_engine_seconds
        if obd_odometer_meters is not None:
            self.obd_odometer_meters = obd_odometer_meters
        if tire_pressure is not None:
            self.tire_pressure = tire_pressure

    @property
    def ambient_air_temperature_milli_c(self):
        """Gets the ambient_air_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501


        :return: The ambient_air_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsAmbientAirTemperatureMilliC
        """
        return self._ambient_air_temperature_milli_c

    @ambient_air_temperature_milli_c.setter
    def ambient_air_temperature_milli_c(self, ambient_air_temperature_milli_c):
        """Sets the ambient_air_temperature_milli_c of this VehicleStatsDecorations.


        :param ambient_air_temperature_milli_c: The ambient_air_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsAmbientAirTemperatureMilliC
        """

        self._ambient_air_temperature_milli_c = ambient_air_temperature_milli_c

    @property
    def aux_input1(self):
        """Gets the aux_input1 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input1 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input1

    @aux_input1.setter
    def aux_input1(self, aux_input1):
        """Sets the aux_input1 of this VehicleStatsDecorations.


        :param aux_input1: The aux_input1 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input1 = aux_input1

    @property
    def aux_input10(self):
        """Gets the aux_input10 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input10 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input10

    @aux_input10.setter
    def aux_input10(self, aux_input10):
        """Sets the aux_input10 of this VehicleStatsDecorations.


        :param aux_input10: The aux_input10 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input10 = aux_input10

    @property
    def aux_input2(self):
        """Gets the aux_input2 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input2 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input2

    @aux_input2.setter
    def aux_input2(self, aux_input2):
        """Sets the aux_input2 of this VehicleStatsDecorations.


        :param aux_input2: The aux_input2 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input2 = aux_input2

    @property
    def aux_input3(self):
        """Gets the aux_input3 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input3 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input3

    @aux_input3.setter
    def aux_input3(self, aux_input3):
        """Sets the aux_input3 of this VehicleStatsDecorations.


        :param aux_input3: The aux_input3 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input3 = aux_input3

    @property
    def aux_input4(self):
        """Gets the aux_input4 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input4 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input4

    @aux_input4.setter
    def aux_input4(self, aux_input4):
        """Sets the aux_input4 of this VehicleStatsDecorations.


        :param aux_input4: The aux_input4 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input4 = aux_input4

    @property
    def aux_input5(self):
        """Gets the aux_input5 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input5 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input5

    @aux_input5.setter
    def aux_input5(self, aux_input5):
        """Sets the aux_input5 of this VehicleStatsDecorations.


        :param aux_input5: The aux_input5 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input5 = aux_input5

    @property
    def aux_input6(self):
        """Gets the aux_input6 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input6 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input6

    @aux_input6.setter
    def aux_input6(self, aux_input6):
        """Sets the aux_input6 of this VehicleStatsDecorations.


        :param aux_input6: The aux_input6 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input6 = aux_input6

    @property
    def aux_input7(self):
        """Gets the aux_input7 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input7 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input7

    @aux_input7.setter
    def aux_input7(self, aux_input7):
        """Sets the aux_input7 of this VehicleStatsDecorations.


        :param aux_input7: The aux_input7 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input7 = aux_input7

    @property
    def aux_input8(self):
        """Gets the aux_input8 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input8 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input8

    @aux_input8.setter
    def aux_input8(self, aux_input8):
        """Sets the aux_input8 of this VehicleStatsDecorations.


        :param aux_input8: The aux_input8 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input8 = aux_input8

    @property
    def aux_input9(self):
        """Gets the aux_input9 of this VehicleStatsDecorations.  # noqa: E501


        :return: The aux_input9 of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsAuxInputDecoration
        """
        return self._aux_input9

    @aux_input9.setter
    def aux_input9(self, aux_input9):
        """Sets the aux_input9 of this VehicleStatsDecorations.


        :param aux_input9: The aux_input9 of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsAuxInputDecoration
        """

        self._aux_input9 = aux_input9

    @property
    def barometric_pressure_pa(self):
        """Gets the barometric_pressure_pa of this VehicleStatsDecorations.  # noqa: E501


        :return: The barometric_pressure_pa of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsBarometricPressurePa
        """
        return self._barometric_pressure_pa

    @barometric_pressure_pa.setter
    def barometric_pressure_pa(self, barometric_pressure_pa):
        """Sets the barometric_pressure_pa of this VehicleStatsDecorations.


        :param barometric_pressure_pa: The barometric_pressure_pa of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsBarometricPressurePa
        """

        self._barometric_pressure_pa = barometric_pressure_pa

    @property
    def battery_milli_volts(self):
        """Gets the battery_milli_volts of this VehicleStatsDecorations.  # noqa: E501


        :return: The battery_milli_volts of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsBatteryMilliVolts
        """
        return self._battery_milli_volts

    @battery_milli_volts.setter
    def battery_milli_volts(self, battery_milli_volts):
        """Sets the battery_milli_volts of this VehicleStatsDecorations.


        :param battery_milli_volts: The battery_milli_volts of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsBatteryMilliVolts
        """

        self._battery_milli_volts = battery_milli_volts

    @property
    def def_level_milli_percent(self):
        """Gets the def_level_milli_percent of this VehicleStatsDecorations.  # noqa: E501


        :return: The def_level_milli_percent of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsDefLevelMilliPercent
        """
        return self._def_level_milli_percent

    @def_level_milli_percent.setter
    def def_level_milli_percent(self, def_level_milli_percent):
        """Sets the def_level_milli_percent of this VehicleStatsDecorations.


        :param def_level_milli_percent: The def_level_milli_percent of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsDefLevelMilliPercent
        """

        self._def_level_milli_percent = def_level_milli_percent

    @property
    def ecu_speed_mph(self):
        """Gets the ecu_speed_mph of this VehicleStatsDecorations.  # noqa: E501


        :return: The ecu_speed_mph of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEcuSpeedMph
        """
        return self._ecu_speed_mph

    @ecu_speed_mph.setter
    def ecu_speed_mph(self, ecu_speed_mph):
        """Sets the ecu_speed_mph of this VehicleStatsDecorations.


        :param ecu_speed_mph: The ecu_speed_mph of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEcuSpeedMph
        """

        self._ecu_speed_mph = ecu_speed_mph

    @property
    def engine_coolant_temperature_milli_c(self):
        """Gets the engine_coolant_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501


        :return: The engine_coolant_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEngineCoolantTemperatureMilliC
        """
        return self._engine_coolant_temperature_milli_c

    @engine_coolant_temperature_milli_c.setter
    def engine_coolant_temperature_milli_c(self, engine_coolant_temperature_milli_c):
        """Sets the engine_coolant_temperature_milli_c of this VehicleStatsDecorations.


        :param engine_coolant_temperature_milli_c: The engine_coolant_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEngineCoolantTemperatureMilliC
        """

        self._engine_coolant_temperature_milli_c = engine_coolant_temperature_milli_c

    @property
    def engine_load_percent(self):
        """Gets the engine_load_percent of this VehicleStatsDecorations.  # noqa: E501


        :return: The engine_load_percent of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEngineLoadPercent
        """
        return self._engine_load_percent

    @engine_load_percent.setter
    def engine_load_percent(self, engine_load_percent):
        """Sets the engine_load_percent of this VehicleStatsDecorations.


        :param engine_load_percent: The engine_load_percent of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEngineLoadPercent
        """

        self._engine_load_percent = engine_load_percent

    @property
    def engine_oil_pressure_k_pa(self):
        """Gets the engine_oil_pressure_k_pa of this VehicleStatsDecorations.  # noqa: E501


        :return: The engine_oil_pressure_k_pa of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEngineOilPressureKPa
        """
        return self._engine_oil_pressure_k_pa

    @engine_oil_pressure_k_pa.setter
    def engine_oil_pressure_k_pa(self, engine_oil_pressure_k_pa):
        """Sets the engine_oil_pressure_k_pa of this VehicleStatsDecorations.


        :param engine_oil_pressure_k_pa: The engine_oil_pressure_k_pa of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEngineOilPressureKPa
        """

        self._engine_oil_pressure_k_pa = engine_oil_pressure_k_pa

    @property
    def engine_rpm(self):
        """Gets the engine_rpm of this VehicleStatsDecorations.  # noqa: E501


        :return: The engine_rpm of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEngineRpm
        """
        return self._engine_rpm

    @engine_rpm.setter
    def engine_rpm(self, engine_rpm):
        """Sets the engine_rpm of this VehicleStatsDecorations.


        :param engine_rpm: The engine_rpm of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEngineRpm
        """

        self._engine_rpm = engine_rpm

    @property
    def engine_states(self):
        """Gets the engine_states of this VehicleStatsDecorations.  # noqa: E501


        :return: The engine_states of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsEngineStates
        """
        return self._engine_states

    @engine_states.setter
    def engine_states(self, engine_states):
        """Sets the engine_states of this VehicleStatsDecorations.


        :param engine_states: The engine_states of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsEngineStates
        """

        self._engine_states = engine_states

    @property
    def fault_codes(self):
        """Gets the fault_codes of this VehicleStatsDecorations.  # noqa: E501


        :return: The fault_codes of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsFaultCodesValue
        """
        return self._fault_codes

    @fault_codes.setter
    def fault_codes(self, fault_codes):
        """Sets the fault_codes of this VehicleStatsDecorations.


        :param fault_codes: The fault_codes of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsFaultCodesValue
        """

        self._fault_codes = fault_codes

    @property
    def fuel_percents(self):
        """Gets the fuel_percents of this VehicleStatsDecorations.  # noqa: E501


        :return: The fuel_percents of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsFuelPercents
        """
        return self._fuel_percents

    @fuel_percents.setter
    def fuel_percents(self, fuel_percents):
        """Sets the fuel_percents of this VehicleStatsDecorations.


        :param fuel_percents: The fuel_percents of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsFuelPercents
        """

        self._fuel_percents = fuel_percents

    @property
    def gps(self):
        """Gets the gps of this VehicleStatsDecorations.  # noqa: E501


        :return: The gps of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsGps
        """
        return self._gps

    @gps.setter
    def gps(self, gps):
        """Sets the gps of this VehicleStatsDecorations.


        :param gps: The gps of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsGps
        """

        self._gps = gps

    @property
    def gps_distance_meters(self):
        """Gets the gps_distance_meters of this VehicleStatsDecorations.  # noqa: E501


        :return: The gps_distance_meters of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsGpsDistanceMeters
        """
        return self._gps_distance_meters

    @gps_distance_meters.setter
    def gps_distance_meters(self, gps_distance_meters):
        """Sets the gps_distance_meters of this VehicleStatsDecorations.


        :param gps_distance_meters: The gps_distance_meters of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsGpsDistanceMeters
        """

        self._gps_distance_meters = gps_distance_meters

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this VehicleStatsDecorations.  # noqa: E501


        :return: The gps_odometer_meters of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsGpsOdometerMeters
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this VehicleStatsDecorations.


        :param gps_odometer_meters: The gps_odometer_meters of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsGpsOdometerMeters
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def intake_manifold_temperature_milli_c(self):
        """Gets the intake_manifold_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501


        :return: The intake_manifold_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsIntakeManifoldTemperatureMilliC
        """
        return self._intake_manifold_temperature_milli_c

    @intake_manifold_temperature_milli_c.setter
    def intake_manifold_temperature_milli_c(self, intake_manifold_temperature_milli_c):
        """Sets the intake_manifold_temperature_milli_c of this VehicleStatsDecorations.


        :param intake_manifold_temperature_milli_c: The intake_manifold_temperature_milli_c of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsIntakeManifoldTemperatureMilliC
        """

        self._intake_manifold_temperature_milli_c = intake_manifold_temperature_milli_c

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this VehicleStatsDecorations.  # noqa: E501


        :return: The obd_engine_seconds of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsObdEngineSeconds
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this VehicleStatsDecorations.


        :param obd_engine_seconds: The obd_engine_seconds of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsObdEngineSeconds
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_odometer_meters(self):
        """Gets the obd_odometer_meters of this VehicleStatsDecorations.  # noqa: E501


        :return: The obd_odometer_meters of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsDecorationsObdOdometerMeters
        """
        return self._obd_odometer_meters

    @obd_odometer_meters.setter
    def obd_odometer_meters(self, obd_odometer_meters):
        """Sets the obd_odometer_meters of this VehicleStatsDecorations.


        :param obd_odometer_meters: The obd_odometer_meters of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsDecorationsObdOdometerMeters
        """

        self._obd_odometer_meters = obd_odometer_meters

    @property
    def tire_pressure(self):
        """Gets the tire_pressure of this VehicleStatsDecorations.  # noqa: E501


        :return: The tire_pressure of this VehicleStatsDecorations.  # noqa: E501
        :rtype: VehicleStatsTirePressures
        """
        return self._tire_pressure

    @tire_pressure.setter
    def tire_pressure(self, tire_pressure):
        """Sets the tire_pressure of this VehicleStatsDecorations.


        :param tire_pressure: The tire_pressure of this VehicleStatsDecorations.  # noqa: E501
        :type: VehicleStatsTirePressures
        """

        self._tire_pressure = tire_pressure

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VehicleStatsDecorations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsDecorations):
            return True

        return self.to_dict() != other.to_dict()
