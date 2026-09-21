# M1-WO001 DRAFT R02 — Direct FAFB v783 Acquisition

Status: `DRAFT / NOT_AUTHORIZED`

Proposal authority:

`.ollin/milestones/M1-PROPOSAL-R02.md`

## Baseline lock

Implementation MUST begin from the exact then-current accepted `main` after owner acceptance.

Proposal-time main:

`a49992dc425d01e71644ab92ebee66f11e7f1d45`

Before any implementation write:

1. re-read remote `main` SHA;
2. re-read remote `main` tree;
3. compare against owner-authorized baseline;
4. fail closed on drift.

## Allowed repository writes

- `src/ollin_flylab/acquisition/**`
- `tests/unit/**`
- `tests/qualification/**`
- `tests/fixtures/**`
- `tools/qualification/m1_qualify.py`
- `tools/data/**`
- `docs/guides/**`
- `docs/research/**`
- `.ollin/evidence/**`
- `.ollin/state/**`
- `.ollin/handoff/**`
- `.ollin/work-orders/M1-WO001.md`
- `.gitignore`
- `CHANGELOG.md`
- `README.md` if local command documentation is required.

No other implementation area is authorized.

## Runtime writes

Runtime data may only be written beneath:

`.data/fafb/v783/**`

These bytes MUST remain outside Git.

## Network boundary

Permitted network purpose:

- direct acquisition or existence-check of explicitly constructed public FAFB v783 static objects.

Initial permitted host:

`storage.googleapis.com`

Initial permitted path prefix:

`/flywire-data/codex/data/fafb/783/`

Prohibited:

- Codex query API;
- Codex download-resource API;
- CAVE;
- Google sign-in automation;
- credential/token handling;
- HTML scraping;
- arbitrary URL fetching.

## Candidate static files

Required metadata:

- `neurons.csv.gz`
- `classification.csv.gz`
- `consolidated_cell_types.csv.gz`

Required connectivity semantics:

- an unthresholded connectivity table.

Probe candidates in this order:

1. `connections_princeton_no_threshold.csv.gz`
2. `connections_no_threshold.csv.gz`

Do not silently fall back to `connections.csv.gz`.

## Intended public surfaces

Prefer standard-library Python.

Conceptual surfaces:

```text
StaticArtifactSpec
probe_static_artifact(...)
acquire_static_artifact(...)
verify_artifact(...)
build_manifest(...)
verify_manifest(...)
```

Exact names may change if tests demonstrate a better bounded design.

## Real-data execution

Repository unit/qualification tests MUST NOT download the real brain dataset.

Real acquisition is an explicit owner-local qualification action.

Implementation should expose:

1. offline/synthetic qualification;
2. static-source probe;
3. explicit real acquisition;
4. offline real-data re-validation.

## Stop conditions

Fail closed on:

- baseline mismatch;
- source URL outside allowlist;
- redirect outside allowlist;
- required unthresholded connectivity file unavailable;
- HTTP error body;
- zero-length response;
- invalid gzip;
- missing minimum source columns;
- hash mismatch;
- attempted overwrite of accepted different bytes;
- runtime data tracked by Git;
- any credential/token requirement introduced by implementation.

## Completion condition

M1-WO001 is complete only when:

1. the real FAFB v783 required bundle is present locally;
2. the connectivity artifact is explicitly unthresholded;
3. all accepted bytes are SHA-256 bound;
4. the manifest validates deterministically;
5. the entire accepted bundle re-validates offline;
6. M0 qualification still passes.
