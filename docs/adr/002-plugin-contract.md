# ADR 002 — Plugin Contract

**Status:** Accepted

**Date:** July 2026

---

# Context

TORANA requires a mechanism for extending the Engine without modifying its implementation.

New analyses should be added as independent modules while exposing a consistent interface.

---

# Decision

Every analysis is implemented as a Plugin that conforms to a common Plugin contract.

The Engine communicates only through this contract.

Individual Plugin implementations remain independent of the Engine.

---

# Alternatives Considered

## Hardcoded Analyses

Advantages

- Simpler implementation.

Disadvantages

- Poor extensibility.
- Tight coupling.
- Difficult maintenance.

---

## Plugin Contract

Advantages

- Extensible.
- Testable.
- Modular.

---

# Consequences

Advantages

- New analyses require no Engine modifications.
- Consistent interface.
- Future third-party plugins become possible.

Trade-offs

- Plugin authors must implement the required contract.

---

# Notes

The Plugin contract forms the primary extension mechanism of TORANA.