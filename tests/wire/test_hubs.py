from .conftest import get_client, verify_request_count


def test_hubs_list_hub_capacities() -> None:
    """Test listHubCapacities endpoint with WireMock"""
    test_id = "hubs.list_hub_capacities.0"
    client = get_client(test_id)
    client.hubs.list_hub_capacities(hub_id="hubId")
    verify_request_count(test_id, "GET", "/hub/capacities", {"hubId": "hubId"}, 1)


def test_hubs_update_hub_location() -> None:
    """Test updateHubLocation endpoint with WireMock"""
    test_id = "hubs.update_hub_location.0"
    client = get_client(test_id)
    client.hubs.update_hub_location(
        id="id",
        data={
            "address": "123 Industrial Blvd, Los Angeles, CA 90210, US",
            "customer_location_id": "LOC-123",
            "driver_instructions": "sample instructions",
            "is_depot": False,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "name": "Customer ABC Warehouse",
            "planner_notes": "sample note",
            "service_time_seconds": 1800,
            "service_windows": [
                {
                    "days_of_week": ["monday", "tuesday", "wednesday", "thursday", "friday"],
                    "end_time": "17:00:00",
                    "start_time": "08:00:00",
                }
            ],
            "skills_required": ["650e8400-e29b-41d4-a716-446655440001"],
        },
    )
    verify_request_count(test_id, "PATCH", "/hub/location/id", None, 1)


def test_hubs_list_hub_locations() -> None:
    """Test listHubLocations endpoint with WireMock"""
    test_id = "hubs.list_hub_locations.0"
    client = get_client(test_id)
    client.hubs.list_hub_locations(hub_id="hubId")
    verify_request_count(test_id, "GET", "/hub/locations", {"hubId": "hubId"}, 1)


def test_hubs_create_hub_locations() -> None:
    """Test createHubLocations endpoint with WireMock"""
    test_id = "hubs.create_hub_locations.0"
    client = get_client(test_id)
    client.hubs.create_hub_locations(
        data=[
            {
                "address": "123 Industrial Blvd, Los Angeles, CA 90210, US",
                "customer_location_id": "LOC-123",
                "driver_instructions": "sample instructions",
                "hub_id": "550e8400-e29b-41d4-a716-446655440000",
                "is_depot": False,
                "latitude": 34.0522,
                "longitude": -118.2437,
                "name": "Customer ABC Warehouse",
                "planner_notes": "sample note",
                "service_time_seconds": 1800,
                "service_windows": [
                    {
                        "days_of_week": ["monday", "tuesday", "wednesday", "thursday", "friday"],
                        "end_time": "17:00:00",
                        "start_time": "08:00:00",
                    }
                ],
                "skills_required": ["650e8400-e29b-41d4-a716-446655440001"],
            }
        ]
    )
    verify_request_count(test_id, "POST", "/hub/locations", None, 1)


def test_hubs_list_hub_skills() -> None:
    """Test listHubSkills endpoint with WireMock"""
    test_id = "hubs.list_hub_skills.0"
    client = get_client(test_id)
    client.hubs.list_hub_skills(hub_id="hubId")
    verify_request_count(test_id, "GET", "/hub/skills", {"hubId": "hubId"}, 1)


def test_hubs_list_hubs() -> None:
    """Test listHubs endpoint with WireMock"""
    test_id = "hubs.list_hubs.0"
    client = get_client(test_id)
    client.hubs.list_hubs()
    verify_request_count(test_id, "GET", "/hubs", None, 1)
