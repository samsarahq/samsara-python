from datetime import datetime

from .conftest import get_client, verify_request_count


def test_previewApIs_create_driver_auth_token() -> None:
    """Test createDriverAuthToken endpoint with WireMock"""
    test_id = "preview_ap_is.create_driver_auth_token.0"
    client = get_client(test_id)
    client.preview_ap_is.create_driver_auth_token(code="dp[gZc1wAigz4uGa0Hh")
    verify_request_count(test_id, "POST", "/preview/fleet/drivers/create-auth-token", None, 1)


def test_previewApIs_get_orders() -> None:
    """Test getOrders endpoint with WireMock"""
    test_id = "preview_ap_is.get_orders.0"
    client = get_client(test_id)
    client.preview_ap_is.get_orders()
    verify_request_count(test_id, "GET", "/preview/fleet/orders", None, 1)


def test_previewApIs_delete_order() -> None:
    """Test deleteOrder endpoint with WireMock"""
    test_id = "preview_ap_is.delete_order.0"
    client = get_client(test_id)
    client.preview_ap_is.delete_order(order_id="orderId")
    verify_request_count(test_id, "DELETE", "/preview/fleet/orders", {"orderId": "orderId"}, 1)


def test_previewApIs_post_orders_batch() -> None:
    """Test postOrdersBatch endpoint with WireMock"""
    test_id = "preview_ap_is.post_orders_batch.0"
    client = get_client(test_id)
    client.preview_ap_is.post_orders_batch(data=[{}])
    verify_request_count(test_id, "POST", "/preview/fleet/orders/batch", None, 1)


def test_previewApIs_get_order_deletions() -> None:
    """Test getOrderDeletions endpoint with WireMock"""
    test_id = "preview_ap_is.get_order_deletions.0"
    client = get_client(test_id)
    client.preview_ap_is.get_order_deletions()
    verify_request_count(test_id, "GET", "/preview/fleet/orders/deletions", None, 1)


def test_previewApIs_get_orders_stream() -> None:
    """Test getOrdersStream endpoint with WireMock"""
    test_id = "preview_ap_is.get_orders_stream.0"
    client = get_client(test_id)
    client.preview_ap_is.get_orders_stream(start_time=datetime.fromisoformat("2024-01-15T09:30:00+00:00"))
    verify_request_count(test_id, "GET", "/preview/fleet/orders/stream", {"startTime": "2024-01-15T09:30:00Z"}, 1)


def test_previewApIs_lock_vehicle() -> None:
    """Test lockVehicle endpoint with WireMock"""
    test_id = "preview_ap_is.lock_vehicle.0"
    client = get_client(test_id)
    client.preview_ap_is.lock_vehicle(id="id")
    verify_request_count(test_id, "PUT", "/preview/fleet/vehicles/id/lock", None, 1)


def test_previewApIs_unlock_vehicle() -> None:
    """Test unlockVehicle endpoint with WireMock"""
    test_id = "preview_ap_is.unlock_vehicle.0"
    client = get_client(test_id)
    client.preview_ap_is.unlock_vehicle(id="id")
    verify_request_count(test_id, "DELETE", "/preview/fleet/vehicles/id/lock", None, 1)


def test_previewApIs_list_part_transactions() -> None:
    """Test listPartTransactions endpoint with WireMock"""
    test_id = "preview_ap_is.list_part_transactions.0"
    client = get_client(test_id)
    client.preview_ap_is.list_part_transactions(happened_at_time_start="happenedAtTimeStart")
    verify_request_count(
        test_id, "GET", "/preview/maintenance/parts/transactions", {"happenedAtTimeStart": "happenedAtTimeStart"}, 1
    )
