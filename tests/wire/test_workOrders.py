from .conftest import get_client, verify_request_count


def test_workOrders_get_service_tasks() -> None:
    """Test getServiceTasks endpoint with WireMock"""
    test_id = "work_orders.get_service_tasks.0"
    client = get_client(test_id)
    client.work_orders.get_service_tasks()
    verify_request_count(test_id, "GET", "/maintenance/service-tasks", None, 1)


def test_workOrders_get_work_orders() -> None:
    """Test getWorkOrders endpoint with WireMock"""
    test_id = "work_orders.get_work_orders.0"
    client = get_client(test_id)
    client.work_orders.get_work_orders()
    verify_request_count(test_id, "GET", "/maintenance/work-orders", None, 1)


def test_workOrders_post_work_orders() -> None:
    """Test postWorkOrders endpoint with WireMock"""
    test_id = "work_orders.post_work_orders.0"
    client = get_client(test_id)
    client.work_orders.post_work_orders(asset_id="12443")
    verify_request_count(test_id, "POST", "/maintenance/work-orders", None, 1)


def test_workOrders_delete_work_orders() -> None:
    """Test deleteWorkOrders endpoint with WireMock"""
    test_id = "work_orders.delete_work_orders.0"
    client = get_client(test_id)
    client.work_orders.delete_work_orders(id="id")
    verify_request_count(test_id, "DELETE", "/maintenance/work-orders", {"id": "id"}, 1)


def test_workOrders_patch_work_orders() -> None:
    """Test patchWorkOrders endpoint with WireMock"""
    test_id = "work_orders.patch_work_orders.0"
    client = get_client(test_id)
    client.work_orders.patch_work_orders(id="5")
    verify_request_count(test_id, "PATCH", "/maintenance/work-orders", None, 1)


def test_workOrders_stream_work_orders() -> None:
    """Test streamWorkOrders endpoint with WireMock"""
    test_id = "work_orders.stream_work_orders.0"
    client = get_client(test_id)
    client.work_orders.stream_work_orders(start_time="startTime")
    verify_request_count(test_id, "GET", "/maintenance/work-orders/stream", {"startTime": "startTime"}, 1)
