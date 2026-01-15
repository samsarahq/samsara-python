from .conftest import get_client, verify_request_count


def test_equipment_list_equipment() -> None:
    """Test listEquipment endpoint with WireMock"""
    test_id = "equipment.list_equipment.0"
    client = get_client(test_id)
    client.equipment.list_equipment()
    verify_request_count(test_id, "GET", "/fleet/equipment", None, 1)


def test_equipment_get_equipment_locations() -> None:
    """Test getEquipmentLocations endpoint with WireMock"""
    test_id = "equipment.get_equipment_locations.0"
    client = get_client(test_id)
    client.equipment.get_equipment_locations()
    verify_request_count(test_id, "GET", "/fleet/equipment/locations", None, 1)


def test_equipment_get_equipment_locations_feed() -> None:
    """Test getEquipmentLocationsFeed endpoint with WireMock"""
    test_id = "equipment.get_equipment_locations_feed.0"
    client = get_client(test_id)
    client.equipment.get_equipment_locations_feed()
    verify_request_count(test_id, "GET", "/fleet/equipment/locations/feed", None, 1)


def test_equipment_get_equipment_locations_history() -> None:
    """Test getEquipmentLocationsHistory endpoint with WireMock"""
    test_id = "equipment.get_equipment_locations_history.0"
    client = get_client(test_id)
    client.equipment.get_equipment_locations_history(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/equipment/locations/history", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_equipment_get_equipment_stats() -> None:
    """Test getEquipmentStats endpoint with WireMock"""
    test_id = "equipment.get_equipment_stats.0"
    client = get_client(test_id)
    client.equipment.get_equipment_stats()
    verify_request_count(test_id, "GET", "/fleet/equipment/stats", None, 1)


def test_equipment_get_equipment_stats_feed() -> None:
    """Test getEquipmentStatsFeed endpoint with WireMock"""
    test_id = "equipment.get_equipment_stats_feed.0"
    client = get_client(test_id)
    client.equipment.get_equipment_stats_feed()
    verify_request_count(test_id, "GET", "/fleet/equipment/stats/feed", None, 1)


def test_equipment_get_equipment_stats_history() -> None:
    """Test getEquipmentStatsHistory endpoint with WireMock"""
    test_id = "equipment.get_equipment_stats_history.0"
    client = get_client(test_id)
    client.equipment.get_equipment_stats_history(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/fleet/equipment/stats/history", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_equipment_get_equipment() -> None:
    """Test getEquipment endpoint with WireMock"""
    test_id = "equipment.get_equipment.0"
    client = get_client(test_id)
    client.equipment.get_equipment(id="id")
    verify_request_count(test_id, "GET", "/fleet/equipment/id", None, 1)
