"""
TORANA Engine

Execution Context
"""

from __future__ import annotations

from dataclasses import dataclass, field

from torana.core.job import Job

from torana.engine.execution_resources import ExecutionResources
from torana.engine.execution_services import ExecutionServices
from torana.engine.execution_state import ExecutionState


@dataclass(slots=True)
class ExecutionContext:
    """
    Runtime environment for executing a Job.
    """

    job: Job

    state: ExecutionState = field(default_factory=ExecutionState)

    resources: ExecutionResources = field(default_factory=ExecutionResources)

    services: ExecutionServices = field(default_factory=ExecutionServices)