"""
Dataset Discovery.
"""

from __future__ import annotations

from .manifest import DatasetManifest
from .registry import DatasetRegistry
from .requirement import DatasetRequirement


class DatasetDiscovery:
    """
    Service responsible for discovering datasets.

    DatasetDiscovery orchestrates Dataset Providers through the
    Dataset Registry and aggregates compatible Dataset Manifests.
    """

    def __init__(
        self,
        registry: DatasetRegistry,
    ) -> None:

        self._registry = registry

    @property
    def registry(
        self,
    ) -> DatasetRegistry:
        """
        Dataset Registry used for discovery.
        """

        return self._registry

    # ------------------------------------------------------------------

    def discover(
        self,
        requirement: DatasetRequirement,
    ) -> tuple[DatasetManifest, ...]:
        """
        Discover datasets matching the supplied requirement.
        """

        matches: list[DatasetManifest] = []

        for provider in self.registry.providers:

            matches.extend(
                provider.discover(requirement)
            )

        return tuple(matches)