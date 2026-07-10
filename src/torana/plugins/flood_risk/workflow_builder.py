"""
Workflow builder for the Flood Risk Plugin.
"""

from __future__ import annotations

from torana.core.task import Task
from torana.core.workflow import Workflow


def build_workflow() -> Workflow:
    """
    Construct the reference workflow for the Flood Risk Plugin.

    This workflow demonstrates how a Plugin defines an execution
    plan without performing any analytical work.
    """

    workflow = Workflow()

    # ------------------------------------------------------------------
    # Create Tasks
    # ------------------------------------------------------------------

    load_dem = Task(
        id="load_dem",
        name="Load DEM",
        description="Load the Digital Elevation Model.",
    )

    load_rainfall = Task(
        id="load_rainfall",
        name="Load Rainfall",
        description="Load rainfall data.",
    )

    compute_flood_risk = Task(
        id="compute_flood_risk",
        name="Compute Flood Risk",
        description="Compute flood risk analysis.",
    )

    produce_outputs = Task(
        id="produce_outputs",
        name="Produce Outputs",
        description="Produce analytical outputs.",
    )

    # ------------------------------------------------------------------
    # Add Tasks
    # ------------------------------------------------------------------

    workflow.add_task(load_dem)
    workflow.add_task(load_rainfall)
    workflow.add_task(compute_flood_risk)
    workflow.add_task(produce_outputs)

    # ------------------------------------------------------------------
    # Define Dependencies
    # ------------------------------------------------------------------

    workflow.add_dependency(
        "load_rainfall",
        "load_dem",
    )

    workflow.add_dependency(
        "compute_flood_risk",
        "load_rainfall",
    )

    workflow.add_dependency(
        "produce_outputs",
        "compute_flood_risk",
    )

    return workflow