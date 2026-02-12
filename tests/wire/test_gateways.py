from .conftest import get_client, verify_request_count


def test_gateways_get_gateways() -> None:
    """Test getGateways endpoint with WireMock"""
    test_id = "gateways.get_gateways.0"
    client = get_client(test_id)
    client.gateways.get_gateways()
    verify_request_count(test_id, "GET", "/gateways", None, 1)


def test_gateways_post_gateway() -> None:
    """Test postGateway endpoint with WireMock"""
    test_id = "gateways.post_gateway.0"
    client = get_client(test_id)
    client.gateways.post_gateway(serial="GFRV-43N-VGX")
    verify_request_count(test_id, "POST", "/gateways", None, 1)


def test_gateways_delete_gateway() -> None:
    """Test deleteGateway endpoint with WireMock"""
    test_id = "gateways.delete_gateway.0"
    client = get_client(test_id)
    client.gateways.delete_gateway(id="id")
    verify_request_count(test_id, "DELETE", "/gateways/id", None, 1)
