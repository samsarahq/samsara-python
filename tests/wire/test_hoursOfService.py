from .conftest import get_client, verify_request_count


def test_hoursOfService_get_hos_clocks() -> None:
    """Test getHosClocks endpoint with WireMock"""
    test_id = "hours_of_service.get_hos_clocks.0"
    client = get_client(test_id)
    client.hours_of_service.get_hos_clocks()
    verify_request_count(test_id, "GET", "/fleet/hos/clocks", None, 1)


def test_hoursOfService_get_hos_daily_logs() -> None:
    """Test getHosDailyLogs endpoint with WireMock"""
    test_id = "hours_of_service.get_hos_daily_logs.0"
    client = get_client(test_id)
    client.hours_of_service.get_hos_daily_logs()
    verify_request_count(test_id, "GET", "/fleet/hos/daily-logs", None, 1)


def test_hoursOfService_get_hos_logs() -> None:
    """Test getHosLogs endpoint with WireMock"""
    test_id = "hours_of_service.get_hos_logs.0"
    client = get_client(test_id)
    client.hours_of_service.get_hos_logs()
    verify_request_count(test_id, "GET", "/fleet/hos/logs", None, 1)


def test_hoursOfService_get_hos_violations() -> None:
    """Test getHosViolations endpoint with WireMock"""
    test_id = "hours_of_service.get_hos_violations.0"
    client = get_client(test_id)
    client.hours_of_service.get_hos_violations()
    verify_request_count(test_id, "GET", "/fleet/hos/violations", None, 1)


def test_hoursOfService_set_current_duty_status() -> None:
    """Test setCurrentDutyStatus endpoint with WireMock"""
    test_id = "hours_of_service.set_current_duty_status.0"
    client = get_client(test_id)
    client.hours_of_service.set_current_duty_status(driver_id=1000000, duty_status="ON_DUTY")
    verify_request_count(test_id, "POST", "/v1/fleet/drivers/1000000/hos/duty_status", None, 1)


def test_hoursOfService_v_1_get_fleet_hos_authentication_logs() -> None:
    """Test V1getFleetHosAuthenticationLogs endpoint with WireMock"""
    test_id = "hours_of_service.v_1_get_fleet_hos_authentication_logs.0"
    client = get_client(test_id)
    client.hours_of_service.v_1_get_fleet_hos_authentication_logs(driver_id=1000000, start_ms=1000000, end_ms=1000000)
    verify_request_count(
        test_id,
        "GET",
        "/v1/fleet/hos_authentication_logs",
        {"driverId": "1000000", "startMs": "1000000", "endMs": "1000000"},
        1,
    )
