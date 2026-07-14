# ADR 004 — Dataset Registry

**Status:** Accepted

**Date:** July 2026

---

# Context

The Engine requires a centralized mechanism for locating available Dataset Providers.

Providers should remain independent while supporting automated discovery.

---

# Decision

The Dataset Registry stores Dataset Providers rather than Dataset Manifests.

Each Provider manages its own catalogue of Dataset Manifests.

---

# Alternatives Considered

## Registry stores Dataset Manifests

Advantages

- Direct lookup.

Disadvantages

- Registry becomes large.
- Provider synchronization required.
- Tight coupling.

---

## Registry stores Providers

Advantages

- Lightweight.
- Provider-centric.
- Scalable.
- Better separation of responsibilities.

---

# Consequences

Advantages

- Registry remains simple.
- Providers own their catalogues.
- Improved scalability.

Trade-offs

- Discovery queries providers dynamically.

---

# Notes

The Dataset Registry is intentionally provider-centric.