# Release Process

Every TORANA Engine milestone follows the same release process to ensure consistency, quality, and traceability.

A milestone is not considered complete until every step in this process has been successfully completed.

---

# Phase 1 — Design

## Architecture

- Design the subsystem architecture.
- Define responsibilities.
- Identify interfaces and interactions.
- Review the architecture before implementation.

---

## Documentation

Document the architecture and specifications.

This may include:

- Architecture documents
- Specifications
- Guides
- ADRs

---

## Test Design

Design tests before implementation.

This includes:

- Unit tests
- Expected behaviour
- Edge cases
- Failure scenarios

---

# Phase 2 — Development

## Implementation

Implement the subsystem according to the approved architecture and specifications.

---

## Refactoring

Review and improve the implementation.

Goals include:

- Readability
- Maintainability
- Consistency
- Reduced duplication

---

## Documentation Synchronization

Update documentation to accurately reflect the implementation.

Review and update where required:

- Architecture
- Specifications
- Guides
- CHANGELOG

---

# Phase 3 — Validation

Run the complete test suite.

```bash
python -m pytest
```

All tests must pass before continuing.

Future validation may also include:

- Static analysis
- Type checking
- Performance benchmarks

---

# Phase 4 — Version Control

Commit completed work.

Typical workflow:

```bash
git add .

git commit -m "Meaningful commit message"

git push
```

Create a milestone tag when appropriate.

```bash
git tag <milestone-name>

git push origin <milestone-name>
```

---

# Phase 5 — Project Documentation

Review and update project documentation.

This may include:

- PROJECT_STATUS.md
- CURRENT_PHASE.md
- MILESTONES.md
- CHANGELOG.md

Ensure the repository accurately reflects the current project state.

---

# Milestone Completion

A milestone is considered complete only when:

- Architecture is finalized.
- Documentation is complete.
- Tests have been designed.
- Implementation is complete.
- Refactoring has been performed.
- Documentation matches the implementation.
- All validation steps pass.
- Changes have been committed and pushed.
- Project documentation has been updated.

Only then should the milestone be marked as **Completed** or **Frozen**.