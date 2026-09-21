# Scientific Source Registry — M0

Freeze date: 2026-09-21.

This file records sources consulted for the repository genesis. External resources may change; ingestion milestones must pin exact downloaded artifact identities and hashes.

## FlyWire Codex

- Home/data explorer: https://codex.flywire.ai/
- FAQ/programmatic download guidance: https://codex.flywire.ai/faq
- Download index: https://codex.flywire.ai/api/download

Observed at M0 freeze:

- FAFB v783 — Female Adult Fly Brain — 139,255 neurons — 3,732,460 aggregate neuron-to-neuron connections.
- BANC v888 — Female Adult Fly Brain and Nerve Cord — 158,262 neurons — 3,037,361 aggregate neuron-to-neuron connections.

Codex recommends programmatic analysis through static downloadable files rather than repeated live-app queries. M1 will therefore use the static download index and will record exact resource metadata before accepting any artifact.

## Whole-brain computational model

- Shiu et al., "A Drosophila computational brain model reveals sensorimotor processing," Nature 634, 210–219 (2024).
- DOI: https://doi.org/10.1038/s41586-024-07763-9

This is a later replication/reference target for connectome-derived leaky-integrate-and-fire modeling. Its existence does not make the connectome itself a complete dynamical brain specification.

## Effectome distinction

- Pospisil et al., "The fly connectome reveals a path to the effectome," Nature 634, 201–209 (2024).
- DOI: https://doi.org/10.1038/s41586-024-07982-0

This source motivates the project law separating anatomical connectivity from causal/dynamical effect parameters.

## Embodiment target

- Wang-Chen et al., "NeuroMechFly v2: simulating embodied sensorimotor control in adult Drosophila," Nature Methods 21, 2353–2362 (2024).
- DOI: https://doi.org/10.1038/s41592-024-02497-y
- FlyGym code: https://github.com/NeLy-EPFL/flygym

No third-party code is vendored in M0.
