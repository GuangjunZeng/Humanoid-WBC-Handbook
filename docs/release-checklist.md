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
- [ ] Inspect every generated social engineering Q&A card for a clickable canonical original-post link, a body/comment locator, and an honest resolved/partial/unresolved/conflicting status.
- [ ] Confirm the social query ontology contains cross-cutting setup, training, simulation, deployment, hardware, safety, and open-ended WBC scopes rather than only the seven paper domains.
- [ ] Confirm X and Zhihu credentials are absent from tracked files and generated reports; inspect `var/` only locally.
- [ ] Confirm Xiaohongshu candidates contain no DOM/full-text/comment archive and each approved item has an explicit human decision.
- [ ] Publish as alpha until real WBC claims have domain-expert and safety review.

## Current local acceptance

- Source gate: `CONDITIONAL GO`; X uses official API v2, Zhihu uses its official invited-preview search API, and Xiaohongshu is manual-review-only without written permission.
- Runtime: Python standard library only.
- Deep-read canonical data: 28 versioned sources and 14 bounded reviewed claims; the broader paper catalog is a candidate/coverage layer, not reviewed guidance.
- Offline regression suite: run `scripts/acceptance.sh` plus the paper-specific checks in `CONTRIBUTING.md`; do not hard-code the test count.
- Remote operations: none; no cloud repository has been created or pushed.
