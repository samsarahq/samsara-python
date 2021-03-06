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


class Address(object):
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
        'address_types': 'list[str]',
        'contacts': 'list[ContactTinyResponse]',
        'created_at_time': 'datetime',
        'external_ids': 'object',
        'formatted_address': 'str',
        'geofence': 'AddressGeofence',
        'id': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'name': 'str',
        'notes': 'str',
        'tags': 'list[TagTinyResponse]'
    }

    attribute_map = {
        'address_types': 'addressTypes',
        'contacts': 'contacts',
        'created_at_time': 'createdAtTime',
        'external_ids': 'externalIds',
        'formatted_address': 'formattedAddress',
        'geofence': 'geofence',
        'id': 'id',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'name': 'name',
        'notes': 'notes',
        'tags': 'tags'
    }

    def __init__(self, address_types=None, contacts=None, created_at_time=None, external_ids=None, formatted_address=None, geofence=None, id=None, latitude=None, longitude=None, name=None, notes=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_types = None
        self._contacts = None
        self._created_at_time = None
        self._external_ids = None
        self._formatted_address = None
        self._geofence = None
        self._id = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._notes = None
        self._tags = None
        self.discriminator = None

        if address_types is not None:
            self.address_types = address_types
        if contacts is not None:
            self.contacts = contacts
        if created_at_time is not None:
            self.created_at_time = created_at_time
        if external_ids is not None:
            self.external_ids = external_ids
        self.formatted_address = formatted_address
        self.geofence = geofence
        self.id = id
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        self.name = name
        if notes is not None:
            self.notes = notes
        if tags is not None:
            self.tags = tags

    @property
    def address_types(self):
        """Gets the address_types of this Address.  # noqa: E501

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :return: The address_types of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_types

    @address_types.setter
    def address_types(self, address_types):
        """Sets the address_types of this Address.

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :param address_types: The address_types of this Address.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(address_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `address_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(address_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._address_types = address_types

    @property
    def contacts(self):
        """Gets the contacts of this Address.  # noqa: E501

        An array Contact mini-objects that are associated the Address.  # noqa: E501

        :return: The contacts of this Address.  # noqa: E501
        :rtype: list[ContactTinyResponse]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Address.

        An array Contact mini-objects that are associated the Address.  # noqa: E501

        :param contacts: The contacts of this Address.  # noqa: E501
        :type: list[ContactTinyResponse]
        """

        self._contacts = contacts

    @property
    def created_at_time(self):
        """Gets the created_at_time of this Address.  # noqa: E501

        The date and time this address was created in RFC 3339 format.  # noqa: E501

        :return: The created_at_time of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_time

    @created_at_time.setter
    def created_at_time(self, created_at_time):
        """Sets the created_at_time of this Address.

        The date and time this address was created in RFC 3339 format.  # noqa: E501

        :param created_at_time: The created_at_time of this Address.  # noqa: E501
        :type: datetime
        """

        self._created_at_time = created_at_time

    @property
    def external_ids(self):
        """Gets the external_ids of this Address.  # noqa: E501

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :return: The external_ids of this Address.  # noqa: E501
        :rtype: object
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Address.

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :param external_ids: The external_ids of this Address.  # noqa: E501
        :type: object
        """

        self._external_ids = external_ids

    @property
    def formatted_address(self):
        """Gets the formatted_address of this Address.  # noqa: E501

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :return: The formatted_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this Address.

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :param formatted_address: The formatted_address of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and formatted_address is None:  # noqa: E501
            raise ValueError("Invalid value for `formatted_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                formatted_address is not None and len(formatted_address) > 1024):
            raise ValueError("Invalid value for `formatted_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._formatted_address = formatted_address

    @property
    def geofence(self):
        """Gets the geofence of this Address.  # noqa: E501


        :return: The geofence of this Address.  # noqa: E501
        :rtype: AddressGeofence
        """
        return self._geofence

    @geofence.setter
    def geofence(self, geofence):
        """Sets the geofence of this Address.


        :param geofence: The geofence of this Address.  # noqa: E501
        :type: AddressGeofence
        """
        if self.local_vars_configuration.client_side_validation and geofence is None:  # noqa: E501
            raise ValueError("Invalid value for `geofence`, must not be `None`")  # noqa: E501

        self._geofence = geofence

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        ID of the Address.  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        ID of the Address.  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def latitude(self):
        """Gets the latitude of this Address.  # noqa: E501

        Latitude of the address. Will be geocoded from `formattedAddress` if not provided.  # noqa: E501

        :return: The latitude of this Address.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Address.

        Latitude of the address. Will be geocoded from `formattedAddress` if not provided.  # noqa: E501

        :param latitude: The latitude of this Address.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Address.  # noqa: E501

        Longitude of the address. Will be geocoded from `formattedAddress` if not provided.  # noqa: E501

        :return: The longitude of this Address.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Address.

        Longitude of the address. Will be geocoded from `formattedAddress` if not provided.  # noqa: E501

        :param longitude: The longitude of this Address.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        Name of the address.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        Name of the address.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this Address.  # noqa: E501

        Notes about the address.  # noqa: E501

        :return: The notes of this Address.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Address.

        Notes about the address.  # noqa: E501

        :param notes: The notes of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 280):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `280`")  # noqa: E501

        self._notes = notes

    @property
    def tags(self):
        """Gets the tags of this Address.  # noqa: E501

        An array of all tag mini-objects that are associated with the given address entry.  # noqa: E501

        :return: The tags of this Address.  # noqa: E501
        :rtype: list[TagTinyResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Address.

        An array of all tag mini-objects that are associated with the given address entry.  # noqa: E501

        :param tags: The tags of this Address.  # noqa: E501
        :type: list[TagTinyResponse]
        """

        self._tags = tags

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
