from .conftest import get_client, verify_request_count


def test_industrial_get_industrial_assets() -> None:
    """Test getIndustrialAssets endpoint with WireMock"""
    test_id = "industrial.get_industrial_assets.0"
    client = get_client(test_id)
    client.industrial.get_industrial_assets()
    verify_request_count(test_id, "GET", "/industrial/assets", None, 1)


def test_industrial_create_industrial_asset() -> None:
    """Test createIndustrialAsset endpoint with WireMock"""
    test_id = "industrial.create_industrial_asset.0"
    client = get_client(test_id)
    client.industrial.create_industrial_asset(name="name")
    verify_request_count(test_id, "POST", "/industrial/assets", None, 1)


def test_industrial_delete_industrial_asset() -> None:
    """Test deleteIndustrialAsset endpoint with WireMock"""
    test_id = "industrial.delete_industrial_asset.0"
    client = get_client(test_id)
    client.industrial.delete_industrial_asset(id="id")
    verify_request_count(test_id, "DELETE", "/industrial/assets/id", None, 1)


def test_industrial_patch_industrial_asset() -> None:
    """Test patchIndustrialAsset endpoint with WireMock"""
    test_id = "industrial.patch_industrial_asset.0"
    client = get_client(test_id)
    client.industrial.patch_industrial_asset(id="id")
    verify_request_count(test_id, "PATCH", "/industrial/assets/id", None, 1)


def test_industrial_patch_asset_data_outputs() -> None:
    """Test patchAssetDataOutputs endpoint with WireMock"""
    test_id = "industrial.patch_asset_data_outputs.0"
    client = get_client(test_id)
    client.industrial.patch_asset_data_outputs(id="id", values={"key": "value"})
    verify_request_count(test_id, "PATCH", "/industrial/assets/id/data-outputs", None, 1)


def test_industrial_get_data_inputs() -> None:
    """Test getDataInputs endpoint with WireMock"""
    test_id = "industrial.get_data_inputs.0"
    client = get_client(test_id)
    client.industrial.get_data_inputs()
    verify_request_count(test_id, "GET", "/industrial/data-inputs", None, 1)


def test_industrial_get_data_input_data_snapshot() -> None:
    """Test getDataInputDataSnapshot endpoint with WireMock"""
    test_id = "industrial.get_data_input_data_snapshot.0"
    client = get_client(test_id)
    client.industrial.get_data_input_data_snapshot()
    verify_request_count(test_id, "GET", "/industrial/data-inputs/data-points", None, 1)


def test_industrial_get_data_input_data_feed() -> None:
    """Test getDataInputDataFeed endpoint with WireMock"""
    test_id = "industrial.get_data_input_data_feed.0"
    client = get_client(test_id)
    client.industrial.get_data_input_data_feed()
    verify_request_count(test_id, "GET", "/industrial/data-inputs/data-points/feed", None, 1)


def test_industrial_get_data_input_data_history() -> None:
    """Test getDataInputDataHistory endpoint with WireMock"""
    test_id = "industrial.get_data_input_data_history.0"
    client = get_client(test_id)
    client.industrial.get_data_input_data_history(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id,
        "GET",
        "/industrial/data-inputs/data-points/history",
        {"startTime": "startTime", "endTime": "endTime"},
        1,
    )


def test_industrial_v_1_get_cameras() -> None:
    """Test V1getCameras endpoint with WireMock"""
    test_id = "industrial.v_1_get_cameras.0"
    client = get_client(test_id)
    client.industrial.v_1_get_cameras()
    verify_request_count(test_id, "GET", "/v1/industrial/vision/cameras", None, 1)


def test_industrial_v_1_get_vision_programs_by_camera() -> None:
    """Test V1getVisionProgramsByCamera endpoint with WireMock"""
    test_id = "industrial.v_1_get_vision_programs_by_camera.0"
    client = get_client(test_id)
    client.industrial.v_1_get_vision_programs_by_camera(camera_id=1000000)
    verify_request_count(test_id, "GET", "/v1/industrial/vision/cameras/1000000/programs", None, 1)


def test_industrial_v_1_get_vision_latest_run_camera() -> None:
    """Test V1getVisionLatestRunCamera endpoint with WireMock"""
    test_id = "industrial.v_1_get_vision_latest_run_camera.0"
    client = get_client(test_id)
    client.industrial.v_1_get_vision_latest_run_camera(camera_id=1000000)
    verify_request_count(test_id, "GET", "/v1/industrial/vision/run/camera/1000000", None, 1)


def test_industrial_v_1_get_vision_runs() -> None:
    """Test V1getVisionRuns endpoint with WireMock"""
    test_id = "industrial.v_1_get_vision_runs.0"
    client = get_client(test_id)
    client.industrial.v_1_get_vision_runs(duration_ms=1000000)
    verify_request_count(test_id, "GET", "/v1/industrial/vision/runs", {"durationMs": "1000000"}, 1)


def test_industrial_get_vision_runs_by_camera() -> None:
    """Test getVisionRunsByCamera endpoint with WireMock"""
    test_id = "industrial.get_vision_runs_by_camera.0"
    client = get_client(test_id)
    client.industrial.get_vision_runs_by_camera(camera_id=1000000, duration_ms=1000000)
    verify_request_count(test_id, "GET", "/v1/industrial/vision/runs/1000000", {"durationMs": "1000000"}, 1)


def test_industrial_v_1_get_vision_runs_by_camera_and_program() -> None:
    """Test V1getVisionRunsByCameraAndProgram endpoint with WireMock"""
    test_id = "industrial.v_1_get_vision_runs_by_camera_and_program.0"
    client = get_client(test_id)
    client.industrial.v_1_get_vision_runs_by_camera_and_program(
        camera_id=1000000, program_id=1000000, started_at_ms=1000000
    )
    verify_request_count(test_id, "GET", "/v1/industrial/vision/runs/1000000/1000000/1000000", None, 1)


def test_industrial_v_1_get_machines_history() -> None:
    """Test V1getMachinesHistory endpoint with WireMock"""
    test_id = "industrial.v_1_get_machines_history.0"
    client = get_client(test_id)
    client.industrial.v_1_get_machines_history(end_ms=1462881998034, start_ms=1462878398034)
    verify_request_count(test_id, "POST", "/v1/machines/history", None, 1)


def test_industrial_v_1_get_machines() -> None:
    """Test V1getMachines endpoint with WireMock"""
    test_id = "industrial.v_1_get_machines.0"
    client = get_client(test_id)
    client.industrial.v_1_get_machines()
    verify_request_count(test_id, "POST", "/v1/machines/list", None, 1)
