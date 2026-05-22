from .conftest import get_client, verify_request_count


def test_media_list_uploaded_media() -> None:
    """Test listUploadedMedia endpoint with WireMock"""
    test_id = "media.list_uploaded_media.0"
    client = get_client(test_id)
    client.media.list_uploaded_media(vehicle_ids="vehicleIds", start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id,
        "GET",
        "/cameras/media",
        {"vehicleIds": "vehicleIds", "startTime": "startTime", "endTime": "endTime"},
        1,
    )


def test_media_get_media_retrieval() -> None:
    """Test getMediaRetrieval endpoint with WireMock"""
    test_id = "media.get_media_retrieval.0"
    client = get_client(test_id)
    client.media.get_media_retrieval(retrieval_id="retrievalId")
    verify_request_count(test_id, "GET", "/cameras/media/retrieval", {"retrievalId": "retrievalId"}, 1)


def test_media_post_media_retrieval() -> None:
    """Test postMediaRetrieval endpoint with WireMock"""
    test_id = "media.post_media_retrieval.0"
    client = get_client(test_id)
    client.media.post_media_retrieval(
        end_time="2019-06-13T19:08:55Z",
        inputs=["dashcamRoadFacing", "dashcamRoadFacing", "dashcamRoadFacing"],
        media_type="image",
        start_time="2019-06-13T19:08:25Z",
        vehicle_id="1234",
    )
    verify_request_count(test_id, "POST", "/cameras/media/retrieval", None, 1)
