"""Pinned external connectome dataset descriptors.

These descriptors are provenance records, not downloaded data and not biological
simulation parameters. Counts are descriptive metadata observed from Codex at the
M0 freeze date and must never be used as a substitute for validating downloaded
artifacts during ingestion.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DatasetDescriptor:
    key: str
    provider: str
    name: str
    version: str
    organism: str
    scope: str
    neuron_count_observed: int
    aggregate_connection_count_observed: int
    download_index_url: str


FAFB_V783 = DatasetDescriptor(
    key="flywire-fafb-v783",
    provider="FlyWire/Codex",
    name="FAFB",
    version="v783",
    organism="Drosophila melanogaster",
    scope="Female Adult Fly Brain",
    neuron_count_observed=139_255,
    aggregate_connection_count_observed=3_732_460,
    download_index_url="https://codex.flywire.ai/api/download?dataset=fafb",
)

BANC_V888 = DatasetDescriptor(
    key="flywire-banc-v888",
    provider="FlyWire/Codex",
    name="BANC",
    version="v888",
    organism="Drosophila melanogaster",
    scope="Female Adult Fly Brain and Nerve Cord",
    neuron_count_observed=158_262,
    aggregate_connection_count_observed=3_037_361,
    download_index_url="https://codex.flywire.ai/api/download?dataset=banc",
)

SUPPORTED_DATASETS = (FAFB_V783, BANC_V888)
