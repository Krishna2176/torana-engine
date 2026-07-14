"""
Tests for BaseProvider.
"""


def test_provider_creation(provider):
    assert provider is not None


def test_provider_identity(provider):
    assert provider.id == "local"
    assert provider.name == "Local Provider"
    assert provider.version == "1.0.0"


def test_provider_catalogue(provider):
    manifests = provider.manifests

    assert len(manifests) == 1
    assert manifests[0].id == "dem_30m"


def test_provider_discovery(
    provider,
    requirement,
):
    manifests = provider.discover(requirement)

    assert len(manifests) == 1


def test_provider_availability(provider):
    assert provider.is_available("dem_30m")
    assert not provider.is_available("other")


def test_provider_acquisition(provider):
    dataset = provider.acquire("dem_30m")

    assert dataset["dataset_id"] == "dem_30m"