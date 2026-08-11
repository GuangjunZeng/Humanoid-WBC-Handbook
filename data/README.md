# Canonical handbook data

Place reviewed source records in `sources/` and Engineering Claims in `claims/`. The initial real content pilot contains one narrowly scoped OmniH2O claim backed by a full-paper review and commit-pinned official code. New guidance must receive the same evidence, applicability, licensing, and safety review rather than being fabricated for a demo.

`social-candidate-index.json` is the minimal, committed inventory of all discovered
social and GitHub Issue candidates. It stores links and triage metadata only. Raw
post text, complete comments, DOM, cookies and temporary media remain under ignored
`var/`. Its counts must satisfy `reviewed + technical_pending + excluded ==
unique_candidates`; exclusions require a Chinese reason and uncertain technical
candidates remain visible as `technical_pending`.

Use `examples/manual-source.json` to exercise the importer. Synthetic acceptance fixtures live in the tests and are never indexed as handbook advice. Reproducible source manifests for curated records live under `research/manifests/`.
