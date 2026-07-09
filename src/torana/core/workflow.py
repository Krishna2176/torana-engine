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

    # --------------------------------------------------

    def add_task(self, task: Task) -> None:
        """
        Add a Task to the Workflow.
        """

        if task.id in self.tasks:
            raise ValueError(
                f"Task '{task.id}' already exists."
            )

        self.tasks[task.id] = task

        self.dependencies.setdefault(task.id, set())

        self.dependents.setdefault(task.id, set())

    # --------------------------------------------------

    def add_dependency(
        self,
        task_id: str,
        depends_on: str,
    ) -> None:
        """
        Create a dependency between two Tasks.
        """

        if task_id not in self.tasks:
            raise KeyError(task_id)

        if depends_on not in self.tasks:
            raise KeyError(depends_on)

        self.dependencies[task_id].add(depends_on)

        self.dependents[depends_on].add(task_id)

    # --------------------------------------------------

    def ready_tasks(self) -> list[Task]:
        """
        Return Tasks that are ready to execute.
        """

        ready: list[Task] = []

        for task in self.tasks.values():

            if task.status != TaskStatus.CREATED:
                continue

            deps = self.dependencies[task.id]

            if all(
                self.tasks[dependency].status == TaskStatus.COMPLETED
                for dependency in deps
            ):
                ready.append(task)

        return ready

    # --------------------------------------------------

    def pending_tasks(self) -> list[Task]:
        """
        Return every Task that has not completed.
        """

        return [
            task
            for task in self.tasks.values()
            if task.status != TaskStatus.COMPLETED
        ]

    # --------------------------------------------------

    def completed_tasks(self) -> list[Task]:
        """
        Return every completed Task.
        """

        return [
            task
            for task in self.tasks.values()
            if task.status == TaskStatus.COMPLETED
        ]

    # --------------------------------------------------

    def failed_tasks(self) -> list[Task]:
        """
        Return every failed Task.
        """

        return [
            task
            for task in self.tasks.values()
            if task.status == TaskStatus.FAILED
        ]

    # --------------------------------------------------

    def is_complete(self) -> bool:
        """
        True if every Task has completed.
        """

        return all(
            task.status == TaskStatus.COMPLETED
            for task in self.tasks.values()
        )

    # --------------------------------------------------

    @property
    def count(self) -> int:
        """
        Number of Tasks in the Workflow.
        """

        return len(self.tasks)

    # --------------------------------------------------

    def __len__(self) -> int:
        return self.count