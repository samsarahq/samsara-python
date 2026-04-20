from .conftest import get_client, verify_request_count


def test_readings_list_readings_definitions() -> None:
    """Test listReadingsDefinitions endpoint with WireMock"""
    test_id = "readings.list_readings_definitions.0"
    client = get_client(test_id)
    client.readings.list_readings_definitions()
    verify_request_count(test_id, "GET", "/readings/definitions", None, 1)


def test_readings_get_readings_history() -> None:
    """Test getReadingsHistory endpoint with WireMock"""
    test_id = "readings.get_readings_history.0"
    client = get_client(test_id)
    client.readings.get_readings_history(reading_id="readingId", entity_type="entityType")
    verify_request_count(test_id, "GET", "/readings/history", {"readingId": "readingId", "entityType": "entityType"}, 1)


def test_readings_get_readings_snapshot() -> None:
    """Test getReadingsSnapshot endpoint with WireMock"""
    test_id = "readings.get_readings_snapshot.0"
    client = get_client(test_id)
    client.readings.get_readings_snapshot(reading_ids="readingIds", entity_type="entityType")
    verify_request_count(
        test_id, "GET", "/readings/latest", {"readingIds": "readingIds", "entityType": "entityType"}, 1
    )
