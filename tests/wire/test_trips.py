from .conftest import get_client, verify_request_count


def test_trips_v_1_get_fleet_trips() -> None:
    """Test V1getFleetTrips endpoint with WireMock"""
    test_id = "trips.v_1_get_fleet_trips.0"
    client = get_client(test_id)
    client.trips.v_1_get_fleet_trips(vehicle_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/trips", {"vehicleId": "1000000", "startMs": "1000000", "endMs": "1000000"}, 1
    )
