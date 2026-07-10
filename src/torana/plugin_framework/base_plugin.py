"""
Abstract base class for all TORANA Plugins.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

from .manifest import PluginManifest

if TYPE_CHECKING:
    from torana.models.job import Job
    from torana.models.workflow import Workflow


class BasePlugin(ABC):
    """
    Base class for every TORANA Plugin.

    The BasePlugin defines the architectural contract between
    Analysis Plugins and the Plugin Framework.

    Plugins describe analyses.

    The Engine executes analyses.
    """

    def __init__(self, manifest: PluginManifest) -> None:
        """
        Initialize the Plugin with its immutable manifest.
        """
        self._manifest: PluginManifest = manifest

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    @property
    def manifest(self) -> PluginManifest:
        """
        Return the Plugin Manifest.

        The manifest is immutable and uniquely identifies the Plugin.
        """
        return self._manifest

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def configuration_schema(self) -> dict:
        """
        Return the Plugin configuration schema.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Dataset Requirements
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def required_datasets(self) -> tuple[str, ...]:
        """
        Return the datasets required by this Plugin.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Outputs
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def outputs(self) -> tuple[str, ...]:
        """
        Return the outputs produced by this Plugin.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    @abstractmethod
    def validate(self, job: Job) -> bool:
        """
        Validate the supplied Job before Workflow construction.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Workflow Construction
    # ------------------------------------------------------------------

    @abstractmethod
    def build_workflow(self, job: Job) -> Workflow:
        """
        Construct and return the Workflow for this Plugin.

        The Plugin defines the Workflow.

        The Engine executes it.
        """
        raise NotImplementedError