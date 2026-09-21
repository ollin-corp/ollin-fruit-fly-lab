# Next Work

After M0 is published and locally qualified, propose **M1 — Deterministic Connectome Acquisition**.

M1 should begin with a single dataset (FAFB v783 is the default candidate) and must:

1. inspect the Codex static download index;
2. select the minimum required data products;
3. record canonical source URLs and source metadata;
4. download to a local ignored data root;
5. compute SHA-256 for every accepted artifact;
6. emit a deterministic manifest;
7. support offline re-validation of already downloaded artifacts;
8. use tiny synthetic fixtures for repository tests;
9. perform no neural simulation.
