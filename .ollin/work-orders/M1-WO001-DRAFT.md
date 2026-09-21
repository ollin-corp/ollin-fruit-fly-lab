# M1-WO001 DRAFT — FAFB v783 Deterministic Acquisition

Status: `DRAFT / NOT_AUTHORIZED`

Proposal authority:

`.ollin/milestones/M1-PROPOSAL-R01.md`

## Baseline lock

Implementation branch MUST be created from the exact then-current accepted `main` only after owner acceptance.

At proposal time:

`main = a49992dc425d01e71644ab92ebee66f11e7f1d45`

Before implementation, re-read `main` SHA and tree and fail closed on drift.

## Allowed writes

Expected bounded implementation writes:

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
- `README.md` if command documentation must be added.

No other source area is authorized.

## Runtime writes

Runtime data may only be written beneath:

`.data/fafb/v783/**`

Runtime data MUST remain ignored by Git.

## Intended public surfaces

Implementation should remain small and prefer standard-library Python.

Expected conceptual surfaces:

```text
discover_fafb_products(...)
acquire_product(...)
verify_artifact(...)
build_manifest(...)
verify_manifest(...)
```

Names may change during implementation if necessary, but responsibilities must remain bounded.

## Secret input

Preferred environment variable:

`OLLIN_FLYLAB_CODEX_API_TOKEN`

The implementation must redact query parameters named `api_token`, `token`, or equivalent before logging or manifest persistence.

## Real-data execution

The repository tests MUST NOT require network access or a real token.

Real FAFB acquisition is a qualification action initiated locally by the owner.

The M1 qualification harness may provide two phases:

1. deterministic offline qualification;
2. explicitly invoked real-source acquisition qualification.

## Stop conditions

Fail closed on:

- baseline mismatch;
- unknown dataset/version;
- missing required product;
- token missing when the source endpoint requires one;
- HTTP/non-data error body;
- invalid gzip;
- missing required CSV identity columns;
- file hash mismatch;
- attempted overwrite of accepted bytes;
- secret leakage detection;
- Git tracking of runtime source data.

## Completion condition

M1-WO001 is complete only after the real FAFB v783 core bundle exists locally and the generated manifest can be re-validated offline with all hashes PASS.
