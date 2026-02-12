from .conftest import get_client, verify_request_count


def test_vehicleLocations_get_vehicle_locations() -> None:
    """Test getVehicleLocations endpoint with WireMock"""
    test_id = "vehicle_locations.get_vehicle_locations.0"
    client = get_client(test_id)
    client.vehicle_locations.get_vehicle_locations()
    verify_request_count(test_id, "GET", "/fleet/vehicles/locations", None, 1)


def test_vehicleLocations_get_vehicle_locations_feed() -> None:
    """Test getVehicleLocationsFeed endpoint with WireMock"""
    test_id = "vehicle_locations.get_vehicle_locations_feed.0"
    client = get_client(test_id)
    client.vehicle_locations.get_vehicle_locations_feed()
    verify_request_count(test_id, "GET", "/fleet/vehicles/locations/feed", None, 1)


def test_vehicleLocations_get_vehicle_locations_history() -> None:
    """Test getVehicleLocationsHistory endpoint with WireMock"""
    test_id = "vehicle_locations.get_vehicle_locations_history.0"
    client = get_client(test_id)
    client.vehicle_locations.get_vehicle_locations_history(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/vehicles/locations/history", {"startTime": "startTime", "endTime": "endTime"}, 1
    )
