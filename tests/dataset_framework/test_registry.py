"""
Tests for DatasetRegistry.
"""

import pytest

from torana.dataset_framework import (
    DatasetRegistry,
    DuplicateProviderError,
    ProviderNotFoundError,
)


def test_registry_creation():
    registry = DatasetRegistry()

    assert registry.count == 0


def test_registration(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    assert registry.count == 1


def test_duplicate_registration(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    with pytest.raises(DuplicateProviderError):
        registry.register(provider)


def test_lookup(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    assert registry.get(provider.id) is provider


def test_missing_provider():
    registry = DatasetRegistry()

    with pytest.raises(ProviderNotFoundError):
        registry.get("missing")


def test_exists(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    assert registry.exists(provider.id)
    assert not registry.exists("missing")


def test_providers_property(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    assert len(registry.providers) == 1


def test_remove(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    registry.remove(provider.id)

    assert registry.count == 0


def test_len(provider):
    registry = DatasetRegistry()

    registry.register(provider)

    assert len(registry) == 1