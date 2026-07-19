"""
Tests for AnalysisExecutionContext.
"""

from torana.analysis_framework.context import (
    AnalysisExecutionContext,
)
from torana.core.job import Job
from torana.core.job_specification import JobSpecification
from torana.engine.execution_context import ExecutionContext


def test_context_creation():
    job = Job(
        specification=JobSpecification(
            plugin_id="dummy",
            configuration={},
        )
    )

    execution_context = ExecutionContext(
        job=job,
    )

    context = AnalysisExecutionContext(
        execution_context=execution_context,
        datasets={},
    )

    assert context.execution_context is execution_context
    assert context.datasets == {}