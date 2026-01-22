from .conftest import get_client, verify_request_count


def test_settings_get_compliance_settings() -> None:
    """Test getComplianceSettings endpoint with WireMock"""
    test_id = "settings.get_compliance_settings.0"
    client = get_client(test_id)
    client.settings.get_compliance_settings()
    verify_request_count(test_id, "GET", "/fleet/settings/compliance", None, 1)


def test_settings_patch_compliance_settings() -> None:
    """Test patchComplianceSettings endpoint with WireMock"""
    test_id = "settings.patch_compliance_settings.0"
    client = get_client(test_id)
    client.settings.patch_compliance_settings()
    verify_request_count(test_id, "PATCH", "/fleet/settings/compliance", None, 1)


def test_settings_get_driver_app_settings() -> None:
    """Test getDriverAppSettings endpoint with WireMock"""
    test_id = "settings.get_driver_app_settings.0"
    client = get_client(test_id)
    client.settings.get_driver_app_settings()
    verify_request_count(test_id, "GET", "/fleet/settings/driver-app", None, 1)


def test_settings_patch_driver_app_settings() -> None:
    """Test patchDriverAppSettings endpoint with WireMock"""
    test_id = "settings.patch_driver_app_settings.0"
    client = get_client(test_id)
    client.settings.patch_driver_app_settings()
    verify_request_count(test_id, "PATCH", "/fleet/settings/driver-app", None, 1)


def test_settings_get_safety_settings() -> None:
    """Test getSafetySettings endpoint with WireMock"""
    test_id = "settings.get_safety_settings.0"
    client = get_client(test_id)
    client.settings.get_safety_settings()
    verify_request_count(test_id, "GET", "/fleet/settings/safety", None, 1)
