from torana.core.task import Task
from torana.core.workflow import Workflow
from torana.engine.status import TaskStatus


def test_add_task():

    workflow = Workflow()

    workflow.add_task(
        Task(
            id="download",
            name="Download"
        )
    )

    assert workflow.count == 1


def test_dependencies():

    workflow = Workflow()

    download = Task(
        id="download",
        name="Download"
    )

    clip = Task(
        id="clip",
        name="Clip"
    )

    workflow.add_task(download)

    workflow.add_task(clip)

    workflow.add_dependency(
        "clip",
        "download",
    )

    ready = workflow.ready_tasks()

    assert len(ready) == 1

    assert ready[0].id == "download"

    download.status = TaskStatus.COMPLETED

    ready = workflow.ready_tasks()

    assert len(ready) == 1

    assert ready[0].id == "clip"