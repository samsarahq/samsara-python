from .conftest import get_client, verify_request_count


def test_users_list_user_roles() -> None:
    """Test listUserRoles endpoint with WireMock"""
    test_id = "users.list_user_roles.0"
    client = get_client(test_id)
    client.users.list_user_roles()
    verify_request_count(test_id, "GET", "/user-roles", None, 1)


def test_users_list_users() -> None:
    """Test listUsers endpoint with WireMock"""
    test_id = "users.list_users.0"
    client = get_client(test_id)
    client.users.list_users()
    verify_request_count(test_id, "GET", "/users", None, 1)


def test_users_create_user() -> None:
    """Test createUser endpoint with WireMock"""
    test_id = "users.create_user.0"
    client = get_client(test_id)
    client.users.create_user(
        auth_type="default",
        email="user@company.com",
        name="Bob Smith",
        roles=[{"role_id": "8a9371af-82d1-4158-bf91-4ecc8d3a114c"}],
    )
    verify_request_count(test_id, "POST", "/users", None, 1)


def test_users_get_user() -> None:
    """Test getUser endpoint with WireMock"""
    test_id = "users.get_user.0"
    client = get_client(test_id)
    client.users.get_user(id="id")
    verify_request_count(test_id, "GET", "/users/id", None, 1)


def test_users_delete_user() -> None:
    """Test deleteUser endpoint with WireMock"""
    test_id = "users.delete_user.0"
    client = get_client(test_id)
    client.users.delete_user(id="id")
    verify_request_count(test_id, "DELETE", "/users/id", None, 1)


def test_users_update_user() -> None:
    """Test updateUser endpoint with WireMock"""
    test_id = "users.update_user.0"
    client = get_client(test_id)
    client.users.update_user(id="id")
    verify_request_count(test_id, "PATCH", "/users/id", None, 1)
