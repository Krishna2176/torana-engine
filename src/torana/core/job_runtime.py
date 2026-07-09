"""
TORANA Engine

Job Runtime
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from torana.core.workflow import Workflow
from torana.engine.status import JobStatus


@dataclass(slots=True)
class JobRuntime:
    """
    Mutable execution state of a Job.
    """

    workflow: Workflow | None = None

    status: JobStatus = JobStatus.CREATED

    progress: float = 0.0

    created_at: datetime = field(
    default_factory=lambda: datetime.now(UTC)
)

    started_at: datetime | None = None

    completed_at: datetime | None = None