"""
TORANA Engine

Reusable Job fixture.
"""

from __future__ import annotations

from torana.core.job import Job
from torana.core.job_specification import JobSpecification


def create_sample_job() -> Job:
    """
    Create a reusable Job for tests.
    """

    specification = JobSpecification(
        plugin_id="uhi",
        configuration={}
    )

    return Job(specification=specification)