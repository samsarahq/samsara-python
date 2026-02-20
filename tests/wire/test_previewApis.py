from .conftest import get_client, verify_request_count


def test_previewApis_create_driver_auth_token() -> None:
    """Test createDriverAuthToken endpoint with WireMock"""
    test_id = "preview_apis.create_driver_auth_token.0"
    client = get_client(test_id)
    client.preview_apis.create_driver_auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/preview/fleet/drivers/create-auth-token", None, 1)


def test_previewApis_lock_vehicle() -> None:
    """Test lockVehicle endpoint with WireMock"""
    test_id = "preview_apis.lock_vehicle.0"
    client = get_client(test_id)
    client.preview_apis.lock_vehicle(id="id")
    verify_request_count(test_id, "PUT", "/preview/fleet/vehicles/id/lock", None, 1)


def test_previewApis_unlock_vehicle() -> None:
    """Test unlockVehicle endpoint with WireMock"""
    test_id = "preview_apis.unlock_vehicle.0"
    client = get_client(test_id)
    client.preview_apis.unlock_vehicle(id="id")
    verify_request_count(test_id, "DELETE", "/preview/fleet/vehicles/id/lock", None, 1)
