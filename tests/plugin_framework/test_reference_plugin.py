"""
Integration tests for the Flood Risk reference plugin.
"""

from torana.plugin_framework import PluginRegistry
from torana.plugins.flood_risk.plugin import FloodRiskPlugin


# ---------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------


def create_plugin() -> FloodRiskPlugin:
    """Create a Flood Risk Plugin instance."""

    return FloodRiskPlugin()


# ---------------------------------------------------------------------
# Plugin
# ---------------------------------------------------------------------


def test_plugin_can_be_instantiated():
    """The reference plugin can be instantiated."""

    plugin = create_plugin()

    assert plugin is not None


def test_plugin_exposes_manifest():
    """The plugin exposes its manifest."""

    plugin = create_plugin()

    assert plugin.manifest.id == "flood_risk"
    assert plugin.manifest.name == "Flood Risk"


# ---------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------


def test_plugin_can_be_registered():
    """The plugin can be registered."""

    registry = PluginRegistry()

    plugin = create_plugin()

    registry.register(plugin)

    assert registry.exists(plugin.manifest.id)


def test_registered_plugin_can_be_retrieved():
    """A registered plugin can be retrieved."""

    registry = PluginRegistry()

    plugin = create_plugin()

    registry.register(plugin)

    assert registry.get(plugin.manifest.id) is plugin


# ---------------------------------------------------------------------
# Workflow
# ---------------------------------------------------------------------


def test_plugin_builds_workflow():
    """The plugin constructs a workflow."""

    plugin = create_plugin()

    workflow = plugin.build_workflow(None)

    assert workflow is not None


def test_workflow_contains_expected_tasks():
    """The workflow contains four tasks."""

    plugin = create_plugin()

    workflow = plugin.build_workflow(None)

    assert len(workflow) == 4


def test_workflow_contains_expected_task_ids():
    """The workflow contains the expected tasks."""

    plugin = create_plugin()

    workflow = plugin.build_workflow(None)

    expected = {
        "load_dem",
        "load_rainfall",
        "compute_flood_risk",
        "produce_outputs",
    }

    assert set(workflow.tasks.keys()) == expected


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------


def test_plugin_validation_succeeds():
    """Reference plugin validates successfully."""

    plugin = create_plugin()

    assert plugin.validate(None) is True