# ADR-006

# Stateless Scheduler

## Status

Accepted

---

## Context

A Scheduler was required to determine which Tasks are executable.

The design question was whether the Scheduler should maintain internal execution state.

---

## Decision

The Scheduler is implemented as a stateless component.

It receives a Workflow and returns scheduling decisions without storing execution state.

---

## Consequences

Advantages include:

- deterministic behavior
- thread safety
- improved testing
- future parallel execution

Execution state remains inside the Workflow and ExecutionContext.

---

## Alternatives

A stateful Scheduler maintaining execution progress internally.

This approach was rejected because it tightly couples scheduling with runtime state.

---

## Outcome

Accepted.