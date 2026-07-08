"""
TORANA Engine

Execution Status Enumerations
"""

from enum import Enum, auto


class TaskStatus(Enum):
    """Lifecycle of a Task."""

    CREATED = auto()
    READY = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    CANCELLED = auto()


class JobStatus(Enum):
    """Lifecycle of a Job."""

    CREATED = auto()
    VALIDATING = auto()
    READY = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    CANCELLED = auto()


class EngineStatus(Enum):
    """Lifecycle of the Engine."""

    STOPPED = auto()
    INITIALIZING = auto()
    READY = auto()
    RUNNING = auto()
    SHUTDOWN = auto()