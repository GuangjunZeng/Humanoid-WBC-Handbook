# Humanoid WBC Engineering Handbook — Open-source build plan

## Goal
Create an original, open-source-ready engineering handbook and retrieval project for humanoid whole-body control (WBC). The project must answer concrete engineering questions with traceable evidence, use only independently written code and prose, and remain reproducible from a clean checkout.

## Non-negotiable constraints
- Pass the information-source accessibility gate before implementing product features.
- Study VLA-Handbook only for public behavior, information architecture, and research workflow; do not copy source code, prose, prompts, styles, or data structures verbatim.
- Preserve source provenance and licensing metadata; never redistribute restricted full text.
- Keep documentation concise but sufficient to reproduce implementation and understand key know-how.
- Work in staged milestones with local Git commits; do not create or push a remote repository.
- Never permanently delete files; any removal must use `/usr/bin/trash <absolute-path>`.

## Phases
- [complete] 0. Establish isolated planning, inspect the provided DOCX, and inventory requirements
- [in_progress] 1. Validate target social/research platforms one at a time with reproducible probes and record a go/no-go gate
- [pending] 2. Analyze VLA-Handbook at the behavior and information-workflow level; record originality boundaries
- [pending] 3. Define product architecture, source policy, schemas, threat model, and open-source governance
- [pending] 4. Implement the original ingestion, normalization, retrieval, citation, and handbook workflows
- [pending] 5. Add tests, fixtures, documentation, examples, and offline-safe developer tooling
- [pending] 6. Run functional, quality, licensing, security, and clean-room acceptance checks
- [pending] 7. Mirror the completed local Git repository to a new Desktop folder and verify its history

## Stage commit policy
1. `chore: establish project plan and source validation gate`
2. `docs: record source feasibility and clean-room design`
3. `feat: implement original handbook research pipeline`
4. `test: add acceptance coverage and reproducible fixtures`
5. `docs: finalize open-source handbook and release checklist`

## Gate criteria
- Every proposed platform has a dated probe result, acquisition method, authentication requirement, rate-limit/robots/licensing note, and fallback.
- Core source classes required by the technical plan are accessible through at least one lawful, reproducible method.
- Any unavailable or unstable platform has a documented fallback and is not a hard runtime dependency.
- No product feature implementation begins until the gate decision is `GO` or `CONDITIONAL GO` with explicit limitations.

## Errors encountered
| Error | Attempt | Resolution |
|---|---:|---|
| New goal creation reported an existing active goal | 1 | Reused the automatically created active goal and inspected it with `get_goal` |
| Workspace root already contained planning files for another project | 1 | Created an isolated `Humanoid-WBC-Handbook/` project root with its own planning files |
| Bilibili search page probe exceeded the 30-second browser execution window and reset the browser session | 1 | Record the failure, reconnect once, and retry using a smaller DOM-only probe with a bounded longer timeout |
| GitHub issue search probe used an unsupported compound query/repository combination and returned HTTP 422 | 1 | Stop the batch after the user's serial-validation instruction; retry GitHub alone later with a simple query and verified repository identifier |
| First attempt to hand off the Xiaohongshu login page timed out during navigation | 1 | Read browser recovery guidance, created a fresh tab, showed it, and preserved it for user sign-in |
| Xiaohongshu official agreement page timed out during dynamic browser rendering | 1 | Did not retry the same path; relied on the successful official robots.txt fetch and kept agreement review as a non-blocking legal follow-up |
| Reopening the Xiaohongshu handoff page produced a navigation timeout; the existing explore tab then timed out during DOM inspection | 1 | Stopped browser retries to avoid an unstable loop; require the user to sign in manually, then resume the visible-session acceptance test |

## Serial platform order
1. Xiaohongshu — `in_progress`, waiting for user-authorized sign-in
2. Zhihu — `pending`
3. Bilibili — `pending`
4. GitHub Issues/Releases/commits — `pending`
5. Papers/arXiv — `pending`
6. Project websites, official docs, blogs, Hugging Face — `pending`
7. Discord/other gated communities — `pending`
