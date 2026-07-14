"""
Dataset Registry.
"""

from __future__ import annotations

from .base_provider import BaseProvider
from .exceptions import (
    DuplicateProviderError,
    ProviderNotFoundError,
)


class DatasetRegistry:
    """
    Registry of Dataset Providers.
    """

    def __init__(self) -> None:
        self._providers: dict[str, BaseProvider] = {}

    # ----------------------------------------------------------

    def register(
        self,
        provider: BaseProvider,
    ) -> None:

        if provider.id in self._providers:
            raise DuplicateProviderError(
                f"Provider '{provider.id}' already registered."
            )

        self._providers[provider.id] = provider

    # ----------------------------------------------------------

    def remove(
        self,
        provider_id: str,
    ) -> None:

        if provider_id not in self._providers:
            raise ProviderNotFoundError(provider_id)

        del self._providers[provider_id]

    # ----------------------------------------------------------

    def get(
        self,
        provider_id: str,
    ) -> BaseProvider:

        try:
            return self._providers[provider_id]

        except KeyError as error:
            raise ProviderNotFoundError(provider_id) from error

    # ----------------------------------------------------------

    def exists(
        self,
        provider_id: str,
    ) -> bool:

        return provider_id in self._providers

    # ----------------------------------------------------------

    @property
    def providers(
        self,
    ) -> tuple[BaseProvider, ...]:

        return tuple(self._providers.values())

    # ----------------------------------------------------------

    @property
    def count(self) -> int:
        return len(self._providers)

    # ----------------------------------------------------------

    def __len__(self) -> int:
        return self.count