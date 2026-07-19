"""
Base Analysis definition.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from torana.analysis_framework.configuration import (
    AnalysisConfiguration,
    AnalysisParameterSchema,
)
from torana.analysis_framework.manifest import AnalysisManifest
from torana.analysis_framework.types import AnalysisOutput
from torana.dataset_framework.requirement import DatasetRequirement
from torana.plugin_framework.base_plugin import BasePlugin


class BaseAnalysis(BasePlugin, ABC):
    """
    Base class for all TORANA analyses.

    Analyses describe work.

    They do not execute work.
    """

    @property
    @abstractmethod
    def manifest(self) -> AnalysisManifest:
        """
        Immutable analysis metadata.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def parameter_schema(self) -> AnalysisParameterSchema:
        """
        Parameter schema supported by this analysis.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def configuration(self) -> AnalysisConfiguration:
        """
        Runtime configuration.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def dataset_requirements(
        self,
    ) -> tuple[DatasetRequirement, ...]:
        """
        Dataset requirements declared by this analysis.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def outputs(
        self,
    ) -> tuple[AnalysisOutput, ...]:
        """
        Outputs produced by this analysis.
        """
        raise NotImplementedError