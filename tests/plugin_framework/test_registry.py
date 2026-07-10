"""
Unit tests for the PluginRegistry.
"""

import pytest

from torana.plugin_framework import (
    BasePlugin,
    DuplicatePluginError,
    PluginManifest,
    PluginNotFoundError,
)
from torana.plugin_framework.registry import PluginRegistry


# ---------------------------------------------------------------------
# Dummy Plugin
# ---------------------------------------------------------------------


class DummyPlugin(BasePlugin):
    """Minimal Plugin implementation for registry tests."""

    def __init__(self, plugin_id: str = "dummy") -> None:
        super().__init__(
            PluginManifest(
                id=plugin_id,
                name="Dummy Plugin",
                version="1.0.0",
                description="Registry test plugin.",
                category="analysis",
                domain="Testing",
            )
        )

    @property
    def configuration_schema(self) -> dict:
        return {}

    @property
    def required_datasets(self) -> tuple[str, ...]:
        return ()

    @property
    def outputs(self) -> tuple[str, ...]:
        return ()

    def validate(self, job) -> bool:
        return True

    def build_workflow(self, job):
        return None


# ---------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------


@pytest.fixture
def registry() -> PluginRegistry:
    return PluginRegistry()


@pytest.fixture
def plugin() -> DummyPlugin:
    return DummyPlugin()


# ---------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------


def test_register_plugin(registry, plugin):
    registry.register(plugin)

    assert registry.exists(plugin.manifest.id)


def test_duplicate_registration_raises(registry, plugin):
    registry.register(plugin)

    with pytest.raises(DuplicatePluginError):
        registry.register(plugin)


# ---------------------------------------------------------------------
# Lookup
# ---------------------------------------------------------------------


def test_get_registered_plugin(registry, plugin):
    registry.register(plugin)

    assert registry.get(plugin.manifest.id) is plugin


def test_get_unknown_plugin_raises(registry):
    with pytest.raises(PluginNotFoundError):
        registry.get("unknown")


# ---------------------------------------------------------------------
# Exists
# ---------------------------------------------------------------------


def test_exists_returns_true(registry, plugin):
    registry.register(plugin)

    assert registry.exists(plugin.manifest.id)


def test_exists_returns_false(registry):
    assert registry.exists("unknown") is False


# ---------------------------------------------------------------------
# Listing
# ---------------------------------------------------------------------


def test_list_plugins(registry, plugin):
    registry.register(plugin)

    plugins = registry.list_plugins()

    assert len(plugins) == 1
    assert plugin in plugins


# ---------------------------------------------------------------------
# Unregister
# ---------------------------------------------------------------------


def test_unregister_plugin(registry, plugin):
    registry.register(plugin)

    registry.unregister(plugin.manifest.id)

    assert not registry.exists(plugin.manifest.id)


# ---------------------------------------------------------------------
# Collection Behaviour
# ---------------------------------------------------------------------


def test_registry_is_iterable(registry):
    assert list(registry) == []


def test_registry_reports_length(registry):
    assert len(registry) == 0