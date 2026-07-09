"""
TORANA Engine

Reusable Execution Context fixture.
"""

from __future__ import annotations

from torana.engine.execution_context import ExecutionContext

from tests.fixtures.sample_job import create_sample_job


def create_sample_context() -> ExecutionContext:
    """
    Create a reusable ExecutionContext.
    """

    return ExecutionContext(
        job=create_sample_job()
    )