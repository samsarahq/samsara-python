# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper


class RawIftaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper


class AsyncRawIftaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
