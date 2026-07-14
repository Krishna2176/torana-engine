# Dataset Registry

**Component:** Dataset Framework

**Milestone:** Dataset Framework v1.0

**Status:** In Progress

---

# Purpose

The Dataset Registry manages Dataset Providers within TORANA.

Rather than storing datasets directly, the Registry maintains a collection of registered Dataset Providers.

Each Dataset Provider is responsible for exposing the Dataset Manifests that it can supply.

This architecture keeps provider-specific knowledge isolated from the Engine.

---

# Design Goals

The Dataset Registry is designed to be:

- Lightweight
- Provider-centric
- Extensible
- Testable
- Independent of specific data sources

---

# Responsibilities

The Dataset Registry is responsible for:

- Registering Dataset Providers
- Removing Dataset Providers
- Looking up Dataset Providers
- Enumerating available Dataset Providers
- Supporting Dataset Discovery

The Dataset Registry does **not**:

- Store datasets
- Download datasets
- Validate datasets
- Execute analyses
- Manage workflows

These responsibilities belong to Dataset Providers and other Dataset Framework components.

---

# Registry Model

The Dataset Registry stores Dataset Providers.

```text
Dataset Registry

│

├── Local Provider

├── Google Earth Engine Provider

├── STAC Provider

├── PostGIS Provider
```

Each provider exposes its own Dataset Manifests.

---

# Registration

Providers register with the Dataset Registry during application initialization.

Each Provider must define a unique identifier.

Duplicate registrations are not permitted.

---

# Lookup

The Registry supports lookup by Provider identifier.

Provider lookup enables Dataset Discovery to query available data sources.

---

# Enumeration

The Registry provides access to all registered Dataset Providers.

Dataset Discovery uses this capability to identify providers capable of satisfying dataset requirements.

---

# Collaboration

The Dataset Registry collaborates with:

## Dataset Providers

Registers and manages providers.

---

## Dataset Discovery

Uses registered providers to locate datasets.

---

## Engine Core

Provides a centralized catalogue of available providers.

---

# Design Principles

## Provider Ownership

Providers own Dataset Manifests.

The Registry owns Providers.

---

## Provider Independence

Each Provider manages its own catalogue independently.

---

## Extensibility

New data sources are introduced by registering additional Providers.

The Registry itself remains unchanged.

---

# Future Evolution

Future versions may support:

- Provider priorities
- Provider capabilities
- Provider health monitoring
- Dynamic provider loading
- Remote provider registration

---

# Summary

The Dataset Registry establishes a centralized catalogue of Dataset Providers while delegating dataset-specific knowledge to individual Providers.

This separation allows the Dataset Framework to scale to large collections of datasets without increasing the complexity of the Registry.