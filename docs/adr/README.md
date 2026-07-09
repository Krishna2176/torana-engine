# Architecture Decision Records

The Architecture Decision Records (ADRs) document the significant architectural decisions made during the development of TORANA Engine.

Each ADR captures:

- Context
- Decision
- Consequences
- Alternatives considered

ADRs provide a permanent historical record of why the architecture evolved in a particular direction.

---

# Current ADRs

| ADR | Title | Status |
|-----|-------|--------|
| 001 | Source Layout | Accepted |
| 002 | Plugin Contract | Accepted |
| 003 | Workflow DAG | Accepted |
| 004 | Task Independence | Accepted |
| 005 | Registry Design | Accepted |
| 006 | Stateless Scheduler | Accepted |
| 007 | Execution Manager | Accepted |
| 008 | Engine Composition | Accepted |

---

# ADR Lifecycle

Architecture decisions are immutable historical records.

If a decision changes significantly:

- Create a new ADR.
- Do not rewrite historical ADRs.

This preserves the architectural evolution of the project.

---

# Related Documentation

Architecture Overview

```
docs/architecture/
```

Specifications

```
docs/specifications/
```

Source Code

```
src/torana/
```