from .conftest import get_client, verify_request_count


def test_driverTrailerAssignments_get_driver_trailer_assignments() -> None:
    """Test getDriverTrailerAssignments endpoint with WireMock"""
    test_id = "driver_trailer_assignments.get_driver_trailer_assignments.0"
    client = get_client(test_id)
    client.driver_trailer_assignments.get_driver_trailer_assignments()
    verify_request_count(test_id, "GET", "/driver-trailer-assignments", None, 1)


def test_driverTrailerAssignments_create_driver_trailer_assignment() -> None:
    """Test createDriverTrailerAssignment endpoint with WireMock"""
    test_id = "driver_trailer_assignments.create_driver_trailer_assignment.0"
    client = get_client(test_id)
    client.driver_trailer_assignments.create_driver_trailer_assignment(driver_id="494123", trailer_id="12345")
    verify_request_count(test_id, "POST", "/driver-trailer-assignments", None, 1)


def test_driverTrailerAssignments_update_driver_trailer_assignment() -> None:
    """Test updateDriverTrailerAssignment endpoint with WireMock"""
    test_id = "driver_trailer_assignments.update_driver_trailer_assignment.0"
    client = get_client(test_id)
    client.driver_trailer_assignments.update_driver_trailer_assignment(id="id", end_time="2019-06-13T19:08:25Z")
    verify_request_count(test_id, "PATCH", "/driver-trailer-assignments", {"id": "id"}, 1)
