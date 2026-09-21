# M1 Public Static Data Census — R02

Freeze date: 2026-09-21.

## Result

M1 does not need a live Codex API.

M1 does not need a Codex API token.

M1 does not need a CAVE token.

The direct acquisition design uses plain public static FAFB snapshot objects and becomes offline after acquisition.

## FlyWire release identity

FlyWire public release guidance identifies:

- dataset: FAFB / Female Adult Fly Brain;
- latest public release: v783;
- release snapshot: October 2023;
- public-release license: CC BY-NC 4.0.

Source:

`https://home.flywire.ai/guidelines`

## Codex documentation — reference only

The current Codex FAQ confirms:

- FAFB v783 is the latest public FAFB snapshot;
- Codex serves static connectome snapshots for analysis;
- bulk analysis should use static downloadable files rather than repeated live queries;
- Codex's programmatic `download_resource` route requires a Codex API token.

R02 deliberately does not use that programmatic route.

Source:

`https://codex.flywire.ai/faq`

Codex is therefore treated as:

- optional human explorer;
- metadata cross-check;
- documentation source.

It is not an M1 runtime dependency.

## Public static object convention

The current open-source Codex loader declares:

```text
https://storage.googleapis.com/flywire-data/codex/data/fafb/{version}/{filename}
```

and directly names FAFB raw files including:

- `neurons.csv.gz`
- `classification.csv.gz`
- `consolidated_cell_types.csv.gz`
- `cell_stats.csv.gz`
- `connections.csv.gz`
- `labels.csv.gz`
- `coordinates.csv.gz`
- `nblast.csv.gz`
- `connectivity_tags.csv.gz`

Source code:

`https://github.com/murthylab/codex/blob/main/codex/data/local_data_loader.py`

Observed source blob during R02 research:

`85144aca4bc9928101aefbc4fdc9247303bdc65f`

The static object convention is the initial M1 transport contract.

## Connectivity completeness requirement

The ordinary Codex graph interface applies dataset-specific minimum connection thresholds; the current FAQ documents FAFB graph connectivity at a default minimum of 5 synapses.

Because ŌLLIN Fruit Fly Lab intends to preserve source topology before making analytical choices, M1 requires an explicitly unthresholded connectivity artifact.

Candidate public static filenames to probe:

- `connections_princeton_no_threshold.csv.gz`
- `connections_no_threshold.csv.gz`

R02 does not assume either candidate exists until implementation performs bounded static-object existence checks.

If neither exists under the pinned public snapshot location, implementation stops for owner review rather than silently accepting a thresholded graph.

## Why the path still contains the word "codex"

The current public object location used by the FlyWire/Codex project includes the path segment:

`/codex/data/fafb/783/`

That path name is storage organization only.

ŌLLIN Fruit Fly Lab does not call the Codex application, does not use its live-query API, and does not require Codex authentication after this revision.

## Data/model boundary

Static source bytes remain external scientific evidence.

M1 only acquires, validates, hashes, and manifests them.

Interpretation, graph construction, dynamics, learning, and behavior remain later milestones.
