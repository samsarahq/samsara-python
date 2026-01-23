from .conftest import get_client, verify_request_count


def test_ifta_get_ifta_jurisdiction_reports() -> None:
    """Test getIftaJurisdictionReports endpoint with WireMock"""
    test_id = "ifta.get_ifta_jurisdiction_reports.0"
    client = get_client(test_id)
    client.ifta.get_ifta_jurisdiction_reports(year=1000000)
    verify_request_count(test_id, "GET", "/fleet/reports/ifta/jurisdiction", {"year": "1000000"}, 1)


def test_ifta_get_ifta_vehicle_reports() -> None:
    """Test getIftaVehicleReports endpoint with WireMock"""
    test_id = "ifta.get_ifta_vehicle_reports.0"
    client = get_client(test_id)
    client.ifta.get_ifta_vehicle_reports(year=1000000)
    verify_request_count(test_id, "GET", "/fleet/reports/ifta/vehicle", {"year": "1000000"}, 1)


def test_ifta_create_ifta_detail_job() -> None:
    """Test createIftaDetailJob endpoint with WireMock"""
    test_id = "ifta.create_ifta_detail_job.0"
    client = get_client(test_id)
    client.ifta.create_ifta_detail_job(end_hour="2019-06-13T19:00:00Z", start_hour="2019-06-13T19:00:00Z")
    verify_request_count(test_id, "POST", "/ifta-detail/csv", None, 1)


def test_ifta_get_ifta_detail_job() -> None:
    """Test getIftaDetailJob endpoint with WireMock"""
    test_id = "ifta.get_ifta_detail_job.0"
    client = get_client(test_id)
    client.ifta.get_ifta_detail_job(id="id")
    verify_request_count(test_id, "GET", "/ifta-detail/csv/id", None, 1)
