"""
TORANA Engine

Workflow Tests
"""

from __future__ import annotations

from torana.core.task import Task
from torana.core.workflow import Workflow
from torana.engine.status import TaskStatus


def test_add_task() -> None:

    workflow = Workflow()

    task = Task(
        id="task_1",
        name="Task 1",
    )

    workflow.add_task(task)

    assert workflow.count == 1

    assert task.id in workflow.tasks


def test_add_dependency() -> None:

    workflow = Workflow()

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

    assert "A" in workflow.dependencies["B"]

    assert "B" in workflow.dependents["A"]


def test_ready_tasks() -> None:

    workflow = Workflow()

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

    ready = workflow.ready_tasks()

    assert len(ready) == 1

    assert ready[0].id == "A"

    task_a.status = TaskStatus.COMPLETED

    ready = workflow.ready_tasks()

    assert len(ready) == 1

    assert ready[0].id == "B"


def test_completed_pending_failed_tasks() -> None:

    workflow = Workflow()

    task_a = Task(
        id="A",
        name="Task A",
    )

    task_b = Task(
        id="B",
        name="Task B",
    )

    task_c = Task(
        id="C",
        name="Task C",
    )

    workflow.add_task(task_a)
    workflow.add_task(task_b)
    workflow.add_task(task_c)

    task_a.status = TaskStatus.COMPLETED

    task_b.status = TaskStatus.FAILED

    completed = workflow.completed_tasks()

    pending = workflow.pending_tasks()

    failed = workflow.failed_tasks()

    assert len(completed) == 1

    assert completed[0].id == "A"

    assert len(failed) == 1

    assert failed[0].id == "B"

    assert len(pending) == 2

    assert not workflow.is_complete()


def test_workflow_complete() -> None:

    workflow = Workflow()

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

    task_a.status = TaskStatus.COMPLETED
    task_b.status = TaskStatus.COMPLETED

    assert workflow.is_complete()