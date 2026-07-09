"""
TORANA Engine

Task Executor
"""

from __future__ import annotations

from torana.core.task import Task
from torana.engine.status import TaskStatus


class TaskExecutor:
    """
    Executes a single Task.

    The TaskExecutor manages the Task lifecycle
    but does not perform analysis itself.
    """

    def execute(
        self,
        task: Task,
    ) -> Task:
        """
        Execute a Task.
        """

        task.status = TaskStatus.RUNNING

        #
        # Plugin execution will be inserted here.
        #

        task.status = TaskStatus.COMPLETED

        return task