# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .csv.client import AsyncCsvClient, CsvClient
from .raw_client import AsyncRawIftaClient, RawIftaClient


class IftaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIftaClient(client_wrapper=client_wrapper)
        self.csv = CsvClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIftaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIftaClient
        """
        return self._raw_client


class AsyncIftaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIftaClient(client_wrapper=client_wrapper)
        self.csv = AsyncCsvClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIftaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIftaClient
        """
        return self._raw_client
