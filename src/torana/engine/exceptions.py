"""
TORANA Engine

Engine Exceptions
"""


class ToranaError(Exception):
    """Base exception for TORANA."""


class PluginError(ToranaError):
    """Plugin-related exception."""


class RegistryError(ToranaError):
    """Plugin registry exception."""


class TaskError(ToranaError):
    """Task-related exception."""


class WorkflowError(ToranaError):
    """Workflow-related exception."""


class JobError(ToranaError):
    """Job-related exception."""


class EngineError(ToranaError):
    """Engine-related exception."""