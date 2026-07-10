from dataclasses import dataclass, field

from .types import PluginCategory


@dataclass(frozen=True, slots=True)
class PluginManifest:
    """
    Immutable description of a TORANA Plugin.

    The Plugin Manifest contains all metadata required to identify,
    classify, and manage a Plugin independently of its implementation.
    """

    #
    # Identity
    #

    id: str
    name: str
    version: str
    description: str

    #
    # Classification
    #

    category: PluginCategory
    domain: str

    #
    # Capabilities
    #

    capabilities: tuple[str, ...] = field(default_factory=tuple)

    #
    # Compatibility
    #

    framework_version: str = "1.0"

    #
    # Administration
    #

    author: str = ""
    license: str = ""
    documentation: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)