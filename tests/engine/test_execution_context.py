from torana.core.job import Job
from torana.core.job_specification import JobSpecification

from torana.engine.execution_context import ExecutionContext


def create_job() -> Job:
    specification = JobSpecification(
        plugin_id="uhi",
        configuration={}
    )

    return Job(specification=specification)


def test_create_execution_context():

    job = create_job()

    context = ExecutionContext(job=job)

    assert context.job is job


def test_default_progress():

    context = ExecutionContext(job=create_job())

    assert context.state.progress == 0.0


def test_default_outputs():

    context = ExecutionContext(job=create_job())

    assert context.resources.outputs == {}


def test_services_are_none_by_default():

    context = ExecutionContext(job=create_job())

    assert context.services.logger is None
    assert context.services.cache is None