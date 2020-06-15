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


class TachographDriverFile(object):
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
        'card_number': 'str',
        'created_at_time': 'str',
        'id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'card_number': 'cardNumber',
        'created_at_time': 'createdAtTime',
        'id': 'id',
        'url': 'url'
    }

    def __init__(self, card_number=None, created_at_time=None, id=None, url=None, local_vars_configuration=None):  # noqa: E501
        """TachographDriverFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._card_number = None
        self._created_at_time = None
        self._id = None
        self._url = None
        self.discriminator = None

        if card_number is not None:
            self.card_number = card_number
        if created_at_time is not None:
            self.created_at_time = created_at_time
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url

    @property
    def card_number(self):
        """Gets the card_number of this TachographDriverFile.  # noqa: E501

        Tachograph card number associated with the file.  # noqa: E501

        :return: The card_number of this TachographDriverFile.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this TachographDriverFile.

        Tachograph card number associated with the file.  # noqa: E501

        :param card_number: The card_number of this TachographDriverFile.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def created_at_time(self):
        """Gets the created_at_time of this TachographDriverFile.  # noqa: E501

        Creation time of files in RFC 3339 format. This is either the download time from the tachograph itself (for files downloaded via Samsara VG) or upload time (for files manually uploaded via Samsara UI).  # noqa: E501

        :return: The created_at_time of this TachographDriverFile.  # noqa: E501
        :rtype: str
        """
        return self._created_at_time

    @created_at_time.setter
    def created_at_time(self, created_at_time):
        """Sets the created_at_time of this TachographDriverFile.

        Creation time of files in RFC 3339 format. This is either the download time from the tachograph itself (for files downloaded via Samsara VG) or upload time (for files manually uploaded via Samsara UI).  # noqa: E501

        :param created_at_time: The created_at_time of this TachographDriverFile.  # noqa: E501
        :type: str
        """

        self._created_at_time = created_at_time

    @property
    def id(self):
        """Gets the id of this TachographDriverFile.  # noqa: E501

        ID of the file.  # noqa: E501

        :return: The id of this TachographDriverFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TachographDriverFile.

        ID of the file.  # noqa: E501

        :param id: The id of this TachographDriverFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this TachographDriverFile.  # noqa: E501

        A temporary URL which can be used to download the file. The link can be used multiple times and expires after an hour.  # noqa: E501

        :return: The url of this TachographDriverFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TachographDriverFile.

        A temporary URL which can be used to download the file. The link can be used multiple times and expires after an hour.  # noqa: E501

        :param url: The url of this TachographDriverFile.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, TachographDriverFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TachographDriverFile):
            return True

        return self.to_dict() != other.to_dict()
