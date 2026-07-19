"""
Analysis manifest definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

from torana.analysis_framework.types import AnalysisCategory
from torana.plugin_framework.manifest import PluginManifest


@dataclass(frozen=True, slots=True)
class AnalysisManifest:
    """
    Immutable metadata describing an analysis.
    """

    plugin: PluginManifest

    category: AnalysisCategory

    @property
    def id(self) -> str:
        return self.plugin.id

    @property
    def name(self) -> str:
        return self.plugin.name

    @property
    def version(self) -> str:
        return self.plugin.version

    @property
    def author(self) -> str:
        return self.plugin.author

    @property
    def description(self) -> str:
        return self.plugin.description