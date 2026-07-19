"""
Shared fixtures for Analysis Framework tests.
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest

from torana.analysis_framework.base_analysis import BaseAnalysis
from torana.analysis_framework.configuration import (
    AnalysisConfiguration,
    AnalysisParameterSchema,
)
from torana.analysis_framework.manifest import AnalysisManifest
from torana.analysis_framework.types import (
    AnalysisCategory,
    AnalysisOutput,
    OutputFormat,
    OutputType,
)
from torana.dataset_framework.requirement import DatasetRequirement
from torana.plugin_framework.manifest import PluginManifest
from torana.plugin_framework.types import PluginCategory


@dataclass(slots=True)
class DummyAnalysis(BaseAnalysis):
    """
    Minimal concrete analysis used for testing.
    """

    _manifest: AnalysisManifest
    _schema: AnalysisParameterSchema
    _configuration: AnalysisConfiguration

    def __init__(
        self,
        manifest: AnalysisManifest,
        schema: AnalysisParameterSchema,
        configuration: AnalysisConfiguration,
    ) -> None:
        super().__init__(manifest.plugin)

        self._manifest = manifest
        self._schema = schema
        self._configuration = configuration

    @property
    def manifest(self) -> AnalysisManifest:
        return self._manifest

    @property
    def parameter_schema(self) -> AnalysisParameterSchema:
        return self._schema

    @property
    def configuration(self) -> AnalysisConfiguration:
        return self._configuration

    @property
    def dataset_requirements(
        self,
    ) -> tuple[DatasetRequirement, ...]:
        return ()

    @property
    def outputs(
        self,
    ) -> tuple[AnalysisOutput, ...]:
        return (
            AnalysisOutput(
                name="result",
                output_type=OutputType.RASTER,
                formats=(OutputFormat.GEOTIFF,),
            ),
        )


@pytest.fixture
def plugin_manifest() -> PluginManifest:
    return PluginManifest(
        id="dummy",
        name="Dummy Analysis",
        version="1.0.0",
        description="Dummy analysis",
        category="analysis",
        domain="testing",
        author="TORANA",
    )


@pytest.fixture
def analysis_manifest(
    plugin_manifest: PluginManifest,
) -> AnalysisManifest:
    return AnalysisManifest(
        plugin=plugin_manifest,
        category=AnalysisCategory.HYDROLOGY,
    )


@pytest.fixture
def parameter_schema() -> AnalysisParameterSchema:
    return AnalysisParameterSchema()


@pytest.fixture
def configuration() -> AnalysisConfiguration:
    return AnalysisConfiguration()


@pytest.fixture
def analysis(
    analysis_manifest: AnalysisManifest,
    parameter_schema: AnalysisParameterSchema,
    configuration: AnalysisConfiguration,
) -> DummyAnalysis:
    return DummyAnalysis(
        manifest=analysis_manifest,
        schema=parameter_schema,
        configuration=configuration,
    )