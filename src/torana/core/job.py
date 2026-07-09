"""
TORANA Engine

Job Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from torana.core.job_results import JobResults
from torana.core.job_runtime import JobRuntime
from torana.core.job_specification import JobSpecification


@dataclass(slots=True)
class Job:
    """
    Represents a single execution request.
    """

    specification: JobSpecification

    runtime: JobRuntime = field(default_factory=JobRuntime)

    results: JobResults = field(default_factory=JobResults)

    id: UUID = field(default_factory=uuid4)