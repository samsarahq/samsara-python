from .conftest import get_client, verify_request_count


def test_issues_get_issues() -> None:
    """Test getIssues endpoint with WireMock"""
    test_id = "issues.get_issues.0"
    client = get_client(test_id)
    client.issues.get_issues()
    verify_request_count(test_id, "GET", "/issues", None, 1)


def test_issues_patch_issue() -> None:
    """Test patchIssue endpoint with WireMock"""
    test_id = "issues.patch_issue.0"
    client = get_client(test_id)
    client.issues.patch_issue(id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7")
    verify_request_count(test_id, "PATCH", "/issues", None, 1)


def test_issues_get_issues_stream() -> None:
    """Test getIssuesStream endpoint with WireMock"""
    test_id = "issues.get_issues_stream.0"
    client = get_client(test_id)
    client.issues.get_issues_stream(start_time="startTime")
    verify_request_count(test_id, "GET", "/issues/stream", {"startTime": "startTime"}, 1)
