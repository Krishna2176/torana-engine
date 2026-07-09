"""
TORANA Engine

Job Results
"""

from __future__ import annotations

from dataclasses import dataclass, field

from torana.common.types import OutputCollection, Statistics


@dataclass(slots=True)
class JobResults:
    """
    Outputs produced by a Job.
    """

    outputs: OutputCollection = field(default_factory=dict)

    statistics: Statistics = field(default_factory=dict)

    warnings: list[str] = field(default_factory=list)