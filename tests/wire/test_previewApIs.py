from .conftest import get_client, verify_request_count


def test_previewApIs_create_driver_auth_token() -> None:
    """Test createDriverAuthToken endpoint with WireMock"""
    test_id = "preview_ap_is.create_driver_auth_token.0"
    client = get_client(test_id)
    client.preview_ap_is.create_driver_auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/preview/fleet/drivers/create-auth-token", None, 1)


def test_previewApIs_get_fleet_installer_photo_uploads() -> None:
    """Test getFleetInstallerPhotoUploads endpoint with WireMock"""
    test_id = "preview_ap_is.get_fleet_installer_photo_uploads.0"
    client = get_client(test_id)
    client.preview_ap_is.get_fleet_installer_photo_uploads()
    verify_request_count(test_id, "GET", "/preview/fleet/installer/photo-uploads", None, 1)


def test_previewApIs_post_fleet_installer_photo_upload() -> None:
    """Test postFleetInstallerPhotoUpload endpoint with WireMock"""
    test_id = "preview_ap_is.post_fleet_installer_photo_upload.0"
    client = get_client(test_id)
    client.preview_ap_is.post_fleet_installer_photo_upload(
        content_md_5="rL0Y20zC+Fzt72VPzMSk2A==",
        device_id="281474977961335",
        file_format_type="imageJpeg",
        file_name="front_camera_install.jpg",
        hardware_type="vehicleGateway",
        photo_type="installPhoto",
        size_bytes=482193,
    )
    verify_request_count(test_id, "POST", "/preview/fleet/installer/photo-uploads", None, 1)


def test_previewApIs_post_fleet_installer_photo_upload_complete() -> None:
    """Test postFleetInstallerPhotoUploadComplete endpoint with WireMock"""
    test_id = "preview_ap_is.post_fleet_installer_photo_upload_complete.0"
    client = get_client(test_id)
    client.preview_ap_is.post_fleet_installer_photo_upload_complete(id="id")
    verify_request_count(test_id, "POST", "/preview/fleet/installer/photo-uploads/complete", {"id": "id"}, 1)


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
