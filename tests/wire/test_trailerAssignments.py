from .conftest import get_client, verify_request_count


def test_trailerAssignments_v_1_get_all_trailer_assignments() -> None:
    """Test V1getAllTrailerAssignments endpoint with WireMock"""
    test_id = "trailer_assignments.v_1_get_all_trailer_assignments.0"
    client = get_client(test_id)
    client.trailer_assignments.v_1_get_all_trailer_assignments()
    verify_request_count(test_id, "GET", "/v1/fleet/trailers/assignments", None, 1)


def test_trailerAssignments_v_1_get_fleet_trailer_assignments() -> None:
    """Test V1getFleetTrailerAssignments endpoint with WireMock"""
    test_id = "trailer_assignments.v_1_get_fleet_trailer_assignments.0"
    client = get_client(test_id)
    client.trailer_assignments.v_1_get_fleet_trailer_assignments(trailer_id=1000000)
    verify_request_count(test_id, "GET", "/v1/fleet/trailers/1000000/assignments", None, 1)
