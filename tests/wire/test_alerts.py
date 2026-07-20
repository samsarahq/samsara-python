from .conftest import get_client, verify_request_count


def test_alerts_get_configurations() -> None:
    """Test getConfigurations endpoint with WireMock"""
    test_id = "alerts.get_configurations.0"
    client = get_client(test_id)
    client.alerts.get_configurations()
    verify_request_count(test_id, "GET", "/alerts/configurations", None, 1)


def test_alerts_post_configurations() -> None:
    """Test postConfigurations endpoint with WireMock"""
    test_id = "alerts.post_configurations.0"
    client = get_client(test_id)
    client.alerts.post_configurations(
        actions=[{"action_type_id": 1}],
        is_enabled=True,
        name="My Harsh Event Alert",
        scope={"all_": True},
        triggers=[{"trigger_type_id": 1000}],
    )
    verify_request_count(test_id, "POST", "/alerts/configurations", None, 1)


def test_alerts_delete_configurations() -> None:
    """Test deleteConfigurations endpoint with WireMock"""
    test_id = "alerts.delete_configurations.0"
    client = get_client(test_id)
    client.alerts.delete_configurations(id="id")
    verify_request_count(test_id, "DELETE", "/alerts/configurations", {"id": "id"}, 1)


def test_alerts_patch_configurations() -> None:
    """Test patchConfigurations endpoint with WireMock"""
    test_id = "alerts.patch_configurations.0"
    client = get_client(test_id)
    client.alerts.patch_configurations(id="e1c5dffc-c7b7-47b0-a778-6a65de638abf")
    verify_request_count(test_id, "PATCH", "/alerts/configurations", None, 1)


def test_alerts_get_incidents() -> None:
    """Test getIncidents endpoint with WireMock"""
    test_id = "alerts.get_incidents.0"
    client = get_client(test_id)
    client.alerts.get_incidents(start_time="startTime")
    verify_request_count(test_id, "GET", "/alerts/incidents/stream", {"startTime": "startTime"}, 1)
