# Release checklist

The codebase can be developed and committed locally without a cloud repository. Complete the identity items only when a public remote is explicitly authorized; do not invent them.

## Required before first public push

- [ ] Choose the public repository owner and canonical URL; add it to package metadata.
- [ ] Choose a monitored maintainer/security contact and update `SECURITY.md` and package metadata.
- [ ] Confirm repository name, description, topics, and default branch protection.
- [ ] Confirm Apache-2.0 copyright holder wording and contributor policy.
- [ ] Run a license/provenance review for every non-original source record and excerpt.
- [ ] Re-run the clean-room checklist in `docs/clean-room-study.md`.
- [ ] Confirm no credentials, cookies, private posts, restricted full text, generated indexes, or robot-sensitive logs are tracked.
- [ ] Run `sh scripts/acceptance.sh` from a clean checkout on Python 3.9 and one current Python release.
- [ ] Inspect the generated answer for citations, conflicts, applicability, staleness, and hardware safety warnings.
- [ ] Publish as alpha until real WBC claims have domain-expert and safety review.

## Current local acceptance

- Source gate: `CONDITIONAL GO` with all gated social platforms optional.
- Runtime: Python standard library only.
- Canonical data: two versioned sources and one reviewed OmniH2O pilot claim; no fabricated demo advice.
- Offline regression suite: 10 tests passing on Python 3.9.6.
- Remote operations: none; no cloud repository has been created or pushed.
