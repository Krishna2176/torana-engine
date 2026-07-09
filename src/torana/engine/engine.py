"""
TORANA Engine

Engine
"""

from __future__ import annotations

from torana.core.job import Job
from torana.engine.execution_context import ExecutionContext
from torana.engine.execution_manager import ExecutionManager
from torana.engine.exceptions import PluginNotFoundError
from torana.engine.registry import PluginRegistry
from torana.engine.status import JobStatus


class Engine:
    """
    Coordinates Job execution.
    """

    def __init__(
        self,
        registry: PluginRegistry,
        execution_manager: ExecutionManager | None = None,
    ) -> None:

        self._registry = registry
        self._execution_manager = (
            execution_manager or ExecutionManager()
        )

    @property
    def registry(self) -> PluginRegistry:
        """
        Registered Plugins.
        """

        return self._registry

    @property
    def execution_manager(self) -> ExecutionManager:
        """
        Execution manager used by the Engine.
        """

        return self._execution_manager

    def submit(
        self,
        job: Job,
    ) -> ExecutionContext:
        """
        Validate a Job and prepare it for execution.
        """

        try:
            self._registry.get(
                job.specification.plugin_id
            )

        except KeyError as exc:

            raise PluginNotFoundError(
                f"Plugin '{job.specification.plugin_id}' not found."
            ) from exc

        job.runtime.status = JobStatus.READY

        context = ExecutionContext(
            job=job
        )

        return self._execution_manager.execute(
            context
        )