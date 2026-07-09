"""
TORANA Engine

Scheduler
"""

from __future__ import annotations

from torana.core.task import Task
from torana.core.workflow import Workflow


class Scheduler:
    """
    Determines which Tasks are ready for execution.

    The Scheduler never executes Tasks.
    It only queries the Workflow.
    """

    def get_ready_tasks(
        self,
        workflow: Workflow,
    ) -> list[Task]:
        """
        Return every Task ready to execute.
        """

        return workflow.ready_tasks()

    def has_pending_tasks(
        self,
        workflow: Workflow,
    ) -> bool:
        """
        Return True if the Workflow still has
        unfinished Tasks.
        """

        return len(workflow.pending_tasks()) > 0