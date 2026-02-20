from .conftest import get_client, verify_request_count


def test_forms_get_form_submissions() -> None:
    """Test getFormSubmissions endpoint with WireMock"""
    test_id = "forms.get_form_submissions.0"
    client = get_client(test_id)
    client.forms.get_form_submissions()
    verify_request_count(test_id, "GET", "/form-submissions", None, 1)


def test_forms_post_form_submission() -> None:
    """Test postFormSubmission endpoint with WireMock"""
    test_id = "forms.post_form_submission.0"
    client = get_client(test_id)
    client.forms.post_form_submission(
        form_template={
            "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        }
    )
    verify_request_count(test_id, "POST", "/form-submissions", None, 1)


def test_forms_patch_form_submission() -> None:
    """Test patchFormSubmission endpoint with WireMock"""
    test_id = "forms.patch_form_submission.0"
    client = get_client(test_id)
    client.forms.patch_form_submission(id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac8", status="notStarted")
    verify_request_count(test_id, "PATCH", "/form-submissions", None, 1)


def test_forms_get_form_submissions_pdf_exports() -> None:
    """Test getFormSubmissionsPdfExports endpoint with WireMock"""
    test_id = "forms.get_form_submissions_pdf_exports.0"
    client = get_client(test_id)
    client.forms.get_form_submissions_pdf_exports(pdf_id="pdfId")
    verify_request_count(test_id, "GET", "/form-submissions/pdf-exports", {"pdfId": "pdfId"}, 1)


def test_forms_post_form_submissions_pdf_exports() -> None:
    """Test postFormSubmissionsPdfExports endpoint with WireMock"""
    test_id = "forms.post_form_submissions_pdf_exports.0"
    client = get_client(test_id)
    client.forms.post_form_submissions_pdf_exports(id="id")
    verify_request_count(test_id, "POST", "/form-submissions/pdf-exports", {"id": "id"}, 1)


def test_forms_get_form_submissions_stream() -> None:
    """Test getFormSubmissionsStream endpoint with WireMock"""
    test_id = "forms.get_form_submissions_stream.0"
    client = get_client(test_id)
    client.forms.get_form_submissions_stream(start_time="startTime")
    verify_request_count(test_id, "GET", "/form-submissions/stream", {"startTime": "startTime"}, 1)


def test_forms_get_form_templates() -> None:
    """Test getFormTemplates endpoint with WireMock"""
    test_id = "forms.get_form_templates.0"
    client = get_client(test_id)
    client.forms.get_form_templates()
    verify_request_count(test_id, "GET", "/form-templates", None, 1)
