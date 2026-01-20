from .conftest import get_client, verify_request_count


def test_webhooks_list_webhooks() -> None:
    """Test listWebhooks endpoint with WireMock"""
    test_id = "webhooks.list_webhooks.0"
    client = get_client(test_id)
    client.webhooks.list_webhooks()
    verify_request_count(test_id, "GET", "/webhooks", None, 1)


def test_webhooks_post_webhooks() -> None:
    """Test postWebhooks endpoint with WireMock"""
    test_id = "webhooks.post_webhooks.0"
    client = get_client(test_id)
    client.webhooks.post_webhooks(name="Webhook-123", url="https://www.Webhook-123.com/webhook/listener")
    verify_request_count(test_id, "POST", "/webhooks", None, 1)


def test_webhooks_get_webhook() -> None:
    """Test getWebhook endpoint with WireMock"""
    test_id = "webhooks.get_webhook.0"
    client = get_client(test_id)
    client.webhooks.get_webhook(id="id")
    verify_request_count(test_id, "GET", "/webhooks/id", None, 1)


def test_webhooks_delete_webhook() -> None:
    """Test deleteWebhook endpoint with WireMock"""
    test_id = "webhooks.delete_webhook.0"
    client = get_client(test_id)
    client.webhooks.delete_webhook(id="id")
    verify_request_count(test_id, "DELETE", "/webhooks/id", None, 1)


def test_webhooks_patch_webhook() -> None:
    """Test patchWebhook endpoint with WireMock"""
    test_id = "webhooks.patch_webhook.0"
    client = get_client(test_id)
    client.webhooks.patch_webhook(id="id")
    verify_request_count(test_id, "PATCH", "/webhooks/id", None, 1)
