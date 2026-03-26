from .conftest import get_client, verify_request_count


def test_carbCtc_list_carb_ctc_vehicles() -> None:
    """Test listCarbCtcVehicles endpoint with WireMock"""
    test_id = "carb_ctc.list_carb_ctc_vehicles.0"
    client = get_client(test_id)
    client.carb_ctc.list_carb_ctc_vehicles()
    verify_request_count(test_id, "GET", "/fleet/carb-ctc/vehicles", None, 1)


def test_carbCtc_list_carb_ctc_vehicle_history() -> None:
    """Test listCarbCtcVehicleHistory endpoint with WireMock"""
    test_id = "carb_ctc.list_carb_ctc_vehicle_history.0"
    client = get_client(test_id)
    client.carb_ctc.list_carb_ctc_vehicle_history(vehicle_ids="vehicleIds")
    verify_request_count(test_id, "GET", "/fleet/carb-ctc/vehicles/history", {"vehicleIds": "vehicleIds"}, 1)
