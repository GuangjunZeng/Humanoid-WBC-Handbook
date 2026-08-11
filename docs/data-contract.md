# Data contract

JSON records are the canonical review surface. Unknown fields are rejected so schema drift is visible during review.

## SourceRecord

Required fields:

- `source_id`: stable lowercase identifier using letters, digits, dots, underscores, or hyphens.
- `kind`: `paper`, `official_doc`, `source_code`, `issue`, `release`, `project_page`, `video`, or `community`.
- `title`, `canonical_url`, `captured_at`, `summary`, `access_mode`.
- `content_sha256`: SHA-256 of the normalized imported evidence payload.

Optional fields include authors, publication/version timestamps, publisher, license, a short excerpt, attention metadata, and arbitrary source-specific metadata. Attention is never used as evidence strength.

### Social capture input

Platform discovery precedes capture and has three non-canonical candidate formats:

- Optional paid X API candidates: post ID/text, canonical status URL, author, conversation/reply
  references, expanded referenced-Post links/text, Article/note text, media, metrics
  and all matching WBC scopes. Per-query state can contain an unfinished pagination
  cursor, its original `since_id`, and the window `newest_id`; the official high-water
  mark advances only when the window is complete. Raw candidates and state stay in
  ignored `var/`; `X_BEARER_TOKEN` is never serialized.
- Zhihu API candidates: content ID/type, title, bounded `ContentText` summary,
  author/metrics and canonical answer/article/question URL. They explicitly record
  `full_text_available=false`; `ZHIHU_ACCESS_SECRET` is never serialized.
- Xiaohongshu review candidates: canonical note URL, query/scope, optional search
  title/snippet, discovery source and human review status. They always record
  `content_collected=false` until separate permitted material is manually supplied.
- Visible-browser candidates for X/Xiaohongshu/Zhihu: canonical post/answer URL,
  bounded body text, selected comments, public metadata, image-analysis queue,
  all matching WBC scopes, page state, and extraction provenance. They record
  `access_mode=authorized_visible_browser`, `content_collected=true`, and
  `review_status=pending_analysis`. They also record
  `collection_completeness.status=partial_visible`, bounded reply count/expansion/depth,
  and stable original reply links; this is never a claim of all posts or all replies.
  Login/CAPTCHA/risk/paywall pages become blockers,
  never fake content candidates. Raw DOM, cookies, credentials, transient navigation
  parameters, and signed media URLs are not part of this contract.

Discovery candidates are not `SourceRecord` evidence and cannot be indexed as
engineering guidance. Human/AI analysis produces the capture below.

`import-social-captures` accepts reviewed analysis output with `platform`, engineering
`scope_id`, optional seven-domain hints, exact `query`, stable post URL, capture
time, title, original summary, WBC relevance reason, optional short excerpt,
public author display, visible attention counters, original media summaries, and a
small selected-comment set. Xiaohongshu/Zhihu/X tracking and access parameters are
removed during normalization. The resulting social source has `kind=community`.
GitHub captures use `platform=github_issue`, normalize the root to
`https://github.com/<owner>/<repo>/issues/<number>`, preserve an exact
`#issuecomment-<id>` answer locator, and produce `kind=issue` with
`verification_status=issue_candidate`. Both paths use
`access_mode=public_api`, `manual_import`, or `authorized_visible_browser`, and
`metadata.review_status=candidate`.
For `authorized_visible_browser`, the reviewed capture must carry the bounded
`collection_completeness` object forward. Normalization rejects any claim of
complete coverage and preserves `status=partial_visible`, visible reply count,
expansion count, reply depth/limit, and stop reason in the community source and
the generated engineering Q&A report.

An experience capture also contains structured `engineering_details`: problem,
environment, symptom, diagnostics, suspected cause, attempted changes, effective
fixes, outcomes, limits, and safety notes. Unknown elements remain empty; they are
never inferred merely to complete the form.

Every `engineering_qa` card requires `question_zh`, `answer_zh`, `bilingual_terms`, `answer_status`,
`source_locator`, `problem_id`, `problem_title_zh`, `credibility`, `verification_refs`,
and an answer (or an explicit unresolved marker). Normalization
validates the stable `source_url` and injects
`verification_status=community_candidate` (or `issue_candidate` for GitHub Issues).
Regardless of whether the source post is Chinese or English, the source title,
original summary, engineering question, answer, media analysis, and limitations
are Chinese-first. `question_zh` needs substantive Chinese text and `answer_zh`
needs at least one complete Chinese explanation. `bilingual_terms` contains one to
twelve canonical strings in `中文（English, ABBR）` form, for example
`全身控制（Whole-Body Control, WBC）`. Product names, code identifiers, CLI flags,
and mathematical symbols keep their original spelling; they do not replace the
Chinese explanation.
Therefore every rendered problem and candidate answer has a clickable original
post citation. X answers may cite the exact reply URL instead of the thread root.
A card without an original URL is invalid output. The report repeats the source-level
environment, symptom, diagnosis/cause, attempted/effective treatment, outcome,
limits, safety notes, and available Chinese image analysis beside each problem so
the engineering context is not separated from its citation.

`problem_id` is stable and conservative: records merge only when scope, component,
symptom and environment are consistent. `credibility.computed_grade` is generated by
rules and `credibility.final_grade` is the reviewed visible grade. Both are one of
`可信度很高 / 值得参考 / 需要实际验证`; no numeric score is used. The object also stores a
Chinese rationale and `basis.source_basis`, `basis.reproduction`,
`basis.applicability`, independent source IDs, conflict state, and image-analysis
state. If final and computed grades differ, `override_rationale_zh` is mandatory.
An experience cannot be upgraded to `可信度很高` without exact formal verification or
independent reproduction, and cannot be upgraded while conflict, unknown applicability,
or required-but-unverified visual evidence remains.

`verification_refs` contains exact paper/document/source/PR/Issue/reproduction
locators. Each entry has one `relation`, one precise `locator`, and exactly one of a
repository `source_id` or an absolute `source_url`. Likes, views, saves, and author
audience never enter this calculation. Problem-level grades are computed only when
rendering groups of experience cards and never create or modify `EngineeringClaim`.

### Minimal social candidate inventory

`data/social-candidate-index.json` is a committed, minimal catalogue of every unique
social/Issue candidate. Each record stores only `candidate_id`, canonical URL, title,
platform, scope IDs, discovering queries, first/last seen time, related problem IDs,
and `triage_status`. It must not contain bodies, complete comments, cookies,
credentials, raw DOM, or transient media URLs.

`triage_status` is exactly `reviewed`, `technical_pending`, or `excluded`. Uncertain
technical candidates default to `technical_pending`; exclusions require a Chinese
reason. Reviewed cards appear in the main engineering handbook, pending candidates
appear with original links in `content/social-engineering-pending/`, and exclusions
remain auditable in the JSON with their reasons. See
`docs/social-credibility-and-inventory.md` for aggregation and display invariants.

Raw cross-run identity and scheduling state is not a `SourceRecord`. Query signatures,
canonical URL history, zero-yield backoff, the machine-readable dynamic frontier,
GitHub pagination, and incomplete page cursors stay under ignored `var/social-state/`.
The generated `content/social-query-frontier.md` exposes all deduplicated topics and
all root evidence links without a display cap. Their schema and recovery invariants
are defined in `docs/social-discovery-evolution.md`.

Raw API/browser/manual captures belong under ignored `var/`; only normalized metadata,
original summaries, short necessary excerpts, and stable citations belong in
`data/sources/`.

## EngineeringClaim

Required fields:

- `claim_id`, one of the seven `domain` values, `question`, and one atomic `statement`.
- `status`: `draft` or `reviewed`.
- `confidence` in `[0, 1]` plus a written `confidence_rationale`.
- `applicability`: robot, simulator, controller, environment, and assumptions.
- one or more `evidence` links.
- `safety_level`, `reviewed_at`, and `review_due_at`.

An evidence link names a source and its role (`support`, `conflict`, `supersede`, or `context`), strength (`primary`, `secondary`, or `community`), and a precise locator such as a section, figure, table, file/function, issue comment, or timestamp.

## Seven WBC domains

1. `training_data_retargeting`
2. `universal_tracking_teleoperation`
3. `locomotion_terrain`
4. `loco_manipulation_wbc`
5. `sports`
6. `motion_generation`
7. `recovery_safety_force`

## SafetyCase

Claims marked `hardware_critical` require:

- `simulation_validated: true`
- explicit command/torque/velocity/position/force limits;
- a tested emergency-stop description;
- protective equipment or test-area controls;
- a robot-specific warning;
- a staged deployment procedure.

These fields are publication gates, not a guarantee that hardware execution is safe.
