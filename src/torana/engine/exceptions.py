"""
TORANA Engine

Engine Exceptions
"""


class EngineError(Exception):
    """Base exception for the Engine."""


class PluginNotFoundError(EngineError):
    """Raised when a requested plugin cannot be found."""