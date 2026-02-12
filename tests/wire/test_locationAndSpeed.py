from .conftest import get_client, verify_request_count


def test_locationAndSpeed_get_location_and_speed() -> None:
    """Test getLocationAndSpeed endpoint with WireMock"""
    test_id = "location_and_speed.get_location_and_speed.0"
    client = get_client(test_id)
    client.location_and_speed.get_location_and_speed()
    verify_request_count(test_id, "GET", "/assets/location-and-speed/stream", None, 1)
