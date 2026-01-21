from .conftest import get_client, verify_request_count


def test_assets_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "assets.list_.0"
    client = get_client(test_id)
    client.assets.list()
    verify_request_count(test_id, "GET", "/assets", None, 1)


def test_assets_create_asset() -> None:
    """Test createAsset endpoint with WireMock"""
    test_id = "assets.create_asset.0"
    client = get_client(test_id)
    client.assets.create_asset()
    verify_request_count(test_id, "POST", "/assets", None, 1)


def test_assets_delete_asset() -> None:
    """Test deleteAsset endpoint with WireMock"""
    test_id = "assets.delete_asset.0"
    client = get_client(test_id)
    client.assets.delete_asset(id="id")
    verify_request_count(test_id, "DELETE", "/assets", {"id": "id"}, 1)


def test_assets_update_asset() -> None:
    """Test updateAsset endpoint with WireMock"""
    test_id = "assets.update_asset.0"
    client = get_client(test_id)
    client.assets.update_asset(id="id")
    verify_request_count(test_id, "PATCH", "/assets", {"id": "id"}, 1)


def test_assets_v_1_get_all_asset_current_locations() -> None:
    """Test V1getAllAssetCurrentLocations endpoint with WireMock"""
    test_id = "assets.v_1_get_all_asset_current_locations.0"
    client = get_client(test_id)
    client.assets.v_1_get_all_asset_current_locations()
    verify_request_count(test_id, "GET", "/v1/fleet/assets/locations", None, 1)


def test_assets_v_1_get_assets_reefers() -> None:
    """Test V1getAssetsReefers endpoint with WireMock"""
    test_id = "assets.v_1_get_assets_reefers.0"
    client = get_client(test_id)
    client.assets.v_1_get_assets_reefers(start_ms=1000000, end_ms=1000000)
    verify_request_count(test_id, "GET", "/v1/fleet/assets/reefers", {"startMs": "1000000", "endMs": "1000000"}, 1)


def test_assets_v_1_get_asset_location() -> None:
    """Test V1getAssetLocation endpoint with WireMock"""
    test_id = "assets.v_1_get_asset_location.0"
    client = get_client(test_id)
    client.assets.v_1_get_asset_location(asset_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/assets/1000000/locations", {"startMs": "1000000", "endMs": "1000000"}, 1
    )


def test_assets_v_1_get_asset_reefer() -> None:
    """Test V1getAssetReefer endpoint with WireMock"""
    test_id = "assets.v_1_get_asset_reefer.0"
    client = get_client(test_id)
    client.assets.v_1_get_asset_reefer(asset_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id, "GET", "/v1/fleet/assets/1000000/reefer", {"startMs": "1000000", "endMs": "1000000"}, 1
    )


def test_assets_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "assets.get.0"
    client = get_client(test_id)
    client.assets.get(id="id")
    verify_request_count(test_id, "GET", "/assets/id", None, 1)


def test_assets_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "assets.update.0"
    client = get_client(test_id)
    client.assets.update(id="id")
    verify_request_count(test_id, "PATCH", "/assets/id", None, 1)
