"""
TORANA Plugin Framework.

Provides the architectural foundation for developing and managing
Plugins within TORANA Engine.
"""

from .base_plugin import BasePlugin
from .manifest import PluginManifest

__all__ = [
    "BasePlugin",
    "PluginManifest",
]