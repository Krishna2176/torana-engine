"""
TORANA Engine

Plugin Registry
===============

Responsible for registering and discovering analysis plugins.
"""

from __future__ import annotations

from typing import Dict

from torana.core.plugin import Plugin


class PluginRegistry:
    """
    Stores every plugin available to the Engine.
    """

    def __init__(self) -> None:
        self._plugins: Dict[str, Plugin] = {}

    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(self, plugin: Plugin) -> None:
        """
        Register a plugin.

        Raises
        ------
        ValueError
            If a plugin with the same ID already exists.
        """

        if plugin.id in self._plugins:
            raise ValueError(
                f"Plugin '{plugin.id}' is already registered."
            )

        self._plugins[plugin.id] = plugin

    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------

    def get(self, plugin_id: str) -> Plugin:
        """
        Retrieve a plugin by ID.

        Raises
        ------
        KeyError
            If the plugin does not exist.
        """

        if plugin_id not in self._plugins:
            raise KeyError(
                f"Plugin '{plugin_id}' not found."
            )

        return self._plugins[plugin_id]

    # --------------------------------------------------
    # Queries
    # --------------------------------------------------

    def exists(self, plugin_id: str) -> bool:
        """
        Check whether a plugin exists.
        """

        return plugin_id in self._plugins

    def list_plugins(self) -> list[str]:
        """
        Return all registered plugin IDs.
        """

        return sorted(self._plugins.keys())

    # --------------------------------------------------
    # Properties
    # --------------------------------------------------

    @property
    def count(self) -> int:
        """
        Number of registered plugins.
        """

        return len(self._plugins)

    # --------------------------------------------------

    def __len__(self) -> int:
        return self.count