# Dataset Manifest

**Component:** Dataset Framework

**Milestone:** Dataset Framework v1.0

**Status:** In Progress

---

# Purpose

The Dataset Manifest is the canonical description of a dataset within TORANA.

Every dataset available to the Engine is represented by exactly one Dataset Manifest.

The Dataset Manifest provides the metadata required for dataset discovery, validation, compatibility checking, and acquisition.

It is the primary source of truth for dataset metadata throughout the Dataset Framework.

---

# Design Goals

The Dataset Manifest is designed to be:

- Immutable
- Type-safe
- Provider independent
- Extensible
- Discoverable
- Machine-readable

The Dataset Manifest describes a dataset.

It does not load, download, process, or validate datasets.

---

# Responsibilities

The Dataset Manifest is responsible for:

- Dataset identity
- Dataset metadata
- Spatial metadata
- Temporal metadata
- Provider metadata
- Licensing information
- Dataset capabilities

The Dataset Manifest does **not**:

- Download datasets
- Read datasets
- Validate datasets
- Manage storage
- Perform analysis

These responsibilities belong to other Dataset Framework components.

---

# Dataset Identity

Every Dataset Manifest defines a unique identity.

Required fields:

- id
- name
- version
- description

The dataset identifier must remain stable across framework versions.

---

# Dataset Classification

Datasets are classified to support discovery.

Required fields:

- category
- type
- domain

Examples

Category

- elevation
- imagery
- transportation
- hydrology
- landcover
- climate

Type

- raster
- vector
- table
- point-cloud

Domain

- urban
- environmental
- climate
- infrastructure

---

# Spatial Metadata

Datasets include spatial properties.

Required fields:

- coordinate reference system (CRS)
- spatial extent
- spatial resolution

Examples

- EPSG:4326
- EPSG:3857

Resolution examples

- 10 m
- 30 m
- 250 m

---

# Temporal Metadata

Datasets describe their temporal characteristics.

Required fields:

- acquisition date
- update frequency

Typical update frequencies include:

- static
- daily
- weekly
- monthly
- yearly

---

# Provider Metadata

Datasets identify their source.

Required fields:

- provider
- provider version

Examples

- Google Earth Engine
- PostGIS
- STAC
- Local Storage

---

# Licensing

Every dataset declares its licensing information.

Required fields:

- license
- attribution

---

# Tags

Datasets may include descriptive tags.

Examples

- DEM
- Sentinel
- Landsat
- NDVI
- Roads
- Buildings

Tags support discovery.

---

# Manifest Relationships

The Dataset Manifest collaborates with several framework components.

Dataset Provider

- Supplies the dataset.

Dataset Registry

- Stores the manifest.

Dataset Discovery

- Searches manifests.

Dataset Validation

- Validates compatibility.

Analysis Plugins

- Request datasets using manifest metadata.

---

# Design Principles

The Dataset Manifest follows several architectural principles.

## Immutable

Dataset metadata should not change during execution.

---

## Provider Independent

The same manifest structure applies regardless of where the dataset originates.

---

## Rich Metadata

The manifest should expose sufficient metadata to support automated discovery.

---

## Single Source of Truth

Every component should obtain dataset metadata from the Dataset Manifest rather than maintaining independent copies.

---

# Future Extensions

Future versions may support:

- Quality metrics
- Confidence scores
- Checksums
- Multiple providers
- Semantic metadata
- Dataset lineage
- Provenance tracking

---

# Summary

The Dataset Manifest is the foundational metadata model of the Dataset Framework.

It enables automated dataset discovery, validation, and acquisition while remaining independent of dataset providers and analysis plugins.