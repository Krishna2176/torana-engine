"""
Tests for DatasetManifest.
"""

from dataclasses import FrozenInstanceError

import pytest

from torana.dataset_framework import UpdateFrequency


def test_manifest_creation(manifest):
    assert manifest is not None


def test_identity(manifest):
    assert manifest.id == "dem_30m"
    assert manifest.name == "30m Digital Elevation Model"
    assert manifest.version == "1.0.0"


def test_characteristics(manifest):
    assert manifest.characteristics.category.value == "elevation"
    assert manifest.characteristics.dataset_type.value == "raster"
    assert manifest.characteristics.domain.value == "terrain"


def test_temporal(manifest):
    assert manifest.acquisition_date == "2025-01-01"
    assert manifest.update_frequency is UpdateFrequency.STATIC


def test_provider(manifest):
    assert manifest.provider == "Local Provider"
    assert manifest.provider_version == "1.0.0"


def test_license(manifest):
    assert manifest.license == "CC BY 4.0"
    assert manifest.attribution == "TORANA"


def test_identifier(manifest):
    assert manifest.identifier == "dem_30m"


def test_immutable(manifest):
    with pytest.raises(FrozenInstanceError):
        manifest.name = "Modified"


def test_slots(manifest):
    with pytest.raises(AttributeError):
        manifest.invalid = True