# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .fuel_energy.client import AsyncFuelEnergyClient, FuelEnergyClient
from .idling.client import AsyncIdlingClient, IdlingClient
from .raw_client import AsyncRawVehiclesClient, RawVehiclesClient


class VehiclesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVehiclesClient(client_wrapper=client_wrapper)
        self.idling = IdlingClient(client_wrapper=client_wrapper)

        self.fuel_energy = FuelEnergyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVehiclesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVehiclesClient
        """
        return self._raw_client


class AsyncVehiclesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVehiclesClient(client_wrapper=client_wrapper)
        self.idling = AsyncIdlingClient(client_wrapper=client_wrapper)

        self.fuel_energy = AsyncFuelEnergyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVehiclesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVehiclesClient
        """
        return self._raw_client
