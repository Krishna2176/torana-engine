from torana.core.task import Task
from torana.engine.status import TaskStatus


def test_task_defaults():

    task = Task(
        id="download",
        name="Download Sentinel"
    )

    assert task.status == TaskStatus.CREATED

    assert task.metadata == {}


def test_task_string():

    task = Task(
        id="download",
        name="Download Sentinel"
    )

    assert str(task) == "Task<download>"