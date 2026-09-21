# M1 Proposal R01 — Deterministic Connectome Acquisition

Status: `PROPOSAL_R01 / OWNER_REVIEW_PENDING`

Baseline:

- main SHA: `a49992dc425d01e71644ab92ebee66f11e7f1d45`
- M0 accepted software baseline: `a99aefcaa4f667d47fd4a9a3ac2e750824139974`
- M0 accepted tree: `8f48f2d3cfd0b4ee54c1b48c5cbe88c0c897b02d`

## Objective

Acquire one public FlyWire connectome snapshot reproducibly, preserve the downloaded artifacts as immutable local source data, and emit deterministic provenance sufficient to re-validate the same artifacts offline.

M1 does not normalize graph semantics and does not simulate neurons.

## Dataset selected

`FAFB v783` — Female Adult Fly Brain.

Rationale:

1. it is the public whole-brain dataset underlying the original FlyWire whole-brain release;
2. M0 already pins the dataset identity;
3. the current Codex FAQ identifies v783 as the latest public FAFB release;
4. Codex explicitly recommends static downloads for bulk/programmatic analysis.

BANC is deferred until the acquisition path is qualified once on FAFB.

## Acquisition authority

Primary user-facing source:

`https://codex.flywire.ai/api/download?dataset=fafb`

Programmatic resource form documented by Codex:

`https://codex.flywire.ai/api/download_resource?data_product=<PRODUCT>&dataset=fafb&api_token=<TOKEN>`

Authentication material is runtime-only.

A Codex API token:

- MUST NOT be committed;
- MUST NOT appear in logs/evidence;
- MUST NOT be embedded in manifests;
- MUST be supplied through an environment variable or interactive local input.

## M1 core bundle

M1 targets the minimum bundle needed to preserve connectome topology plus essential neuron identity/annotation data for M2/M3.

Required logical products:

1. `connections_princeton_no_threshold` — preferred complete connectivity table if exposed by the current portal;
2. `neurons` — neuron metadata including neurotransmitter prediction fields;
3. `classification` — hierarchical neuron classification;
4. `consolidated_cell_types` — consolidated cell-type annotations.

The exact product inventory MUST be discovered from the current Codex download portal during implementation.

If `connections_princeton_no_threshold` is unavailable under that exact product key, M1 MUST fail closed and report the available connectivity products. It MUST NOT silently substitute a thresholded table.

Optional products such as coordinates, labels, cell statistics, connectivity tags, NBLAST data, raw synapse-coordinate tables, meshes, and skeletons are explicitly outside the M1 required bundle.

## Local storage

Ignored runtime root:

`.data/fafb/v783/`

Proposed shape:

```text
.data/
└── fafb/
    └── v783/
        ├── raw/
        │   ├── <downloaded source artifacts>
        │   └── ...
        ├── manifests/
        │   ├── acquisition.json
        │   └── acquisition.sha256
        └── staging/
```

`raw/` becomes read-only-by-convention after successful acceptance.

No bulk source artifact is committed to Git.

## Deterministic manifest

For every accepted artifact M1 records:

- dataset: `fafb`
- dataset_version: `783`
- logical data product
- original filename
- canonical request URL with secret parameters redacted
- byte size
- SHA-256
- acquisition UTC timestamp
- media/compression type when known
- acquisition tool/version
- source/license identifier
- validation status

The manifest itself is canonical JSON with deterministic key ordering and UTF-8 encoding.

The manifest digest is recorded separately.

## Download behavior

The downloader MUST:

1. create a staging file;
2. stream bytes rather than holding the full connectivity file in memory;
3. compute SHA-256 while streaming;
4. close and flush the staging file;
5. reject empty/truncated/error-body artifacts;
6. validate gzip readability for `.gz` products;
7. inspect the CSV header without fully extracting the file;
8. atomically move the accepted artifact into `raw/`;
9. never overwrite an accepted artifact with different bytes;
10. re-use and re-validate an already accepted matching artifact offline.

No automatic retry loop may hammer Codex. Retries must be bounded.

## Minimum schema guards

These are acquisition guards, not the M2 normalized schema.

Connectivity product must expose columns corresponding to:

- presynaptic neuron/root ID;
- postsynaptic neuron/root ID;
- synapse count.

Neuron/annotation products must expose a neuron/root ID column.

Exact source-column names are captured in evidence rather than rewritten in M1.

## Qualification gates

M1 passes only if all gates pass:

- `M1Q01` exact accepted M0 parent baseline;
- `M1Q02` secrets excluded from Git and emitted evidence;
- `M1Q03` runtime data root ignored by Git;
- `M1Q04` product discovery works without downloading bulk data;
- `M1Q05` synthetic fixture download/import path PASS;
- `M1Q06` streaming SHA-256 deterministic;
- `M1Q07` gzip/header validation PASS;
- `M1Q08` atomic staging/acceptance PASS;
- `M1Q09` mismatched existing artifact fails closed;
- `M1Q10` offline re-validation PASS;
- `M1Q11` canonical manifest determinism PASS;
- `M1Q12` no bulk source artifact tracked by Git;
- `M1Q13` real FAFB v783 required bundle acquired;
- `M1Q14` real artifacts hash-bound in local manifest;
- `M1Q15` provenance/license/citation note present;
- `M1Q16` M0 regression qualification still PASS.

## Out of scope

M1 MUST NOT:

- turn the connectivity table into an application graph;
- assign excitatory/inhibitory signs;
- infer synaptic strength beyond source fields;
- aggregate or threshold source connectivity;
- normalize neuron IDs;
- build morphology;
- download full neuron meshes/skeletons;
- implement LIF/spiking dynamics;
- implement embodiment;
- commit Codex tokens or downloaded source artifacts.

## Repository profile

Remain `ŌLLIN Lite`.

M1 adds one bounded acquisition capability; this alone does not justify Cells.

## Authorization rule

Owner acceptance of this proposal authorizes only `M1-WO001` as bounded below.

No M2 work is implied.
