# ADR-001 — Plugin Framework

**Status:** Accepted

**Date:** July 2026

**Milestone:** Plugin Framework v1.0

---

# Context

The Engine Core of TORANA is intentionally small, stable, and independent of domain-specific analysis.

As new analytical capabilities are introduced, modifying the Engine Core for every analysis would violate the principles of modularity, extensibility, and separation of concerns.

TORANA requires a standardized mechanism that allows new analytical capabilities to be added without changing the Engine Core.

---

# Decision

TORANA introduces a dedicated Plugin Framework as the primary extension mechanism for analytical capabilities.

The Plugin Framework defines:

- Plugin architecture
- Plugin contract
- Plugin lifecycle
- Plugin Manifest
- Plugin Registry
- Plugin development standards

The Engine Core remains responsible for orchestration and execution.

The Plugin Framework contributes domain knowledge by constructing Workflows and describing analytical capabilities.

Future analyses are implemented as independent Analysis Plugins that conform to the Plugin Framework.

---

# Rationale

Separating the Plugin Framework from the Engine Core provides several architectural benefits.

- Keeps the Engine Core stable.
- Allows new analyses without modifying the Engine.
- Encourages modular development.
- Establishes a consistent Plugin architecture.
- Simplifies testing and maintenance.
- Enables future third-party Plugin development.

The Plugin Framework becomes the standard extension point for all analytical functionality.

---

# Alternatives Considered

## Embed Analyses in the Engine

Every analysis would be implemented directly within the Engine Core.

Advantages

- Simpler initial implementation.
- Fewer architectural components.

Disadvantages

- Tight coupling.
- Difficult maintenance.
- Engine grows continuously.
- Violates Single Responsibility.
- Reduces extensibility.

---

## Independent Plugin Framework (Accepted)

Analyses are implemented as Plugins that integrate through a dedicated Plugin Framework.

Advantages

- Clear separation of responsibilities.
- Stable Engine Core.
- Extensible architecture.
- Reusable Plugin infrastructure.
- Consistent Plugin development process.

Trade-offs

- Additional architectural components.
- Initial design effort.
- Plugin authors must follow the Plugin Framework.

---

# Consequences

Positive

- Engine Core remains frozen and stable.
- New analyses require no Engine modifications.
- Plugins become reusable architectural units.
- Future frameworks integrate naturally with the Engine.

Negative

- Plugin Framework introduces additional abstractions.
- Plugin authors must understand the Plugin lifecycle and contract.

These trade-offs are considered acceptable because they significantly improve long-term maintainability and scalability.

---

# Related Documents

- plugin_architecture.md
- plugin_contract.md
- plugin_lifecycle.md
- plugin_registry.md
- plugin_development_guide.md

---

# Notes

This ADR establishes the Plugin Framework as the primary architectural extension mechanism for TORANA.

Future Plugin categories—including Dataset Provider Plugins, Visualization Plugins, Report Plugins, and Export Plugins—should build upon this framework rather than extending the Engine Core directly.