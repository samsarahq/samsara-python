from .conftest import get_client, verify_request_count


def test_industrial_assets_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "industrial.assets.delete.0"
    client = get_client(test_id)
    client.industrial.assets.delete(id="id")
    verify_request_count(test_id, "DELETE", "/industrial/assets/id", None, 1)
