from .conftest import get_client, verify_request_count


def test_addresses_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "addresses.list_.0"
    client = get_client(test_id)
    client.addresses.list()
    verify_request_count(test_id, "GET", "/addresses", None, 1)


def test_addresses_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "addresses.create.0"
    client = get_client(test_id)
    client.addresses.create(formatted_address="350 Rhode Island St, San Francisco, CA", geofence={}, name="Samsara HQ")
    verify_request_count(test_id, "POST", "/addresses", None, 1)


def test_addresses_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "addresses.get.0"
    client = get_client(test_id)
    client.addresses.get(id="id")
    verify_request_count(test_id, "GET", "/addresses/id", None, 1)


def test_addresses_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "addresses.delete.0"
    client = get_client(test_id)
    client.addresses.delete(id="id")
    verify_request_count(test_id, "DELETE", "/addresses/id", None, 1)


def test_addresses_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "addresses.update.0"
    client = get_client(test_id)
    client.addresses.update(id="id")
    verify_request_count(test_id, "PATCH", "/addresses/id", None, 1)
