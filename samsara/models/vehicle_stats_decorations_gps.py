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


class VehicleStatsDecorationsGps(object):
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
        'address': 'VehicleLocationAddress',
        'heading_degrees': 'float',
        'is_ecu_speed': 'bool',
        'latitude': 'float',
        'longitude': 'float',
        'reverse_geo': 'VehicleLocationReverseGeo',
        'speed_miles_per_hour': 'float'
    }

    attribute_map = {
        'address': 'address',
        'heading_degrees': 'headingDegrees',
        'is_ecu_speed': 'isEcuSpeed',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'reverse_geo': 'reverseGeo',
        'speed_miles_per_hour': 'speedMilesPerHour'
    }

    def __init__(self, address=None, heading_degrees=None, is_ecu_speed=None, latitude=None, longitude=None, reverse_geo=None, speed_miles_per_hour=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsDecorationsGps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._heading_degrees = None
        self._is_ecu_speed = None
        self._latitude = None
        self._longitude = None
        self._reverse_geo = None
        self._speed_miles_per_hour = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if heading_degrees is not None:
            self.heading_degrees = heading_degrees
        if is_ecu_speed is not None:
            self.is_ecu_speed = is_ecu_speed
        self.latitude = latitude
        self.longitude = longitude
        if reverse_geo is not None:
            self.reverse_geo = reverse_geo
        if speed_miles_per_hour is not None:
            self.speed_miles_per_hour = speed_miles_per_hour

    @property
    def address(self):
        """Gets the address of this VehicleStatsDecorationsGps.  # noqa: E501


        :return: The address of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: VehicleLocationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this VehicleStatsDecorationsGps.


        :param address: The address of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: VehicleLocationAddress
        """

        self._address = address

    @property
    def heading_degrees(self):
        """Gets the heading_degrees of this VehicleStatsDecorationsGps.  # noqa: E501

        Heading of the vehicle in degrees.  # noqa: E501

        :return: The heading_degrees of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: float
        """
        return self._heading_degrees

    @heading_degrees.setter
    def heading_degrees(self, heading_degrees):
        """Sets the heading_degrees of this VehicleStatsDecorationsGps.

        Heading of the vehicle in degrees.  # noqa: E501

        :param heading_degrees: The heading_degrees of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: float
        """

        self._heading_degrees = heading_degrees

    @property
    def is_ecu_speed(self):
        """Gets the is_ecu_speed of this VehicleStatsDecorationsGps.  # noqa: E501

        True if the speed value is reported from the ECU. Speed value is reported from GPS otherwise.  # noqa: E501

        :return: The is_ecu_speed of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: bool
        """
        return self._is_ecu_speed

    @is_ecu_speed.setter
    def is_ecu_speed(self, is_ecu_speed):
        """Sets the is_ecu_speed of this VehicleStatsDecorationsGps.

        True if the speed value is reported from the ECU. Speed value is reported from GPS otherwise.  # noqa: E501

        :param is_ecu_speed: The is_ecu_speed of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: bool
        """

        self._is_ecu_speed = is_ecu_speed

    @property
    def latitude(self):
        """Gets the latitude of this VehicleStatsDecorationsGps.  # noqa: E501

        GPS latitude represented in degrees  # noqa: E501

        :return: The latitude of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this VehicleStatsDecorationsGps.

        GPS latitude represented in degrees  # noqa: E501

        :param latitude: The latitude of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and latitude is None:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this VehicleStatsDecorationsGps.  # noqa: E501

        GPS longitude represented in degrees  # noqa: E501

        :return: The longitude of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this VehicleStatsDecorationsGps.

        GPS longitude represented in degrees  # noqa: E501

        :param longitude: The longitude of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and longitude is None:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def reverse_geo(self):
        """Gets the reverse_geo of this VehicleStatsDecorationsGps.  # noqa: E501


        :return: The reverse_geo of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: VehicleLocationReverseGeo
        """
        return self._reverse_geo

    @reverse_geo.setter
    def reverse_geo(self, reverse_geo):
        """Sets the reverse_geo of this VehicleStatsDecorationsGps.


        :param reverse_geo: The reverse_geo of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: VehicleLocationReverseGeo
        """

        self._reverse_geo = reverse_geo

    @property
    def speed_miles_per_hour(self):
        """Gets the speed_miles_per_hour of this VehicleStatsDecorationsGps.  # noqa: E501

        GPS speed of the vehicle in miles per hour.  # noqa: E501

        :return: The speed_miles_per_hour of this VehicleStatsDecorationsGps.  # noqa: E501
        :rtype: float
        """
        return self._speed_miles_per_hour

    @speed_miles_per_hour.setter
    def speed_miles_per_hour(self, speed_miles_per_hour):
        """Sets the speed_miles_per_hour of this VehicleStatsDecorationsGps.

        GPS speed of the vehicle in miles per hour.  # noqa: E501

        :param speed_miles_per_hour: The speed_miles_per_hour of this VehicleStatsDecorationsGps.  # noqa: E501
        :type: float
        """

        self._speed_miles_per_hour = speed_miles_per_hour

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
        if not isinstance(other, VehicleStatsDecorationsGps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsDecorationsGps):
            return True

        return self.to_dict() != other.to_dict()
