from .conftest import get_client, verify_request_count


def test_trainingAssignments_post_training_assignments() -> None:
    """Test postTrainingAssignments endpoint with WireMock"""
    test_id = "training_assignments.post_training_assignments.0"
    client = get_client(test_id)
    client.training_assignments.post_training_assignments(course_id="courseId", due_at_time="dueAtTime")
    verify_request_count(
        test_id, "POST", "/training-assignments", {"courseId": "courseId", "dueAtTime": "dueAtTime"}, 1
    )


def test_trainingAssignments_delete_training_assignments() -> None:
    """Test deleteTrainingAssignments endpoint with WireMock"""
    test_id = "training_assignments.delete_training_assignments.0"
    client = get_client(test_id)
    client.training_assignments.delete_training_assignments()
    verify_request_count(test_id, "DELETE", "/training-assignments", None, 1)


def test_trainingAssignments_patch_training_assignments() -> None:
    """Test patchTrainingAssignments endpoint with WireMock"""
    test_id = "training_assignments.patch_training_assignments.0"
    client = get_client(test_id)
    client.training_assignments.patch_training_assignments(due_at_time="dueAtTime")
    verify_request_count(test_id, "PATCH", "/training-assignments", {"dueAtTime": "dueAtTime"}, 1)


def test_trainingAssignments_get_training_assignments_stream() -> None:
    """Test getTrainingAssignmentsStream endpoint with WireMock"""
    test_id = "training_assignments.get_training_assignments_stream.0"
    client = get_client(test_id)
    client.training_assignments.get_training_assignments_stream(start_time="startTime")
    verify_request_count(test_id, "GET", "/training-assignments/stream", {"startTime": "startTime"}, 1)
