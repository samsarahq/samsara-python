from .conftest import get_client, verify_request_count


def test_fuelAndEnergy_get_fuel_energy_driver_reports() -> None:
    """Test getFuelEnergyDriverReports endpoint with WireMock"""
    test_id = "fuel_and_energy.get_fuel_energy_driver_reports.0"
    client = get_client(test_id)
    client.fuel_and_energy.get_fuel_energy_driver_reports(start_date="startDate", end_date="endDate")
    verify_request_count(
        test_id, "GET", "/fleet/reports/drivers/fuel-energy", {"startDate": "startDate", "endDate": "endDate"}, 1
    )


def test_fuelAndEnergy_get_fuel_energy_vehicle_reports() -> None:
    """Test getFuelEnergyVehicleReports endpoint with WireMock"""
    test_id = "fuel_and_energy.get_fuel_energy_vehicle_reports.0"
    client = get_client(test_id)
    client.fuel_and_energy.get_fuel_energy_vehicle_reports(start_date="startDate", end_date="endDate")
    verify_request_count(
        test_id, "GET", "/fleet/reports/vehicles/fuel-energy", {"startDate": "startDate", "endDate": "endDate"}, 1
    )


def test_fuelAndEnergy_post_fuel_purchase() -> None:
    """Test postFuelPurchase endpoint with WireMock"""
    test_id = "fuel_and_energy.post_fuel_purchase.0"
    client = get_client(test_id)
    client.fuel_and_energy.post_fuel_purchase(
        fuel_quantity_liters="676.8",
        transaction_location="350 Rhode Island St, San Francisco, CA 94103",
        transaction_price={"amount": "640.2", "currency": "usd"},
        transaction_reference="5454534",
        transaction_time="2022-07-13T14:20:50.52-07:00",
    )
    verify_request_count(test_id, "POST", "/fuel-purchase", None, 1)


def test_fuelAndEnergy_list_preferred_stations() -> None:
    """Test listPreferredStations endpoint with WireMock"""
    test_id = "fuel_and_energy.list_preferred_stations.0"
    client = get_client(test_id)
    client.fuel_and_energy.list_preferred_stations()
    verify_request_count(test_id, "GET", "/preferred-stations", None, 1)


def test_fuelAndEnergy_post_preferred_station() -> None:
    """Test postPreferredStation endpoint with WireMock"""
    test_id = "fuel_and_energy.post_preferred_station.0"
    client = get_client(test_id)
    client.fuel_and_energy.post_preferred_station(
        address={"city": "Green River", "country": "US", "line_1": "8901 US Hwy 374", "postal_code": "82935"},
        external_ids={"key": "value"},
        name="Station #432",
    )
    verify_request_count(test_id, "POST", "/preferred-stations", None, 1)


def test_fuelAndEnergy_delete_preferred_station() -> None:
    """Test deletePreferredStation endpoint with WireMock"""
    test_id = "fuel_and_energy.delete_preferred_station.0"
    client = get_client(test_id)
    client.fuel_and_energy.delete_preferred_station(id="id")
    verify_request_count(test_id, "DELETE", "/preferred-stations", {"id": "id"}, 1)


def test_fuelAndEnergy_patch_preferred_station() -> None:
    """Test patchPreferredStation endpoint with WireMock"""
    test_id = "fuel_and_energy.patch_preferred_station.0"
    client = get_client(test_id)
    client.fuel_and_energy.patch_preferred_station(id="id")
    verify_request_count(test_id, "PATCH", "/preferred-stations", {"id": "id"}, 1)


def test_fuelAndEnergy_get_preferred_station() -> None:
    """Test getPreferredStation endpoint with WireMock"""
    test_id = "fuel_and_energy.get_preferred_station.0"
    client = get_client(test_id)
    client.fuel_and_energy.get_preferred_station(id="id")
    verify_request_count(test_id, "GET", "/preferred-stations/id", None, 1)
