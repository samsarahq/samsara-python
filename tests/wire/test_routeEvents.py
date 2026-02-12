from .conftest import get_client, verify_request_count


def test_routeEvents_get_route_events_stream() -> None:
    """Test getRouteEventsStream endpoint with WireMock"""
    test_id = "route_events.get_route_events_stream.0"
    client = get_client(test_id)
    client.route_events.get_route_events_stream()
    verify_request_count(test_id, "GET", "/route-events/stream", None, 1)
