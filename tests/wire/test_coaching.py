from datetime import datetime

from .conftest import get_client, verify_request_count


def test_coaching_get_driver_coach_assignment() -> None:
    """Test getDriverCoachAssignment endpoint with WireMock"""
    test_id = "coaching.get_driver_coach_assignment.0"
    client = get_client(test_id)
    client.coaching.get_driver_coach_assignment()
    verify_request_count(test_id, "GET", "/coaching/driver-coach-assignments", None, 1)


def test_coaching_put_driver_coach_assignment() -> None:
    """Test putDriverCoachAssignment endpoint with WireMock"""
    test_id = "coaching.put_driver_coach_assignment.0"
    client = get_client(test_id)
    client.coaching.put_driver_coach_assignment(driver_id="driverId")
    verify_request_count(test_id, "PUT", "/coaching/driver-coach-assignments", {"driverId": "driverId"}, 1)


def test_coaching_get_coaching_sessions() -> None:
    """Test getCoachingSessions endpoint with WireMock"""
    test_id = "coaching.get_coaching_sessions.0"
    client = get_client(test_id)
    client.coaching.get_coaching_sessions(start_time=datetime.fromisoformat("2024-01-15T09:30:00+00:00"))
    verify_request_count(test_id, "GET", "/coaching/sessions/stream", {"startTime": "2024-01-15T09:30:00Z"}, 1)
