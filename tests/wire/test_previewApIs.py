from .conftest import get_client, verify_request_count


def test_previewApIs_lock_vehicle() -> None:
    """Test lockVehicle endpoint with WireMock"""
    test_id = "preview_ap_is.lock_vehicle.0"
    client = get_client(test_id)
    client.preview_ap_is.lock_vehicle(id="id")
    verify_request_count(test_id, "PUT", "/preview/fleet/vehicles/id/lock", None, 1)


def test_previewApIs_unlock_vehicle() -> None:
    """Test unlockVehicle endpoint with WireMock"""
    test_id = "preview_ap_is.unlock_vehicle.0"
    client = get_client(test_id)
    client.preview_ap_is.unlock_vehicle(id="id")
    verify_request_count(test_id, "DELETE", "/preview/fleet/vehicles/id/lock", None, 1)
