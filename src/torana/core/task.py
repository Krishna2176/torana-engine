"""
TORANA Engine

Task Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from torana.engine.status import TaskStatus


@dataclass(slots=True)
class Task:
    """
    Represents a single executable unit of work.

    Tasks are intentionally independent.
    Execution order is managed by the Workflow,
    not by the Task itself.
    """

    id: str

    name: str

    description: str = ""

    status: TaskStatus = TaskStatus.CREATED

    metadata: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"Task<{self.id}>"