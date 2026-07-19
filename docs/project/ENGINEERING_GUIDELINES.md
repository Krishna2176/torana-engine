# TORANA Engineering Guidelines

Version: 1.1

---

# Engineering Philosophy

TORANA is developed from the architecture downward.

Every implementation must have a clearly defined architectural purpose.

---

# Development Workflow

Architecture

↓

Documentation

↓

Public API

↓

Tests

↓

Implementation

↓

Refinement

↓

Freeze

---

# Framework Lifecycle

Planning

↓

Architecture

↓

Implementation

↓

Testing

↓

Documentation

↓

Freeze

Frozen frameworks are considered stable.

Future work extends them rather than redesigning them.

---

# Demand-Driven Implementations

Frameworks define contracts.

Implementations satisfy contracts.

Analysis Plugins define Dataset Requirements.

Dataset Providers evolve to satisfy those requirements.

Avoid speculative implementations.

---

# Architecture First

Do not introduce abstractions until they naturally emerge.

Extract common concepts only after they demonstrate reuse.

Prefer composition over inheritance.

---

# Public APIs

Public APIs are explicit.

Public APIs are strongly typed.

Public APIs remain stable after framework freeze.

---

# Testing

Every public component requires automated tests.

Tests are considered part of implementation.

---

# Documentation

Documentation must always match implementation.

Every framework freeze requires documentation review.