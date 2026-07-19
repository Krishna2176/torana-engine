"""
Tests for DatasetDiscovery.
"""

from __future__ import annotations

from torana.dataset_framework import (
    DatasetDiscovery,
    DatasetRegistry,
)


# ---------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------


def test_discovery_can_be_created():
    registry = DatasetRegistry()

    discovery = DatasetDiscovery(registry)

    assert discovery is not None


# ---------------------------------------------------------------------
# Empty Registry
# ---------------------------------------------------------------------


def test_empty_registry_returns_empty_result(requirement):
    registry = DatasetRegistry()

    discovery = DatasetDiscovery(registry)

    manifests = discovery.discover(requirement)

    assert manifests == ()


# ---------------------------------------------------------------------
# Single Provider
# ---------------------------------------------------------------------


def test_single_provider_returns_manifest(
    provider,
    requirement,
):
    registry = DatasetRegistry()

    registry.register(provider)

    discovery = DatasetDiscovery(registry)

    manifests = discovery.discover(requirement)

    assert len(manifests) == 1

    assert manifests[0].id == "dem_30m"


# ---------------------------------------------------------------------
# Multiple Providers
# ---------------------------------------------------------------------


from tests.dataset_framework.conftest import DummyProvider


def test_multiple_providers_are_aggregated(
    provider,
    requirement,
):
    registry = DatasetRegistry()

    provider2 = DummyProvider(
        provider.manifests[0],
        provider_id="local2",
    )

    registry.register(provider)
    registry.register(provider2)

    discovery = DatasetDiscovery(registry)

    manifests = discovery.discover(requirement)

    assert len(manifests) == 2

# ---------------------------------------------------------------------
# Return Type
# ---------------------------------------------------------------------


def test_discovery_returns_tuple(
    provider,
    requirement,
):
    registry = DatasetRegistry()

    registry.register(provider)

    discovery = DatasetDiscovery(registry)

    manifests = discovery.discover(requirement)

    assert isinstance(
        manifests,
        tuple,
    )