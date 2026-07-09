"""
TORANA Engine

Task Executor Tests
"""

from __future__ import annotations

from torana.engine.task_executor import TaskExecutor
from torana.engine.status import TaskStatus

from tests.fixtures.sample_task import create_sample_task


def test_execute_task() -> None:

    executor = TaskExecutor()

    task = create_sample_task()

    result = executor.execute(task)

    assert result is task

    assert task.status == TaskStatus.COMPLETED