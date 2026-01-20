from .conftest import get_client, verify_request_count


def test_sensors_v_1_get_sensors_cargo() -> None:
    """Test V1getSensorsCargo endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors_cargo.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors_cargo(sensors=[122])
    verify_request_count(test_id, "POST", "/v1/sensors/cargo", None, 1)


def test_sensors_v_1_get_sensors_door() -> None:
    """Test V1getSensorsDoor endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors_door.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors_door(sensors=[122])
    verify_request_count(test_id, "POST", "/v1/sensors/door", None, 1)


def test_sensors_v_1_get_sensors_history() -> None:
    """Test V1getSensorsHistory endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors_history.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors_history(
        end_ms=1462881998034,
        series=[{"field": "ambientTemperature", "widget_id": 1}],
        start_ms=1462878398034,
        step_ms=3600000,
    )
    verify_request_count(test_id, "POST", "/v1/sensors/history", None, 1)


def test_sensors_v_1_get_sensors_humidity() -> None:
    """Test V1getSensorsHumidity endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors_humidity.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors_humidity(sensors=[122])
    verify_request_count(test_id, "POST", "/v1/sensors/humidity", None, 1)


def test_sensors_v_1_get_sensors() -> None:
    """Test V1getSensors endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors()
    verify_request_count(test_id, "POST", "/v1/sensors/list", None, 1)


def test_sensors_v_1_get_sensors_temperature() -> None:
    """Test V1getSensorsTemperature endpoint with WireMock"""
    test_id = "sensors.v_1_get_sensors_temperature.0"
    client = get_client(test_id)
    client.sensors.v_1_get_sensors_temperature(sensors=[122])
    verify_request_count(test_id, "POST", "/v1/sensors/temperature", None, 1)
