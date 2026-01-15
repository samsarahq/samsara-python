from .conftest import get_client, verify_request_count


def test_documents_get_document_types() -> None:
    """Test getDocumentTypes endpoint with WireMock"""
    test_id = "documents.get_document_types.0"
    client = get_client(test_id)
    client.documents.get_document_types()
    verify_request_count(test_id, "GET", "/fleet/document-types", None, 1)


def test_documents_get_documents() -> None:
    """Test getDocuments endpoint with WireMock"""
    test_id = "documents.get_documents.0"
    client = get_client(test_id)
    client.documents.get_documents(start_time="startTime", end_time="endTime")
    verify_request_count(test_id, "GET", "/fleet/documents", {"startTime": "startTime", "endTime": "endTime"}, 1)


def test_documents_post_document() -> None:
    """Test postDocument endpoint with WireMock"""
    test_id = "documents.post_document.0"
    client = get_client(test_id)
    client.documents.post_document(document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7", driver_id="45646")
    verify_request_count(test_id, "POST", "/fleet/documents", None, 1)


def test_documents_generate_document_pdf() -> None:
    """Test generateDocumentPdf endpoint with WireMock"""
    test_id = "documents.generate_document_pdf.0"
    client = get_client(test_id)
    client.documents.generate_document_pdf(document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb")
    verify_request_count(test_id, "POST", "/fleet/documents/pdfs", None, 1)


def test_documents_get_document_pdf() -> None:
    """Test getDocumentPdf endpoint with WireMock"""
    test_id = "documents.get_document_pdf.0"
    client = get_client(test_id)
    client.documents.get_document_pdf(id="id")
    verify_request_count(test_id, "GET", "/fleet/documents/pdfs/id", None, 1)


def test_documents_get_document() -> None:
    """Test getDocument endpoint with WireMock"""
    test_id = "documents.get_document.0"
    client = get_client(test_id)
    client.documents.get_document(id="id")
    verify_request_count(test_id, "GET", "/fleet/documents/id", None, 1)


def test_documents_delete_document() -> None:
    """Test deleteDocument endpoint with WireMock"""
    test_id = "documents.delete_document.0"
    client = get_client(test_id)
    client.documents.delete_document(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/documents/id", None, 1)
