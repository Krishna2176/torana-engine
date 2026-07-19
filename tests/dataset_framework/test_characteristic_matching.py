"""
Tests for DatasetCharacteristics compatibility.
"""

from torana.dataset_framework import (
    DatasetCategory,
    DatasetCharacteristics,
    DatasetDomain,
    DatasetType,
)


def create_characteristics():

    return DatasetCharacteristics(
        category=DatasetCategory.ELEVATION,
        dataset_type=DatasetType.RASTER,
        domain=DatasetDomain.TERRAIN,
        crs="EPSG:4326",
        resolution=30,
        extent="India",
        tags=("dem", "terrain"),
    )


def test_identical_characteristics_are_compatible():

    c = create_characteristics()

    assert c.is_compatible_with(c)


def test_different_category_is_not_compatible():

    source = create_characteristics()

    requirement = DatasetCharacteristics(
        category=DatasetCategory.IMAGERY,
        dataset_type=DatasetType.RASTER,
        domain=DatasetDomain.TERRAIN,
    )

    assert not source.is_compatible_with(requirement)


def test_required_tags_must_exist():

    source = create_characteristics()

    requirement = DatasetCharacteristics(
        category=DatasetCategory.ELEVATION,
        dataset_type=DatasetType.RASTER,
        domain=DatasetDomain.TERRAIN,
        tags=("dem",),
    )

    assert source.is_compatible_with(requirement)