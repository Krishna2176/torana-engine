"""
Tests for AnalysisManifest.
"""


def test_plugin_metadata_is_forwarded(
    analysis_manifest,
):
    assert analysis_manifest.id == "dummy"
    assert analysis_manifest.name == "Dummy Analysis"
    assert analysis_manifest.version == "1.0.0"
    assert analysis_manifest.author == "TORANA"
    assert analysis_manifest.description == "Dummy analysis"