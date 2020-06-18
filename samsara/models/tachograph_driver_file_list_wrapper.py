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


class TachographDriverFileListWrapper(object):
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
        'driver': 'DriverTinyResponse',
        'files': 'list[TachographDriverFile]'
    }

    attribute_map = {
        'driver': 'driver',
        'files': 'files'
    }

    def __init__(self, driver=None, files=None, local_vars_configuration=None):  # noqa: E501
        """TachographDriverFileListWrapper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._driver = None
        self._files = None
        self.discriminator = None

        if driver is not None:
            self.driver = driver
        if files is not None:
            self.files = files

    @property
    def driver(self):
        """Gets the driver of this TachographDriverFileListWrapper.  # noqa: E501


        :return: The driver of this TachographDriverFileListWrapper.  # noqa: E501
        :rtype: DriverTinyResponse
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this TachographDriverFileListWrapper.


        :param driver: The driver of this TachographDriverFileListWrapper.  # noqa: E501
        :type: DriverTinyResponse
        """

        self._driver = driver

    @property
    def files(self):
        """Gets the files of this TachographDriverFileListWrapper.  # noqa: E501

        List of all tachograph driver files in a specified time range.  # noqa: E501

        :return: The files of this TachographDriverFileListWrapper.  # noqa: E501
        :rtype: list[TachographDriverFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this TachographDriverFileListWrapper.

        List of all tachograph driver files in a specified time range.  # noqa: E501

        :param files: The files of this TachographDriverFileListWrapper.  # noqa: E501
        :type: list[TachographDriverFile]
        """

        self._files = files

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
        if not isinstance(other, TachographDriverFileListWrapper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TachographDriverFileListWrapper):
            return True

        return self.to_dict() != other.to_dict()