from .conftest import get_client, verify_request_count


def test_safety_get_safety_events_v_2() -> None:
    """Test getSafetyEventsV2 endpoint with WireMock"""
    test_id = "safety.get_safety_events_v_2.0"
    client = get_client(test_id)
    client.safety.get_safety_events_v_2()
    verify_request_count(test_id, "GET", "/safety-events", None, 1)


def test_safety_get_safety_events_v_2_stream() -> None:
    """Test getSafetyEventsV2Stream endpoint with WireMock"""
    test_id = "safety.get_safety_events_v_2_stream.0"
    client = get_client(test_id)
    client.safety.get_safety_events_v_2_stream(start_time="startTime")
    verify_request_count(test_id, "GET", "/safety-events/stream", {"startTime": "startTime"}, 1)


def test_safety_v_1_get_driver_safety_score() -> None:
    """Test V1getDriverSafetyScore endpoint with WireMock"""
    test_id = "safety.v_1_get_driver_safety_score.0"
    client = get_client(test_id)
    client.safety.v_1_get_driver_safety_score(driver_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/drivers/1000000/safety/score", {"startMs": "1000000", "endMs": "1000000"}, 1
    )


def test_safety_v_1_get_vehicle_safety_score() -> None:
    """Test V1getVehicleSafetyScore endpoint with WireMock"""
    test_id = "safety.v_1_get_vehicle_safety_score.0"
    client = get_client(test_id)
    client.safety.v_1_get_vehicle_safety_score(vehicle_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/vehicles/1000000/safety/score", {"startMs": "1000000", "endMs": "1000000"}, 1
    )
