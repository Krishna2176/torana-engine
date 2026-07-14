# ADR 002 — Dataset Manifest

**Status:** Accepted

**Date:** July 2026

---

# Context

Datasets require significantly richer metadata than Plugins.

The Engine must understand dataset characteristics to support automated discovery, validation, and provider selection.

---

# Decision

Every dataset is represented by an immutable Dataset Manifest.

The Dataset Manifest serves as the authoritative description of dataset metadata.

All Dataset Framework components rely on the Dataset Manifest.

---

# Alternatives Considered

## Provider-specific Metadata

Advantages

- Flexible.

Disadvantages

- Inconsistent.
- Difficult discovery.
- Tight coupling.

---

## Standard Dataset Manifest

Advantages

- Consistent.
- Machine-readable.
- Provider independent.
- Supports automated discovery.

---

# Consequences

Advantages

- Standard metadata model.
- Simplified validation.
- Reusable discovery.

Trade-offs

- Providers must construct Dataset Manifests.

---

# Notes

The Dataset Manifest is the central metadata model of the Dataset Framework.