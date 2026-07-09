"""
TORANA Engine

Execution State
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ExecutionState:
    """
    Tracks runtime execution state.
    """

    current_task: str | None = None

    completed_tasks: list[str] = field(default_factory=list)

    failed_tasks: list[str] = field(default_factory=list)

    progress: float = 0.0