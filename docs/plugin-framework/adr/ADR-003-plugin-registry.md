# ADR-003 — Plugin Registry

**Status:** Accepted

**Date:** July 2026

**Milestone:** Plugin Framework v1.0

---

# Context

As the number of Plugins grows, the Engine requires a consistent mechanism for discovering, registering, validating, and locating Plugins.

Allowing the Engine or individual Plugins to manage Plugin discovery would create tight coupling, duplicate responsibilities, and reduce extensibility.

TORANA requires a centralized architectural component responsible for Plugin management.

---

# Decision

TORANA introduces a centralized Plugin Registry.

The Plugin Registry is the authoritative management component for all Plugins within the Plugin Framework.

The Registry is responsible for:

- Plugin discovery
- Plugin registration
- Plugin validation
- Plugin lookup
- Plugin lifecycle management

The Engine interacts with Plugins exclusively through the Plugin Registry.

Plugins never register themselves and never communicate directly with the Engine.

---

# Rationale

Centralizing Plugin management provides several architectural benefits.

- Single source of truth for Plugin information.
- Consistent Plugin discovery.
- Simplified validation.
- Reduced coupling between the Engine and Plugins.
- Support for future Plugin tooling.
- Improved extensibility.

The Plugin Registry establishes a clear architectural boundary between the Engine Core and the Plugin Framework.

---

# Alternatives Considered

## Self-Registering Plugins

Each Plugin registers itself during initialization.

Advantages

- Simple implementation.
- Minimal infrastructure.

Disadvantages

- Increased coupling.
- Difficult testing.
- Unpredictable registration order.
- Reduced control over Plugin lifecycle.

---

## Engine-Managed Plugin Collection

The Engine stores and manages all Plugins directly.

Advantages

- Fewer architectural components.
- Straightforward implementation.

Disadvantages

- Violates Engine Core responsibilities.
- Reduces modularity.
- Makes Engine responsible for Plugin management.

---

## Centralized Plugin Registry (Accepted)

A dedicated Plugin Registry manages all Plugin-related operations.

Advantages

- Clear separation of responsibilities.
- Stable Engine Core.
- Consistent Plugin management.
- Extensible architecture.
- Simplified testing.

Trade-offs

- Additional architectural component.
- Registry becomes a critical subsystem.

---

# Consequences

Positive

- Plugin management is centralized.
- Engine Core remains Plugin-agnostic.
- Plugins remain independent of one another.
- Future Plugin categories integrate through the same Registry.
- Plugin discovery and validation become standardized.

Negative

- Registry implementation introduces additional complexity.
- Registry availability becomes essential for Plugin management.

These trade-offs are acceptable because they significantly improve long-term maintainability and extensibility.

---

# Related Documents

- plugin_architecture.md
- plugin_registry.md
- plugin_contract.md
- plugin_manifest.md
- plugin_lifecycle.md

---

# Notes

The Plugin Registry manages Plugins throughout their architectural lifecycle.

It does not execute Plugins, construct Workflows, or participate in runtime execution.

Execution remains the responsibility of the Engine Core.