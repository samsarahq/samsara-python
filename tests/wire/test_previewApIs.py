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


def test_previewApIs_list_warranties() -> None:
    """Test listWarranties endpoint with WireMock"""
    test_id = "preview_ap_is.list_warranties.0"
    client = get_client(test_id)
    client.preview_ap_is.list_warranties()
    verify_request_count(test_id, "GET", "/preview/maintenance/warranties", None, 1)


def test_previewApIs_create_warranty() -> None:
    """Test createWarranty endpoint with WireMock"""
    test_id = "preview_ap_is.create_warranty.0"
    client = get_client(test_id)
    client.preview_ap_is.create_warranty(name="12345")
    verify_request_count(test_id, "POST", "/preview/maintenance/warranties", None, 1)


def test_previewApIs_delete_warranty() -> None:
    """Test deleteWarranty endpoint with WireMock"""
    test_id = "preview_ap_is.delete_warranty.0"
    client = get_client(test_id)
    client.preview_ap_is.delete_warranty(id="id")
    verify_request_count(test_id, "DELETE", "/preview/maintenance/warranties", {"id": "id"}, 1)


def test_previewApIs_update_warranty() -> None:
    """Test updateWarranty endpoint with WireMock"""
    test_id = "preview_ap_is.update_warranty.0"
    client = get_client(test_id)
    client.preview_ap_is.update_warranty(id="id")
    verify_request_count(test_id, "PATCH", "/preview/maintenance/warranties", {"id": "id"}, 1)


def test_previewApIs_replace_warranty_asset_assignments() -> None:
    """Test replaceWarrantyAssetAssignments endpoint with WireMock"""
    test_id = "preview_ap_is.replace_warranty_asset_assignments.0"
    client = get_client(test_id)
    client.preview_ap_is.replace_warranty_asset_assignments()
    verify_request_count(test_id, "POST", "/preview/maintenance/warranties/assets/replace", None, 1)


def test_previewApIs_list_warranty_claims() -> None:
    """Test listWarrantyClaims endpoint with WireMock"""
    test_id = "preview_ap_is.list_warranty_claims.0"
    client = get_client(test_id)
    client.preview_ap_is.list_warranty_claims()
    verify_request_count(test_id, "GET", "/preview/maintenance/warranty-claims", None, 1)


def test_previewApIs_create_warranty_claim() -> None:
    """Test createWarrantyClaim endpoint with WireMock"""
    test_id = "preview_ap_is.create_warranty_claim.0"
    client = get_client(test_id)
    client.preview_ap_is.create_warranty_claim(asset_id="281474976710656")
    verify_request_count(test_id, "POST", "/preview/maintenance/warranty-claims", None, 1)


def test_previewApIs_delete_warranty_claim() -> None:
    """Test deleteWarrantyClaim endpoint with WireMock"""
    test_id = "preview_ap_is.delete_warranty_claim.0"
    client = get_client(test_id)
    client.preview_ap_is.delete_warranty_claim(id="id")
    verify_request_count(test_id, "DELETE", "/preview/maintenance/warranty-claims", {"id": "id"}, 1)


def test_previewApIs_update_warranty_claim() -> None:
    """Test updateWarrantyClaim endpoint with WireMock"""
    test_id = "preview_ap_is.update_warranty_claim.0"
    client = get_client(test_id)
    client.preview_ap_is.update_warranty_claim(id="id")
    verify_request_count(test_id, "PATCH", "/preview/maintenance/warranty-claims", {"id": "id"}, 1)
