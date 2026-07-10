# ADR-002 — Plugin Manifest

**Status:** Accepted

**Date:** July 2026

**Milestone:** Plugin Framework v1.0

---

# Context

Every Plugin requires descriptive information that allows the Plugin Framework to identify, classify, validate, and manage Plugins independently of their implementation.

Without a standardized metadata model, Plugins would expose inconsistent information, making discovery, validation, compatibility checking, and future tooling significantly more difficult.

TORANA requires a consistent architectural representation of Plugin identity and capabilities.

---

# Decision

Every Plugin shall provide a standardized Plugin Manifest.

The Plugin Manifest serves as the authoritative description of a Plugin and contains all information required for identification, classification, compatibility, and administration.

The Plugin Manifest is separate from Plugin implementation and remains independent of runtime execution.

The Plugin Framework relies on the Plugin Manifest for discovery, validation, and Plugin management.

---

# Rationale

Separating Plugin description from Plugin implementation provides several architectural benefits.

- Standardized Plugin metadata.
- Consistent Plugin discovery.
- Simplified validation.
- Framework-independent Plugin management.
- Improved documentation.
- Support for future Plugin tooling.

The Plugin Manifest becomes the single source of truth describing every Plugin.

---

# Alternatives Considered

## Metadata Embedded in Plugin Classes

Plugin information would be defined directly within Plugin implementation classes.

Advantages

- Simpler implementation.
- Fewer architectural components.

Disadvantages

- Tight coupling between metadata and implementation.
- Difficult Plugin discovery.
- Reduced flexibility.
- Harder validation and tooling.

---

## Dedicated Plugin Manifest (Accepted)

Plugin description is separated into a standardized Plugin Manifest.

Advantages

- Consistent Plugin identification.
- Independent validation.
- Improved maintainability.
- Extensible metadata model.
- Future support for Plugin repositories and tooling.

Trade-offs

- Requires maintaining an additional architectural component.
- Plugin authors must provide Manifest information.

---

# Consequences

Positive

- Every Plugin exposes a consistent description.
- Plugin Registry can operate independently of Plugin implementation.
- Future Plugin categories share the same descriptive model.
- Documentation and tooling become easier to automate.

Negative

- Plugin authors must maintain both implementation and Manifest information.
- Changes to the Manifest structure require careful versioning within the Plugin Framework.

These trade-offs are acceptable because they significantly improve consistency and extensibility.

---

# Related Documents

- plugin_architecture.md
- plugin_metadata.md
- plugin_registry.md
- plugin_contract.md

---

# Notes

The Plugin Manifest is an architectural description of a Plugin.

It does not contain runtime state, execution logic, or analysis implementation.

Its purpose is to describe a Plugin in a standardized manner so that the Plugin Framework can manage Plugins consistently throughout their lifecycle.