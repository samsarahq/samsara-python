from .conftest import get_client, verify_request_count


def test_carrierProposedAssignments_list_carrier_proposed_assignments() -> None:
    """Test listCarrierProposedAssignments endpoint with WireMock"""
    test_id = "carrier_proposed_assignments.list_carrier_proposed_assignments.0"
    client = get_client(test_id)
    client.carrier_proposed_assignments.list_carrier_proposed_assignments()
    verify_request_count(test_id, "GET", "/fleet/carrier-proposed-assignments", None, 1)


def test_carrierProposedAssignments_create_carrier_proposed_assignment() -> None:
    """Test createCarrierProposedAssignment endpoint with WireMock"""
    test_id = "carrier_proposed_assignments.create_carrier_proposed_assignment.0"
    client = get_client(test_id)
    client.carrier_proposed_assignments.create_carrier_proposed_assignment(driver_id="42", vehicle_id="123")
    verify_request_count(test_id, "POST", "/fleet/carrier-proposed-assignments", None, 1)
