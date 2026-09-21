# Architecture — M0

## Profile

M0 uses **ŌLLIN Lite**. The codebase does not yet contain enough independent implemented capabilities to justify Cells.

## Separation law

The system must preserve this direction:

```text
external scientific source
        |
        v
immutable/raw local artifact + provenance
        |
        v
validated normalized connectome model
        |
        +-------------------+
        |                   |
        v                   v
graph analysis       dynamics assumptions
                            |
                            v
                    executable simulation
                            |
                            v
                    experiment record
```

Measured source data must never be silently rewritten to match a model assumption.

## Candidate future capabilities

These are **promotion candidates**, not M0 directories:

- connectome-data
- graph
- dynamics
- sensory
- body/world
- experiment
- learning
- edge-runtime

When at least two become independently understandable/testable implementation boundaries, the architect may propose promotion to ŌLLIN Modular.
