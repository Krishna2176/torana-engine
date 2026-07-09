"""
TORANA Engine

Execution Manager
"""

from __future__ import annotations

from torana.engine.execution_context import ExecutionContext
from torana.engine.scheduler import Scheduler
from torana.engine.task_executor import TaskExecutor


class ExecutionManager:
    """
    Coordinates Workflow execution.

    The ExecutionManager owns the execution
    lifecycle while delegating scheduling and
    task execution to dedicated components.
    """

    def __init__(
        self,
        scheduler: Scheduler | None = None,
        task_executor: TaskExecutor | None = None,
    ) -> None:

        self._scheduler = scheduler or Scheduler()
        self._task_executor = task_executor or TaskExecutor()

    # --------------------------------------------------

    @property
    def scheduler(self) -> Scheduler:
        """
        Scheduler used during execution.
        """

        return self._scheduler

    # --------------------------------------------------

    @property
    def task_executor(self) -> TaskExecutor:
        """
        TaskExecutor used during execution.
        """

        return self._task_executor

    # --------------------------------------------------

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:
        """
        Execute the supplied ExecutionContext.

        Scheduler determines which Tasks are
        executable.

        TaskExecutor performs Task execution.
        """

        workflow = context.job.runtime.workflow

        if workflow is None:
            return context

        while self._scheduler.has_pending_tasks(workflow):

            ready_tasks = self._scheduler.get_ready_tasks(workflow)

            if not ready_tasks:
                break

            for task in ready_tasks:
                self._task_executor.execute(task)

        return context