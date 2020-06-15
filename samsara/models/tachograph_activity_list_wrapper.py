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


class TachographActivityListWrapper(object):
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
        'activity': 'list[TachographActivity]',
        'driver': 'DriverTinyResponse'
    }

    attribute_map = {
        'activity': 'activity',
        'driver': 'driver'
    }

    def __init__(self, activity=None, driver=None, local_vars_configuration=None):  # noqa: E501
        """TachographActivityListWrapper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._activity = None
        self._driver = None
        self.discriminator = None

        if activity is not None:
            self.activity = activity
        if driver is not None:
            self.driver = driver

    @property
    def activity(self):
        """Gets the activity of this TachographActivityListWrapper.  # noqa: E501

        List of all driver tachograph activities in a specified time range.  # noqa: E501

        :return: The activity of this TachographActivityListWrapper.  # noqa: E501
        :rtype: list[TachographActivity]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this TachographActivityListWrapper.

        List of all driver tachograph activities in a specified time range.  # noqa: E501

        :param activity: The activity of this TachographActivityListWrapper.  # noqa: E501
        :type: list[TachographActivity]
        """

        self._activity = activity

    @property
    def driver(self):
        """Gets the driver of this TachographActivityListWrapper.  # noqa: E501


        :return: The driver of this TachographActivityListWrapper.  # noqa: E501
        :rtype: DriverTinyResponse
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this TachographActivityListWrapper.


        :param driver: The driver of this TachographActivityListWrapper.  # noqa: E501
        :type: DriverTinyResponse
        """

        self._driver = driver

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
        if not isinstance(other, TachographActivityListWrapper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TachographActivityListWrapper):
            return True

        return self.to_dict() != other.to_dict()
