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

- X API candidates: post ID/text, canonical status URL, author, conversation/reply
  references, media, metrics and all matching WBC scopes. Raw candidates stay in
  ignored `var/`; `X_BEARER_TOKEN` is never serialized.
- Zhihu API candidates: content ID/type, title, bounded `ContentText` summary,
  author/metrics and canonical answer/article/question URL. They explicitly record
  `full_text_available=false`; `ZHIHU_ACCESS_SECRET` is never serialized.
- Xiaohongshu review candidates: canonical note URL, query/scope, optional search
  title/snippet, discovery source and human review status. They always record
  `content_collected=false` until separate permitted material is manually supplied.

Discovery candidates are not `SourceRecord` evidence and cannot be indexed as
engineering guidance. Human/AI analysis produces the capture below.

`import-social-captures` accepts reviewed analysis output with `platform`, engineering
`scope_id`, optional seven-domain hints, exact `query`, stable post URL, capture
time, title, original summary, WBC relevance reason, optional short excerpt,
public author display, visible attention counters, original media summaries, and a
small selected-comment set. Xiaohongshu/Zhihu/X tracking and access parameters are
removed during normalization. The resulting source has `kind=community`,
`access_mode=public_api`, `manual_import`, or `authorized_visible_browser`, and
`metadata.review_status=candidate`.

An experience capture also contains structured `engineering_details`: problem,
environment, symptom, diagnostics, suspected cause, attempted changes, effective
fixes, outcomes, limits, and safety notes. Unknown elements remain empty; they are
never inferred merely to complete the form.

Every `engineering_qa` card requires `question_zh`, `answer_status`,
`source_locator`, and an answer (or an explicit unresolved marker). Normalization
validates the stable `source_url` and injects
`verification_status=community_candidate`.
Therefore every rendered problem and candidate answer has a clickable original
post citation. X answers may cite the exact reply URL instead of the thread root.
A card without an original URL is invalid output.

Raw API/manual captures belong under ignored `var/`; only normalized metadata,
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
