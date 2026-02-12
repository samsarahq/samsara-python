from .conftest import get_client, verify_request_count


def test_authTokenForDriver_auth_token() -> None:
    """Test authToken endpoint with WireMock"""
    test_id = "auth_token_for_driver.auth_token.0"
    client = get_client(test_id)
    client.auth_token_for_driver.auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/fleet/drivers/auth-token", None, 1)
