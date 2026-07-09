from torana.core.job import Job
from torana.core.job_specification import JobSpecification
from torana.engine.status import JobStatus


def test_create_job():

    specification = JobSpecification(
        plugin_id="uhi",
        configuration={}
    )

    job = Job(specification=specification)

    assert job.specification.plugin_id == "uhi"

    assert job.runtime.status == JobStatus.CREATED

    assert job.runtime.progress == 0.0

    assert job.results.outputs == {}


def test_job_has_uuid():

    specification = JobSpecification(
        plugin_id="uhi",
        configuration={}
    )

    job = Job(specification=specification)

    assert job.id is not None


def test_job_specification_is_immutable():

    specification = JobSpecification(
        plugin_id="uhi",
        configuration={}
    )

    try:
        specification.plugin_id = "flood"
        assert False
    except Exception:
        assert True