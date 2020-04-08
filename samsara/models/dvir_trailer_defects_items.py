# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class DvirTrailerDefectsItems(object):
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
        'comment': 'str',
        'created_at_time': 'str',
        'defect_type': 'str',
        'id': 'str',
        'is_resolved': 'bool',
        'resolved_at_time': 'str',
        'resolved_by': 'DefectResolvedBy',
        'trailer': 'object',
        'vehicle': 'object'
    }

    attribute_map = {
        'comment': 'comment',
        'created_at_time': 'createdAtTime',
        'defect_type': 'defectType',
        'id': 'id',
        'is_resolved': 'isResolved',
        'resolved_at_time': 'resolvedAtTime',
        'resolved_by': 'resolvedBy',
        'trailer': 'trailer',
        'vehicle': 'vehicle'
    }

    def __init__(self, comment=None, created_at_time=None, defect_type=None, id=None, is_resolved=None, resolved_at_time=None, resolved_by=None, trailer=None, vehicle=None, local_vars_configuration=None):  # noqa: E501
        """DvirTrailerDefectsItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._created_at_time = None
        self._defect_type = None
        self._id = None
        self._is_resolved = None
        self._resolved_at_time = None
        self._resolved_by = None
        self._trailer = None
        self._vehicle = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if created_at_time is not None:
            self.created_at_time = created_at_time
        if defect_type is not None:
            self.defect_type = defect_type
        self.id = id
        self.is_resolved = is_resolved
        if resolved_at_time is not None:
            self.resolved_at_time = resolved_at_time
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if trailer is not None:
            self.trailer = trailer
        if vehicle is not None:
            self.vehicle = vehicle

    @property
    def comment(self):
        """Gets the comment of this DvirTrailerDefectsItems.  # noqa: E501

        Comment on the defect.  # noqa: E501

        :return: The comment of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DvirTrailerDefectsItems.

        Comment on the defect.  # noqa: E501

        :param comment: The comment of this DvirTrailerDefectsItems.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_at_time(self):
        """Gets the created_at_time of this DvirTrailerDefectsItems.  # noqa: E501

        Time when the defect was created. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The created_at_time of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: str
        """
        return self._created_at_time

    @created_at_time.setter
    def created_at_time(self, created_at_time):
        """Sets the created_at_time of this DvirTrailerDefectsItems.

        Time when the defect was created. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param created_at_time: The created_at_time of this DvirTrailerDefectsItems.  # noqa: E501
        :type: str
        """

        self._created_at_time = created_at_time

    @property
    def defect_type(self):
        """Gets the defect_type of this DvirTrailerDefectsItems.  # noqa: E501

        The type of DVIR defect.  # noqa: E501

        :return: The defect_type of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: str
        """
        return self._defect_type

    @defect_type.setter
    def defect_type(self, defect_type):
        """Sets the defect_type of this DvirTrailerDefectsItems.

        The type of DVIR defect.  # noqa: E501

        :param defect_type: The defect_type of this DvirTrailerDefectsItems.  # noqa: E501
        :type: str
        """

        self._defect_type = defect_type

    @property
    def id(self):
        """Gets the id of this DvirTrailerDefectsItems.  # noqa: E501

        ID of the defect.  # noqa: E501

        :return: The id of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DvirTrailerDefectsItems.

        ID of the defect.  # noqa: E501

        :param id: The id of this DvirTrailerDefectsItems.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_resolved(self):
        """Gets the is_resolved of this DvirTrailerDefectsItems.  # noqa: E501

        Signifies if this defect is resolved.  # noqa: E501

        :return: The is_resolved of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: bool
        """
        return self._is_resolved

    @is_resolved.setter
    def is_resolved(self, is_resolved):
        """Sets the is_resolved of this DvirTrailerDefectsItems.

        Signifies if this defect is resolved.  # noqa: E501

        :param is_resolved: The is_resolved of this DvirTrailerDefectsItems.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_resolved is None:  # noqa: E501
            raise ValueError("Invalid value for `is_resolved`, must not be `None`")  # noqa: E501

        self._is_resolved = is_resolved

    @property
    def resolved_at_time(self):
        """Gets the resolved_at_time of this DvirTrailerDefectsItems.  # noqa: E501

        Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The resolved_at_time of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: str
        """
        return self._resolved_at_time

    @resolved_at_time.setter
    def resolved_at_time(self, resolved_at_time):
        """Sets the resolved_at_time of this DvirTrailerDefectsItems.

        Time when this defect was resolved. Will not be returned if the defect is unresolved. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param resolved_at_time: The resolved_at_time of this DvirTrailerDefectsItems.  # noqa: E501
        :type: str
        """

        self._resolved_at_time = resolved_at_time

    @property
    def resolved_by(self):
        """Gets the resolved_by of this DvirTrailerDefectsItems.  # noqa: E501


        :return: The resolved_by of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: DefectResolvedBy
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this DvirTrailerDefectsItems.


        :param resolved_by: The resolved_by of this DvirTrailerDefectsItems.  # noqa: E501
        :type: DefectResolvedBy
        """

        self._resolved_by = resolved_by

    @property
    def trailer(self):
        """Gets the trailer of this DvirTrailerDefectsItems.  # noqa: E501


        :return: The trailer of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: object
        """
        return self._trailer

    @trailer.setter
    def trailer(self, trailer):
        """Sets the trailer of this DvirTrailerDefectsItems.


        :param trailer: The trailer of this DvirTrailerDefectsItems.  # noqa: E501
        :type: object
        """

        self._trailer = trailer

    @property
    def vehicle(self):
        """Gets the vehicle of this DvirTrailerDefectsItems.  # noqa: E501


        :return: The vehicle of this DvirTrailerDefectsItems.  # noqa: E501
        :rtype: object
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this DvirTrailerDefectsItems.


        :param vehicle: The vehicle of this DvirTrailerDefectsItems.  # noqa: E501
        :type: object
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
        if not isinstance(other, DvirTrailerDefectsItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DvirTrailerDefectsItems):
            return True

        return self.to_dict() != other.to_dict()
