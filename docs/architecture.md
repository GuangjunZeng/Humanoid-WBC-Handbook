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
| Source adapters | Optional discovery/metadata acquisition | Must obey `docs/source-feasibility/README.md`; never required offline |
| Domain model | Parse and serialize sources, claims, evidence, applicability, and safety case | Reject invalid IDs, URLs, timestamps, enums, and unsafe critical claims |
| Validator | Produce stable issue codes and decide publication readiness | Deterministic; no LLM judgment |
| Index builder | Rebuild a local SQLite search index from reviewed JSON records | Generated index is disposable; JSON records are canonical |
| Answer renderer | Rank matching reviewed claims and attach canonical citations/warnings | Never invent a claim or citation |
| Paper brief workflow | Record full-paper interpretation and paper-to-code mapping | Uses the selected `paper-daily` interpretation method only |

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

## Failure behavior

- Missing or malformed provenance fails validation.
- A claim with unknown evidence IDs fails validation.
- Community-only support cannot make a claim publishable.
- Hardware-critical guidance fails unless every safety field is present and simulation validation is recorded.
- A network adapter failure never prevents offline validation, indexing, or querying.
- A zero-result query returns a transparent no-evidence response instead of synthesized advice.

## Originality rationale

The architecture is derived from the supplied WBC technical plan's Engineering Claim unit, the verified platform constraints, robotics hardware safety, and standard deterministic indexing practice. It does not reuse the reference repository's pipeline names, schemas, scheduling, storage, prompts, or presentation.
