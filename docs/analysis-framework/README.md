# Analysis Framework

## Purpose

The Analysis Framework defines how spatial analyses are described within
TORANA Engine.

An analysis does not execute work.

Instead, it describes:

- required datasets
- configuration
- parameters
- expected outputs

The framework separates analysis description from execution planning.

---

## Components

- Analysis Manifest
- Parameter Schema
- Configuration
- Analysis Context
- Base Analysis
- Analysis Planner

---

## Execution Flow

Analysis

↓

Planner

↓

Workflow

↓

Engine

↓

Execution

---

## Design Principles

- Declarative
- Immutable
- Testable
- Engine Independent
- Plugin Based