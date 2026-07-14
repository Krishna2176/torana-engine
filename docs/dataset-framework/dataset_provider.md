# Dataset Discovery

**Component:** Dataset Framework

**Milestone:** Dataset Framework v1.0

**Status:** In Progress

---

# Purpose

Dataset Discovery is responsible for locating datasets that satisfy the requirements of Analysis Plugins.

Rather than requiring Plugins to specify where datasets originate, Plugins declare only their dataset requirements.

The Dataset Framework identifies appropriate Dataset Providers and returns compatible datasets.

This architecture separates analytical implementation from data acquisition.

---

# Design Goals

Dataset Discovery is designed to be:

- Automated
- Provider independent
- Deterministic
- Extensible
- Repeatable

Dataset Discovery should always produce consistent results for identical dataset requirements.

---

# Responsibilities

Dataset Discovery is responsible for:

- Receiving dataset requirements
- Querying registered Dataset Providers
- Identifying compatible datasets
- Returning matching Dataset Manifests
- Supporting automated dataset acquisition

Dataset Discovery does **not**:

- Download datasets
- Validate datasets
- Execute analyses
- Manage workflows
- Maintain provider catalogues

---

# Discovery Workflow

Dataset Discovery follows the workflow below.

```text
Analysis Plugin

↓

Dataset Requirements

↓

Dataset Discovery

↓

Dataset Registry

↓

Registered Providers

↓

Dataset Manifests

↓

Compatible Dataset

↓

Dataset Provider
```

Discovery determines *what* should be acquired.

Dataset Providers determine *how* it is acquired.

---

# Discovery Inputs

Dataset Discovery receives dataset requirements supplied by Analysis Plugins.

Typical requirements include:

- Category
- Dataset Type
- CRS
- Spatial Extent
- Resolution
- Temporal Coverage

The Plugin does not identify a specific provider.

---

# Discovery Process

The discovery process consists of the following stages.

## 1. Receive Requirements

Dataset requirements are supplied by the Plugin.

---

## 2. Query Providers

The Dataset Registry returns all registered Dataset Providers.

---

## 3. Search Provider Catalogues

Each Provider evaluates its own Dataset Manifests.

---

## 4. Identify Compatible Datasets

Providers return Dataset Manifests that satisfy the requested requirements.

---

## 5. Return Results

Dataset Discovery returns one or more compatible Dataset Manifests.

Dataset acquisition occurs later through the selected Provider.

---

# Discovery Criteria

Typical discovery criteria include:

- Dataset Category
- Dataset Type
- CRS
- Spatial Resolution
- Spatial Coverage
- Temporal Coverage
- Provider Availability

Additional criteria may be introduced in future versions.

---

# Collaboration

Dataset Discovery collaborates with:

## Dataset Registry

Obtains registered Dataset Providers.

---

## Dataset Providers

Search provider catalogues.

---

## Dataset Validation

Validates discovered datasets.

---

## Analysis Plugins

Receive discovered datasets.

---

# Design Principles

## Requirement Driven

Plugins declare requirements.

Discovery determines suitable datasets.

---

## Provider Independence

Discovery operates independently of provider implementations.

---

## Multiple Candidates

More than one provider may satisfy a dataset request.

Discovery should support multiple compatible results.

---

## Deterministic Results

Identical requirements should produce identical discovery results.

---

# Future Evolution

Future versions may support:

- Ranking candidate datasets
- Provider prioritization
- Spatial relevance scoring
- Temporal relevance scoring
- Quality scoring
- Cost-aware discovery
- Cached discovery results

---

# Summary

Dataset Discovery provides the intelligence layer of the Dataset Framework.

It transforms dataset requirements into compatible Dataset Manifests while remaining independent of providers, plugins, and analytical implementation.