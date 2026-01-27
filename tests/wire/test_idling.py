from .conftest import get_client, verify_request_count


def test_idling_get_idling_events() -> None:
    """Test getIdlingEvents endpoint with WireMock"""
    test_id = "idling.get_idling_events.0"
    client = get_client(test_id)
    client.idling.get_idling_events(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/idling/events", {"startTime": "startTime", "endTime": "endTime"}, 1)
