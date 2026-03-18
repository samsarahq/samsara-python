from .conftest import get_client, verify_request_count


def test_previewApIs_list_associations() -> None:
    """Test listAssociations endpoint with WireMock"""
    test_id = "preview_ap_is.list_associations.0"
    client = get_client(test_id)
    client.preview_ap_is.list_associations(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/preview/fleet/assets/associations", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


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


def test_previewApIs_patch_safety_events_v_2_batch() -> None:
    """Test patchSafetyEventsV2Batch endpoint with WireMock"""
    test_id = "preview_ap_is.patch_safety_events_v_2_batch.0"
    client = get_client(test_id)
    client.preview_ap_is.patch_safety_events_v_2_batch(
        safety_event_ids=["bb2ff5ab-30ad-49ec-9d2d-55ec30bbf590", "bb2ff5ab-30ad-49ec-9d2d-55ec30bbf590"]
    )
    verify_request_count(test_id, "PATCH", "/preview/safety-events/batch", None, 1)
