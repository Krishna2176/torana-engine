# ADR 003 — Workflow as a Directed Acyclic Graph

**Status:** Accepted

**Date:** July 2026

---

# Context

Geospatial analyses frequently contain independent processing stages that can execute in parallel.

A simple ordered list of Tasks would unnecessarily limit execution flexibility.

---

# Decision

Every Workflow is represented as a Directed Acyclic Graph (DAG).

Tasks remain independent.

The Workflow owns dependency relationships.

---

# Alternatives Considered

## Linear Task List

Advantages

- Simpler implementation.

Disadvantages

- No parallel execution.
- Limited flexibility.
- Difficult optimization.

---

## Directed Acyclic Graph

Advantages

- Dependency tracking.
- Parallel execution.
- Future distributed execution.

---

# Consequences

Advantages

- Scalable scheduling.
- Cleaner architecture.
- Better reuse of Tasks.

Trade-offs

- Slightly more complex implementation.

---

# Notes

The DAG architecture enables future scheduling strategies without changing the Engine API.