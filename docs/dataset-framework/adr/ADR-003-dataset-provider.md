# ADR 003 — Dataset Provider

**Status:** Accepted

**Date:** July 2026

---

# Context

Datasets originate from multiple independent systems.

The Engine should not communicate directly with those systems.

---

# Decision

Introduce Dataset Providers as the abstraction responsible for dataset discovery and acquisition.

Each Provider encapsulates one data source.

---

# Alternatives Considered

## Engine-managed Acquisition

Advantages

- Centralized.

Disadvantages

- Tight coupling.
- Difficult extension.
- Engine complexity.

---

## Provider Architecture

Advantages

- Modular.
- Replaceable.
- Testable.
- Extensible.

---

# Consequences

Advantages

- New providers require no Engine modifications.
- Acquisition logic remains isolated.

Trade-offs

- Additional abstraction layer.

---

# Notes

Dataset Providers establish the extension mechanism of the Dataset Framework.