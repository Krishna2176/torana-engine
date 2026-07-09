"""
TORANA Engine

Execution Manager
"""

from __future__ import annotations

from torana.engine.execution_context import ExecutionContext
from torana.engine.scheduler import Scheduler


class ExecutionManager:
    """
    Coordinates execution of a Workflow.

    The ExecutionManager owns the execution
    lifecycle while delegating scheduling to
    the Scheduler.
    """

    def __init__(
        self,
        scheduler: Scheduler | None = None,
    ) -> None:

        self._scheduler = scheduler or Scheduler()

    @property
    def scheduler(self) -> Scheduler:
        """
        Scheduler used for execution.
        """

        return self._scheduler

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:
        """
        Execute a Job.

        Scheduler v1 only determines whether
        work remains.

        Task execution will be added in the
        next milestone.
        """

        workflow = context.job.runtime.workflow

        if workflow is None:
            return context

        while self._scheduler.has_pending_tasks(workflow):

            ready = self._scheduler.get_ready_tasks(workflow)

            if not ready:
                break

            #
            # TaskExecutor will be inserted here.
            #
            break

        return context