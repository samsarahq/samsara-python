# coding: utf-8

# flake8: noqa

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from samsara.api.samsara_api import SamsaraApi

# import ApiClient
from samsara.api_client import ApiClient
from samsara.configuration import Configuration
from samsara.exceptions import OpenApiException
from samsara.exceptions import ApiTypeError
from samsara.exceptions import ApiValueError
from samsara.exceptions import ApiKeyError
from samsara.exceptions import ApiException
# import models into sdk package
from samsara.models.address import Address
from samsara.models.address_external_ids import AddressExternalIds
from samsara.models.address_geofence import AddressGeofence
from samsara.models.address_geofence_circle import AddressGeofenceCircle
from samsara.models.address_geofence_polygon import AddressGeofencePolygon
from samsara.models.address_geofence_polygon_vertices import AddressGeofencePolygonVertices
from samsara.models.address_response import AddressResponse
from samsara.models.carrier_proposed_assignment import CarrierProposedAssignment
from samsara.models.carrier_proposed_assignment_driver import CarrierProposedAssignmentDriver
from samsara.models.carrier_proposed_assignment_response import CarrierProposedAssignmentResponse
from samsara.models.carrier_proposed_assignment_vehicle import CarrierProposedAssignmentVehicle
from samsara.models.contact import Contact
from samsara.models.contact_response import ContactResponse
from samsara.models.contact_tiny_response import ContactTinyResponse
from samsara.models.create_address_request import CreateAddressRequest
from samsara.models.create_carrier_proposed_assignment_request import CreateCarrierProposedAssignmentRequest
from samsara.models.create_contact_request import CreateContactRequest
from samsara.models.create_driver_request import CreateDriverRequest
from samsara.models.create_dvir_request import CreateDvirRequest
from samsara.models.create_tag_request import CreateTagRequest
from samsara.models.create_user_request import CreateUserRequest
from samsara.models.defect import Defect
from samsara.models.defect_patch import DefectPatch
from samsara.models.defect_resolved_by import DefectResolvedBy
from samsara.models.defect_response import DefectResponse
from samsara.models.defects_response import DefectsResponse
from samsara.models.driver import Driver
from samsara.models.driver_activation_status import DriverActivationStatus
from samsara.models.driver_carrier_settings import DriverCarrierSettings
from samsara.models.driver_external_ids import DriverExternalIds
from samsara.models.driver_locale import DriverLocale
from samsara.models.driver_response import DriverResponse
from samsara.models.driver_static_assigned_vehicle import DriverStaticAssignedVehicle
from samsara.models.driver_tachograph_activity_response import DriverTachographActivityResponse
from samsara.models.driver_tiny_response import DriverTinyResponse
from samsara.models.driver_vehicle_group_tag import DriverVehicleGroupTag
from samsara.models.dvir import Dvir
from samsara.models.dvir_author_signature import DvirAuthorSignature
from samsara.models.dvir_response import DvirResponse
from samsara.models.dvir_second_signature import DvirSecondSignature
from samsara.models.dvir_signature import DvirSignature
from samsara.models.dvir_third_signature import DvirThirdSignature
from samsara.models.dvir_trailer import DvirTrailer
from samsara.models.dvir_trailer_defects_items import DvirTrailerDefectsItems
from samsara.models.dvir_vehicle import DvirVehicle
from samsara.models.dvirs_list_response import DvirsListResponse
from samsara.models.equipment import Equipment
from samsara.models.equipment_engine_rpm import EquipmentEngineRpm
from samsara.models.equipment_engine_seconds import EquipmentEngineSeconds
from samsara.models.equipment_engine_state import EquipmentEngineState
from samsara.models.equipment_fuel_percent import EquipmentFuelPercent
from samsara.models.equipment_gateway_engine_seconds import EquipmentGatewayEngineSeconds
from samsara.models.equipment_gateway_engine_state import EquipmentGatewayEngineState
from samsara.models.equipment_gps_odometer_meters import EquipmentGpsOdometerMeters
from samsara.models.equipment_list_response import EquipmentListResponse
from samsara.models.equipment_location import EquipmentLocation
from samsara.models.equipment_locations_list_response import EquipmentLocationsListResponse
from samsara.models.equipment_locations_list_response_data import EquipmentLocationsListResponseData
from samsara.models.equipment_locations_response import EquipmentLocationsResponse
from samsara.models.equipment_locations_response_data import EquipmentLocationsResponseData
from samsara.models.equipment_obd_engine_seconds import EquipmentObdEngineSeconds
from samsara.models.equipment_obd_engine_state import EquipmentObdEngineState
from samsara.models.equipment_response import EquipmentResponse
from samsara.models.equipment_stats_list_response import EquipmentStatsListResponse
from samsara.models.equipment_stats_list_response_data import EquipmentStatsListResponseData
from samsara.models.equipment_stats_response import EquipmentStatsResponse
from samsara.models.equipment_stats_response_data import EquipmentStatsResponseData
from samsara.models.list_addresses_response import ListAddressesResponse
from samsara.models.list_carrier_proposed_assignment_response import ListCarrierProposedAssignmentResponse
from samsara.models.list_contacts_response import ListContactsResponse
from samsara.models.list_drivers_response import ListDriversResponse
from samsara.models.list_tags_response import ListTagsResponse
from samsara.models.list_user_roles_response import ListUserRolesResponse
from samsara.models.list_users_response import ListUsersResponse
from samsara.models.list_vehicles_response import ListVehiclesResponse
from samsara.models.pagination_response import PaginationResponse
from samsara.models.parent_tag import ParentTag
from samsara.models.patch_tag_request import PatchTagRequest
from samsara.models.replace_tag_request import ReplaceTagRequest
from samsara.models.resolved_by import ResolvedBy
from samsara.models.standard_error_response import StandardErrorResponse
from samsara.models.tachograph_activity import TachographActivity
from samsara.models.tachograph_activity_list_wrapper import TachographActivityListWrapper
from samsara.models.tag import Tag
from samsara.models.tag_all_of import TagAllOf
from samsara.models.tag_response import TagResponse
from samsara.models.tag_tiny_response import TagTinyResponse
from samsara.models.tagged_object import TaggedObject
from samsara.models.tiny_tag import TinyTag
from samsara.models.trailer_name_only_response import TrailerNameOnlyResponse
from samsara.models.trailer_tiny_response import TrailerTinyResponse
from samsara.models.update_address_request import UpdateAddressRequest
from samsara.models.update_contact_request import UpdateContactRequest
from samsara.models.update_driver_request import UpdateDriverRequest
from samsara.models.update_dvir_request import UpdateDvirRequest
from samsara.models.update_user_request import UpdateUserRequest
from samsara.models.update_vehicle_request import UpdateVehicleRequest
from samsara.models.user import User
from samsara.models.user_auth_type import UserAuthType
from samsara.models.user_response import UserResponse
from samsara.models.user_role import UserRole
from samsara.models.user_role_assignment import UserRoleAssignment
from samsara.models.user_role_assignment_request import UserRoleAssignmentRequest
from samsara.models.user_tiny_response import UserTinyResponse
from samsara.models.vehicle import Vehicle
from samsara.models.vehicle_aux_input_type import VehicleAuxInputType
from samsara.models.vehicle_aux_input_type1 import VehicleAuxInputType1
from samsara.models.vehicle_aux_input_type2 import VehicleAuxInputType2
from samsara.models.vehicle_external_ids import VehicleExternalIds
from samsara.models.vehicle_harsh_acceleration_setting_type import VehicleHarshAccelerationSettingType
from samsara.models.vehicle_location import VehicleLocation
from samsara.models.vehicle_location_reverse_geo import VehicleLocationReverseGeo
from samsara.models.vehicle_location_time import VehicleLocationTime
from samsara.models.vehicle_locations_list_response import VehicleLocationsListResponse
from samsara.models.vehicle_locations_list_response_data import VehicleLocationsListResponseData
from samsara.models.vehicle_locations_response import VehicleLocationsResponse
from samsara.models.vehicle_locations_response_data import VehicleLocationsResponseData
from samsara.models.vehicle_response import VehicleResponse
from samsara.models.vehicle_static_assigned_driver import VehicleStaticAssignedDriver
from samsara.models.vehicle_stats_aux_input import VehicleStatsAuxInput
from samsara.models.vehicle_stats_battery_voltage import VehicleStatsBatteryVoltage
from samsara.models.vehicle_stats_engine_state import VehicleStatsEngineState
from samsara.models.vehicle_stats_fuel_percent import VehicleStatsFuelPercent
from samsara.models.vehicle_stats_gps_distance_meters import VehicleStatsGpsDistanceMeters
from samsara.models.vehicle_stats_gps_odometer_meters import VehicleStatsGpsOdometerMeters
from samsara.models.vehicle_stats_list_response import VehicleStatsListResponse
from samsara.models.vehicle_stats_list_response_data import VehicleStatsListResponseData
from samsara.models.vehicle_stats_obd_engine_seconds import VehicleStatsObdEngineSeconds
from samsara.models.vehicle_stats_obd_odometer_meters import VehicleStatsObdOdometerMeters
from samsara.models.vehicle_stats_response import VehicleStatsResponse
from samsara.models.vehicle_stats_response_data import VehicleStatsResponseData
from samsara.models.vehicle_stats_time import VehicleStatsTime
from samsara.models.vehicle_stats_tire_pressure import VehicleStatsTirePressure
from samsara.models.vehicle_stats_tire_pressures import VehicleStatsTirePressures
from samsara.models.vehicle_tiny_response import VehicleTinyResponse

