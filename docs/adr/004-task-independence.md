# ADR 004 — Independent Tasks

**Status:** Accepted

**Date:** July 2026

---

# Context

Early designs stored dependency information directly within Tasks.

This tightly coupled Tasks to a specific Workflow.

---

# Decision

Tasks are independent objects.

Dependency management belongs exclusively to the Workflow.

Execution belongs to the Engine.

---

# Alternatives Considered

## Dependencies Inside Tasks

Advantages

- Simple model.

Disadvantages

- Tight coupling.
- Difficult reuse.

---

## Dependencies Inside Workflow

Advantages

- Reusable Tasks.
- Cleaner architecture.
- Better separation of responsibilities.

---

# Consequences

Advantages

- Independent Task model.
- Flexible Workflows.
- Easier testing.

Trade-offs

- Workflow implementation becomes slightly more complex.

---

# Notes

This decision reinforces the Single Responsibility Principle throughout the execution model.