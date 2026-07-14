"""
Tests for DatasetRequirement.
"""

from dataclasses import FrozenInstanceError

import pytest


def test_requirement_creation(requirement):
    assert requirement is not None


def test_requirement_characteristics(requirement):
    c = requirement.characteristics

    assert c.category.value == "elevation"
    assert c.dataset_type.value == "raster"
    assert c.domain.value == "terrain"


def test_requirement_spatial(requirement):
    c = requirement.characteristics

    assert c.crs == "EPSG:4326"
    assert c.resolution == 30.0
    assert c.extent == "India"


def test_requirement_tags(requirement):
    assert requirement.characteristics.tags == ("dem",)


def test_requirement_immutable(requirement):
    with pytest.raises(FrozenInstanceError):
        requirement.characteristics = None


def test_requirement_slots(requirement):
    with pytest.raises(AttributeError):
        requirement.invalid = True