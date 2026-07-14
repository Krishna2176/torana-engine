# TORANA Design Principles

---

# Core Principles

## Composition over Inheritance

Reuse behavior through composition.

Inheritance should only model genuine "is-a" relationships.

---

## Immutable Domain Models

Value objects are immutable.

Examples:

- PluginManifest
- DatasetManifest
- DatasetRequirement
- DatasetCharacteristics

---

## Single Responsibility

Each component owns one responsibility.

Examples:

Registry

Stores providers.

Discovery

Finds datasets.

Validation

Checks compatibility.

Providers

Acquire datasets.

---

## Explicit APIs

Framework APIs are explicit and strongly typed.

Magic behavior is avoided.

---

## Separation of Concerns

Analysis

Discovery

Validation

Acquisition

Visualization

Export

remain independent subsystems.