# Data contract

JSON records are the canonical review surface. Unknown fields are rejected so schema drift is visible during review.

## SourceRecord

Required fields:

- `source_id`: stable lowercase identifier using letters, digits, dots, underscores, or hyphens.
- `kind`: `paper`, `official_doc`, `source_code`, `issue`, `release`, `project_page`, `video`, or `community`.
- `title`, `canonical_url`, `captured_at`, `summary`, `access_mode`.
- `content_sha256`: SHA-256 of the normalized imported evidence payload.

Optional fields include authors, publication/version timestamps, publisher, license, a short excerpt, attention metadata, and arbitrary source-specific metadata. Attention is never used as evidence strength.

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
