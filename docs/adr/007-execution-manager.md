# ADR-007

# Execution Manager

## Status

Accepted

---

## Context

Initially the Engine coordinated execution directly.

As responsibilities increased, orchestration logic risked making the Engine difficult to maintain.

---

## Decision

Introduce an ExecutionManager responsible for coordinating execution.

The Engine validates Jobs and delegates execution immediately.

---

## Consequences

Advantages:

- smaller Engine
- improved separation of concerns
- easier testing
- extensibility

Future execution features naturally belong inside the ExecutionManager.

---

## Alternatives

Keeping execution loops inside the Engine.

Rejected because it would gradually turn the Engine into a God Object.

---

## Outcome

Accepted.