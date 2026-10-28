"""
Pytest plugin that manages the WireMock container lifecycle for wire tests.

This plugin is loaded globally for the test suite and is responsible for
starting and stopping the WireMock container exactly once per test run,
including when running with pytest-xdist over the entire project.

It lives under tests/ (as tests/conftest.py) and is discovered automatically
by pytest's normal test collection rules.
"""

import json
import os
import subprocess

import httpx
import pytest

_STARTED: bool = False
_WIREMOCK_PORT: str = "8080"  # Default, will be updated after container starts
_PROJECT_NAME: str = "samsara-api"

# This file lives at tests/conftest.py, so the project root is one level up.
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_COMPOSE_FILE = os.path.join(_PROJECT_ROOT, "wiremock", "docker-compose.test.yml")


def _get_wiremock_port() -> str:
    """Gets the dynamically assigned port for the WireMock container."""
    try:
        result = subprocess.run(
            ["docker", "compose", "-f", _COMPOSE_FILE, "-p", _PROJECT_NAME, "port", "wiremock", "8080"],
            check=True,
            capture_output=True,
            text=True,
        )
        # Output is like "0.0.0.0:32768" or "[::]:32768"
        port = result.stdout.strip().split(":")[-1]
        return port
    except subprocess.CalledProcessError:
        return "8080"  # Fallback to default


def _isolate_asset_location_mappings() -> None:
    """Distinguish legacy and GOA response stubs in the shared mock server."""
    mappings_path = os.path.join(_PROJECT_ROOT, "wiremock", "wiremock-mappings.json")
    with open(mappings_path, encoding="utf-8") as mappings_file:
        mappings = json.load(mappings_file)["mappings"]

    test_ids = {
        "/v1/fleet/assets/{assetId}/locations": "assets.get_asset_location.0",
        "/v1/fleet/assets/{asset_id}/locations": "assets.v_1_get_asset_location.0",
    }
    for mapping in mappings:
        request = mapping["request"]
        path = request.get("urlPathTemplate")
        if request.get("method") != "GET" or path not in test_ids:
            continue

        request.setdefault("headers", {})["X-Test-Id"] = {"equalTo": test_ids[path]}
        mapping["persistent"] = False
        response = httpx.put(
            f"http://localhost:{_WIREMOCK_PORT}/__admin/mappings/{mapping['id']}",
            json=mapping,
            timeout=10,
        )
        response.raise_for_status()


def _start_wiremock() -> None:
    """Starts the WireMock container using docker-compose."""
    global _STARTED, _WIREMOCK_PORT
    if _STARTED:
        return

    print(f"\nStarting WireMock container (project: {_PROJECT_NAME})...")
    try:
        subprocess.run(
            ["docker", "compose", "-f", _COMPOSE_FILE, "-p", _PROJECT_NAME, "up", "-d", "--wait"],
            check=True,
            capture_output=True,
            text=True,
        )
        _WIREMOCK_PORT = _get_wiremock_port()
        os.environ["WIREMOCK_PORT"] = _WIREMOCK_PORT
        _isolate_asset_location_mappings()
        print(f"WireMock container is ready on port {_WIREMOCK_PORT}")
        _STARTED = True
    except subprocess.CalledProcessError as e:
        print(f"Failed to start WireMock: {e.stderr}")
        raise


def _stop_wiremock() -> None:
    """Stops and removes the WireMock container."""
    print("\nStopping WireMock container...")
    subprocess.run(
        ["docker", "compose", "-f", _COMPOSE_FILE, "-p", _PROJECT_NAME, "down", "-v"],
        check=False,
        capture_output=True,
    )


def _is_xdist_worker(config: pytest.Config) -> bool:
    """
    Determines if the current process is an xdist worker.

    In pytest-xdist, worker processes have a 'workerinput' attribute
    on the config object, while the controller process does not.
    """
    return hasattr(config, "workerinput")


def pytest_configure(config: pytest.Config) -> None:
    """
    Pytest hook that runs during test session setup.

    Starts WireMock container only from the controller process (xdist)
    or the single process (non-xdist). This ensures only one container
    is started regardless of the number of worker processes.
    """
    if _is_xdist_worker(config):
        # Workers never manage the container lifecycle.
        return

    _start_wiremock()


def pytest_unconfigure(config: pytest.Config) -> None:
    """
    Pytest hook that runs during test session teardown.

    Stops WireMock container only from the controller process (xdist)
    or the single process (non-xdist). This ensures the container is
    cleaned up after all workers have finished.
    """
    if _is_xdist_worker(config):
        # Workers never manage the container lifecycle.
        return

    _stop_wiremock()
