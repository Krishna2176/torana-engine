# Versioning Strategy

TORANA Engine uses **milestone-based versioning** during active development.

Each major framework is developed as an independent milestone. A milestone is versioned, validated, documented, and frozen before development proceeds to the next milestone.

This ensures that development follows a stable, incremental progression with no leapfrogging between frameworks.

---

# Development Philosophy

TORANA follows a sequential development model.

```
Engine Core
      ↓
Plugin Framework
      ↓
Dataset Framework
      ↓
Analysis Framework
      ↓
Visualization Framework
      ↓
Desktop Framework
      ↓
Cloud Framework
```

A new framework does not begin until the previous framework satisfies the Definition of Done.

---

# Internal Milestones

During development, milestones use descriptive version identifiers.

| Milestone | Status |
|-----------|--------|
| engine-core-v1.0 | ❄️ Frozen |
| plugin-framework-v1.0 | 🟡 In Progress |
| dataset-framework-v1.0 | ⚪ Planned |
| analysis-framework-v1.0 | ⚪ Planned |
| visualization-framework-v1.0 | ⚪ Planned |
| desktop-framework-v1.0 | ⚪ Planned |
| cloud-framework-v1.0 | ⚪ Planned |

Each milestone represents a stable architectural subsystem.

---

# Git Tags

Every completed milestone receives a Git tag.

Examples:

```text
engine-core-v1.0

plugin-framework-v1.0

dataset-framework-v1.0
```

Milestone tags should correspond to completed work and documented repository state.

---

# Public Releases

Internal milestones are eventually combined into public releases.

| Version | Description |
|----------|-------------|
| v0.1 | Developer Preview |
| v0.5 | Feature Complete |
| v1.0 | First Stable Production Release |

Future public releases will follow semantic versioning after Version 1.0.

---

# Documentation

Every milestone completion requires updates to:

- CHANGELOG.md
- PROJECT_STATUS.md
- CURRENT_PHASE.md
- MILESTONES.md

where applicable.

---

# Guiding Principle

Version numbers represent **engineering milestones**, not development activity.

A milestone is versioned only after:

- Architecture is complete.
- Documentation is synchronized.
- Tests pass.
- Implementation is validated.
- The milestone satisfies the TORANA Definition of Done.

Only then should a Git tag be created and the milestone marked as **Frozen**.