# Coding Standards

---

# Language

Python 3.13+

---

# Formatting

PEP 8

Black-compatible formatting

Four-space indentation

Maximum readability

---

# Typing

Type hints are required.

Public APIs must be strongly typed.

Avoid Any whenever possible.

---

# Dataclasses

Domain models use

- frozen=True
- slots=True

unless mutability is required.

---

# Enumerations

Controlled vocabularies use StrEnum.

Free-form strings remain str.

---

# Comments

Explain why.

Avoid comments that merely repeat what code already expresses.

---

# Public API

Every public class requires

- Docstring
- Type hints
- Stable interface