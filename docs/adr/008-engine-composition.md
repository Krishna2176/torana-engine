# ADR-008

# Engine Composition

## Status

Accepted

---

## Context

The Engine required several collaborating components.

A decision was required regarding inheritance versus composition.

---

## Decision

The Engine composes specialized components rather than implementing all behavior itself.

Current composition:

- PluginRegistry
- ExecutionManager

ExecutionManager further composes:

- Scheduler
- TaskExecutor

---

## Consequences

Advantages:

- modular architecture
- dependency injection
- improved testing
- easier extension

New functionality can be added by composing additional components.

---

## Alternatives

A monolithic Engine implementing scheduling, execution, and orchestration internally.

Rejected because it violates the Single Responsibility Principle.

---

## Outcome

Accepted.