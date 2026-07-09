import pytest

from torana.core.plugin import Plugin
from torana.engine.registry import PluginRegistry


class DummyPlugin(Plugin):

    @property
    def id(self):
        return "dummy"

    @property
    def name(self):
        return "Dummy"

    @property
    def version(self):
        return "1.0"

    @property
    def description(self):
        return "Test plugin"

    @property
    def metadata(self):
        return {}

    @property
    def configuration_schema(self):
        return {}

    @property
    def required_datasets(self):
        return []

    @property
    def optional_datasets(self):
        return []

    @property
    def workflow(self):
        return None

    @property
    def outputs(self):
        return []

    def validate(self):
        return True


def test_register_plugin():

    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    assert registry.count == 1
    assert registry.exists("dummy")


def test_duplicate_plugin():

    registry = PluginRegistry()

    plugin = DummyPlugin()

    registry.register(plugin)

    with pytest.raises(ValueError):
        registry.register(plugin)