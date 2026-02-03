from .conftest import get_client, verify_request_count


def test_trainingCourses_get_training_courses() -> None:
    """Test getTrainingCourses endpoint with WireMock"""
    test_id = "training_courses.get_training_courses.0"
    client = get_client(test_id)
    client.training_courses.get_training_courses()
    verify_request_count(test_id, "GET", "/training-courses", None, 1)
