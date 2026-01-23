from .conftest import get_client, verify_request_count


def test_driverQrCodes_get_drivers_qr_codes() -> None:
    """Test getDriversQrCodes endpoint with WireMock"""
    test_id = "driver_qr_codes.get_drivers_qr_codes.0"
    client = get_client(test_id)
    client.driver_qr_codes.get_drivers_qr_codes()
    verify_request_count(test_id, "GET", "/drivers/qr-codes", None, 1)


def test_driverQrCodes_create_driver_qr_code() -> None:
    """Test createDriverQrCode endpoint with WireMock"""
    test_id = "driver_qr_codes.create_driver_qr_code.0"
    client = get_client(test_id)
    client.driver_qr_codes.create_driver_qr_code(driver_id=494123)
    verify_request_count(test_id, "POST", "/drivers/qr-codes", None, 1)


def test_driverQrCodes_delete_driver_qr_code() -> None:
    """Test deleteDriverQrCode endpoint with WireMock"""
    test_id = "driver_qr_codes.delete_driver_qr_code.0"
    client = get_client(test_id)
    client.driver_qr_codes.delete_driver_qr_code(driver_id=494123)
    verify_request_count(test_id, "DELETE", "/drivers/qr-codes", None, 1)
