from .conftest import get_client, verify_request_count


def test_safetyScores_get_driver_safety_scores() -> None:
    """Test getDriverSafetyScores endpoint with WireMock"""
    test_id = "safety_scores.get_driver_safety_scores.0"
    client = get_client(test_id)
    client.safety_scores.get_driver_safety_scores(end_time="endTime", start_time="startTime")
    verify_request_count(test_id, "GET", "/safety-scores/drivers", {"endTime": "endTime", "startTime": "startTime"}, 1)


def test_safetyScores_get_tag_group_safety_scores() -> None:
    """Test getTagGroupSafetyScores endpoint with WireMock"""
    test_id = "safety_scores.get_tag_group_safety_scores.0"
    client = get_client(test_id)
    client.safety_scores.get_tag_group_safety_scores(end_time="endTime", start_time="startTime", score_type="driver")
    verify_request_count(
        test_id,
        "GET",
        "/safety-scores/tag-group",
        {"endTime": "endTime", "startTime": "startTime", "scoreType": "driver"},
        1,
    )


def test_safetyScores_get_tag_safety_scores() -> None:
    """Test getTagSafetyScores endpoint with WireMock"""
    test_id = "safety_scores.get_tag_safety_scores.0"
    client = get_client(test_id)
    client.safety_scores.get_tag_safety_scores(end_time="endTime", start_time="startTime", score_type="driver")
    verify_request_count(
        test_id,
        "GET",
        "/safety-scores/tags",
        {"endTime": "endTime", "startTime": "startTime", "scoreType": "driver"},
        1,
    )


def test_safetyScores_get_vehicle_safety_scores() -> None:
    """Test getVehicleSafetyScores endpoint with WireMock"""
    test_id = "safety_scores.get_vehicle_safety_scores.0"
    client = get_client(test_id)
    client.safety_scores.get_vehicle_safety_scores(end_time="endTime", start_time="startTime")
    verify_request_count(test_id, "GET", "/safety-scores/vehicles", {"endTime": "endTime", "startTime": "startTime"}, 1)
