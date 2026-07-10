"""
Unit tests for the PluginManifest model.
"""

import pytest
from dataclasses import FrozenInstanceError

from torana.plugin_framework import PluginManifest


# ---------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------


@pytest.fixture
def manifest() -> PluginManifest:
    """Return a valid PluginManifest."""

    return PluginManifest(
        id="flood_risk",
        name="Flood Risk Analysis",
        version="1.0.0",
        description="Flood hazard analysis.",
        category="analysis",
        domain="Hydrology",
        capabilities=(
            "Flood Hazard",
            "Flood Depth",
        ),
        framework_version="1.0",
        author="TORANA",
        license="All Rights Reserved",
        documentation="docs/plugins/flood_risk",
        tags=("flood", "hydrology"),
    )


# ---------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------


def test_manifest_has_id(manifest: PluginManifest):
    """PluginManifest exposes an identifier."""

    assert manifest.id == "flood_risk"


def test_manifest_has_name(manifest: PluginManifest):
    """PluginManifest exposes a name."""

    assert manifest.name == "Flood Risk Analysis"


def test_manifest_has_version(manifest: PluginManifest):
    """PluginManifest exposes a version."""

    assert manifest.version == "1.0.0"


def test_manifest_has_description(manifest: PluginManifest):
    """PluginManifest exposes a description."""

    assert manifest.description == "Flood hazard analysis."


# ---------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------


def test_manifest_has_category(manifest: PluginManifest):
    """PluginManifest exposes a category."""

    assert manifest.category == "analysis"


def test_manifest_has_domain(manifest: PluginManifest):
    """PluginManifest exposes a domain."""

    assert manifest.domain == "Hydrology"


# ---------------------------------------------------------------------
# Capabilities
# ---------------------------------------------------------------------


def test_manifest_has_capabilities(manifest: PluginManifest):
    """PluginManifest exposes capabilities."""

    assert len(manifest.capabilities) == 2


def test_manifest_capabilities_are_tuple(manifest: PluginManifest):
    """Capabilities are immutable."""

    assert isinstance(manifest.capabilities, tuple)


# ---------------------------------------------------------------------
# Administration
# ---------------------------------------------------------------------


def test_manifest_has_author(manifest: PluginManifest):
    assert manifest.author == "TORANA"


def test_manifest_has_license(manifest: PluginManifest):
    assert manifest.license == "All Rights Reserved"


def test_manifest_has_documentation(manifest: PluginManifest):
    assert manifest.documentation == "docs/plugins/flood_risk"


def test_manifest_has_tags(manifest: PluginManifest):
    assert manifest.tags == ("flood", "hydrology")


# ---------------------------------------------------------------------
# Immutability
# ---------------------------------------------------------------------


def test_manifest_is_immutable(manifest: PluginManifest):
    """PluginManifest cannot be modified."""

    with pytest.raises(FrozenInstanceError):
        manifest.name = "Modified"


# ---------------------------------------------------------------------
# Equality
# ---------------------------------------------------------------------


def test_manifests_with_same_data_are_equal():
    """Equal manifests compare equal."""

    manifest_one = PluginManifest(
        id="flood_risk",
        name="Flood Risk Analysis",
        version="1.0.0",
        description="Flood hazard analysis.",
        category="analysis",
        domain="Hydrology",
    )

    manifest_two = PluginManifest(
        id="flood_risk",
        name="Flood Risk Analysis",
        version="1.0.0",
        description="Flood hazard analysis.",
        category="analysis",
        domain="Hydrology",
    )

    assert manifest_one == manifest_two