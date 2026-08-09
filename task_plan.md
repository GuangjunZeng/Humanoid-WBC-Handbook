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
- The only writable local root is `/Users/cengguangjun/Desktop/Humanoid-WBC-Handbook`. Everything outside it is read-only and must not be edited, moved, renamed, or deleted.
- Use only the single-paper interpretation method from `/Users/cengguangjun/Desktop/paper-daily`; do not invoke its Scholar Inbox, scheduling, Feishu, deduplication, or local-workdir automation.

## Phases
- [complete] 0. Establish isolated planning, inspect the provided DOCX, and inventory requirements
- [complete] 1. Validate target social/research platforms one at a time with reproducible probes and record a conditional-go gate
- [complete] 2. Analyze VLA-Handbook at the behavior and information-workflow level; record originality boundaries
- [complete] 3. Define product architecture, source policy, schemas, threat model, and open-source governance
- [complete] 4. Implement the original ingestion, normalization, retrieval, citation, and handbook workflows
- [complete] 5. Add tests, fixtures, documentation, examples, and offline-safe developer tooling
- [complete] 6. Run functional, quality, licensing, security, and clean-room acceptance checks
- [complete] 7. Establish the Desktop repository as the sole writable project root and verify its copied history
- [complete] 8. Curate and validate the first real paper-to-code Engineering Claim as an end-to-end content pilot
- [complete] 9. Freeze a seven-domain seed-paper registry with explicit inclusion, exclusion, and completeness criteria
- [in_progress] 10. Read every registered paper in full and write an original, implementation-aware Chinese interpretation
- [pending] 11. Add canonical paper/code source records and bounded Engineering Claims for every registered paper
- [pending] 12. Build domain indexes, run corpus-wide quality/safety/originality acceptance, and create staged local commits

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
| Reopening the Xiaohongshu handoff page produced a navigation timeout; the existing explore tab then timed out during DOM inspection | 1 | Diagnosed browser-session isolation: the user is signed in to Chrome, but the selected profile lacks the ChatGPT extension and native messaging bridge |
| `git add .` could not create `.git/index.lock` under the managed filesystem sandbox | 1 | Re-ran the same repository-scoped staging command with approved Desktop-project write access; no other path was touched |
| First offline test run could not create ignored artifacts under the Desktop project's `var/` directory because the managed sandbox mounted the copied project read-only | 1 | Keep tests project-local and non-deleting; rerun with approved write access limited to the sole writable project root |
| Legacy `setuptools check` warned that public project URL and maintainer email are absent | 1 | Do not invent contact/remote metadata because no cloud repository is authorized; record both as explicit pre-publication checklist items. Package name/version checks still pass |
| GitHub code search for the OmniH2O repository returned one internal error and otherwise no indexed matches | 1 | Used public repository navigation plus exact, commit-pinned file fetches; no repository clone or copied code was added |
| First content patch could not create two missing parent directories | 1 | Created only `content/papers` and `data/claims` inside the sole writable project root, then reapplied the file patch |
| Combined skill-file read exceeded the terminal output budget and was truncated | 1 | Re-read `paper-daily`, its paper write-up guide, and the file-planning skill completely in bounded line ranges before research |

## Serial platform order
1. Xiaohongshu — `skipped_optional`, authenticated browser bridge unavailable; manual import only
2. Zhihu — `conditional`, external discovery works; direct fetch returns 403; authorized/manual reading only
3. Bilibili — `conditional_pass`, public discovery and metadata work; comments/subtitles are optional authorized context
4. GitHub Issues/Releases/commits — `pass`
5. Papers/arXiv — `pass`
6. Project websites and official docs/blogs — `pass`; Hugging Face web pages `conditional_pass`
7. Discord/other gated communities — `skipped_optional`, authentication and membership required

Gate decision: `CONDITIONAL GO`. GitHub, arXiv, official documentation, and public project pages form a complete core evidence path. Community platforms are supplemental and never required for builds, tests, or conclusions.
