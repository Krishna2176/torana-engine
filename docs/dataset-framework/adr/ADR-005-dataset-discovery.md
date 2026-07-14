# ADR 005 — Dataset Discovery

**Status:** Accepted

**Date:** July 2026

---

# Context

Analysis Plugins should describe dataset requirements without identifying specific providers.

TORANA requires an automated mechanism for matching requirements to available datasets.

---

# Decision

Introduce Dataset Discovery as the component responsible for identifying compatible Dataset Manifests using registered Dataset Providers.

Dataset acquisition occurs only after successful discovery.

---

# Alternatives Considered

## Plugins choose Providers

Advantages

- Simple.

Disadvantages

- Tight coupling.
- Reduced portability.
- Provider-specific Plugins.

---

## Dataset Discovery

Advantages

- Automated.
- Provider independent.
- Extensible.
- Reusable.

---

# Consequences

Advantages

- Plugins remain provider independent.
- New providers integrate transparently.
- Discovery becomes reusable.

Trade-offs

- Additional discovery stage before acquisition.

---

# Notes

Dataset Discovery provides the intelligence layer of the Dataset Framework.