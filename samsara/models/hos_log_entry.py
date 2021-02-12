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


class HosLogEntry(object):
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
        'codrivers': 'list[DriverTinyResponse]',
        'hos_status_type': 'str',
        'log_end_time': 'str',
        'log_recorded_location': 'Location',
        'log_start_time': 'str',
        'remark': 'str',
        'vehicle': 'VehicleTinyResponse'
    }

    attribute_map = {
        'codrivers': 'codrivers',
        'hos_status_type': 'hosStatusType',
        'log_end_time': 'logEndTime',
        'log_recorded_location': 'logRecordedLocation',
        'log_start_time': 'logStartTime',
        'remark': 'remark',
        'vehicle': 'vehicle'
    }

    def __init__(self, codrivers=None, hos_status_type=None, log_end_time=None, log_recorded_location=None, log_start_time=None, remark=None, vehicle=None, local_vars_configuration=None):  # noqa: E501
        """HosLogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._codrivers = None
        self._hos_status_type = None
        self._log_end_time = None
        self._log_recorded_location = None
        self._log_start_time = None
        self._remark = None
        self._vehicle = None
        self.discriminator = None

        if codrivers is not None:
            self.codrivers = codrivers
        if hos_status_type is not None:
            self.hos_status_type = hos_status_type
        if log_end_time is not None:
            self.log_end_time = log_end_time
        if log_recorded_location is not None:
            self.log_recorded_location = log_recorded_location
        self.log_start_time = log_start_time
        if remark is not None:
            self.remark = remark
        if vehicle is not None:
            self.vehicle = vehicle

    @property
    def codrivers(self):
        """Gets the codrivers of this HosLogEntry.  # noqa: E501

        The codriver information.  # noqa: E501

        :return: The codrivers of this HosLogEntry.  # noqa: E501
        :rtype: list[DriverTinyResponse]
        """
        return self._codrivers

    @codrivers.setter
    def codrivers(self, codrivers):
        """Sets the codrivers of this HosLogEntry.

        The codriver information.  # noqa: E501

        :param codrivers: The codrivers of this HosLogEntry.  # noqa: E501
        :type: list[DriverTinyResponse]
        """

        self._codrivers = codrivers

    @property
    def hos_status_type(self):
        """Gets the hos_status_type of this HosLogEntry.  # noqa: E501

        The Hours of Service status type.  # noqa: E501

        :return: The hos_status_type of this HosLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._hos_status_type

    @hos_status_type.setter
    def hos_status_type(self, hos_status_type):
        """Sets the hos_status_type of this HosLogEntry.

        The Hours of Service status type.  # noqa: E501

        :param hos_status_type: The hos_status_type of this HosLogEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["offDuty", "sleeperBed", "driving", "onDuty", "yardMove", "personalConveyance"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and hos_status_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `hos_status_type` ({0}), must be one of {1}"  # noqa: E501
                .format(hos_status_type, allowed_values)
            )

        self._hos_status_type = hos_status_type

    @property
    def log_end_time(self):
        """Gets the log_end_time of this HosLogEntry.  # noqa: E501

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The log_end_time of this HosLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._log_end_time

    @log_end_time.setter
    def log_end_time(self, log_end_time):
        """Sets the log_end_time of this HosLogEntry.

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param log_end_time: The log_end_time of this HosLogEntry.  # noqa: E501
        :type: str
        """

        self._log_end_time = log_end_time

    @property
    def log_recorded_location(self):
        """Gets the log_recorded_location of this HosLogEntry.  # noqa: E501


        :return: The log_recorded_location of this HosLogEntry.  # noqa: E501
        :rtype: Location
        """
        return self._log_recorded_location

    @log_recorded_location.setter
    def log_recorded_location(self, log_recorded_location):
        """Sets the log_recorded_location of this HosLogEntry.


        :param log_recorded_location: The log_recorded_location of this HosLogEntry.  # noqa: E501
        :type: Location
        """

        self._log_recorded_location = log_recorded_location

    @property
    def log_start_time(self):
        """Gets the log_start_time of this HosLogEntry.  # noqa: E501

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The log_start_time of this HosLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._log_start_time

    @log_start_time.setter
    def log_start_time(self, log_start_time):
        """Sets the log_start_time of this HosLogEntry.

        UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param log_start_time: The log_start_time of this HosLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and log_start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `log_start_time`, must not be `None`")  # noqa: E501

        self._log_start_time = log_start_time

    @property
    def remark(self):
        """Gets the remark of this HosLogEntry.  # noqa: E501

        Remark associated with the log entry.  # noqa: E501

        :return: The remark of this HosLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this HosLogEntry.

        Remark associated with the log entry.  # noqa: E501

        :param remark: The remark of this HosLogEntry.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def vehicle(self):
        """Gets the vehicle of this HosLogEntry.  # noqa: E501


        :return: The vehicle of this HosLogEntry.  # noqa: E501
        :rtype: VehicleTinyResponse
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this HosLogEntry.


        :param vehicle: The vehicle of this HosLogEntry.  # noqa: E501
        :type: VehicleTinyResponse
        """

        self._vehicle = vehicle

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
        if not isinstance(other, HosLogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HosLogEntry):
            return True

        return self.to_dict() != other.to_dict()
