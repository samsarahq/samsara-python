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


class VehicleStatsFaultCodesValueObdii(object):
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
        'check_engine_light_is_on': 'bool',
        'diagnostic_trouble_codes': 'list[VehicleStatsFaultCodesValueObdiiDiagnosticTroubleCodes]'
    }

    attribute_map = {
        'check_engine_light_is_on': 'checkEngineLightIsOn',
        'diagnostic_trouble_codes': 'diagnosticTroubleCodes'
    }

    def __init__(self, check_engine_light_is_on=None, diagnostic_trouble_codes=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsFaultCodesValueObdii - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_engine_light_is_on = None
        self._diagnostic_trouble_codes = None
        self.discriminator = None

        if check_engine_light_is_on is not None:
            self.check_engine_light_is_on = check_engine_light_is_on
        if diagnostic_trouble_codes is not None:
            self.diagnostic_trouble_codes = diagnostic_trouble_codes

    @property
    def check_engine_light_is_on(self):
        """Gets the check_engine_light_is_on of this VehicleStatsFaultCodesValueObdii.  # noqa: E501

        True if the check engine light is illuminated (MIL status field is nonzero for any faults).  # noqa: E501

        :return: The check_engine_light_is_on of this VehicleStatsFaultCodesValueObdii.  # noqa: E501
        :rtype: bool
        """
        return self._check_engine_light_is_on

    @check_engine_light_is_on.setter
    def check_engine_light_is_on(self, check_engine_light_is_on):
        """Sets the check_engine_light_is_on of this VehicleStatsFaultCodesValueObdii.

        True if the check engine light is illuminated (MIL status field is nonzero for any faults).  # noqa: E501

        :param check_engine_light_is_on: The check_engine_light_is_on of this VehicleStatsFaultCodesValueObdii.  # noqa: E501
        :type: bool
        """

        self._check_engine_light_is_on = check_engine_light_is_on

    @property
    def diagnostic_trouble_codes(self):
        """Gets the diagnostic_trouble_codes of this VehicleStatsFaultCodesValueObdii.  # noqa: E501

        Diagnostic trouble codes for passenger vehicles.  # noqa: E501

        :return: The diagnostic_trouble_codes of this VehicleStatsFaultCodesValueObdii.  # noqa: E501
        :rtype: list[VehicleStatsFaultCodesValueObdiiDiagnosticTroubleCodes]
        """
        return self._diagnostic_trouble_codes

    @diagnostic_trouble_codes.setter
    def diagnostic_trouble_codes(self, diagnostic_trouble_codes):
        """Sets the diagnostic_trouble_codes of this VehicleStatsFaultCodesValueObdii.

        Diagnostic trouble codes for passenger vehicles.  # noqa: E501

        :param diagnostic_trouble_codes: The diagnostic_trouble_codes of this VehicleStatsFaultCodesValueObdii.  # noqa: E501
        :type: list[VehicleStatsFaultCodesValueObdiiDiagnosticTroubleCodes]
        """

        self._diagnostic_trouble_codes = diagnostic_trouble_codes

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
        if not isinstance(other, VehicleStatsFaultCodesValueObdii):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsFaultCodesValueObdii):
            return True

        return self.to_dict() != other.to_dict()