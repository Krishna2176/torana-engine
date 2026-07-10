"""
Plugin Registry for the TORANA Plugin Framework.
"""

from __future__ import annotations

from .base_plugin import BasePlugin
from .exceptions import (
    DuplicatePluginError,
    InvalidPluginError,
    PluginNotFoundError,
)


class PluginRegistry:
    """
    Registry responsible for managing Plugins.

    The Plugin Registry provides Plugin discovery,
    registration, lookup, and validation.

    It does not execute Plugins or Workflows.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, BasePlugin] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register(self, plugin: BasePlugin) -> None:
        """
        Register a Plugin with the Registry.
        """
        self._validate_plugin(plugin)
        self._check_duplicate(plugin)

        self._plugins[plugin.manifest.id] = plugin

    def unregister(self, plugin_id: str) -> None:
        """
        Remove a Plugin from the Registry.
        """
        try:
            del self._plugins[plugin_id]
        except KeyError as exc:
            raise PluginNotFoundError(
                f"Plugin '{plugin_id}' is not registered."
            ) from exc

    def get(self, plugin_id: str) -> BasePlugin:
        """
        Retrieve a registered Plugin.
        """
        try:
            return self._plugins[plugin_id]
        except KeyError as exc:
            raise PluginNotFoundError(
                f"Plugin '{plugin_id}' was not found."
            ) from exc

    def exists(self, plugin_id: str) -> bool:
        """
        Determine whether a Plugin is registered.
        """
        try:
            self.get(plugin_id)
            return True
        except PluginNotFoundError:
            return False

    def list_plugins(self) -> tuple[BasePlugin, ...]:
        """
        Return an immutable snapshot of all registered Plugins.
        """
        return tuple(self._plugins.values())

    # ------------------------------------------------------------------
    # Python Collection Protocol
    # ------------------------------------------------------------------

    def __iter__(self):
        """
        Iterate over registered Plugins.
        """
        return iter(self._plugins.values())

    def __len__(self) -> int:
        """
        Return the number of registered Plugins.
        """
        return len(self._plugins)

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    def _validate_plugin(self, plugin: BasePlugin) -> None:
        """
        Validate a Plugin before registration.
        """
        if not isinstance(plugin, BasePlugin):
            raise InvalidPluginError(
                "Object is not a valid BasePlugin."
            )

        if plugin.manifest is None:
            raise InvalidPluginError(
                "Plugin Manifest is missing."
            )

    def _check_duplicate(self, plugin: BasePlugin) -> None:
        """
        Ensure Plugin IDs remain unique.
        """
        plugin_id = plugin.manifest.id

        if plugin_id in self._plugins:
            raise DuplicatePluginError(
                f"Plugin '{plugin_id}' is already registered."
            )