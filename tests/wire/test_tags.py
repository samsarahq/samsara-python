from .conftest import get_client, verify_request_count


def test_tags_list_tags() -> None:
    """Test listTags endpoint with WireMock"""
    test_id = "tags.list_tags.0"
    client = get_client(test_id)
    client.tags.list_tags()
    verify_request_count(test_id, "GET", "/tags", None, 1)


def test_tags_create_tag() -> None:
    """Test createTag endpoint with WireMock"""
    test_id = "tags.create_tag.0"
    client = get_client(test_id)
    client.tags.create_tag(name="California")
    verify_request_count(test_id, "POST", "/tags", None, 1)


def test_tags_get_tag() -> None:
    """Test getTag endpoint with WireMock"""
    test_id = "tags.get_tag.0"
    client = get_client(test_id)
    client.tags.get_tag(id="id")
    verify_request_count(test_id, "GET", "/tags/id", None, 1)


def test_tags_replace_tag() -> None:
    """Test replaceTag endpoint with WireMock"""
    test_id = "tags.replace_tag.0"
    client = get_client(test_id)
    client.tags.replace_tag(id="id")
    verify_request_count(test_id, "PUT", "/tags/id", None, 1)


def test_tags_delete_tag() -> None:
    """Test deleteTag endpoint with WireMock"""
    test_id = "tags.delete_tag.0"
    client = get_client(test_id)
    client.tags.delete_tag(id="id")
    verify_request_count(test_id, "DELETE", "/tags/id", None, 1)


def test_tags_patch_tag() -> None:
    """Test patchTag endpoint with WireMock"""
    test_id = "tags.patch_tag.0"
    client = get_client(test_id)
    client.tags.patch_tag(id="id")
    verify_request_count(test_id, "PATCH", "/tags/id", None, 1)
