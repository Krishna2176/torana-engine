"""
Abstract base class for all TORANA plugins.
"""

from __future__ import annotations

from abc import ABC

from .manifest import PluginManifest


class BasePlugin(ABC):
    """
    Base class for every TORANA plugin.

    A plugin is a discoverable extension that can be registered with the
    Plugin Framework.

    Domain-specific behavior belongs to specialized plugin types
    (for example, BaseAnalysis).
    """

    def __init__(self, manifest: PluginManifest) -> None:
        self._manifest = manifest

    @property
    def manifest(self) -> PluginManifest:
        """
        Immutable plugin metadata.
        """
        return self._manifest

    def initialize(self) -> None:
        """
        Optional lifecycle hook executed when the plugin is loaded.
        """
        return None

    def shutdown(self) -> None:
        """
        Optional lifecycle hook executed before the plugin is unloaded.
        """
        return None