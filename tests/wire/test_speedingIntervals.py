from .conftest import get_client, verify_request_count


def test_speedingIntervals_get_speeding_intervals() -> None:
    """Test getSpeedingIntervals endpoint with WireMock"""
    test_id = "speeding_intervals.get_speeding_intervals.0"
    client = get_client(test_id)
    client.speeding_intervals.get_speeding_intervals(asset_ids=["assetIds"], start_time="startTime")
    verify_request_count(
        test_id, "GET", "/speeding-intervals/stream", {"assetIds": "assetIds", "startTime": "startTime"}, 1
    )
