from .conftest import get_client, verify_request_count


def test_fleet_get_fleet_locations() -> None:
    """Test getFleetLocations endpoint with WireMock"""
    test_id = "fleet.get_fleet_locations.0"
    client = get_client(test_id)
    client.fleet.get_fleet_locations()
    verify_request_count(test_id, "GET", "/v1/fleet/locations", None, 1)
