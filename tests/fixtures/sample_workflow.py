"""
TORANA Engine

Reusable Workflow fixture.
"""

from __future__ import annotations

from torana.core.workflow import Workflow


def create_sample_workflow() -> Workflow:
    """
    Create a reusable Workflow.
    """

    return Workflow()