from .conftest import get_client, verify_request_count


def test_organizationInfo_get_organization_info() -> None:
    """Test getOrganizationInfo endpoint with WireMock"""
    test_id = "organization_info.get_organization_info.0"
    client = get_client(test_id)
    client.organization_info.get_organization_info()
    verify_request_count(test_id, "GET", "/me", None, 1)
