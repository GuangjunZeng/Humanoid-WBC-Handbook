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
- [ ] Confirm an interrupted X pagination test preserves `next_token` and does not advance `since_id` until the result window is fully drained; confirm 429 retry is bounded.
- [ ] Confirm visible-browser runs contain no cookies, credentials, raw DOM dumps, transient access tokens, signed media URLs, CAPTCHA/paywall bypass, or private content; full extracted text remains ignored under `var/`.
- [ ] Confirm X/Xiaohongshu/Zhihu browser candidates retain canonical original/reply links, bounded selected comments, `partial_visible` completeness, page-state provenance, and `pending_analysis` rather than automatic acceptance.
- [ ] Confirm the discovery ledger skips duplicate query signatures, retains canonical URLs across runs, exponentially backs off zero-yield queries, and can be explicitly refreshed without creating a schedule.
- [ ] Confirm every `ready` evolved query has a root evidence URL and title/comment evidence under the activation rule; the full frontier has no topic/evidence display cap while each run still obeys its platform budget.
- [ ] Confirm every social experience has `problem_id`, both computed/final credibility grades, a Chinese rationale, and an original-post or precise-reply link; manual overrides have reasons and cannot bypass the high-grade evidence gate.
- [ ] Confirm `reviewed + technical_pending + excluded == unique_candidates`; every exclusion has a Chinese reason and every technical pending candidate remains linked from the scope appendix.
- [ ] Confirm GitHub historical searches are partitioned by date window, unfinished pages resume without losing the page tail, and every answer from a comment keeps its exact `#issuecomment-<id>` URL.
- [ ] Publish as alpha until real WBC claims have domain-expert and safety review.

## Current release acceptance

- Source gate: `CONDITIONAL GO`; X defaults to bounded visible-browser extraction with paid official API opt-in, Zhihu uses official discovery plus bounded visible-browser enrichment, and Xiaohongshu uses user-authorized visible-browser extraction with a manual queue fallback.
- Runtime: Python standard library only.
- Canonical data: 174 versioned sources, including the 28 paper/code sources behind 14 bounded reviewed claims plus reviewed community/Issue evidence; the broader paper catalog remains a candidate/coverage layer, not reviewed guidance.
- Offline regression suite: run `scripts/acceptance.sh` plus the paper-specific checks in `CONTRIBUTING.md`; do not hard-code the test count.
- Remote: `git@github.com:GuangjunZeng/Humanoid-WBC-Handbook.git`; `main` is the release branch and `.github/workflows/pages.yml` validates and deploys the generated bilingual search site to GitHub Pages.
