"""
Reference implementation of the Flood Risk Plugin.
"""

from __future__ import annotations

from torana.plugin_framework import BasePlugin, PluginManifest

from .configuration import FloodRiskConfiguration
from .workflow_builder import build_workflow


class FloodRiskPlugin(BasePlugin):
    """
    Reference implementation of an Analysis Plugin.

    This Plugin demonstrates how analytical capabilities are
    integrated into TORANA through the Plugin Framework.
    """

    def __init__(self) -> None:
        super().__init__(
            PluginManifest(
                id="flood_risk",
                name="Flood Risk",
                version="1.0.0",
                description="Reference Flood Risk analysis plugin.",
                category="analysis",
                domain="Hydrology",
                capabilities=(
                    "Flood Risk Analysis",
                ),
                framework_version="1.0",
                author="TORANA",
                license="All Rights Reserved",
                documentation="docs/plugin-framework",
                tags=("flood", "hydrology"),
            )
        )

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    @property
    def configuration_schema(self):
        return FloodRiskConfiguration

    # ------------------------------------------------------------------
    # Dataset Requirements
    # ------------------------------------------------------------------

    @property
    def required_datasets(self) -> tuple[str, ...]:
        return (
            "Digital Elevation Model",
            "Rainfall",
        )

    # ------------------------------------------------------------------
    # Outputs
    # ------------------------------------------------------------------

    @property
    def outputs(self) -> tuple[str, ...]:
        return (
            "Flood Risk Layer",
        )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self, job) -> bool:
        """
        Validate the supplied Job.

        Validation rules will expand as the Analysis Framework evolves.
        """
        return True

    # ------------------------------------------------------------------
    # Workflow Construction
    # ------------------------------------------------------------------

    def build_workflow(self, job):
        """
        Construct the Flood Risk workflow.
        """
        return build_workflow()