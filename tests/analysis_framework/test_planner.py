"""
Tests for AnalysisPlanner.
"""

from __future__ import annotations

from torana.analysis_framework.context import (
    AnalysisExecutionContext,
)
from torana.analysis_framework.planner import (
    AnalysisPlanner,
)
from torana.core.job import Job
from torana.core.job_specification import JobSpecification
from torana.core.workflow import Workflow
from torana.engine.execution_context import (
    ExecutionContext,
)


class DummyPlanner(AnalysisPlanner):

    def plan(
        self,
        analysis,
        context,
    ) -> Workflow:
        return Workflow()


def test_plan_returns_workflow(
    analysis,
):
    planner = DummyPlanner()

    job = Job(
        specification=JobSpecification(
            plugin_id="dummy",
            configuration={},
        )
    )

    context = AnalysisExecutionContext(
        execution_context=ExecutionContext(
            job=job,
        ),
        datasets={},
    )

    workflow = planner.plan(
        analysis,
        context,
    )

    assert isinstance(
        workflow,
        Workflow,
    )