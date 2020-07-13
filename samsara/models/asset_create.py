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


class AssetCreate(object):
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
        'custom_metadata': 'dict(str, str)',
        'location': 'AssetLocation',
        'location_data_input_id': 'str',
        'location_type': 'LocationType',
        'name': 'str',
        'parent_id': 'str',
        'running_status_data_input_id': 'str',
        'tag_ids': 'list[str]'
    }

    attribute_map = {
        'custom_metadata': 'customMetadata',
        'location': 'location',
        'location_data_input_id': 'locationDataInputId',
        'location_type': 'locationType',
        'name': 'name',
        'parent_id': 'parentId',
        'running_status_data_input_id': 'runningStatusDataInputId',
        'tag_ids': 'tagIds'
    }

    def __init__(self, custom_metadata=None, location=None, location_data_input_id=None, location_type=None, name=None, parent_id=None, running_status_data_input_id=None, tag_ids=None, local_vars_configuration=None):  # noqa: E501
        """AssetCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._custom_metadata = None
        self._location = None
        self._location_data_input_id = None
        self._location_type = None
        self._name = None
        self._parent_id = None
        self._running_status_data_input_id = None
        self._tag_ids = None
        self.discriminator = None

        if custom_metadata is not None:
            self.custom_metadata = custom_metadata
        if location is not None:
            self.location = location
        if location_data_input_id is not None:
            self.location_data_input_id = location_data_input_id
        if location_type is not None:
            self.location_type = location_type
        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if running_status_data_input_id is not None:
            self.running_status_data_input_id = running_status_data_input_id
        if tag_ids is not None:
            self.tag_ids = tag_ids

    @property
    def custom_metadata(self):
        """Gets the custom_metadata of this AssetCreate.  # noqa: E501

        The custom fields of an asset.  # noqa: E501

        :return: The custom_metadata of this AssetCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """Sets the custom_metadata of this AssetCreate.

        The custom fields of an asset.  # noqa: E501

        :param custom_metadata: The custom_metadata of this AssetCreate.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_metadata = custom_metadata

    @property
    def location(self):
        """Gets the location of this AssetCreate.  # noqa: E501


        :return: The location of this AssetCreate.  # noqa: E501
        :rtype: AssetLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AssetCreate.


        :param location: The location of this AssetCreate.  # noqa: E501
        :type: AssetLocation
        """

        self._location = location

    @property
    def location_data_input_id(self):
        """Gets the location_data_input_id of this AssetCreate.  # noqa: E501

        Required if locationType is \"dataInput\". Specifies the id of a location data input which will determine the asset's location.  # noqa: E501

        :return: The location_data_input_id of this AssetCreate.  # noqa: E501
        :rtype: str
        """
        return self._location_data_input_id

    @location_data_input_id.setter
    def location_data_input_id(self, location_data_input_id):
        """Sets the location_data_input_id of this AssetCreate.

        Required if locationType is \"dataInput\". Specifies the id of a location data input which will determine the asset's location.  # noqa: E501

        :param location_data_input_id: The location_data_input_id of this AssetCreate.  # noqa: E501
        :type: str
        """

        self._location_data_input_id = location_data_input_id

    @property
    def location_type(self):
        """Gets the location_type of this AssetCreate.  # noqa: E501


        :return: The location_type of this AssetCreate.  # noqa: E501
        :rtype: LocationType
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this AssetCreate.


        :param location_type: The location_type of this AssetCreate.  # noqa: E501
        :type: LocationType
        """

        self._location_type = location_type

    @property
    def name(self):
        """Gets the name of this AssetCreate.  # noqa: E501

        The name of the asset.  # noqa: E501

        :return: The name of this AssetCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetCreate.

        The name of the asset.  # noqa: E501

        :param name: The name of this AssetCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this AssetCreate.  # noqa: E501

        The id of the parent asset that the asset belongs to.  # noqa: E501

        :return: The parent_id of this AssetCreate.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this AssetCreate.

        The id of the parent asset that the asset belongs to.  # noqa: E501

        :param parent_id: The parent_id of this AssetCreate.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def running_status_data_input_id(self):
        """Gets the running_status_data_input_id of this AssetCreate.  # noqa: E501

        The asset's isRunning status will be true when the associated data input's value is 1  # noqa: E501

        :return: The running_status_data_input_id of this AssetCreate.  # noqa: E501
        :rtype: str
        """
        return self._running_status_data_input_id

    @running_status_data_input_id.setter
    def running_status_data_input_id(self, running_status_data_input_id):
        """Sets the running_status_data_input_id of this AssetCreate.

        The asset's isRunning status will be true when the associated data input's value is 1  # noqa: E501

        :param running_status_data_input_id: The running_status_data_input_id of this AssetCreate.  # noqa: E501
        :type: str
        """

        self._running_status_data_input_id = running_status_data_input_id

    @property
    def tag_ids(self):
        """Gets the tag_ids of this AssetCreate.  # noqa: E501

        The ids of the tags that the asset should belong to.  # noqa: E501

        :return: The tag_ids of this AssetCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this AssetCreate.

        The ids of the tags that the asset should belong to.  # noqa: E501

        :param tag_ids: The tag_ids of this AssetCreate.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

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
        if not isinstance(other, AssetCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetCreate):
            return True

        return self.to_dict() != other.to_dict()
