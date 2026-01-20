from .conftest import get_client, verify_request_count


def test_tachographEuOnly_get_driver_tachograph_activity() -> None:
    """Test getDriverTachographActivity endpoint with WireMock"""
    test_id = "tachograph_eu_only.get_driver_tachograph_activity.0"
    client = get_client(test_id)
    client.tachograph_eu_only.get_driver_tachograph_activity(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id,
        "GET",
        "/fleet/drivers/tachograph-activity/history",
        {"startTime": "startTime", "endTime": "endTime"},
        1,
    )


def test_tachographEuOnly_get_driver_tachograph_files() -> None:
    """Test getDriverTachographFiles endpoint with WireMock"""
    test_id = "tachograph_eu_only.get_driver_tachograph_files.0"
    client = get_client(test_id)
    client.tachograph_eu_only.get_driver_tachograph_files(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/drivers/tachograph-files/history", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_tachographEuOnly_get_vehicle_tachograph_files() -> None:
    """Test getVehicleTachographFiles endpoint with WireMock"""
    test_id = "tachograph_eu_only.get_vehicle_tachograph_files.0"
    client = get_client(test_id)
    client.tachograph_eu_only.get_vehicle_tachograph_files(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/vehicles/tachograph-files/history", {"startTime": "startTime", "endTime": "endTime"}, 1
    )
