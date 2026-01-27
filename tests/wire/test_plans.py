from .conftest import get_client, verify_request_count


def test_plans_create_hub_plan() -> None:
    """Test createHubPlan endpoint with WireMock"""
    test_id = "plans.create_hub_plan.0"
    client = get_client(test_id)
    client.plans.create_hub_plan(hub_id="550e8400-e29b-41d4-a716-446655440000", name="Weekly Plan - Week 15")
    verify_request_count(test_id, "POST", "/hub/plan", None, 1)


def test_plans_list_hub_plans() -> None:
    """Test listHubPlans endpoint with WireMock"""
    test_id = "plans.list_hub_plans.0"
    client = get_client(test_id)
    client.plans.list_hub_plans(hub_id="hubId")
    verify_request_count(test_id, "GET", "/hub/plans", {"hubId": "hubId"}, 1)
