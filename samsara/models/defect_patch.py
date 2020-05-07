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


class DefectPatch(object):
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
        'is_resolved': 'bool',
        'mechanic_notes': 'str',
        'resolved_at_time': 'str',
        'resolved_by': 'ResolvedBy'
    }

    attribute_map = {
        'is_resolved': 'isResolved',
        'mechanic_notes': 'mechanicNotes',
        'resolved_at_time': 'resolvedAtTime',
        'resolved_by': 'resolvedBy'
    }

    def __init__(self, is_resolved=None, mechanic_notes=None, resolved_at_time=None, resolved_by=None, local_vars_configuration=None):  # noqa: E501
        """DefectPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_resolved = None
        self._mechanic_notes = None
        self._resolved_at_time = None
        self._resolved_by = None
        self.discriminator = None

        if is_resolved is not None:
            self.is_resolved = is_resolved
        if mechanic_notes is not None:
            self.mechanic_notes = mechanic_notes
        if resolved_at_time is not None:
            self.resolved_at_time = resolved_at_time
        if resolved_by is not None:
            self.resolved_by = resolved_by

    @property
    def is_resolved(self):
        """Gets the is_resolved of this DefectPatch.  # noqa: E501

        Resolves the defect. Must be `true`.  # noqa: E501

        :return: The is_resolved of this DefectPatch.  # noqa: E501
        :rtype: bool
        """
        return self._is_resolved

    @is_resolved.setter
    def is_resolved(self, is_resolved):
        """Sets the is_resolved of this DefectPatch.

        Resolves the defect. Must be `true`.  # noqa: E501

        :param is_resolved: The is_resolved of this DefectPatch.  # noqa: E501
        :type: bool
        """

        self._is_resolved = is_resolved

    @property
    def mechanic_notes(self):
        """Gets the mechanic_notes of this DefectPatch.  # noqa: E501

        The mechanics notes on the defect.  # noqa: E501

        :return: The mechanic_notes of this DefectPatch.  # noqa: E501
        :rtype: str
        """
        return self._mechanic_notes

    @mechanic_notes.setter
    def mechanic_notes(self, mechanic_notes):
        """Sets the mechanic_notes of this DefectPatch.

        The mechanics notes on the defect.  # noqa: E501

        :param mechanic_notes: The mechanic_notes of this DefectPatch.  # noqa: E501
        :type: str
        """

        self._mechanic_notes = mechanic_notes

    @property
    def resolved_at_time(self):
        """Gets the resolved_at_time of this DefectPatch.  # noqa: E501

        Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :return: The resolved_at_time of this DefectPatch.  # noqa: E501
        :rtype: str
        """
        return self._resolved_at_time

    @resolved_at_time.setter
    def resolved_at_time(self, resolved_at_time):
        """Sets the resolved_at_time of this DefectPatch.

        Time when defect was resolved. Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.  # noqa: E501

        :param resolved_at_time: The resolved_at_time of this DefectPatch.  # noqa: E501
        :type: str
        """

        self._resolved_at_time = resolved_at_time

    @property
    def resolved_by(self):
        """Gets the resolved_by of this DefectPatch.  # noqa: E501


        :return: The resolved_by of this DefectPatch.  # noqa: E501
        :rtype: ResolvedBy
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this DefectPatch.


        :param resolved_by: The resolved_by of this DefectPatch.  # noqa: E501
        :type: ResolvedBy
        """

        self._resolved_by = resolved_by

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
        if not isinstance(other, DefectPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefectPatch):
            return True

        return self.to_dict() != other.to_dict()
