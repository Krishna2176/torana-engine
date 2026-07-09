"""
TORANA Engine

Execution Manager Tests
"""

from __future__ import annotations

from torana.engine.execution_manager import ExecutionManager
from torana.engine.scheduler import Scheduler

from tests.fixtures.sample_context import create_sample_context


def test_create_execution_manager() -> None:

    manager = ExecutionManager()

    assert isinstance(manager.scheduler, Scheduler)


def test_execute_returns_context() -> None:

    manager = ExecutionManager()

    context = create_sample_context()

    result = manager.execute(context)

    assert result is context