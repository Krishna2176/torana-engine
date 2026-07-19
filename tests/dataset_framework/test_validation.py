"""
Tests for DatasetValidation.
"""

from torana.dataset_framework import (
    DatasetValidation,
)


def test_validation_accepts_matching_dataset(
    manifest,
    requirement,
):

    validation = DatasetValidation()

    assert validation.validate(
        requirement,
        manifest,
    )


def test_validation_returns_bool(
    manifest,
    requirement,
):

    validation = DatasetValidation()

    result = validation.validate(
        requirement,
        manifest,
    )

    assert isinstance(
        result,
        bool,
    )