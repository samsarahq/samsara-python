"""Pagination must not mistake an empty page for the end of results."""

import asyncio
from typing import List, Optional

import httpx
import pytest

from samsara import AsyncSamsara, Samsara
from samsara.core.pagination import AsyncPager, SyncPager


@pytest.mark.parametrize("empty_items", [[], None])
@pytest.mark.parametrize("iterate_pages", [False, True])
def test_sync_pager_continues_after_empty_page(empty_items: Optional[List[str]], iterate_pages: bool) -> None:
    last = SyncPager(get_next=None, has_next=False, items=["last"], response=None)
    middle = SyncPager(get_next=lambda: last, has_next=True, items=empty_items, response=None)
    first = SyncPager(get_next=lambda: middle, has_next=True, items=["first"], response=None)
    if iterate_pages:
        assert list(first.iter_pages()) == [first, middle, last]
    else:
        assert list(first) == ["first", "last"]


@pytest.mark.parametrize("empty_items", [[], None])
@pytest.mark.parametrize("iterate_pages", [False, True])
async def test_async_pager_continues_after_empty_page(empty_items: Optional[List[str]], iterate_pages: bool) -> None:
    last = AsyncPager(get_next=None, has_next=False, items=["last"], response=None)

    async def get_last():
        return last

    middle = AsyncPager(get_next=get_last, has_next=True, items=empty_items, response=None)

    async def get_middle():
        return middle

    first = AsyncPager(get_next=get_middle, has_next=True, items=["first"], response=None)
    if iterate_pages:
        assert [page async for page in first.iter_pages()] == [first, middle, last]
    else:
        assert [item async for item in first] == ["first", "last"]


@pytest.mark.parametrize("is_async", [False, True])
def test_vehicle_iteration_crosses_empty_http_page(is_async: bool) -> None:
    cursors = []

    def respond(request: httpx.Request) -> httpx.Response:
        cursor = request.url.params.get("after")
        cursors.append(cursor)
        pages = {
            None: ([{"id": "first", "createdAtTime": "2026-01-01T00:00:00Z"}], "a", True),
            "a": ([], "b", True),
            "b": ([{"id": "last", "createdAtTime": "2026-01-01T00:00:00Z"}], "", False),
        }
        data, next_cursor, has_next = pages[cursor]
        return httpx.Response(
            200, json={"data": data, "pagination": {"endCursor": next_cursor, "hasNextPage": has_next}}
        )

    if is_async:

        async def consume():
            async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http_client:
                client = AsyncSamsara(token="test-token", httpx_client=http_client)
                pager = await client.vehicles.list()
                return [vehicle.id async for vehicle in pager]

        result = asyncio.run(consume())
    else:
        with httpx.Client(transport=httpx.MockTransport(respond)) as http_client:
            client = Samsara(token="test-token", httpx_client=http_client)
            result = [vehicle.id for vehicle in client.vehicles.list()]
    assert result == ["first", "last"]
    assert cursors == [None, "a", "b"]


@pytest.mark.parametrize("stop_reason", ["has_next_false", "no_callback", "none_page"])
def test_sync_pager_termination_controls(stop_reason: str) -> None:
    calls = []

    def get_next():
        calls.append(True)
        return None

    page = SyncPager(
        get_next=None if stop_reason == "no_callback" else get_next,
        has_next=stop_reason != "has_next_false",
        items=[],
        response=None,
    )
    assert list(page.iter_pages()) == [page]
    assert calls == ([True] if stop_reason == "none_page" else [])


@pytest.mark.parametrize("stop_reason", ["has_next_false", "no_callback", "none_page"])
async def test_async_pager_termination_controls(stop_reason: str) -> None:
    calls = []

    async def get_next():
        calls.append(True)
        return None

    page = AsyncPager(
        get_next=None if stop_reason == "no_callback" else get_next,
        has_next=stop_reason != "has_next_false",
        items=[],
        response=None,
    )
    assert [item async for item in page.iter_pages()] == [page]
    assert calls == ([True] if stop_reason == "none_page" else [])
