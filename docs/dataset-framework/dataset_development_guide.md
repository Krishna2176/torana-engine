# Dataset Development Guide

**Component:** Dataset Framework

**Milestone:** Dataset Framework v1.0

**Status:** In Progress

---

# Purpose

This guide describes the recommended approach for implementing Dataset Providers within TORANA.

All Dataset Providers should follow the architectural principles established by the Dataset Framework.

The goal is to ensure consistency, maintainability, and interoperability across all providers.

---

# Development Principles

Dataset Providers should be:

- Modular
- Provider independent
- Testable
- Deterministic
- Reusable

Every provider should implement a single responsibility.

---

# Provider Responsibilities

A Dataset Provider is responsible for:

- Advertising supported datasets
- Discovering datasets
- Acquiring datasets
- Reporting availability

A Dataset Provider should not:

- Execute analyses
- Perform visualization
- Build workflows
- Manage jobs
- Modify Engine behaviour

---

# Dataset Manifest

Every dataset supplied by a provider must expose a Dataset Manifest.

The Dataset Manifest is the authoritative source of dataset metadata.

Providers should never duplicate metadata outside the manifest.

---

# Discovery

Providers participate in Dataset Discovery.

Providers should:

- Search their own catalogue
- Return compatible Dataset Manifests
- Avoid performing expensive operations during discovery

Discovery should remain lightweight.

---

# Acquisition

Providers are responsible for acquiring datasets.

Acquisition may include:

- Local file access
- Database queries
- Remote downloads
- Cloud services

The acquisition mechanism should remain internal to the provider.

---

# Validation

Providers should expose sufficient metadata to support Dataset Validation.

Validation itself belongs to the Dataset Framework rather than individual providers.

---

# Error Handling

Providers should report meaningful errors.

Errors should clearly distinguish between:

- Dataset unavailable
- Provider unavailable
- Network failure
- Authentication failure
- Invalid request

---

# Testing

Every Dataset Provider should include:

- Unit tests
- Integration tests
- Provider validation tests

Reference providers should serve as examples for future implementations.

---

# Future Providers

Examples include:

- Local File Provider
- Google Earth Engine Provider
- STAC Provider
- PostGIS Provider
- OpenStreetMap Provider

Each implementation should remain independent while conforming to the common provider architecture.

---

# Summary

Dataset Providers extend TORANA by supplying datasets through a standardized interface.

Provider implementations should remain independent of the Engine Core and Analysis Plugins while following the architectural principles established by the Dataset Framework.