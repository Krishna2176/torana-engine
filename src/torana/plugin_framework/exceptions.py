"""
Exceptions raised by the TORANA Plugin Framework.
"""


class PluginFrameworkError(Exception):
    """Base exception for the Plugin Framework."""


class PluginRegistrationError(PluginFrameworkError):
    """Raised when a Plugin cannot be registered."""


class DuplicatePluginError(PluginRegistrationError):
    """Raised when a Plugin with the same ID already exists."""


class PluginNotFoundError(PluginFrameworkError):
    """Raised when a Plugin cannot be found in the Registry."""


class InvalidPluginError(PluginRegistrationError):
    """Raised when a Plugin does not satisfy the Plugin contract."""