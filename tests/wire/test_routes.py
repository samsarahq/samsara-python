from .conftest import get_client, verify_request_count


def test_routes_fetch_routes() -> None:
    """Test fetchRoutes endpoint with WireMock"""
    test_id = "routes.fetch_routes.0"
    client = get_client(test_id)
    client.routes.fetch_routes(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/routes", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_routes_create_route() -> None:
    """Test createRoute endpoint with WireMock"""
    test_id = "routes.create_route.0"
    client = get_client(test_id)
    client.routes.create_route(name="Bid 123", stops=[{}])
    verify_request_count(test_id, "POST", "/fleet/routes", None, 1)


def test_routes_get_routes_feed() -> None:
    """Test getRoutesFeed endpoint with WireMock"""
    test_id = "routes.get_routes_feed.0"
    client = get_client(test_id)
    client.routes.get_routes_feed()
    verify_request_count(test_id, "GET", "/fleet/routes/audit-logs/feed", None, 1)


def test_routes_fetch_route() -> None:
    """Test fetchRoute endpoint with WireMock"""
    test_id = "routes.fetch_route.0"
    client = get_client(test_id)
    client.routes.fetch_route(id="id")
    verify_request_count(test_id, "GET", "/fleet/routes/id", None, 1)


def test_routes_delete_route() -> None:
    """Test deleteRoute endpoint with WireMock"""
    test_id = "routes.delete_route.0"
    client = get_client(test_id)
    client.routes.delete_route(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/routes/id", None, 1)


def test_routes_patch_route() -> None:
    """Test patchRoute endpoint with WireMock"""
    test_id = "routes.patch_route.0"
    client = get_client(test_id)
    client.routes.patch_route(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/routes/id", None, 1)


def test_routes_list_hub_plan_routes() -> None:
    """Test listHubPlanRoutes endpoint with WireMock"""
    test_id = "routes.list_hub_plan_routes.0"
    client = get_client(test_id)
    client.routes.list_hub_plan_routes(plan_id="planId")
    verify_request_count(test_id, "GET", "/hub/plan/routes", {"planId": "planId"}, 1)


def test_routes_v_1_delete_dispatch_route_by_id() -> None:
    """Test V1deleteDispatchRouteById endpoint with WireMock"""
    test_id = "routes.v_1_delete_dispatch_route_by_id.0"
    client = get_client(test_id)
    client.routes.v_1_delete_dispatch_route_by_id(route_id_or_external_id="route_id_or_external_id")
    verify_request_count(test_id, "DELETE", "/v1/fleet/dispatch/routes/route_id_or_external_id", None, 1)
