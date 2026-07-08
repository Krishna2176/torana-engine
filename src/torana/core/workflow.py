"""
TORANA Engine

Workflow Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from torana.core.task import Task
from torana.engine.status import TaskStatus


@dataclass(slots=True)
class Workflow:
    """
    Represents a directed acyclic graph (DAG)
    of Tasks.
    """

    tasks: dict[str, Task] = field(default_factory=dict)

    dependencies: dict[str, set[str]] = field(default_factory=dict)

    dependents: dict[str, set[str]] = field(default_factory=dict)

    # ------------------------------------------

    def add_task(self, task: Task) -> None:

        if task.id in self.tasks:
            raise ValueError(
                f"Task '{task.id}' already exists."
            )

        self.tasks[task.id] = task

        self.dependencies.setdefault(task.id, set())

        self.dependents.setdefault(task.id, set())

    # ------------------------------------------

    def add_dependency(
        self,
        task_id: str,
        depends_on: str,
    ) -> None:

        if task_id not in self.tasks:
            raise KeyError(task_id)

        if depends_on not in self.tasks:
            raise KeyError(depends_on)

        self.dependencies[task_id].add(depends_on)

        self.dependents[depends_on].add(task_id)

    # ------------------------------------------

    def ready_tasks(self) -> list[Task]:

        ready = []

        for task in self.tasks.values():

            if task.status != TaskStatus.CREATED:
                continue

            deps = self.dependencies[task.id]

            if all(
                self.tasks[d].status == TaskStatus.COMPLETED
                for d in deps
            ):
                ready.append(task)

        return ready

    # ------------------------------------------

    @property
    def count(self) -> int:

        return len(self.tasks)