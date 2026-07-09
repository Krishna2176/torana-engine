"""
TORANA Engine

Engine
"""

from __future__ import annotations

from torana.core.job import Job
from torana.engine.execution_context import ExecutionContext
from torana.engine.exceptions import PluginNotFoundError
from torana.engine.registry import PluginRegistry
from torana.engine.status import JobStatus


class Engine:
    """
    Coordinates Job execution.
    """

    def __init__(self, registry: PluginRegistry) -> None:
        self._registry = registry

    @property
    def registry(self) -> PluginRegistry:
        return self._registry

    def submit(self, job: Job) -> ExecutionContext:
        """
        Validate a Job and create its execution context.
        """

        try:
            self._registry.get(job.specification.plugin_id)
        except KeyError as exc:
            raise PluginNotFoundError(
                f"Plugin '{job.specification.plugin_id}' not found."
            ) from exc

        job.runtime.status = JobStatus.READY

        return ExecutionContext(job=job)