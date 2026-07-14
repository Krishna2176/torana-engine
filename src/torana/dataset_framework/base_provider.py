"""
Base Provider for the TORANA Dataset Framework.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .manifest import DatasetManifest
from .requirement import DatasetRequirement


class BaseProvider(ABC):
    """
    Abstract base class for Dataset Providers.
    """

    def __init__(
        self,
        *,
        id: str,
        name: str,
        version: str,
        description: str,
    ) -> None:

        self._id = id
        self._name = name
        self._version = version
        self._description = description

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def description(self) -> str:
        return self._description

    # ------------------------------------------------------------------
    # Dataset Catalogue
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def manifests(self) -> tuple[DatasetManifest, ...]:
        """
        Return every Dataset Manifest exposed by the provider.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    @abstractmethod
    def discover(
        self,
        requirement: DatasetRequirement,
    ) -> tuple[DatasetManifest, ...]:
        """
        Return manifests matching the supplied requirement.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Availability
    # ------------------------------------------------------------------

    @abstractmethod
    def is_available(
        self,
        dataset_id: str,
    ) -> bool:
        """
        Return True if the dataset is available.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Acquisition
    # ------------------------------------------------------------------

    @abstractmethod
    def acquire(
        self,
        dataset_id: str,
    ):
        """
        Acquire the requested dataset.
        """
        raise NotImplementedError