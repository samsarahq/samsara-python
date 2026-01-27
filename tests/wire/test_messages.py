from .conftest import get_client, verify_request_count


def test_messages_v_1_get_messages() -> None:
    """Test V1getMessages endpoint with WireMock"""
    test_id = "messages.v_1_get_messages.0"
    client = get_client(test_id)
    client.messages.v_1_get_messages()
    verify_request_count(test_id, "GET", "/v1/fleet/messages", None, 1)


def test_messages_v_1_create_messages() -> None:
    """Test V1createMessages endpoint with WireMock"""
    test_id = "messages.v_1_create_messages.0"
    client = get_client(test_id)
    client.messages.v_1_create_messages(driver_ids=[111, 222, 333], text="This is a message.")
    verify_request_count(test_id, "POST", "/v1/fleet/messages", None, 1)
