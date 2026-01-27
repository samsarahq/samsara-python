from datetime import datetime

from .conftest import get_client, verify_request_count


def test_betaApIs_get_depreciation_transactions() -> None:
    """Test getDepreciationTransactions endpoint with WireMock"""
    test_id = "beta_ap_is.get_depreciation_transactions.0"
    client = get_client(test_id)
    client.beta_ap_is.get_depreciation_transactions()
    verify_request_count(test_id, "GET", "/assets/depreciation", None, 1)


def test_betaApIs_get_assets_inputs() -> None:
    """Test getAssetsInputs endpoint with WireMock"""
    test_id = "beta_ap_is.get_assets_inputs.0"
    client = get_client(test_id)
    client.beta_ap_is.get_assets_inputs(type="auxInput1", start_time="startTime")
    verify_request_count(test_id, "GET", "/assets/inputs/stream", {"type": "auxInput1", "startTime": "startTime"}, 1)


def test_betaApIs_get_aemp_equipment_list() -> None:
    """Test getAempEquipmentList endpoint with WireMock"""
    test_id = "beta_ap_is.get_aemp_equipment_list.0"
    client = get_client(test_id)
    client.beta_ap_is.get_aemp_equipment_list(page_number="pageNumber")
    verify_request_count(test_id, "GET", "/beta/aemp/Fleet/pageNumber", None, 1)


def test_betaApIs_get_driver_efficiency() -> None:
    """Test getDriverEfficiency endpoint with WireMock"""
    test_id = "beta_ap_is.get_driver_efficiency.0"
    client = get_client(test_id)
    client.beta_ap_is.get_driver_efficiency()
    verify_request_count(test_id, "GET", "/beta/fleet/drivers/efficiency", None, 1)


def test_betaApIs_patch_equipment() -> None:
    """Test patchEquipment endpoint with WireMock"""
    test_id = "beta_ap_is.patch_equipment.0"
    client = get_client(test_id)
    client.beta_ap_is.patch_equipment(id="id")
    verify_request_count(test_id, "PATCH", "/beta/fleet/equipment/id", None, 1)


def test_betaApIs_get_hos_eld_events() -> None:
    """Test getHosEldEvents endpoint with WireMock"""
    test_id = "beta_ap_is.get_hos_eld_events.0"
    client = get_client(test_id)
    client.beta_ap_is.get_hos_eld_events(start_time="startTime", end_time="endTime")
    verify_request_count(
        test_id, "GET", "/beta/fleet/hos/drivers/eld-events", {"startTime": "startTime", "endTime": "endTime"}, 1
    )


def test_betaApIs_get_trailer_stats_snapshot() -> None:
    """Test getTrailerStatsSnapshot endpoint with WireMock"""
    test_id = "beta_ap_is.get_trailer_stats_snapshot.0"
    client = get_client(test_id)
    client.beta_ap_is.get_trailer_stats_snapshot(types="types")
    verify_request_count(test_id, "GET", "/beta/fleet/trailers/stats", {"types": "types"}, 1)


def test_betaApIs_get_trailer_stats_feed() -> None:
    """Test getTrailerStatsFeed endpoint with WireMock"""
    test_id = "beta_ap_is.get_trailer_stats_feed.0"
    client = get_client(test_id)
    client.beta_ap_is.get_trailer_stats_feed(types="types")
    verify_request_count(test_id, "GET", "/beta/fleet/trailers/stats/feed", {"types": "types"}, 1)


def test_betaApIs_get_trailer_stats_history() -> None:
    """Test getTrailerStatsHistory endpoint with WireMock"""
    test_id = "beta_ap_is.get_trailer_stats_history.0"
    client = get_client(test_id)
    client.beta_ap_is.get_trailer_stats_history(start_time="startTime", end_time="endTime", types="types")
    verify_request_count(
        test_id,
        "GET",
        "/beta/fleet/trailers/stats/history",
        {"startTime": "startTime", "endTime": "endTime", "types": "types"},
        1,
    )


def test_betaApIs_update_engine_immobilizer_state() -> None:
    """Test updateEngineImmobilizerState endpoint with WireMock"""
    test_id = "beta_ap_is.update_engine_immobilizer_state.0"
    client = get_client(test_id)
    client.beta_ap_is.update_engine_immobilizer_state(id=1000000, relay_states=[{"id": "relay1", "is_open": True}])
    verify_request_count(test_id, "PATCH", "/beta/fleet/vehicles/1000000/immobilizer", None, 1)


def test_betaApIs_get_jobs() -> None:
    """Test getJobs endpoint with WireMock"""
    test_id = "beta_ap_is.get_jobs.0"
    client = get_client(test_id)
    client.beta_ap_is.get_jobs()
    verify_request_count(test_id, "GET", "/beta/industrial/jobs", None, 1)


def test_betaApIs_create_job() -> None:
    """Test createJob endpoint with WireMock"""
    test_id = "beta_ap_is.create_job.0"
    client = get_client(test_id)
    client.beta_ap_is.create_job(
        job={
            "end_date": "2019-06-13T19:08:25Z",
            "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
            "name": "My Job Name",
            "start_date": "2019-06-13T19:08:25Z",
        }
    )
    verify_request_count(test_id, "POST", "/beta/industrial/jobs", None, 1)


def test_betaApIs_delete_job() -> None:
    """Test deleteJob endpoint with WireMock"""
    test_id = "beta_ap_is.delete_job.0"
    client = get_client(test_id)
    client.beta_ap_is.delete_job(id="id")
    verify_request_count(test_id, "DELETE", "/beta/industrial/jobs", {"id": "id"}, 1)


def test_betaApIs_patch_job() -> None:
    """Test patchJob endpoint with WireMock"""
    test_id = "beta_ap_is.patch_job.0"
    client = get_client(test_id)
    client.beta_ap_is.patch_job(id="id", job={})
    verify_request_count(test_id, "PATCH", "/beta/industrial/jobs", {"id": "id"}, 1)


def test_betaApIs_get_detections() -> None:
    """Test getDetections endpoint with WireMock"""
    test_id = "beta_ap_is.get_detections.0"
    client = get_client(test_id)
    client.beta_ap_is.get_detections(start_time="startTime")
    verify_request_count(test_id, "GET", "/detections/stream", {"startTime": "startTime"}, 1)


def test_betaApIs_get_devices() -> None:
    """Test getDevices endpoint with WireMock"""
    test_id = "beta_ap_is.get_devices.0"
    client = get_client(test_id)
    client.beta_ap_is.get_devices()
    verify_request_count(test_id, "GET", "/devices", None, 1)


def test_betaApIs_get_engine_immobilizer_states() -> None:
    """Test getEngineImmobilizerStates endpoint with WireMock"""
    test_id = "beta_ap_is.get_engine_immobilizer_states.0"
    client = get_client(test_id)
    client.beta_ap_is.get_engine_immobilizer_states(vehicle_ids="vehicleIds", start_time="startTime")
    verify_request_count(
        test_id, "GET", "/fleet/vehicles/immobilizer/stream", {"vehicleIds": "vehicleIds", "startTime": "startTime"}, 1
    )


def test_betaApIs_start_function_run() -> None:
    """Test startFunctionRun endpoint with WireMock"""
    test_id = "beta_ap_is.start_function_run.0"
    client = get_client(test_id)
    client.beta_ap_is.start_function_run(name="name", params_override={})
    verify_request_count(test_id, "POST", "/functions/name/runs", None, 1)


def test_betaApIs_update_shipping_docs() -> None:
    """Test updateShippingDocs endpoint with WireMock"""
    test_id = "beta_ap_is.update_shipping_docs.0"
    client = get_client(test_id)
    client.beta_ap_is.update_shipping_docs(
        hos_date="hosDate", driver_id="driverID", shipping_docs="ShippingID1, ShippingID2"
    )
    verify_request_count(
        test_id, "PATCH", "/hos/daily-logs/log-meta-data", {"hosDate": "hosDate", "driverID": "driverID"}, 1
    )


def test_betaApIs_list_hub_custom_properties() -> None:
    """Test listHubCustomProperties endpoint with WireMock"""
    test_id = "beta_ap_is.list_hub_custom_properties.0"
    client = get_client(test_id)
    client.beta_ap_is.list_hub_custom_properties(hub_id="hubId")
    verify_request_count(test_id, "GET", "/hub/customProperties", {"hubId": "hubId"}, 1)


def test_betaApIs_create_plan_orders() -> None:
    """Test createPlanOrders endpoint with WireMock"""
    test_id = "beta_ap_is.create_plan_orders.0"
    client = get_client(test_id)
    client.beta_ap_is.create_plan_orders(
        data=[
            {
                "customer_order_id": "ORDER-2024-001",
                "hub_id": "550e8400-e29b-41d4-a716-446655440000",
                "plan_id": "650e8400-e29b-41d4-a716-446655440023",
            }
        ]
    )
    verify_request_count(test_id, "POST", "/hub/plan/orders", None, 1)


def test_betaApIs_get_qualification_records() -> None:
    """Test getQualificationRecords endpoint with WireMock"""
    test_id = "beta_ap_is.get_qualification_records.0"
    client = get_client(test_id)
    client.beta_ap_is.get_qualification_records()
    verify_request_count(test_id, "GET", "/qualification-records", None, 1)


def test_betaApIs_post_qualification_record() -> None:
    """Test postQualificationRecord endpoint with WireMock"""
    test_id = "beta_ap_is.post_qualification_record.0"
    client = get_client(test_id)
    client.beta_ap_is.post_qualification_record(
        fields=[{"id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7", "type": "number"}],
        issue_date=datetime.fromisoformat("2025-08-27T10:20:30+00:00"),
        owner={"entity_type": "worker", "id": "281474"},
        qualification_type={"id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7"},
    )
    verify_request_count(test_id, "POST", "/qualification-records", None, 1)


def test_betaApIs_delete_qualification_record() -> None:
    """Test deleteQualificationRecord endpoint with WireMock"""
    test_id = "beta_ap_is.delete_qualification_record.0"
    client = get_client(test_id)
    client.beta_ap_is.delete_qualification_record(id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7")
    verify_request_count(test_id, "DELETE", "/qualification-records", None, 1)


def test_betaApIs_patch_qualification_record() -> None:
    """Test patchQualificationRecord endpoint with WireMock"""
    test_id = "beta_ap_is.patch_qualification_record.0"
    client = get_client(test_id)
    client.beta_ap_is.patch_qualification_record(
        id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        issue_date=datetime.fromisoformat("2025-08-27T10:20:30+00:00"),
        owner={"entity_type": "worker", "id": "281474"},
    )
    verify_request_count(test_id, "PATCH", "/qualification-records", None, 1)


def test_betaApIs_archive_qualification_record() -> None:
    """Test archiveQualificationRecord endpoint with WireMock"""
    test_id = "beta_ap_is.archive_qualification_record.0"
    client = get_client(test_id)
    client.beta_ap_is.archive_qualification_record(id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7")
    verify_request_count(test_id, "POST", "/qualification-records/archive", None, 1)


def test_betaApIs_get_qualification_records_stream() -> None:
    """Test getQualificationRecordsStream endpoint with WireMock"""
    test_id = "beta_ap_is.get_qualification_records_stream.0"
    client = get_client(test_id)
    client.beta_ap_is.get_qualification_records_stream(
        entity_type="worker", start_time=datetime.fromisoformat("2024-01-15T09:30:00+00:00")
    )
    verify_request_count(
        test_id,
        "GET",
        "/qualification-records/stream",
        {"entityType": "worker", "startTime": "2024-01-15T09:30:00Z"},
        1,
    )


def test_betaApIs_unarchive_qualification_record() -> None:
    """Test unarchiveQualificationRecord endpoint with WireMock"""
    test_id = "beta_ap_is.unarchive_qualification_record.0"
    client = get_client(test_id)
    client.beta_ap_is.unarchive_qualification_record(id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7")
    verify_request_count(test_id, "POST", "/qualification-records/unarchive", None, 1)


def test_betaApIs_get_qualification_types() -> None:
    """Test getQualificationTypes endpoint with WireMock"""
    test_id = "beta_ap_is.get_qualification_types.0"
    client = get_client(test_id)
    client.beta_ap_is.get_qualification_types(entity_type="worker")
    verify_request_count(test_id, "GET", "/qualification-types", {"entityType": "worker"}, 1)


def test_betaApIs_post_readings() -> None:
    """Test postReadings endpoint with WireMock"""
    test_id = "beta_ap_is.post_readings.0"
    client = get_client(test_id)
    client.beta_ap_is.post_readings(
        data=[
            {
                "entity_id": "123451234512345",
                "entity_type": "asset",
                "happened_at_time": "2023-10-27T10:00:00Z",
                "reading_id": "airInletPressure",
                "value": {"key": "value"},
            }
        ]
    )
    verify_request_count(test_id, "POST", "/readings", None, 1)


def test_betaApIs_list_readings_definitions() -> None:
    """Test listReadingsDefinitions endpoint with WireMock"""
    test_id = "beta_ap_is.list_readings_definitions.0"
    client = get_client(test_id)
    client.beta_ap_is.list_readings_definitions()
    verify_request_count(test_id, "GET", "/readings/definitions", None, 1)


def test_betaApIs_get_readings_history() -> None:
    """Test getReadingsHistory endpoint with WireMock"""
    test_id = "beta_ap_is.get_readings_history.0"
    client = get_client(test_id)
    client.beta_ap_is.get_readings_history(reading_id="readingId", entity_type="entityType")
    verify_request_count(test_id, "GET", "/readings/history", {"readingId": "readingId", "entityType": "entityType"}, 1)


def test_betaApIs_get_readings_snapshot() -> None:
    """Test getReadingsSnapshot endpoint with WireMock"""
    test_id = "beta_ap_is.get_readings_snapshot.0"
    client = get_client(test_id)
    client.beta_ap_is.get_readings_snapshot(reading_ids="readingIds", entity_type="entityType")
    verify_request_count(
        test_id, "GET", "/readings/latest", {"readingIds": "readingIds", "entityType": "entityType"}, 1
    )


def test_betaApIs_get_report_configs() -> None:
    """Test getReportConfigs endpoint with WireMock"""
    test_id = "beta_ap_is.get_report_configs.0"
    client = get_client(test_id)
    client.beta_ap_is.get_report_configs()
    verify_request_count(test_id, "GET", "/reports/configs", None, 1)


def test_betaApIs_get_datasets() -> None:
    """Test getDatasets endpoint with WireMock"""
    test_id = "beta_ap_is.get_datasets.0"
    client = get_client(test_id)
    client.beta_ap_is.get_datasets()
    verify_request_count(test_id, "GET", "/reports/datasets", None, 1)


def test_betaApIs_get_report_runs() -> None:
    """Test getReportRuns endpoint with WireMock"""
    test_id = "beta_ap_is.get_report_runs.0"
    client = get_client(test_id)
    client.beta_ap_is.get_report_runs()
    verify_request_count(test_id, "GET", "/reports/runs", None, 1)


def test_betaApIs_create_report_run() -> None:
    """Test createReportRun endpoint with WireMock"""
    test_id = "beta_ap_is.create_report_run.0"
    client = get_client(test_id)
    client.beta_ap_is.create_report_run(report_config={})
    verify_request_count(test_id, "POST", "/reports/runs", None, 1)


def test_betaApIs_get_report_run_data() -> None:
    """Test getReportRunData endpoint with WireMock"""
    test_id = "beta_ap_is.get_report_run_data.0"
    client = get_client(test_id)
    client.beta_ap_is.get_report_run_data(id="id")
    verify_request_count(test_id, "GET", "/reports/runs/data", {"id": "id"}, 1)


def test_betaApIs_get_driver_safety_scores() -> None:
    """Test getDriverSafetyScores endpoint with WireMock"""
    test_id = "beta_ap_is.get_driver_safety_scores.0"
    client = get_client(test_id)
    client.beta_ap_is.get_driver_safety_scores(end_time="endTime", start_time="startTime")
    verify_request_count(test_id, "GET", "/safety-scores/drivers", {"endTime": "endTime", "startTime": "startTime"}, 1)


def test_betaApIs_get_driver_safety_score_trips() -> None:
    """Test getDriverSafetyScoreTrips endpoint with WireMock"""
    test_id = "beta_ap_is.get_driver_safety_score_trips.0"
    client = get_client(test_id)
    client.beta_ap_is.get_driver_safety_score_trips(end_time="endTime", start_time="startTime")
    verify_request_count(
        test_id, "GET", "/safety-scores/drivers/trips", {"endTime": "endTime", "startTime": "startTime"}, 1
    )


def test_betaApIs_get_tag_group_safety_scores() -> None:
    """Test getTagGroupSafetyScores endpoint with WireMock"""
    test_id = "beta_ap_is.get_tag_group_safety_scores.0"
    client = get_client(test_id)
    client.beta_ap_is.get_tag_group_safety_scores(end_time="endTime", start_time="startTime", score_type="driver")
    verify_request_count(
        test_id,
        "GET",
        "/safety-scores/tag-group",
        {"endTime": "endTime", "startTime": "startTime", "scoreType": "driver"},
        1,
    )


def test_betaApIs_get_tag_safety_scores() -> None:
    """Test getTagSafetyScores endpoint with WireMock"""
    test_id = "beta_ap_is.get_tag_safety_scores.0"
    client = get_client(test_id)
    client.beta_ap_is.get_tag_safety_scores(end_time="endTime", start_time="startTime", score_type="driver")
    verify_request_count(
        test_id,
        "GET",
        "/safety-scores/tags",
        {"endTime": "endTime", "startTime": "startTime", "scoreType": "driver"},
        1,
    )


def test_betaApIs_get_vehicle_safety_scores() -> None:
    """Test getVehicleSafetyScores endpoint with WireMock"""
    test_id = "beta_ap_is.get_vehicle_safety_scores.0"
    client = get_client(test_id)
    client.beta_ap_is.get_vehicle_safety_scores(end_time="endTime", start_time="startTime")
    verify_request_count(test_id, "GET", "/safety-scores/vehicles", {"endTime": "endTime", "startTime": "startTime"}, 1)


def test_betaApIs_get_vehicle_safety_score_trips() -> None:
    """Test getVehicleSafetyScoreTrips endpoint with WireMock"""
    test_id = "beta_ap_is.get_vehicle_safety_score_trips.0"
    client = get_client(test_id)
    client.beta_ap_is.get_vehicle_safety_score_trips(end_time="endTime", start_time="startTime")
    verify_request_count(
        test_id, "GET", "/safety-scores/vehicles/trips", {"endTime": "endTime", "startTime": "startTime"}, 1
    )


def test_betaApIs_post_training_assignments() -> None:
    """Test postTrainingAssignments endpoint with WireMock"""
    test_id = "beta_ap_is.post_training_assignments.0"
    client = get_client(test_id)
    client.beta_ap_is.post_training_assignments(course_id="courseId", due_at_time="dueAtTime")
    verify_request_count(
        test_id, "POST", "/training-assignments", {"courseId": "courseId", "dueAtTime": "dueAtTime"}, 1
    )


def test_betaApIs_delete_training_assignments() -> None:
    """Test deleteTrainingAssignments endpoint with WireMock"""
    test_id = "beta_ap_is.delete_training_assignments.0"
    client = get_client(test_id)
    client.beta_ap_is.delete_training_assignments()
    verify_request_count(test_id, "DELETE", "/training-assignments", None, 1)


def test_betaApIs_patch_training_assignments() -> None:
    """Test patchTrainingAssignments endpoint with WireMock"""
    test_id = "beta_ap_is.patch_training_assignments.0"
    client = get_client(test_id)
    client.beta_ap_is.patch_training_assignments(due_at_time="dueAtTime")
    verify_request_count(test_id, "PATCH", "/training-assignments", {"dueAtTime": "dueAtTime"}, 1)


def test_betaApIs_get_training_assignments_stream() -> None:
    """Test getTrainingAssignmentsStream endpoint with WireMock"""
    test_id = "beta_ap_is.get_training_assignments_stream.0"
    client = get_client(test_id)
    client.beta_ap_is.get_training_assignments_stream(start_time="startTime")
    verify_request_count(test_id, "GET", "/training-assignments/stream", {"startTime": "startTime"}, 1)


def test_betaApIs_get_training_courses() -> None:
    """Test getTrainingCourses endpoint with WireMock"""
    test_id = "beta_ap_is.get_training_courses.0"
    client = get_client(test_id)
    client.beta_ap_is.get_training_courses()
    verify_request_count(test_id, "GET", "/training-courses", None, 1)
