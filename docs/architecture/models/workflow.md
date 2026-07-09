# Workflow

**Version:** 0.2

---

# Purpose

A Workflow describes the execution order of Tasks.

It contains no execution logic.

---

# Responsibilities

Workflow manages:

- Tasks
- Dependencies
- Execution graph

It does not execute Tasks.

---

# Architecture

```
Workflow

├── Task A

├── Task B

├── Task C

└── Dependencies
```

Internally TORANA models a Workflow as a Directed Acyclic Graph (DAG).

---

# Relationship with Execution Context

A Workflow becomes part of the Execution Context during execution.

The Scheduler traverses the Workflow.

The Task Executor executes Tasks.

---

# Design Principles

- Directed Acyclic Graph
- Independent Tasks
- Scheduler controlled
- Reusable execution plans

---

# Current Status

Implemented.

Future Scheduler development will consume Workflows to determine executable Tasks.