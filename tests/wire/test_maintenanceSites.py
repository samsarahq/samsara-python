from .conftest import get_client, verify_request_count


def test_maintenanceSites_list_maintenance_sites() -> None:
    """Test listMaintenanceSites endpoint with WireMock"""
    test_id = "maintenance_sites.list_maintenance_sites.0"
    client = get_client(test_id)
    client.maintenance_sites.list_maintenance_sites()
    verify_request_count(test_id, "GET", "/maintenance/sites", None, 1)


def test_maintenanceSites_create_maintenance_site() -> None:
    """Test createMaintenanceSite endpoint with WireMock"""
    test_id = "maintenance_sites.create_maintenance_site.0"
    client = get_client(test_id)
    client.maintenance_sites.create_maintenance_site(name="12345", site_code="12345", site_type="Unknown")
    verify_request_count(test_id, "POST", "/maintenance/sites", None, 1)


def test_maintenanceSites_update_maintenance_site() -> None:
    """Test updateMaintenanceSite endpoint with WireMock"""
    test_id = "maintenance_sites.update_maintenance_site.0"
    client = get_client(test_id)
    client.maintenance_sites.update_maintenance_site(id="id")
    verify_request_count(test_id, "PATCH", "/maintenance/sites", {"id": "id"}, 1)
