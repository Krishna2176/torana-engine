"""
TORANA Engine

Engine Tests
"""

from __future__ import annotations

from tests.fixtures.dummy_plugin import DummyPlugin
from tests.fixtures.sample_job import create_sample_job

from torana.engine.engine import Engine
from torana.engine.execution_context import ExecutionContext
from torana.engine.registry import PluginRegistry
from torana.engine.status import JobStatus


def test_submit_job() -> None:
    """
    A valid Job should be accepted by the Engine.
    """

    registry = PluginRegistry()
    registry.register(DummyPlugin())

    engine = Engine(registry)

    job = create_sample_job()

    context = engine.submit(job)

    assert isinstance(context, ExecutionContext)

    assert context.job is job

    assert job.runtime.status == JobStatus.READY