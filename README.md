# ŌLLIN Fruit Fly Lab

Computational laboratory for reproducible experiments on fruit-fly connectomes.

The project begins from public biological wiring data and keeps three things strictly separate:

1. **measured data** — connectome records and annotations from external scientific sources;
2. **model assumptions** — transforms from anatomy to executable dynamics;
3. **experimental results** — outputs produced by a particular model, dataset, configuration, and seed.

M0 intentionally contains no whole-brain simulator. It establishes project identity, dataset provenance, architecture law, and deterministic qualification before data ingestion or modeling begins.

## Initial scientific targets

- FlyWire/Codex **FAFB v783** — Female Adult Fly Brain.
- FlyWire/Codex **BANC v888** — Female Adult Fly Brain and Nerve Cord.
- Published whole-brain leaky-integrate-and-fire work as a later replication target.
- NeuroMechFly/FlyGym as a later embodied-agent integration target.

See `docs/research/SOURCES.md` for source URLs and the exact current observations used by M0.

## Repository profile

**ŌLLIN Lite — M0.**

The project will promote to ŌLLIN Modular when multiple independently understandable product capabilities exist in code. Candidate future Cells include connectome-data, graph, dynamics, sensory, body/world, experiment, and edge-runtime. They are not created merely because they are imaginable.

## Local qualification

Windows PowerShell:

```powershell
cd D:\Dev\ollin-fruit-fly-lab
python tools\qualification\m0_qualify.py
```

Expected result:

```text
OLLIN FRUIT FLY LAB M0 QUALIFICATION: PASS
```

## Current boundary

M0 does **not**:

- download bulk connectome data;
- claim that a connectome is a complete executable brain;
- infer biological parameters that are not present in the source data;
- train a model;
- run a whole-brain simulation;
- vendor third-party datasets or code.

The next authorized engineering target is M1: deterministic connectome manifest and importer.
