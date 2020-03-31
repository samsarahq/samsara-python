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


class UpdateVehicleRequest(object):
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
        'aux_input_type1': 'VehicleAuxInputType',
        'aux_input_type2': 'VehicleAuxInputType',
        'engine_hours': 'int',
        'external_ids': 'dict(str, str)',
        'harsh_acceleration_setting_type': 'VehicleHarshAccelerationSettingType',
        'license_plate': 'str',
        'name': 'str',
        'notes': 'str',
        'odometer_meters': 'int',
        'static_assigned_driver_id': 'str',
        'tag_ids': 'list[str]',
        'vin': 'str'
    }

    attribute_map = {
        'aux_input_type1': 'auxInputType1',
        'aux_input_type2': 'auxInputType2',
        'engine_hours': 'engineHours',
        'external_ids': 'externalIds',
        'harsh_acceleration_setting_type': 'harshAccelerationSettingType',
        'license_plate': 'licensePlate',
        'name': 'name',
        'notes': 'notes',
        'odometer_meters': 'odometerMeters',
        'static_assigned_driver_id': 'staticAssignedDriverId',
        'tag_ids': 'tagIds',
        'vin': 'vin'
    }

    def __init__(self, aux_input_type1=None, aux_input_type2=None, engine_hours=None, external_ids=None, harsh_acceleration_setting_type=None, license_plate=None, name=None, notes='', odometer_meters=None, static_assigned_driver_id=None, tag_ids=None, vin=None, local_vars_configuration=None):  # noqa: E501
        """UpdateVehicleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aux_input_type1 = None
        self._aux_input_type2 = None
        self._engine_hours = None
        self._external_ids = None
        self._harsh_acceleration_setting_type = None
        self._license_plate = None
        self._name = None
        self._notes = None
        self._odometer_meters = None
        self._static_assigned_driver_id = None
        self._tag_ids = None
        self._vin = None
        self.discriminator = None

        if aux_input_type1 is not None:
            self.aux_input_type1 = aux_input_type1
        if aux_input_type2 is not None:
            self.aux_input_type2 = aux_input_type2
        if engine_hours is not None:
            self.engine_hours = engine_hours
        if external_ids is not None:
            self.external_ids = external_ids
        if harsh_acceleration_setting_type is not None:
            self.harsh_acceleration_setting_type = harsh_acceleration_setting_type
        if license_plate is not None:
            self.license_plate = license_plate
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if odometer_meters is not None:
            self.odometer_meters = odometer_meters
        if static_assigned_driver_id is not None:
            self.static_assigned_driver_id = static_assigned_driver_id
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if vin is not None:
            self.vin = vin

    @property
    def aux_input_type1(self):
        """Gets the aux_input_type1 of this UpdateVehicleRequest.  # noqa: E501


        :return: The aux_input_type1 of this UpdateVehicleRequest.  # noqa: E501
        :rtype: VehicleAuxInputType
        """
        return self._aux_input_type1

    @aux_input_type1.setter
    def aux_input_type1(self, aux_input_type1):
        """Sets the aux_input_type1 of this UpdateVehicleRequest.


        :param aux_input_type1: The aux_input_type1 of this UpdateVehicleRequest.  # noqa: E501
        :type: VehicleAuxInputType
        """

        self._aux_input_type1 = aux_input_type1

    @property
    def aux_input_type2(self):
        """Gets the aux_input_type2 of this UpdateVehicleRequest.  # noqa: E501


        :return: The aux_input_type2 of this UpdateVehicleRequest.  # noqa: E501
        :rtype: VehicleAuxInputType
        """
        return self._aux_input_type2

    @aux_input_type2.setter
    def aux_input_type2(self, aux_input_type2):
        """Sets the aux_input_type2 of this UpdateVehicleRequest.


        :param aux_input_type2: The aux_input_type2 of this UpdateVehicleRequest.  # noqa: E501
        :type: VehicleAuxInputType
        """

        self._aux_input_type2 = aux_input_type2

    @property
    def engine_hours(self):
        """Gets the engine_hours of this UpdateVehicleRequest.  # noqa: E501

        A manual override for the vehicle's engine hours. You may only override a vehicle's engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle's engine hours based on when the Samsara Vehicle Gateway is recieving power or not.  # noqa: E501

        :return: The engine_hours of this UpdateVehicleRequest.  # noqa: E501
        :rtype: int
        """
        return self._engine_hours

    @engine_hours.setter
    def engine_hours(self, engine_hours):
        """Sets the engine_hours of this UpdateVehicleRequest.

        A manual override for the vehicle's engine hours. You may only override a vehicle's engine hours if it cannot be read from on-board diagnostics. When you provide a manual engine hours override, Samsara will begin updating a vehicle's engine hours based on when the Samsara Vehicle Gateway is recieving power or not.  # noqa: E501

        :param engine_hours: The engine_hours of this UpdateVehicleRequest.  # noqa: E501
        :type: int
        """

        self._engine_hours = engine_hours

    @property
    def external_ids(self):
        """Gets the external_ids of this UpdateVehicleRequest.  # noqa: E501

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :return: The external_ids of this UpdateVehicleRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this UpdateVehicleRequest.

        The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.  # noqa: E501

        :param external_ids: The external_ids of this UpdateVehicleRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def harsh_acceleration_setting_type(self):
        """Gets the harsh_acceleration_setting_type of this UpdateVehicleRequest.  # noqa: E501


        :return: The harsh_acceleration_setting_type of this UpdateVehicleRequest.  # noqa: E501
        :rtype: VehicleHarshAccelerationSettingType
        """
        return self._harsh_acceleration_setting_type

    @harsh_acceleration_setting_type.setter
    def harsh_acceleration_setting_type(self, harsh_acceleration_setting_type):
        """Sets the harsh_acceleration_setting_type of this UpdateVehicleRequest.


        :param harsh_acceleration_setting_type: The harsh_acceleration_setting_type of this UpdateVehicleRequest.  # noqa: E501
        :type: VehicleHarshAccelerationSettingType
        """

        self._harsh_acceleration_setting_type = harsh_acceleration_setting_type

    @property
    def license_plate(self):
        """Gets the license_plate of this UpdateVehicleRequest.  # noqa: E501

        The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The license_plate of this UpdateVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, license_plate):
        """Sets the license_plate of this UpdateVehicleRequest.

        The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param license_plate: The license_plate of this UpdateVehicleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                license_plate is not None and len(license_plate) > 12):
            raise ValueError("Invalid value for `license_plate`, length must be less than or equal to `12`")  # noqa: E501

        self._license_plate = license_plate

    @property
    def name(self):
        """Gets the name of this UpdateVehicleRequest.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this UpdateVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVehicleRequest.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this UpdateVehicleRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this UpdateVehicleRequest.  # noqa: E501

        These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The notes of this UpdateVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UpdateVehicleRequest.

        These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param notes: The notes of this UpdateVehicleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 255):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `255`")  # noqa: E501

        self._notes = notes

    @property
    def odometer_meters(self):
        """Gets the odometer_meters of this UpdateVehicleRequest.  # noqa: E501

        A manual override for the vehicle's odometer. You may only override a vehicle's odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle's odometer using GPS distance traveled since this override was set. See [here](https://kb.samsara.com/hc/en-us/articles/115005273667) for more details.  # noqa: E501

        :return: The odometer_meters of this UpdateVehicleRequest.  # noqa: E501
        :rtype: int
        """
        return self._odometer_meters

    @odometer_meters.setter
    def odometer_meters(self, odometer_meters):
        """Sets the odometer_meters of this UpdateVehicleRequest.

        A manual override for the vehicle's odometer. You may only override a vehicle's odometer if it cannot be read from on-board diagnostics. When you provide a manual odometer override, Samsara will begin updating a vehicle's odometer using GPS distance traveled since this override was set. See [here](https://kb.samsara.com/hc/en-us/articles/115005273667) for more details.  # noqa: E501

        :param odometer_meters: The odometer_meters of this UpdateVehicleRequest.  # noqa: E501
        :type: int
        """

        self._odometer_meters = odometer_meters

    @property
    def static_assigned_driver_id(self):
        """Gets the static_assigned_driver_id of this UpdateVehicleRequest.  # noqa: E501

        ID for the static assigned driver of the vehicle.  # noqa: E501

        :return: The static_assigned_driver_id of this UpdateVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._static_assigned_driver_id

    @static_assigned_driver_id.setter
    def static_assigned_driver_id(self, static_assigned_driver_id):
        """Sets the static_assigned_driver_id of this UpdateVehicleRequest.

        ID for the static assigned driver of the vehicle.  # noqa: E501

        :param static_assigned_driver_id: The static_assigned_driver_id of this UpdateVehicleRequest.  # noqa: E501
        :type: str
        """

        self._static_assigned_driver_id = static_assigned_driver_id

    @property
    def tag_ids(self):
        """Gets the tag_ids of this UpdateVehicleRequest.  # noqa: E501

        An array of IDs of tags to associate with this vehicle.  # noqa: E501

        :return: The tag_ids of this UpdateVehicleRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this UpdateVehicleRequest.

        An array of IDs of tags to associate with this vehicle.  # noqa: E501

        :param tag_ids: The tag_ids of this UpdateVehicleRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

    @property
    def vin(self):
        """Gets the vin of this UpdateVehicleRequest.  # noqa: E501

        The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :return: The vin of this UpdateVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this UpdateVehicleRequest.

        The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.  # noqa: E501

        :param vin: The vin of this UpdateVehicleRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                vin is not None and len(vin) > 17):
            raise ValueError("Invalid value for `vin`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vin is not None and len(vin) < 11):
            raise ValueError("Invalid value for `vin`, length must be greater than or equal to `11`")  # noqa: E501

        self._vin = vin

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
        if not isinstance(other, UpdateVehicleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateVehicleRequest):
            return True

        return self.to_dict() != other.to_dict()
