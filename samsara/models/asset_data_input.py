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


class AssetDataInput(object):
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
        'data_group': 'str',
        'id': 'str',
        'last_point': 'AssetDataInputLastPoint',
        'name': 'str',
        'units': 'str'
    }

    attribute_map = {
        'data_group': 'dataGroup',
        'id': 'id',
        'last_point': 'lastPoint',
        'name': 'name',
        'units': 'units'
    }

    def __init__(self, data_group=None, id=None, last_point=None, name=None, units=None, local_vars_configuration=None):  # noqa: E501
        """AssetDataInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_group = None
        self._id = None
        self._last_point = None
        self._name = None
        self._units = None
        self.discriminator = None

        if data_group is not None:
            self.data_group = data_group
        if id is not None:
            self.id = id
        if last_point is not None:
            self.last_point = last_point
        if name is not None:
            self.name = name
        if units is not None:
            self.units = units

    @property
    def data_group(self):
        """Gets the data_group of this AssetDataInput.  # noqa: E501

        Name of the data group that the data input is associated with  # noqa: E501

        :return: The data_group of this AssetDataInput.  # noqa: E501
        :rtype: str
        """
        return self._data_group

    @data_group.setter
    def data_group(self, data_group):
        """Sets the data_group of this AssetDataInput.

        Name of the data group that the data input is associated with  # noqa: E501

        :param data_group: The data_group of this AssetDataInput.  # noqa: E501
        :type: str
        """

        self._data_group = data_group

    @property
    def id(self):
        """Gets the id of this AssetDataInput.  # noqa: E501

        ID of the data input  # noqa: E501

        :return: The id of this AssetDataInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetDataInput.

        ID of the data input  # noqa: E501

        :param id: The id of this AssetDataInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_point(self):
        """Gets the last_point of this AssetDataInput.  # noqa: E501


        :return: The last_point of this AssetDataInput.  # noqa: E501
        :rtype: AssetDataInputLastPoint
        """
        return self._last_point

    @last_point.setter
    def last_point(self, last_point):
        """Sets the last_point of this AssetDataInput.


        :param last_point: The last_point of this AssetDataInput.  # noqa: E501
        :type: AssetDataInputLastPoint
        """

        self._last_point = last_point

    @property
    def name(self):
        """Gets the name of this AssetDataInput.  # noqa: E501

        Name of the data input  # noqa: E501

        :return: The name of this AssetDataInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetDataInput.

        Name of the data input  # noqa: E501

        :param name: The name of this AssetDataInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def units(self):
        """Gets the units of this AssetDataInput.  # noqa: E501

        Units of data for this data input  # noqa: E501

        :return: The units of this AssetDataInput.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this AssetDataInput.

        Units of data for this data input  # noqa: E501

        :param units: The units of this AssetDataInput.  # noqa: E501
        :type: str
        """

        self._units = units

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
        if not isinstance(other, AssetDataInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetDataInput):
            return True

        return self.to_dict() != other.to_dict()
