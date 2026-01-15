from .conftest import get_client, verify_request_count


def test_contacts_list_contacts() -> None:
    """Test listContacts endpoint with WireMock"""
    test_id = "contacts.list_contacts.0"
    client = get_client(test_id)
    client.contacts.list_contacts()
    verify_request_count(test_id, "GET", "/contacts", None, 1)


def test_contacts_create_contact() -> None:
    """Test createContact endpoint with WireMock"""
    test_id = "contacts.create_contact.0"
    client = get_client(test_id)
    client.contacts.create_contact()
    verify_request_count(test_id, "POST", "/contacts", None, 1)


def test_contacts_get_contact() -> None:
    """Test getContact endpoint with WireMock"""
    test_id = "contacts.get_contact.0"
    client = get_client(test_id)
    client.contacts.get_contact(id="id")
    verify_request_count(test_id, "GET", "/contacts/id", None, 1)


def test_contacts_delete_contact() -> None:
    """Test deleteContact endpoint with WireMock"""
    test_id = "contacts.delete_contact.0"
    client = get_client(test_id)
    client.contacts.delete_contact(id="id")
    verify_request_count(test_id, "DELETE", "/contacts/id", None, 1)


def test_contacts_update_contact() -> None:
    """Test updateContact endpoint with WireMock"""
    test_id = "contacts.update_contact.0"
    client = get_client(test_id)
    client.contacts.update_contact(id="id")
    verify_request_count(test_id, "PATCH", "/contacts/id", None, 1)
