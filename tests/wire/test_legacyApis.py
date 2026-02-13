from .conftest import get_client, verify_request_count


def test_legacyApis_get_dvir_defects() -> None:
    """Test getDvirDefects endpoint with WireMock"""
    test_id = "legacy_apis.get_dvir_defects.0"
    client = get_client(test_id)
    client.legacy_apis.get_dvir_defects(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/defects/history", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_legacyApis_get_drivers_vehicle_assignments() -> None:
    """Test getDriversVehicleAssignments endpoint with WireMock"""
    test_id = "legacy_apis.get_drivers_vehicle_assignments.0"
    client = get_client(test_id)
    client.legacy_apis.get_drivers_vehicle_assignments()
    verify_request_count(test_id, "GET", "/fleet/drivers/vehicle-assignments", None, 1)


def test_legacyApis_get_dvir_history() -> None:
    """Test getDvirHistory endpoint with WireMock"""
    test_id = "legacy_apis.get_dvir_history.0"
    client = get_client(test_id)
    client.legacy_apis.get_dvir_history(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/dvirs/history", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_legacyApis_get_vehicle_idling_reports() -> None:
    """Test getVehicleIdlingReports endpoint with WireMock"""
    test_id = "legacy_apis.get_vehicle_idling_reports.0"
    client = get_client(test_id)
    client.legacy_apis.get_vehicle_idling_reports(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/reports/vehicle/idling", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_legacyApis_get_safety_events() -> None:
    """Test getSafetyEvents endpoint with WireMock"""
    test_id = "legacy_apis.get_safety_events.0"
    client = get_client(test_id)
    client.legacy_apis.get_safety_events(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/safety-events", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_legacyApis_get_safety_activity_event_feed() -> None:
    """Test getSafetyActivityEventFeed endpoint with WireMock"""
    test_id = "legacy_apis.get_safety_activity_event_feed.0"
    client = get_client(test_id)
    client.legacy_apis.get_safety_activity_event_feed()
    verify_request_count(test_id, "GET", "/fleet/safety-events/audit-logs/feed", None, 1)


def test_legacyApis_get_vehicles_driver_assignments() -> None:
    """Test getVehiclesDriverAssignments endpoint with WireMock"""
    test_id = "legacy_apis.get_vehicles_driver_assignments.0"
    client = get_client(test_id)
    client.legacy_apis.get_vehicles_driver_assignments()
    verify_request_count(test_id, "GET", "/fleet/vehicles/driver-assignments", None, 1)


def test_legacyApis_v_1_get_all_assets() -> None:
    """Test V1getAllAssets endpoint with WireMock"""
    test_id = "legacy_apis.v_1_get_all_assets.0"
    client = get_client(test_id)
    client.legacy_apis.v_1_get_all_assets()
    verify_request_count(test_id, "GET", "/v1/fleet/assets", None, 1)


def test_legacyApis_v_1_get_vehicle_harsh_event() -> None:
    """Test V1getVehicleHarshEvent endpoint with WireMock"""
    test_id = "legacy_apis.v_1_get_vehicle_harsh_event.0"
    client = get_client(test_id)
    client.legacy_apis.v_1_get_vehicle_harsh_event(vehicle_id=1000000, timestamp=1000000)
    verify_request_count(test_id, "GET", "/v1/fleet/vehicles/1000000/safety/harsh_event", {"timestamp": "1000000"}, 1)
