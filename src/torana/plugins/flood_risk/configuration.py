"""
Configuration model for the Flood Risk Plugin.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FloodRiskConfiguration:
    """
    Configuration for Flood Risk analysis.

    This model defines the user-supplied parameters required
    to construct the Flood Risk workflow.

    It does not perform validation.
    """

    dem_dataset: str

    rainfall_dataset: str

    output_resolution: float = 30.0

    include_exposure: bool = False