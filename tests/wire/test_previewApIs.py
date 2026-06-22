from .conftest import get_client, verify_request_count


def test_previewApIs_create_driver_auth_token() -> None:
    """Test createDriverAuthToken endpoint with WireMock"""
    test_id = "preview_ap_is.create_driver_auth_token.0"
    client = get_client(test_id)
    client.preview_ap_is.create_driver_auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/preview/fleet/drivers/create-auth-token", None, 1)


def test_previewApIs_post_tachograph_file_upload() -> None:
    """Test postTachographFileUpload endpoint with WireMock"""
    test_id = "preview_ap_is.post_tachograph_file_upload.0"
    client = get_client(test_id)
    client.preview_ap_is.post_tachograph_file_upload(
        content_md_5="rL0Y20zC+Fzt72VPzMSk2A==",
        content_type="application/octet-stream",
        file_size_bytes=8192,
        file_type="driverCard",
    )
    verify_request_count(test_id, "POST", "/preview/fleet/tachograph/file-uploads", None, 1)


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
