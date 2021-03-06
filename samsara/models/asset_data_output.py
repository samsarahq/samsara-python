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


class AssetDataOutput(object):
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
        'data_input': 'AssetDataInput',
        'device_id': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'data_group': 'dataGroup',
        'data_input': 'dataInput',
        'device_id': 'deviceId',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, data_group=None, data_input=None, device_id=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """AssetDataOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_group = None
        self._data_input = None
        self._device_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        if data_group is not None:
            self.data_group = data_group
        if data_input is not None:
            self.data_input = data_input
        if device_id is not None:
            self.device_id = device_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def data_group(self):
        """Gets the data_group of this AssetDataOutput.  # noqa: E501

        Name of the data group that the data output is associated with  # noqa: E501

        :return: The data_group of this AssetDataOutput.  # noqa: E501
        :rtype: str
        """
        return self._data_group

    @data_group.setter
    def data_group(self, data_group):
        """Sets the data_group of this AssetDataOutput.

        Name of the data group that the data output is associated with  # noqa: E501

        :param data_group: The data_group of this AssetDataOutput.  # noqa: E501
        :type: str
        """

        self._data_group = data_group

    @property
    def data_input(self):
        """Gets the data_input of this AssetDataOutput.  # noqa: E501


        :return: The data_input of this AssetDataOutput.  # noqa: E501
        :rtype: AssetDataInput
        """
        return self._data_input

    @data_input.setter
    def data_input(self, data_input):
        """Sets the data_input of this AssetDataOutput.


        :param data_input: The data_input of this AssetDataOutput.  # noqa: E501
        :type: AssetDataInput
        """

        self._data_input = data_input

    @property
    def device_id(self):
        """Gets the device_id of this AssetDataOutput.  # noqa: E501

        ID of the device that the data output is configured on  # noqa: E501

        :return: The device_id of this AssetDataOutput.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AssetDataOutput.

        ID of the device that the data output is configured on  # noqa: E501

        :param device_id: The device_id of this AssetDataOutput.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def id(self):
        """Gets the id of this AssetDataOutput.  # noqa: E501

        ID of the data output  # noqa: E501

        :return: The id of this AssetDataOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetDataOutput.

        ID of the data output  # noqa: E501

        :param id: The id of this AssetDataOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetDataOutput.  # noqa: E501

        Name of the data output  # noqa: E501

        :return: The name of this AssetDataOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetDataOutput.

        Name of the data output  # noqa: E501

        :param name: The name of this AssetDataOutput.  # noqa: E501
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
        if not isinstance(other, AssetDataOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetDataOutput):
            return True

        return self.to_dict() != other.to_dict()
