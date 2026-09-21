# M1 Codex Download Census — 2026-09-21

Purpose: record what is externally supported before implementing M1.

## Official Codex observations

Source:

`https://codex.flywire.ai/faq`

Observed:

- FAFB current public/default snapshot is v783.
- Codex serves static connectome snapshots intended for analysis.
- Codex recommends static downloadable files for bulk/programmatic analysis instead of repeated live app queries.
- The documented resource pattern is:
  `/api/download_resource?data_product=...&dataset=fafb&api_token=...`
- Codex's example explicitly uses `consolidated_cell_types` and `connections_princeton`.
- A Codex API token is obtained from the signed-in account page.

Source:

`https://codex.flywire.ai/api/download?dataset=fafb`

Observed public dataset identity:

- FAFB v783
- Female Adult Fly Brain
- 139,255 neurons
- 3,732,460 aggregate displayed connections

## Codex source-code observations

Repository:

`https://github.com/murthylab/codex`

Current code inspected during proposal work declares raw FAFB data file names including:

- `neurons.csv.gz`
- `classification.csv.gz`
- `consolidated_cell_types.csv.gz`
- `cell_stats.csv.gz`
- `connections.csv.gz`
- `labels.csv.gz`
- `coordinates.csv.gz`
- `nblast.csv.gz`
- `connectivity_tags.csv.gz`

Codex source code also contains a Google Cloud Storage template for snapshot-specific raw data, but M1 does not treat an internal bucket path as the primary acquisition contract because the current public FAQ directs programmatic users through the download product interface.

## Connectivity preservation decision

M1 prefers the unthresholded Princeton connectivity product if exposed by the current portal.

Reason:

A source-preserving acquisition milestone should not discard weak edges before M2/M3 can make explicit analytical threshold choices.

No substitution from unthresholded to thresholded connectivity is allowed silently.

## License

FlyWire's public-release guidance states that public release data is made available under `CC BY-NC 4.0`.

M1 will store license/citation metadata in provenance and will not relicense source data.

## Important distinction

Codex displayed connection count and raw downloadable connectivity row/synapse counts are not assumed to be the same quantity.

M1 records source files exactly; interpretation belongs to later milestones.
