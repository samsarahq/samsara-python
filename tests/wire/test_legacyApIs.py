from .conftest import get_client, verify_request_count


def test_legacyApIs_get_dvir_defects() -> None:
    """Test getDvirDefects endpoint with WireMock"""
    test_id = "legacy_ap_is.get_dvir_defects.0"
    client = get_client(test_id)
    client.legacy_ap_is.get_dvir_defects(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/defects/history", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_legacyApIs_get_drivers_vehicle_assignments() -> None:
    """Test getDriversVehicleAssignments endpoint with WireMock"""
    test_id = "legacy_ap_is.get_drivers_vehicle_assignments.0"
    client = get_client(test_id)
    client.legacy_ap_is.get_drivers_vehicle_assignments()
    verify_request_count(test_id, "GET", "/fleet/drivers/vehicle-assignments", None, 1)


def test_legacyApIs_get_dvir_history() -> None:
    """Test getDvirHistory endpoint with WireMock"""
    test_id = "legacy_ap_is.get_dvir_history.0"
    client = get_client(test_id)
    client.legacy_ap_is.get_dvir_history(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/dvirs/history", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_legacyApIs_get_vehicle_idling_reports() -> None:
    """Test getVehicleIdlingReports endpoint with WireMock"""
    test_id = "legacy_ap_is.get_vehicle_idling_reports.0"
    client = get_client(test_id)
    client.legacy_ap_is.get_vehicle_idling_reports(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/reports/vehicle/idling", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_legacyApIs_get_vehicles_driver_assignments() -> None:
    """Test getVehiclesDriverAssignments endpoint with WireMock"""
    test_id = "legacy_ap_is.get_vehicles_driver_assignments.0"
    client = get_client(test_id)
    client.legacy_ap_is.get_vehicles_driver_assignments()
    verify_request_count(test_id, "GET", "/fleet/vehicles/driver-assignments", None, 1)
