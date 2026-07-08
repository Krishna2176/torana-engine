# TORANA Engine Architecture

## Vision

TORANA Engine is a modular geospatial computation framework that automatically acquires spatial data, performs geospatial analyses, and generates high-quality visualizations for urban planning, design, and research.

---

# Core Principle

Analysis is the source of truth.

Visualization is only a representation of the analysis.

```
Data
    ↓
Analysis
    ↓
Results
    ↓
Visualization
```

---

# System Layers

## Layer 1 — Data

Responsible for acquiring spatial datasets.

Examples:

- DEM
- Buildings
- Roads
- Rainfall
- Land Cover
- Population

---

## Layer 2 — Analysis

Responsible for transforming datasets into useful information.

Examples:

- Flood Analysis
- Urban Heat Analysis
- Walkability Analysis
- Solar Potential
- Noise Analysis

---

## Layer 3 — Visualization

Responsible for communicating results.

Outputs include:

- Maps
- 3D Models
- Interactive Scenes
- Dashboards

---

## Layer 4 — Export

Responsible for delivering outputs.

Examples:

- GeoTIFF
- GeoPackage
- PNG
- GLB
- HTML
- PDF

---

# High-Level Architecture

```
User
    ↓
Project
    ↓
Place
    ↓
Dataset Manager
    ↓
Analysis Engine
    ↓
Visualization Engine
    ↓
Export Engine
```

---

# Design Principles

- Everything is modular.
- Every analysis is independent.
- Datasets are reusable.
- Visualization never changes analysis results.
- Every module should have a single responsibility.