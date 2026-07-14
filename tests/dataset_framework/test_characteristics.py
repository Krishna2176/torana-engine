"""
Tests for DatasetCharacteristics.
"""

from dataclasses import FrozenInstanceError

import pytest

from torana.dataset_framework import (
    DatasetCategory,
    DatasetCharacteristics,
    DatasetDomain,
    DatasetType,
)


@pytest.fixture
def characteristics() -> DatasetCharacteristics:
    return DatasetCharacteristics(
        category=DatasetCategory.ELEVATION,
        dataset_type=DatasetType.RASTER,
        domain=DatasetDomain.TERRAIN,
        crs="EPSG:4326",
        resolution=30.0,
        extent="India",
        tags=("dem",),
    )


def test_characteristics_can_be_created(characteristics):
    assert characteristics is not None


def test_classification(characteristics):
    assert characteristics.category is DatasetCategory.ELEVATION
    assert characteristics.dataset_type is DatasetType.RASTER
    assert characteristics.domain is DatasetDomain.TERRAIN


def test_spatial(characteristics):
    assert characteristics.crs == "EPSG:4326"
    assert characteristics.resolution == 30.0
    assert characteristics.extent == "India"


def test_tags(characteristics):
    assert characteristics.tags == ("dem",)


def test_characteristics_are_immutable(characteristics):
    with pytest.raises(FrozenInstanceError):
        characteristics.crs = "EPSG:3857"


def test_characteristics_use_slots(characteristics):
    with pytest.raises(AttributeError):
        characteristics.new_field = "invalid"