# Scheduler

**Version:** 0.1

**Status:** Implemented

---

# Purpose

The Scheduler determines which Tasks are ready for execution.

It never executes Tasks.

It never modifies the Workflow.

It never changes Task state.

The Scheduler is a pure decision component.

---

# Responsibilities

The Scheduler is responsible for:

- Querying the Workflow
- Determining executable Tasks
- Reporting pending execution

The Scheduler is NOT responsible for:

- Running Tasks
- Updating Task status
- Managing execution state
- Performing analysis

