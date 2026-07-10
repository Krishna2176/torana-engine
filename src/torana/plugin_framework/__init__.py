"""
TORANA Plugin Framework.

Provides the architectural foundation for developing and managing
Plugins within TORANA Engine.
"""

from .base_plugin import BasePlugin
from .exceptions import (
    DuplicatePluginError,
    InvalidPluginError,
    PluginFrameworkError,
    PluginNotFoundError,
    PluginRegistrationError,
)
from .manifest import PluginManifest
from .registry import PluginRegistry

__all__ = [
    "BasePlugin",
    "PluginManifest",
    "PluginRegistry",
    "PluginFrameworkError",
    "PluginRegistrationError",
    "DuplicatePluginError",
    "PluginNotFoundError",
    "InvalidPluginError",
]