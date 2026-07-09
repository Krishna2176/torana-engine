# ADR 001 — Source Layout

**Status:** Accepted

**Date:** July 2026

---

# Context

TORANA is intended to grow into a large modular geospatial framework.

A consistent project structure is essential for maintainability, packaging, testing, and future collaboration.

The project required a layout that clearly separates implementation, documentation, tests, configuration, and generated outputs.

---

# Decision

The project adopts the modern Python **src layout**.

Application code resides exclusively within:

```text
src/
    torana/
```

Supporting resources are organized into dedicated top-level directories such as:

- docs/
- tests/
- configs/
- data/
- outputs/
- scripts/

---

# Alternatives Considered

## Flat Layout

Python modules stored directly at the project root.

Advantages:

- Simpler for very small projects.

Disadvantages:

- Higher risk of accidental imports.
- Less suitable for packaging.
- Poor scalability.

---

## Multiple Independent Packages

Separating every subsystem into its own package.

Advantages:

- Maximum modularity.

Disadvantages:

- Unnecessary complexity during early development.

---

# Consequences

Advantages

- Clear project organization.
- Standard Python packaging.
- Better testing isolation.
- Easier future distribution.

Trade-offs

- Slightly more verbose imports.
- Requires editable installation during development.

---

# Notes

The chosen layout follows modern Python packaging recommendations and provides a scalable foundation for future development.