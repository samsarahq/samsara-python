from .conftest import get_client, verify_request_count


def test_trailers_list_trailers() -> None:
    """Test listTrailers endpoint with WireMock"""
    test_id = "trailers.list_trailers.0"
    client = get_client(test_id)
    client.trailers.list_trailers()
    verify_request_count(test_id, "GET", "/fleet/trailers", None, 1)


def test_trailers_create_trailer() -> None:
    """Test createTrailer endpoint with WireMock"""
    test_id = "trailers.create_trailer.0"
    client = get_client(test_id)
    client.trailers.create_trailer(name="Trailer-123")
    verify_request_count(test_id, "POST", "/fleet/trailers", None, 1)


def test_trailers_get_trailer_stats_snapshot() -> None:
    """Test getTrailerStatsSnapshot endpoint with WireMock"""
    test_id = "trailers.get_trailer_stats_snapshot.0"
    client = get_client(test_id)
    client.trailers.get_trailer_stats_snapshot(types="types")
    verify_request_count(test_id, "GET", "/fleet/trailers/stats", {"types": "types"}, 1)


def test_trailers_get_trailer_stats_feed() -> None:
    """Test getTrailerStatsFeed endpoint with WireMock"""
    test_id = "trailers.get_trailer_stats_feed.0"
    client = get_client(test_id)
    client.trailers.get_trailer_stats_feed(types="types")
    verify_request_count(test_id, "GET", "/fleet/trailers/stats/feed", {"types": "types"}, 1)


def test_trailers_get_trailer_stats_history() -> None:
    """Test getTrailerStatsHistory endpoint with WireMock"""
    test_id = "trailers.get_trailer_stats_history.0"
    client = get_client(test_id)
    client.trailers.get_trailer_stats_history(start_time="startTime", end_time="endTime", types="types")
    verify_request_count(
        test_id,
        "GET",
        "/fleet/trailers/stats/history",
        {"startTime": "startTime", "endTime": "endTime", "types": "types"},
        1,
    )


def test_trailers_get_trailer() -> None:
    """Test getTrailer endpoint with WireMock"""
    test_id = "trailers.get_trailer.0"
    client = get_client(test_id)
    client.trailers.get_trailer(id="id")
    verify_request_count(test_id, "GET", "/fleet/trailers/id", None, 1)


def test_trailers_delete_trailer() -> None:
    """Test deleteTrailer endpoint with WireMock"""
    test_id = "trailers.delete_trailer.0"
    client = get_client(test_id)
    client.trailers.delete_trailer(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/trailers/id", None, 1)


def test_trailers_update_trailer() -> None:
    """Test updateTrailer endpoint with WireMock"""
    test_id = "trailers.update_trailer.0"
    client = get_client(test_id)
    client.trailers.update_trailer(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/trailers/id", None, 1)
