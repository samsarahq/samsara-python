from .conftest import get_client, verify_request_count


def test_legacy_v_1_get_all_assets() -> None:
    """Test V1getAllAssets endpoint with WireMock"""
    test_id = "legacy.v_1_get_all_assets.0"
    client = get_client(test_id)
    client.legacy.v_1_get_all_assets()
    verify_request_count(test_id, "GET", "/v1/fleet/assets", None, 1)
