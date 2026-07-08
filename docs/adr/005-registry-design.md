# ADR 005 — Central Plugin Registry

**Status:** Accepted

**Date:** July 2026

---

# Context

The Engine must locate Plugins without containing knowledge of individual analyses.

A centralized discovery mechanism was required.

---

# Decision

A dedicated Plugin Registry manages Plugin registration and discovery.

The Engine interacts only with the Registry.

---

# Alternatives Considered

## Direct Imports

Advantages

- Simple implementation.

Disadvantages

- Tight coupling.
- Difficult extension.

---

## Central Registry

Advantages

- Loose coupling.
- Dynamic discovery.
- Scalable architecture.

---

# Consequences

Advantages

- Cleaner Engine.
- Easier Plugin management.
- Future automatic discovery.

Trade-offs

- Additional infrastructure component.

---

# Notes

The Registry acts as the single source of truth for available Plugins.