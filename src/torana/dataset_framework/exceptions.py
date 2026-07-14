"""
Exceptions for the TORANA Dataset Framework.
"""

from __future__ import annotations


class DatasetFrameworkError(Exception):
    """
    Base exception for all Dataset Framework errors.
    """

    pass


# ---------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------


class DatasetRegistrationError(DatasetFrameworkError):
    """
    Raised when a Dataset Provider cannot be registered.
    """

    pass


class DuplicateProviderError(DatasetRegistrationError):
    """
    Raised when attempting to register a Provider
    whose identifier already exists.
    """

    pass


class ProviderNotFoundError(DatasetRegistrationError):
    """
    Raised when a requested Dataset Provider
    cannot be found.
    """

    pass


# ---------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------


class DatasetDiscoveryError(DatasetFrameworkError):
    """
    Raised when dataset discovery fails.
    """

    pass


class DatasetNotFoundError(DatasetDiscoveryError):
    """
    Raised when no compatible dataset
    can be discovered.
    """

    pass


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------


class DatasetValidationError(DatasetFrameworkError):
    """
    Raised when dataset validation fails.
    """

    pass


class InvalidDatasetError(DatasetValidationError):
    """
    Raised when a dataset is invalid or incompatible.
    """

    pass


# ---------------------------------------------------------------------
# Providers
# ---------------------------------------------------------------------


class DatasetProviderError(DatasetFrameworkError):
    """
    Base exception raised by Dataset Providers.
    """

    pass


class DatasetUnavailableError(DatasetProviderError):
    """
    Raised when a dataset cannot be acquired.
    """

    pass


class ProviderUnavailableError(DatasetProviderError):
    """
    Raised when a Dataset Provider is unavailable.
    """

    pass