from .conftest import get_client, verify_request_count


def test_driverVehicleAssignments_get_driver_vehicle_assignments() -> None:
    """Test getDriverVehicleAssignments endpoint with WireMock"""
    test_id = "driver_vehicle_assignments.get_driver_vehicle_assignments.0"
    client = get_client(test_id)
    client.driver_vehicle_assignments.get_driver_vehicle_assignments(filter_by="drivers")
    verify_request_count(test_id, "GET", "/fleet/driver-vehicle-assignments", {"filterBy": "drivers"}, 1)


def test_driverVehicleAssignments_create_driver_vehicle_assignment() -> None:
    """Test createDriverVehicleAssignment endpoint with WireMock"""
    test_id = "driver_vehicle_assignments.create_driver_vehicle_assignment.0"
    client = get_client(test_id)
    client.driver_vehicle_assignments.create_driver_vehicle_assignment(driver_id="494123", vehicle_id="281474978683353")
    verify_request_count(test_id, "POST", "/fleet/driver-vehicle-assignments", None, 1)


def test_driverVehicleAssignments_delete_driver_vehicle_assignments() -> None:
    """Test deleteDriverVehicleAssignments endpoint with WireMock"""
    test_id = "driver_vehicle_assignments.delete_driver_vehicle_assignments.0"
    client = get_client(test_id)
    client.driver_vehicle_assignments.delete_driver_vehicle_assignments(vehicle_id="281474978683353")
    verify_request_count(test_id, "DELETE", "/fleet/driver-vehicle-assignments", None, 1)


def test_driverVehicleAssignments_update_driver_vehicle_assignment() -> None:
    """Test updateDriverVehicleAssignment endpoint with WireMock"""
    test_id = "driver_vehicle_assignments.update_driver_vehicle_assignment.0"
    client = get_client(test_id)
    client.driver_vehicle_assignments.update_driver_vehicle_assignment(
        driver_id="494123", start_time="2019-06-13T19:08:25Z", vehicle_id="281474978683353"
    )
    verify_request_count(test_id, "PATCH", "/fleet/driver-vehicle-assignments", None, 1)
