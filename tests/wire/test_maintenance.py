from .conftest import get_client, verify_request_count


def test_maintenance_get_defect_types() -> None:
    """Test getDefectTypes endpoint with WireMock"""
    test_id = "maintenance.get_defect_types.0"
    client = get_client(test_id)
    client.maintenance.get_defect_types()
    verify_request_count(test_id, "GET", "/defect-types", None, 1)


def test_maintenance_stream_defects() -> None:
    """Test streamDefects endpoint with WireMock"""
    test_id = "maintenance.stream_defects.0"
    client = get_client(test_id)
    client.maintenance.stream_defects(start_time="startTime")
    verify_request_count(test_id, "GET", "/defects/stream", {"startTime": "startTime"}, 1)


def test_maintenance_get_defect() -> None:
    """Test getDefect endpoint with WireMock"""
    test_id = "maintenance.get_defect.0"
    client = get_client(test_id)
    client.maintenance.get_defect(id="id")
    verify_request_count(test_id, "GET", "/defects/id", None, 1)


def test_maintenance_get_dvirs() -> None:
    """Test getDvirs endpoint with WireMock"""
    test_id = "maintenance.get_dvirs.0"
    client = get_client(test_id)
    client.maintenance.get_dvirs(start_time="startTime")
    verify_request_count(test_id, "GET", "/dvirs/stream", {"startTime": "startTime"}, 1)


def test_maintenance_get_dvir() -> None:
    """Test getDvir endpoint with WireMock"""
    test_id = "maintenance.get_dvir.0"
    client = get_client(test_id)
    client.maintenance.get_dvir(id="id")
    verify_request_count(test_id, "GET", "/dvirs/id", None, 1)


def test_maintenance_update_dvir_defect() -> None:
    """Test updateDvirDefect endpoint with WireMock"""
    test_id = "maintenance.update_dvir_defect.0"
    client = get_client(test_id)
    client.maintenance.update_dvir_defect(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/defects/id", None, 1)


def test_maintenance_create_dvir() -> None:
    """Test createDvir endpoint with WireMock"""
    test_id = "maintenance.create_dvir.0"
    client = get_client(test_id)
    client.maintenance.create_dvir(author_id="11", safety_status="safe")
    verify_request_count(test_id, "POST", "/fleet/dvirs", None, 1)


def test_maintenance_update_dvir() -> None:
    """Test updateDvir endpoint with WireMock"""
    test_id = "maintenance.update_dvir.0"
    client = get_client(test_id)
    client.maintenance.update_dvir(id="id", author_id="11", is_resolved=True)
    verify_request_count(test_id, "PATCH", "/fleet/dvirs/id", None, 1)


def test_maintenance_v_1_get_fleet_maintenance_list() -> None:
    """Test V1getFleetMaintenanceList endpoint with WireMock"""
    test_id = "maintenance.v_1_get_fleet_maintenance_list.0"
    client = get_client(test_id)
    client.maintenance.v_1_get_fleet_maintenance_list()
    verify_request_count(test_id, "GET", "/v1/fleet/maintenance/list", None, 1)
