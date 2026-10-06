from .conftest import get_client, verify_request_count


def test_preventiveMaintenance_resolve_preventive_maintenance() -> None:
    """Test resolvePreventiveMaintenance endpoint with WireMock"""
    test_id = "preventive_maintenance.resolve_preventive_maintenance.0"
    client = get_client(test_id)
    client.preventive_maintenance.resolve_preventive_maintenance()
    verify_request_count(test_id, "POST", "/maintenance/preventive/resolve", None, 1)


def test_preventiveMaintenance_list_preventive_maintenance_schedules() -> None:
    """Test listPreventiveMaintenanceSchedules endpoint with WireMock"""
    test_id = "preventive_maintenance.list_preventive_maintenance_schedules.0"
    client = get_client(test_id)
    client.preventive_maintenance.list_preventive_maintenance_schedules(ids="281474976710656")
    verify_request_count(test_id, "GET", "/maintenance/preventive/schedules", {"ids": "281474976710656"}, 1)


def test_preventiveMaintenance_list_upcoming_preventive_maintenance() -> None:
    """Test listUpcomingPreventiveMaintenance endpoint with WireMock"""
    test_id = "preventive_maintenance.list_upcoming_preventive_maintenance.0"
    client = get_client(test_id)
    client.preventive_maintenance.list_upcoming_preventive_maintenance()
    verify_request_count(test_id, "GET", "/maintenance/preventive/upcoming", None, 1)


def test_preventiveMaintenance_update_upcoming_preventive_maintenance() -> None:
    """Test updateUpcomingPreventiveMaintenance endpoint with WireMock"""
    test_id = "preventive_maintenance.update_upcoming_preventive_maintenance.0"
    client = get_client(test_id)
    client.preventive_maintenance.update_upcoming_preventive_maintenance()
    verify_request_count(test_id, "PATCH", "/maintenance/preventive/upcoming", None, 1)
