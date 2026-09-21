# M1 Proposal R02 — Direct Static FAFB v783 Acquisition

Status: `PROPOSAL_R02 / OWNER_REVIEW_PENDING`

Supersedes: `M1-PROPOSAL-R01`

Baseline:

- main SHA: `a49992dc425d01e71644ab92ebee66f11e7f1d45`
- M0 accepted software baseline: `a99aefcaa4f667d47fd4a9a3ac2e750824139974`
- M0 accepted tree: `8f48f2d3cfd0b4ee54c1b48c5cbe88c0c897b02d`

## Owner amendment incorporated

M1 MUST NOT depend on:

- the Codex live application;
- a Codex programmatic API;
- a Codex API token;
- a CAVE token;
- Google sign-in;
- any online query service at experiment runtime.

Codex may be used by humans as an optional explorer/reference surface only.

## Objective

Acquire the public FlyWire FAFB v783 connectome snapshot from plain versioned static files, preserve the downloaded bytes as immutable local source data, and emit deterministic provenance sufficient to re-validate those same bytes offline.

M1 does not normalize graph semantics and does not simulate neurons.

## Scientific source identity

Dataset:

`FlyWire FAFB v783 — Female Adult Fly Brain`

The public FlyWire release guidelines identify v783 as the latest public FAFB release.

The current open-source Codex loader independently exposes the static storage convention used for FAFB snapshot files:

```text
https://storage.googleapis.com/flywire-data/codex/data/fafb/{version}/{filename}
```

M1 treats this as a plain static-object transport path, not as a Codex application/API dependency.

## Direct acquisition principle

The desired acquisition path is:

```text
public static object
        |
        v
streamed local staging file
        |
        v
content validation
        |
        v
SHA-256
        |
        v
immutable accepted raw file
        |
        v
offline-only downstream work
```

After acquisition, graph/model/experiment work MUST NOT require network access.

## M1 required bundle

Metadata/annotation files:

1. `neurons.csv.gz`
2. `classification.csv.gz`
3. `consolidated_cell_types.csv.gz`

Connectivity requirement:

M1 MUST acquire an unthresholded FAFB connectivity table so weak source edges are not silently discarded before later analytical decisions.

Preferred candidate:

`connections_princeton_no_threshold.csv.gz`

Secondary candidate:

`connections_no_threshold.csv.gz`

Implementation MUST probe candidate static objects before bulk acquisition.

If neither unthresholded candidate is publicly reachable at the pinned FAFB v783 static location, M1 MUST fail closed and return evidence. It MUST NOT silently substitute `connections.csv.gz` or another thresholded table.

A later owner amendment may authorize a thresholded fallback if necessary.

## Static-object discovery

M1 may use lightweight HTTP `HEAD` requests, or bounded `GET` requests when a host does not support `HEAD`, against explicitly constructed static-object URLs.

Discovery MUST NOT:

- scrape Codex HTML;
- call a live query API;
- require authentication;
- enumerate arbitrary buckets;
- follow unrelated links;
- download large candidate files merely to learn whether they exist.

The selected exact URLs become part of the local acquisition manifest.

## Local storage

Ignored runtime root:

`.data/fafb/v783/`

Shape:

```text
.data/
└── fafb/
    └── v783/
        ├── raw/
        │   ├── neurons.csv.gz
        │   ├── classification.csv.gz
        │   ├── consolidated_cell_types.csv.gz
        │   ├── <accepted unthresholded connectivity file>
        │   └── ...
        ├── manifests/
        │   ├── acquisition.json
        │   └── acquisition.sha256
        └── staging/
```

No bulk source artifact is committed to Git.

## Immutable raw-data rule

A successfully accepted file is immutable source evidence.

If the same filename is encountered later:

- identical SHA-256 -> re-use is permitted;
- different SHA-256 -> fail closed;
- automatic replacement -> prohibited.

Updating to a new source snapshot or corrected upstream artifact requires a new provenance identity.

## Deterministic manifest

For each accepted artifact M1 records:

- dataset family: `FAFB`
- dataset version: `783`
- source project: `FlyWire`
- logical role
- exact filename
- exact public static URL
- byte size
- SHA-256
- acquisition UTC timestamp
- media/compression type when known
- acquisition implementation version
- source license/citation metadata
- validation status

The manifest is UTF-8 JSON with deterministic key ordering and formatting.

The manifest digest is recorded separately.

No credentials exist in the M1 design, therefore the manifest contains no credential/redaction machinery.

## Download behavior

The downloader MUST:

1. accept only the pinned FAFB v783 source family;
2. construct only approved static-object URLs;
3. create a staging file;
4. stream bytes to disk;
5. compute SHA-256 during streaming;
6. bound redirects and reject host escape;
7. reject HTTP error bodies and zero-length files;
8. close/flush the staging file;
9. validate gzip structure;
10. inspect CSV headers without full extraction;
11. atomically move accepted bytes into `raw/`;
12. never overwrite an accepted different artifact;
13. support offline re-validation after download.

Retries, if implemented, are bounded and explicit.

## Host boundary

Initial allowed static host:

`storage.googleapis.com`

Initial allowed bucket/path prefix:

`/flywire-data/codex/data/fafb/783/`

Redirects outside approved hosts fail closed unless later explicitly authorized.

The appearance of `codex` inside the storage path does not create a runtime dependency on the Codex application. It is simply part of the public static object location currently used by the FlyWire/Codex project.

## Minimum acquisition schema guards

These are acquisition guards only.

Neuron metadata files must expose a root/neuron identifier column appropriate to the source file.

The unthresholded connectivity file must expose fields corresponding to:

- presynaptic root/neuron ID;
- postsynaptic root/neuron ID;
- synapse count.

If neuropil or neurotransmitter fields are present they are preserved unchanged.

Exact source headers are captured in evidence.

M1 MUST NOT rename or semantically reinterpret source columns.

## Qualification gates

M1 passes only if:

- `M1Q01` exact accepted parent baseline is verified;
- `M1Q02` implementation has no token/API credential input surface;
- `M1Q03` runtime data root is Git-ignored;
- `M1Q04` direct static-object discovery is bounded and deterministic;
- `M1Q05` synthetic fixture acquisition path PASS;
- `M1Q06` streaming SHA-256 deterministic;
- `M1Q07` gzip/header validation PASS;
- `M1Q08` atomic staging/acceptance PASS;
- `M1Q09` mismatched existing artifact fails closed;
- `M1Q10` offline re-validation PASS;
- `M1Q11` canonical manifest determinism PASS;
- `M1Q12` no bulk source artifact is tracked by Git;
- `M1Q13` public unthresholded FAFB v783 connectivity object is identified;
- `M1Q14` required real FAFB v783 bundle is acquired;
- `M1Q15` all real artifacts are SHA-256 bound locally;
- `M1Q16` provenance/license/citation record is present;
- `M1Q17` no network is required for post-acquisition verification;
- `M1Q18` M0 regression qualification remains PASS.

## Out of scope

M1 MUST NOT:

- depend on Codex application/API availability;
- require a Codex or CAVE token;
- scrape interactive websites;
- turn connectivity rows into an application graph;
- infer excitatory/inhibitory signs;
- infer biological synaptic weights;
- threshold or aggregate the source connectivity;
- normalize IDs or source semantics;
- download meshes/skeletons;
- implement LIF/spiking dynamics;
- implement embodiment;
- commit downloaded source files.

## Repository profile

Remain `ŌLLIN Lite`.

The project earns modular Cells later when multiple implemented capabilities need explicit boundaries.

## Authorization rule

Owner acceptance of R02 authorizes only the bounded M1-WO001 implementation described by the current draft.

No M2 work is implied.
