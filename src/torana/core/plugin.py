"""
TORANA Engine

Plugin Base Class

Every analysis plugin (UHI, Flood, Walkability, etc.)
inherits from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Plugin(ABC):
    """
    Abstract base class for every TORANA analysis plugin.
    """

    def __init__(self) -> None:
        self._metadata: dict[str, Any] = {}

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    @property
    @abstractmethod
    def id(self) -> str:
        """Unique plugin identifier."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable plugin name."""

    @property
    @abstractmethod
    def version(self) -> str:
        """Plugin version."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Short plugin description."""

    # --------------------------------------------------
    # Configuration
    # --------------------------------------------------

    @abstractmethod
    def configuration_schema(self) -> dict[str, Any]:
        """
        Returns the configuration schema
        supported by this plugin.
        """

    # --------------------------------------------------
    # Datasets
    # --------------------------------------------------

    @abstractmethod
    def required_datasets(self) -> list[str]:
        """
        Required datasets.
        """

    @abstractmethod
    def optional_datasets(self) -> list[str]:
        """
        Optional datasets.
        """

    # --------------------------------------------------
    # Workflow
    # --------------------------------------------------

    @abstractmethod
    def workflow(self):
        """
        Return the workflow definition.
        """

    # --------------------------------------------------
    # Outputs
    # --------------------------------------------------

    @abstractmethod
    def outputs(self) -> list[str]:
        """
        List of outputs generated.
        """

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate plugin configuration.
        """

    # --------------------------------------------------
    # Representation
    # --------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(id='{self.id}', version='{self.version}')"
        )