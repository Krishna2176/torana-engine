"""
Unit tests for the BasePlugin abstract base class.
"""

from abc import ABC

import pytest

from torana.plugin_framework import BasePlugin, PluginManifest


# ---------------------------------------------------------------------
# Dummy Plugin
# ---------------------------------------------------------------------


class DummyPlugin(BasePlugin):
    """Minimal implementation of BasePlugin for testing."""

    def __init__(self) -> None:
        super().__init__(
            PluginManifest(
                id="dummy",
                name="Dummy Plugin",
                version="1.0.0",
                description="Plugin used for unit testing.",
                category="analysis",
                domain="Testing",
            )
        )

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    @property
    def configuration_schema(self) -> dict:
        return {}

    # ------------------------------------------------------------------
    # Dataset Requirements
    # ------------------------------------------------------------------

    @property
    def required_datasets(self) -> tuple[str, ...]:
        return ()

    # ------------------------------------------------------------------
    # Outputs
    # ------------------------------------------------------------------

    @property
    def outputs(self) -> tuple[str, ...]:
        return ()

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self, job) -> bool:
        return True

    # ------------------------------------------------------------------
    # Workflow Construction
    # ------------------------------------------------------------------

    def build_workflow(self, job):
        return None


# ---------------------------------------------------------------------
# BasePlugin
# ---------------------------------------------------------------------


def test_base_plugin_is_abstract():
    """BasePlugin cannot be instantiated."""

    with pytest.raises(TypeError):
        BasePlugin()  # type: ignore


def test_base_plugin_inherits_from_abc():
    """BasePlugin inherits from ABC."""

    assert issubclass(BasePlugin, ABC)


# ---------------------------------------------------------------------
# Dummy Plugin
# ---------------------------------------------------------------------


def test_dummy_plugin_can_be_instantiated():
    """Concrete subclasses can be instantiated."""

    plugin = DummyPlugin()

    assert plugin is not None


def test_dummy_plugin_exposes_manifest():
    """Concrete plugin exposes a PluginManifest."""

    plugin = DummyPlugin()

    assert isinstance(plugin.manifest, PluginManifest)


def test_dummy_plugin_exposes_configuration_schema():
    """Concrete plugin exposes configuration schema."""

    plugin = DummyPlugin()

    assert plugin.configuration_schema == {}


def test_dummy_plugin_exposes_required_datasets():
    """Concrete plugin exposes dataset requirements."""

    plugin = DummyPlugin()

    assert plugin.required_datasets == ()


def test_dummy_plugin_exposes_outputs():
    """Concrete plugin exposes output specification."""

    plugin = DummyPlugin()

    assert plugin.outputs == ()


def test_dummy_plugin_validates():
    """Concrete plugin performs validation."""

    plugin = DummyPlugin()

    assert plugin.validate(None) is True


def test_dummy_plugin_builds_workflow():
    """Concrete plugin constructs a workflow."""

    plugin = DummyPlugin()

    assert plugin.build_workflow(None) is None