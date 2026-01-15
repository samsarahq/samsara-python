from .conftest import get_client, verify_request_count


def test_drivers_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "drivers.list_.0"
    client = get_client(test_id)
    client.drivers.list()
    verify_request_count(test_id, "GET", "/fleet/drivers", None, 1)


def test_drivers_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "drivers.create.0"
    client = get_client(test_id)
    client.drivers.create(name="Susan Jones", password="aSecurePassword1234", username="SusanJones")
    verify_request_count(test_id, "POST", "/fleet/drivers", None, 1)


def test_drivers_post_driver_remote_signout() -> None:
    """Test postDriverRemoteSignout endpoint with WireMock"""
    test_id = "drivers.post_driver_remote_signout.0"
    client = get_client(test_id)
    client.drivers.post_driver_remote_signout(driver_id="12434")
    verify_request_count(test_id, "POST", "/fleet/drivers/remote-sign-out", None, 1)


def test_drivers_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "drivers.get.0"
    client = get_client(test_id)
    client.drivers.get(id="id")
    verify_request_count(test_id, "GET", "/fleet/drivers/id", None, 1)


def test_drivers_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "drivers.delete.0"
    client = get_client(test_id)
    client.drivers.delete(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/drivers/id", None, 1)


def test_drivers_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "drivers.update.0"
    client = get_client(test_id)
    client.drivers.update(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/drivers/id", None, 1)
