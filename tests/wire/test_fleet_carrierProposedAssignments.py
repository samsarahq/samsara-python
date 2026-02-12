from .conftest import get_client, verify_request_count


def test_fleet_carrierProposedAssignments_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "fleet.carrier_proposed_assignments.delete.0"
    client = get_client(test_id)
    client.fleet.carrier_proposed_assignments.delete(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/carrier-proposed-assignments/id", None, 1)
