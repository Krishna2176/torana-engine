"""
Tests for BaseAnalysis.
"""


def test_manifest(analysis):
    assert analysis.manifest.name == "Dummy Analysis"


def test_parameter_schema(
    analysis,
    parameter_schema,
):
    assert analysis.parameter_schema is parameter_schema


def test_configuration(
    analysis,
    configuration,
):
    assert analysis.configuration is configuration


def test_dataset_requirements(
    analysis,
):
    assert analysis.dataset_requirements == ()


def test_outputs(
    analysis,
):
    outputs = analysis.outputs

    assert len(outputs) == 1
    assert outputs[0].name == "result"