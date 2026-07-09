"""
TORANA Engine

Scheduler Tests
"""

from __future__ import annotations

from torana.core.task import Task
from torana.core.workflow import Workflow
from torana.engine.scheduler import Scheduler
from torana.engine.status import TaskStatus


def test_ready_tasks():

    workflow = Workflow()

    scheduler = Scheduler()

    task_a = Task(
        id="A",
        name="Task A",
    )

    task_b = Task(
        id="B",
        name="Task B",
    )

    workflow.add_task(task_a)
    workflow.add_task(task_b)

    workflow.add_dependency("B", "A")

    ready = scheduler.get_ready_tasks(workflow)

    assert len(ready) == 1

    assert ready[0].id == "A"


def test_pending_tasks():

    workflow = Workflow()

    scheduler = Scheduler()

    task = Task(
        id="A",
        name="Task A",
    )

    workflow.add_task(task)

    assert scheduler.has_pending_tasks(workflow)

    task.status = TaskStatus.COMPLETED

    assert not scheduler.has_pending_tasks(workflow)