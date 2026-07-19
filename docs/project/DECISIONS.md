# ADR-004

## Analysis Framework Separation

Status

Accepted

---

Analysis plugins are purely declarative.

They define:

- configuration
- parameter schema
- datasets
- outputs

They never execute work.

Workflow construction is delegated to an Analysis Planner.

Execution remains the responsibility of the Engine.

---

Reason

This keeps analyses independent from execution while allowing multiple
planning strategies to exist for the same analysis.