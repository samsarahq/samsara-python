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


class OrganizationInfo(object):
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
        'carrier_settings': 'OrganizationInfoCarrierSettings',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'carrier_settings': 'carrierSettings',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, carrier_settings=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._carrier_settings = None
        self._id = None
        self._name = None
        self.discriminator = None

        if carrier_settings is not None:
            self.carrier_settings = carrier_settings
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def carrier_settings(self):
        """Gets the carrier_settings of this OrganizationInfo.  # noqa: E501


        :return: The carrier_settings of this OrganizationInfo.  # noqa: E501
        :rtype: OrganizationInfoCarrierSettings
        """
        return self._carrier_settings

    @carrier_settings.setter
    def carrier_settings(self, carrier_settings):
        """Sets the carrier_settings of this OrganizationInfo.


        :param carrier_settings: The carrier_settings of this OrganizationInfo.  # noqa: E501
        :type: OrganizationInfoCarrierSettings
        """

        self._carrier_settings = carrier_settings

    @property
    def id(self):
        """Gets the id of this OrganizationInfo.  # noqa: E501

        ID of the organization.  # noqa: E501

        :return: The id of this OrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationInfo.

        ID of the organization.  # noqa: E501

        :param id: The id of this OrganizationInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationInfo.  # noqa: E501

        Name of organization.  # noqa: E501

        :return: The name of this OrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationInfo.

        Name of organization.  # noqa: E501

        :param name: The name of this OrganizationInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, OrganizationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationInfo):
            return True

        return self.to_dict() != other.to_dict()
