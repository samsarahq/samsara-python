from .conftest import get_client, verify_request_count


def test_vehicles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "vehicles.list_.0"
    client = get_client(test_id)
    client.vehicles.list()
    verify_request_count(test_id, "GET", "/fleet/vehicles", None, 1)


def test_vehicles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "vehicles.get.0"
    client = get_client(test_id)
    client.vehicles.get(id="id")
    verify_request_count(test_id, "GET", "/fleet/vehicles/id", None, 1)


def test_vehicles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "vehicles.update.0"
    client = get_client(test_id)
    client.vehicles.update(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/vehicles/id", None, 1)
