from .conftest import get_client, verify_request_count


def test_previewApIs_list_device_recovery_missing_assets() -> None:
    """Test listDeviceRecoveryMissingAssets endpoint with WireMock"""
    test_id = "preview_ap_is.list_device_recovery_missing_assets.0"
    client = get_client(test_id)
    client.preview_ap_is.list_device_recovery_missing_assets()
    verify_request_count(test_id, "GET", "/preview/fleet/assets/device-recovery-missing", None, 1)


def test_previewApIs_mark_asset_missing() -> None:
    """Test markAssetMissing endpoint with WireMock"""
    test_id = "preview_ap_is.mark_asset_missing.0"
    client = get_client(test_id)
    client.preview_ap_is.mark_asset_missing(id="id")
    verify_request_count(test_id, "POST", "/preview/fleet/assets/device-recovery/id/missing", None, 1)


def test_previewApIs_recover_asset() -> None:
    """Test recoverAsset endpoint with WireMock"""
    test_id = "preview_ap_is.recover_asset.0"
    client = get_client(test_id)
    client.preview_ap_is.recover_asset(id="id", missing_reason="MISPLACED", recovery_status="YES", status="RECOVERED")
    verify_request_count(test_id, "POST", "/preview/fleet/assets/device-recovery/id/recovered", None, 1)


def test_previewApIs_create_driver_auth_token() -> None:
    """Test createDriverAuthToken endpoint with WireMock"""
    test_id = "preview_ap_is.create_driver_auth_token.0"
    client = get_client(test_id)
    client.preview_ap_is.create_driver_auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/preview/fleet/drivers/create-auth-token", None, 1)


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
