"""
Shared type definitions for the Plugin Framework.
"""

from typing import Literal

PluginCategory = Literal[
    "analysis",
    "dataset",
    "visualization",
    "report",
    "export",
]