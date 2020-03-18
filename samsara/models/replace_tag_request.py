# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class ReplaceTagRequest(object):
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
        'addresses': 'list[str]',
        'assets': 'list[str]',
        'drivers': 'list[str]',
        'machines': 'list[str]',
        'name': 'str',
        'parent_tag_id': 'str',
        'sensors': 'list[str]',
        'vehicles': 'list[str]'
    }

    attribute_map = {
        'addresses': 'addresses',
        'assets': 'assets',
        'drivers': 'drivers',
        'machines': 'machines',
        'name': 'name',
        'parent_tag_id': 'parentTagId',
        'sensors': 'sensors',
        'vehicles': 'vehicles'
    }

    def __init__(self, addresses=None, assets=None, drivers=None, machines=None, name=None, parent_tag_id=None, sensors=None, vehicles=None, local_vars_configuration=None):  # noqa: E501
        """ReplaceTagRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._assets = None
        self._drivers = None
        self._machines = None
        self._name = None
        self._parent_tag_id = None
        self._sensors = None
        self._vehicles = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if assets is not None:
            self.assets = assets
        if drivers is not None:
            self.drivers = drivers
        if machines is not None:
            self.machines = machines
        if name is not None:
            self.name = name
        if parent_tag_id is not None:
            self.parent_tag_id = parent_tag_id
        if sensors is not None:
            self.sensors = sensors
        if vehicles is not None:
            self.vehicles = vehicles

    @property
    def addresses(self):
        """Gets the addresses of this ReplaceTagRequest.  # noqa: E501

        The addresses that belong to this tag.  # noqa: E501

        :return: The addresses of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ReplaceTagRequest.

        The addresses that belong to this tag.  # noqa: E501

        :param addresses: The addresses of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def assets(self):
        """Gets the assets of this ReplaceTagRequest.  # noqa: E501

        The trailers, unpowered, and powered assets that belong to this tag.  # noqa: E501

        :return: The assets of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ReplaceTagRequest.

        The trailers, unpowered, and powered assets that belong to this tag.  # noqa: E501

        :param assets: The assets of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._assets = assets

    @property
    def drivers(self):
        """Gets the drivers of this ReplaceTagRequest.  # noqa: E501

        The drivers that belong to this tag.  # noqa: E501

        :return: The drivers of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this ReplaceTagRequest.

        The drivers that belong to this tag.  # noqa: E501

        :param drivers: The drivers of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._drivers = drivers

    @property
    def machines(self):
        """Gets the machines of this ReplaceTagRequest.  # noqa: E501

        The machines that belong to this tag.  # noqa: E501

        :return: The machines of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._machines

    @machines.setter
    def machines(self, machines):
        """Sets the machines of this ReplaceTagRequest.

        The machines that belong to this tag.  # noqa: E501

        :param machines: The machines of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._machines = machines

    @property
    def name(self):
        """Gets the name of this ReplaceTagRequest.  # noqa: E501

        Name of this tag.  # noqa: E501

        :return: The name of this ReplaceTagRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReplaceTagRequest.

        Name of this tag.  # noqa: E501

        :param name: The name of this ReplaceTagRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 191):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `191`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def parent_tag_id(self):
        """Gets the parent_tag_id of this ReplaceTagRequest.  # noqa: E501

        If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.  # noqa: E501

        :return: The parent_tag_id of this ReplaceTagRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_tag_id

    @parent_tag_id.setter
    def parent_tag_id(self, parent_tag_id):
        """Sets the parent_tag_id of this ReplaceTagRequest.

        If this tag is part a hierarchical tag tree, this is the ID of the parent tag, otherwise this will be omitted.  # noqa: E501

        :param parent_tag_id: The parent_tag_id of this ReplaceTagRequest.  # noqa: E501
        :type: str
        """

        self._parent_tag_id = parent_tag_id

    @property
    def sensors(self):
        """Gets the sensors of this ReplaceTagRequest.  # noqa: E501

        The sensors that belong to this tag.  # noqa: E501

        :return: The sensors of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this ReplaceTagRequest.

        The sensors that belong to this tag.  # noqa: E501

        :param sensors: The sensors of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

    @property
    def vehicles(self):
        """Gets the vehicles of this ReplaceTagRequest.  # noqa: E501

        The vehicles that belong to this tag.  # noqa: E501

        :return: The vehicles of this ReplaceTagRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles):
        """Sets the vehicles of this ReplaceTagRequest.

        The vehicles that belong to this tag.  # noqa: E501

        :param vehicles: The vehicles of this ReplaceTagRequest.  # noqa: E501
        :type: list[str]
        """

        self._vehicles = vehicles

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
        if not isinstance(other, ReplaceTagRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplaceTagRequest):
            return True

        return self.to_dict() != other.to_dict()
