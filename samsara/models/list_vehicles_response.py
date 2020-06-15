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


class ListVehiclesResponse(object):
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
        'data': 'list[Vehicle]',
        'pagination': 'PaginationResponse'
    }

    attribute_map = {
        'data': 'data',
        'pagination': 'pagination'
    }

    def __init__(self, data=None, pagination=None, local_vars_configuration=None):  # noqa: E501
        """ListVehiclesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._pagination = None
        self.discriminator = None

        self.data = data
        self.pagination = pagination

    @property
    def data(self):
        """Gets the data of this ListVehiclesResponse.  # noqa: E501


        :return: The data of this ListVehiclesResponse.  # noqa: E501
        :rtype: list[Vehicle]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListVehiclesResponse.


        :param data: The data of this ListVehiclesResponse.  # noqa: E501
        :type: list[Vehicle]
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def pagination(self):
        """Gets the pagination of this ListVehiclesResponse.  # noqa: E501


        :return: The pagination of this ListVehiclesResponse.  # noqa: E501
        :rtype: PaginationResponse
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ListVehiclesResponse.


        :param pagination: The pagination of this ListVehiclesResponse.  # noqa: E501
        :type: PaginationResponse
        """
        if self.local_vars_configuration.client_side_validation and pagination is None:  # noqa: E501
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

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
        if not isinstance(other, ListVehiclesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListVehiclesResponse):
            return True

        return self.to_dict() != other.to_dict()
