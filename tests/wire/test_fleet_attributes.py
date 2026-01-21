from .conftest import get_client, verify_request_count


def test_fleet_attributes_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "fleet.attributes.update.0"
    client = get_client(test_id)
    client.fleet.attributes.update(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/attributes/id", None, 1)
