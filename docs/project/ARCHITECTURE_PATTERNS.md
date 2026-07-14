# Architecture Patterns

---

# Value Object

Immutable domain models.

Examples

- PluginManifest
- DatasetManifest
- DatasetCharacteristics

---

# Registry

Owns a collection of components.

Examples

- PluginRegistry
- DatasetRegistry

---

# Service

Contains behavior without owning domain state.

Examples

- DatasetDiscovery
- DatasetValidation

---

# Provider

Represents an external capability.

Examples

- DatasetProvider
- Google Earth Engine Provider
- Local Provider

---

# Composition

Prefer

Object A contains Object B

instead of inheritance whenever ownership is not an "is-a" relationship.

Example

DatasetManifest

contains

DatasetCharacteristics

rather than inheriting from it.

---

# Dependency Injection

Dependencies are provided externally.

Framework components should avoid constructing their own collaborators.

---

# Frozen Frameworks

Once a framework reaches version 1.0,

its public API becomes stable.

Subsequent improvements should preserve backward compatibility whenever practical.