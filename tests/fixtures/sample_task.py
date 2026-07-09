"""
TORANA Engine

Reusable Task fixture.
"""

from __future__ import annotations

from torana.core.task import Task


def create_sample_task() -> Task:
    """
    Create a reusable Task.
    """

    return Task(
        id="sample_task",
        name="Sample Task"
    )