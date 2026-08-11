# Architecture

## Product invariant

The handbook answers a concrete Humanoid WBC engineering question only through reviewable `EngineeringClaim` records. A claim is useful when readers can see what supports it, what conflicts with it, where it applies, when it was reviewed, and which safety constraints block hardware use.

```text
authorized/public source
        |
        v
SourceRecord -- provenance, access, version, integrity
        |
        v
EvidenceLink -- support / conflict / supersede / context
        |
        v
EngineeringClaim -- question, statement, applicability, confidence rationale
        |
        +--> deterministic validation --> publication state
        |
        +--> local SQLite index --> cited answer
```

## Components

| Component | Responsibility | Trust boundary |
|---|---|---|
| Manual importer | Normalize a user-supplied public/authorized record | Treat all imported text as untrusted data |
| On-demand social collector | Select low-repeat queries from an open WBC ontology; run free bounded visible-browser tasks for X/知乎/小红书; mine evidence-linked subtopics from bodies/comments; normalize and render linked candidate Q&A | Explicit user trigger only; browser results are `partial_visible`; no cookies, hidden APIs, scheduler, CAPTCHA bypass, or uncontrolled bulk archive |
| GitHub Issue collector | Split 34 WBC repositories and engineering queries into resumable date-window search tasks; merge Issue bodies/comments by canonical root and exact comment URL | Documented free API/connected app only; 1,000-result windows are partitioned; raw scale is not reviewed evidence |
| Source adapters | Optional discovery/metadata acquisition | Must obey `docs/source-feasibility/README.md`; never required offline |
| Domain model | Parse and serialize sources, claims, evidence, applicability, and safety case | Reject invalid IDs, URLs, timestamps, enums, and unsafe critical claims |
| Validator | Produce stable issue codes and decide publication readiness | Deterministic; no LLM judgment |
| Index builder | Rebuild a local SQLite search index from reviewed JSON records | Generated index is disposable; JSON records are canonical |
| Answer renderer | Rank matching reviewed claims and attach canonical citations/warnings | Never invent a claim or citation |
| Paper coverage catalog | Track classic anchors, official-code papers, deep reads, and topic gaps | A catalog entry is not a reviewed conclusion |
| On-demand paper discovery | Query bounded arXiv searches and deduplicate by normalized paper ID | Runs only when a user asks; never schedules, pushes, or auto-accepts |
| Paper brief workflow | Record full-paper interpretation, key figures, and paper-to-code mapping | Uses only the analysis portion of `paper-daily`; promotion requires deterministic quality checks |

## Repository data flow

Canonical data is human-reviewable JSON under `data/`. Generated SQLite files belong under `var/` and are ignored by Git. The builder performs a full deterministic rebuild, which avoids hidden incremental state.

```text
data/sources/*.json + data/claims/*.json
                  |
                  +--> validate
                  |
                  +--> build-index --> var/handbook.sqlite
                                           |
                                           +--> query --> Markdown or JSON answer
```

Paper coverage has a separate, reviewable path. `catalog.json` may be broader than
the deep-read `registry.json`; a paper moves into the registry only after its PDF,
official code status, figures, Chinese analysis, locators, and limitations pass the
quality gate.

```text
content/papers/catalog.json -- papers-status --> coverage gaps
             |
             +-- user request --> papers-discover --> var/paper-update/candidates.json
                                                    |
                                                    +--> primary-source review
                                                             |
                                                             +--> deep brief + figures + registry
```

## Failure behavior

- Missing or malformed provenance fails validation.
- A claim with unknown evidence IDs fails validation.
- Community-only support cannot make a claim publishable.
- Hardware-critical guidance fails unless every safety field is present and simulation validation is recorded.
- A network adapter failure never prevents offline validation, indexing, or querying.
- A social platform login, CAPTCHA, risk-control, or access denial stops that platform's current task and leaves an explicit partial result.
- Free X browser runs preserve exact post/reply links, visible media review paths, and bounded expansion/depth metadata; they never claim complete thread coverage. In optional paid API mode, an incomplete page window persists its `next_token` and old `since_id`; the high-water mark advances only after every retained page is consumed.
- Social captures enter as `review_status=candidate`; collection never promotes them to reviewed engineering guidance.
- Every extracted social engineering question/answer carries the stable original-post URL and a body/comment locator. Missing answers remain `unresolved`; the collector must not synthesize a fix.
- Paper discovery failure leaves the existing catalog and deep reads unchanged.
- Discovered papers remain candidates until a human-reviewable primary-source check and all brief gates pass.
- A zero-result query returns a transparent no-evidence response instead of synthesized advice.

## Originality rationale

The architecture is derived from the supplied WBC technical plan's Engineering Claim unit, the verified platform constraints, robotics hardware safety, and standard deterministic indexing practice. It does not reuse the reference repository's pipeline names, schemas, scheduling, storage, prompts, or presentation.
