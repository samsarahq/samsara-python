from .conftest import get_client, verify_request_count


def test_fuelAndEnergy_get_driver_efficiency_by_drivers() -> None:
    """Test getDriverEfficiencyByDrivers endpoint with WireMock"""
    test_id = "fuel_and_energy.get_driver_efficiency_by_drivers.0"
    client = get_client(test_id)
    client.fuel_and_energy.get_driver_efficiency_by_drivers(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/driver-efficiency/drivers", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_fuelAndEnergy_get_driver_efficiency_by_vehicles() -> None:
    """Test getDriverEfficiencyByVehicles endpoint with WireMock"""
    test_id = "fuel_and_energy.get_driver_efficiency_by_vehicles.0"
    client = get_client(test_id)
    client.fuel_and_energy.get_driver_efficiency_by_vehicles(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/driver-efficiency/vehicles", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


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
