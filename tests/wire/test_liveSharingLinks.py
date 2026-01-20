from .conftest import get_client, verify_request_count


def test_liveSharingLinks_get_live_sharing_links() -> None:
    """Test getLiveSharingLinks endpoint with WireMock"""
    test_id = "live_sharing_links.get_live_sharing_links.0"
    client = get_client(test_id)
    client.live_sharing_links.get_live_sharing_links()
    verify_request_count(test_id, "GET", "/live-shares", None, 1)


def test_liveSharingLinks_create_live_sharing_link() -> None:
    """Test createLiveSharingLink endpoint with WireMock"""
    test_id = "live_sharing_links.create_live_sharing_link.0"
    client = get_client(test_id)
    client.live_sharing_links.create_live_sharing_link(name="Example Live Sharing Link name", type="assetsLocation")
    verify_request_count(test_id, "POST", "/live-shares", None, 1)


def test_liveSharingLinks_delete_live_sharing_link() -> None:
    """Test deleteLiveSharingLink endpoint with WireMock"""
    test_id = "live_sharing_links.delete_live_sharing_link.0"
    client = get_client(test_id)
    client.live_sharing_links.delete_live_sharing_link(id="id")
    verify_request_count(test_id, "DELETE", "/live-shares", {"id": "id"}, 1)


def test_liveSharingLinks_update_live_sharing_link() -> None:
    """Test updateLiveSharingLink endpoint with WireMock"""
    test_id = "live_sharing_links.update_live_sharing_link.0"
    client = get_client(test_id)
    client.live_sharing_links.update_live_sharing_link(id="id", name="Example Live Sharing Link name")
    verify_request_count(test_id, "PATCH", "/live-shares", {"id": "id"}, 1)
