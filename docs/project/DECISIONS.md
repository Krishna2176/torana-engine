---

# ADR Summary — Dataset Framework

## Decision

Dataset metadata is divided into three independent domain models.

### Dataset Characteristics

Represents the intrinsic characteristics of a dataset.

Contains

- Category
- Dataset Type
- Domain
- CRS
- Resolution
- Extent
- Tags

Dataset Characteristics are immutable.

---

### Dataset Requirement

Represents the requirements declared by Analysis Plugins.

A Dataset Requirement contains Dataset Characteristics.

It represents what an analysis requires.

---

### Dataset Manifest

Represents metadata describing an available dataset.

A Dataset Manifest contains

- Identity
- Dataset Characteristics
- Temporal Metadata
- Provider Metadata
- Licensing Metadata

It represents what exists.

---

## Architectural Decision

Dataset Requirement and Dataset Manifest do not inherit from each other.

Both compose Dataset Characteristics.

Reason

The shared fields represent a common domain concept rather than an inheritance relationship.

Composition preserves separation of responsibilities while eliminating duplicated metadata.

---

## Registry Responsibility

Dataset Registry manages Dataset Providers.

Providers own Dataset Manifests.

The Registry never stores Dataset Manifests directly.

---

## Discovery Responsibility

Dataset Discovery discovers compatible Dataset Manifests.

It never acquires datasets.

Acquisition is delegated to Dataset Providers.

---

## Validation Responsibility

Dataset Validation compares Dataset Requirements against Dataset Manifests.

Validation does not interact with Dataset Providers.