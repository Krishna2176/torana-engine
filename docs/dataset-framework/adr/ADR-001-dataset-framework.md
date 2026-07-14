# ADR 001 — Dataset Framework

**Status:** Accepted

**Date:** July 2026

---

# Context

TORANA requires a standardized mechanism for discovering, acquiring, and validating datasets without embedding data source logic into the Engine Core or Analysis Plugins.

Datasets originate from many different sources including local storage, databases, cloud services, and remote APIs.

A dedicated Dataset Framework is required to isolate these concerns.

---

# Decision

Introduce a dedicated Dataset Framework responsible for:

- Dataset metadata
- Dataset Providers
- Dataset Registry
- Dataset Discovery
- Dataset Validation

The Engine Core and Plugin Framework remain independent of dataset acquisition.

---

# Alternatives Considered

## Direct Plugin Acquisition

Advantages

- Simpler implementation.

Disadvantages

- Tight coupling.
- Poor reusability.
- Difficult maintenance.
- Every Plugin duplicates acquisition logic.

---

## Dedicated Dataset Framework

Advantages

- Modular.
- Extensible.
- Provider independent.
- Reusable.
- Testable.

---

# Consequences

Advantages

- Engine remains data-source independent.
- Plugins remain focused on analysis.
- New providers require no Engine changes.

Trade-offs

- Additional framework layer.
- More initial architecture.

---

# Notes

The Dataset Framework becomes the standardized data acquisition layer of TORANA.