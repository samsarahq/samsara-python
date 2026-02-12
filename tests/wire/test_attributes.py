from .conftest import get_client, verify_request_count


def test_attributes_get_attributes_by_entity_type() -> None:
    """Test getAttributesByEntityType endpoint with WireMock"""
    test_id = "attributes.get_attributes_by_entity_type.0"
    client = get_client(test_id)
    client.attributes.get_attributes_by_entity_type(entity_type="driver")
    verify_request_count(test_id, "GET", "/attributes", {"entityType": "driver"}, 1)


def test_attributes_create_attribute() -> None:
    """Test createAttribute endpoint with WireMock"""
    test_id = "attributes.create_attribute.0"
    client = get_client(test_id)
    client.attributes.create_attribute(
        attribute_type="single-select", entity_type="driver", name="License Certifications"
    )
    verify_request_count(test_id, "POST", "/attributes", None, 1)


def test_attributes_get_attribute() -> None:
    """Test getAttribute endpoint with WireMock"""
    test_id = "attributes.get_attribute.0"
    client = get_client(test_id)
    client.attributes.get_attribute(id="id", entity_type="driver")
    verify_request_count(test_id, "GET", "/attributes/id", {"entityType": "driver"}, 1)


def test_attributes_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "attributes.delete.0"
    client = get_client(test_id)
    client.attributes.delete(id="id", entity_type="driver")
    verify_request_count(test_id, "DELETE", "/attributes/id", {"entityType": "driver"}, 1)


def test_attributes_update_attribute() -> None:
    """Test updateAttribute endpoint with WireMock"""
    test_id = "attributes.update_attribute.0"
    client = get_client(test_id)
    client.attributes.update_attribute(id="id", entity_type="driver")
    verify_request_count(test_id, "PATCH", "/attributes/id", None, 1)
