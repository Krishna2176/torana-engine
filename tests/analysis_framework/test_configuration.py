"""
Tests for Analysis configuration models.
"""

from torana.analysis_framework.configuration import (
    AnalysisConfiguration,
    AnalysisParameterSchema,
)


def test_empty_schema():
    schema = AnalysisParameterSchema()

    assert len(schema) == 0


def test_empty_configuration():
    configuration = AnalysisConfiguration()

    assert len(configuration) == 0


def test_configuration_contains():
    configuration = AnalysisConfiguration(
        values={
            "resolution": 30,
        }
    )

    assert "resolution" in configuration


def test_configuration_lookup():
    configuration = AnalysisConfiguration(
        values={
            "resolution": 30,
        }
    )

    assert configuration["resolution"] == 30