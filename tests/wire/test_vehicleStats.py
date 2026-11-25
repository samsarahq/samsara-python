from .conftest import get_client, verify_request_count


def test_vehicleStats_get_vehicle_stats() -> None:
    """Test getVehicleStats endpoint with WireMock"""
    test_id = "vehicle_stats.get_vehicle_stats.0"
    client = get_client(test_id)
    client.vehicle_stats.get_vehicle_stats(types=["ambientAirTemperatureMilliC"])
    verify_request_count(test_id, "GET", "/fleet/vehicles/stats", {"types": "ambientAirTemperatureMilliC"}, 1)


def test_vehicleStats_get_vehicle_stats_feed() -> None:
    """Test getVehicleStatsFeed endpoint with WireMock"""
    test_id = "vehicle_stats.get_vehicle_stats_feed.0"
    client = get_client(test_id)
    client.vehicle_stats.get_vehicle_stats_feed(types=["ambientAirTemperatureMilliC"])
    verify_request_count(test_id, "GET", "/fleet/vehicles/stats/feed", {"types": "ambientAirTemperatureMilliC"}, 1)


def test_vehicleStats_get_vehicle_stats_history() -> None:
    """Test getVehicleStatsHistory endpoint with WireMock"""
    test_id = "vehicle_stats.get_vehicle_stats_history.0"
    client = get_client(test_id)
    client.vehicle_stats.get_vehicle_stats_history(
        start_time="startTime", end_time="endTime", types=["ambientAirTemperatureMilliC"]
    )
    verify_request_count(
        test_id,
        "GET",
        "/fleet/vehicles/stats/history",
        {"startTime": "startTime", "endTime": "endTime", "types": "ambientAirTemperatureMilliC"},
        1,
    )
