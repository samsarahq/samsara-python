from .conftest import get_client, verify_request_count


def test_safety_get_safety_events() -> None:
    """Test getSafetyEvents endpoint with WireMock"""
    test_id = "safety.get_safety_events.0"
    client = get_client(test_id)
    client.safety.get_safety_events(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/safety-events", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_safety_get_safety_activity_event_feed() -> None:
    """Test getSafetyActivityEventFeed endpoint with WireMock"""
    test_id = "safety.get_safety_activity_event_feed.0"
    client = get_client(test_id)
    client.safety.get_safety_activity_event_feed()
    verify_request_count(test_id, "GET", "/fleet/safety-events/audit-logs/feed", None, 1)


def test_safety_v_1_get_driver_safety_score() -> None:
    """Test V1getDriverSafetyScore endpoint with WireMock"""
    test_id = "safety.v_1_get_driver_safety_score.0"
    client = get_client(test_id)
    client.safety.v_1_get_driver_safety_score(driver_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/drivers/1000000/safety/score", {"startMs": "1000000", "endMs": "1000000"}, 1
    )


def test_safety_v_1_get_vehicle_harsh_event() -> None:
    """Test V1getVehicleHarshEvent endpoint with WireMock"""
    test_id = "safety.v_1_get_vehicle_harsh_event.0"
    client = get_client(test_id)
    client.safety.v_1_get_vehicle_harsh_event(vehicle_id=1000000, timestamp=1000000)
    verify_request_count(test_id, "GET", "/v1/fleet/vehicles/1000000/safety/harsh_event", {"timestamp": "1000000"}, 1)


def test_safety_v_1_get_vehicle_safety_score() -> None:
    """Test V1getVehicleSafetyScore endpoint with WireMock"""
    test_id = "safety.v_1_get_vehicle_safety_score.0"
    client = get_client(test_id)
    client.safety.v_1_get_vehicle_safety_score(vehicle_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/vehicles/1000000/safety/score", {"startMs": "1000000", "endMs": "1000000"}, 1
    )
