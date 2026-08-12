# Humanoid WBC Engineering Handbook

**English | [中文](README.zh-CN.md)**

[![Bilingual search preview for the Humanoid WBC Engineering Handbook](site/assets/search-preview.svg)](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/?lang=en)

**[Open the bilingual quick search](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/?lang=en)** — Search every engineering problem in Chinese, English, or a mixture of both. Confidence, resolution status, and evidence boundaries appear only on the detail page.

<!-- BEGIN GENERATED PAPER ROUTES -->
## Paper map: seven WBC engineering topics

Start from a technical route, not a flat paper list. Each route keeps one field-defining or engineering-representative work; the linked brief explains the mechanism, decisive evidence, implementation mapping, and limits.

| Topic | Technical route | Representative deep read |
|---|---|---|
| Training Data and Motion Retargeting | Unified human-motion corpus | [AMASS: Archive of Motion Capture as Surface Shapes](content/papers/en/amass-1904.03278v1.md) |
|  | Robot motion retargeting | [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](content/papers/en/retargeting-matters-2510.02252v1.md) |
|  | Robot-free demonstration with online feasibility feedback | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](content/papers/en/humi-2602.06643v2.md) |
| Universal Tracking and Whole-Body Teleoperation | Dense real-time whole-body teleoperation | [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](content/papers/en/h2o-2403.04436v1.md) |
|  | Sparse head-and-hand commands | [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](content/papers/en/omnih2o-2406.08858v1.md) |
|  | Mask-conditioned multimode control | [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](content/papers/en/hover-2410.21229v2.md) |
| Locomotion and Challenging Terrain | ZMP preview control | [Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point](content/papers/en/zmp-preview-kajita-2003.md) |
|  | Periodic-reward sim-to-real reinforcement learning | [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](content/papers/en/periodic-gaits-2011.01387v2.md) |
|  | Open-source zero-shot transfer | [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](content/papers/en/humanoid-gym-2404.05695v2.md) |
|  | Trajectory pretraining and terrain fine-tuning | [Learning Humanoid Locomotion over Challenging Terrain](content/papers/en/challenging-terrain-2410.03654v1.md) |
| Loco-Manipulation and End-Effector WBC | Hierarchical operational-space whole-body control | [A Whole-Body Control Framework for Humanoids](content/papers/en/sentis-wbc-2006.md) |
|  | Optimization-based task-space inverse dynamics | [Implementing Torque Control with High-Ratio Gear Boxes and without Joint-Torque Sensors](content/papers/en/hrp2-torque-control-hal-01136936.md) |
|  | Force-aware dual-policy learning | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](content/papers/en/falcon-2505.06776v2.md) |
|  | Unified-policy curriculum learning | [ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation](content/papers/en/ulc-2507.06905v2.md) |
| Sports and Highly Dynamic Skills | Example-guided dynamic skills | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](content/papers/en/deepmimic-1804.02717v3.md) |
|  | Integrated locomotion, recovery, and strategy | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](content/papers/en/agile-soccer-2304.13653v2.md) |
|  | Real-physics residual alignment | [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](content/papers/en/asap-2502.01143v3.md) |
|  | Multi-stage task interaction | [Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning](content/papers/en/humanoid-badminton-2511.11218v3.md) |
| Motion Generation and Commandable Behavior | Example-guided motion control | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](content/papers/en/deepmimic-1804.02717v3.md) |
|  | Adversarial motion prior | [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](content/papers/en/amp-2104.02180v2.md) |
|  | Masked motion inpainting | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](content/papers/en/maskedmimic-2409.14393v1.md) |
|  | Test-time guided diffusion | [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](content/papers/en/beyondmimic-2508.08241v4.md) |
| Recovery, Falling, and Force Safety | Unified fall recovery and stand-up | [FRASA: An End-to-End Reinforcement Learning Agent for Fall Recovery and Stand Up of Humanoid Robots](content/papers/en/frasa-2410.08655v3.md) |
|  | Stand-up from diverse postures | [Learning Humanoid Standing-up Control across Diverse Postures](content/papers/en/host-2502.08378v2.md) |
|  | Protective falling | [SafeFall: Learning Protective Control for Humanoid Robots](content/papers/en/safefall-2511.18509v1.md) |
|  | Torque-aware force interaction | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](content/papers/en/falcon-2505.06776v2.md) |

The map is intentionally selective. The complete coverage catalogue—including queued classics and verified official-code works—lives in [`content/papers/`](content/papers/README.md).
<!-- END GENERATED PAPER ROUTES -->
---
An original, offline-first toolkit for turning papers, code, issues, releases, official documentation, and authorized field notes into auditable answers to concrete humanoid whole-body-control questions.

Status: alpha implementation with a coverage catalog spanning seven WBC engineering domains and a quality-gated deep-read corpus. The current snapshot contains 46 unique papers (25 complete Chinese deep reads and 21 queued classics/open-source works). The README map selects 24 unique representative deep reads across 26 technical routes, each with a reviewed English page. Content still requires qualified human technical and safety review before hardware use.

## What makes an answer publishable

An answer is retrieved from reviewed `EngineeringClaim` records. Each claim contains:

- an atomic engineering statement and the question it answers;
- supporting, conflicting, superseding, and contextual evidence links;
- precise evidence locators and canonical URLs;
- robot/simulator/controller/environment applicability;
- confidence with written rationale and a review date;
- a mandatory simulation-first safety case for hardware-critical guidance.

The tool never turns likes, views, or stars into technical confidence, and it returns “no reviewed claim” instead of inventing an answer.

## Quick start

Python 3.9+ is sufficient; runtime dependencies are intentionally zero.

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
wbc-handbook validate --data-dir data
wbc-handbook build-index --data-dir data --index var/handbook.sqlite
wbc-handbook query "全身遥操作需要全局线速度吗？" --index var/handbook.sqlite
```

Without installing:

```bash
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
```

Render the versioned Chinese and English problem pages, then build their shared
offline search index:

```bash
PYTHONPATH=src python3 -m wbc_handbook render-problems \
  --data-dir data --translations-dir data/locales/en/problems \
  --output-dir content/problems
PYTHONPATH=src python3 -m wbc_handbook build-web-index \
  --data-dir data --translations-dir data/locales/en/problems \
  --problems-dir content/problems --output site/search-index.json
```

Chinese detail URLs remain `content/problems/<id>.md`; English versions are
generated at `content/problems/en/<id>.md`. Both interface languages search the
same bilingual corpus, while result links follow the selected interface language.
Source fingerprints make CI reject missing or stale English records.

Representative paper pages use the same reviewed-localization contract. Chinese
analysis remains canonical; English records live in `data/locales/en/papers/`
and bind to the complete Chinese source with SHA-256. Regenerate and verify them
without a translation service:

```bash
PYTHONPATH=src python3 scripts/render_paper_translations.py
PYTHONPATH=src python3 scripts/render_paper_translations.py --check
python3 scripts/render_paper_topics.py --check
PYTHONPATH=src python3 scripts/check_paper_quality.py
```

Any Chinese factual change makes the English record stale until a reviewer
updates it. The English renderer also rejects missing route coverage, orphaned
translations, invented external URLs, missing core sections, or broken language
switches.

Import one manually reviewed source record:

```bash
PYTHONPATH=src python3 -m wbc_handbook import-source examples/manual-source.json --data-dir data
```

The importer performs no network access. Review the resulting JSON and add claims separately.

Create plans for each social acquisition level:

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform x --max-posts-per-run 15
PYTHONPATH=src python3 -m wbc_handbook social-collect-zhihu --dry-run
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu
PYTHONPATH=src python3 -m wbc_handbook github-issue-plan
# GITHUB_TOKEN is an optional free rate-limit increase:
PYTHONPATH=src python3 -m wbc_handbook github-issue-collect
# Paid X API is optional: PYTHONPATH=src python3 -m wbc_handbook social-collect-x --dry-run
```

When the user asks for a social-source update, X defaults to no-API-fee bounded
visible-browser search/detail/reply extraction, Zhihu uses the official invited-preview
search API plus bounded visible-browser enrichment, and Xiaohongshu uses bounded visible-browser search/detail extraction with a
no-network review queue as fallback. The user handles only login expiry, CAPTCHA,
risk control, paywalls, or unavailable pages—not individual post navigation. Raw candidates and
incremental state stay under ignored `var/`; the minimal URL-level inventory is committed under `data/`. Reviewed captures are normalized with
`import-social-captures`; `social-report` groups all reviewed experiences by stable
problem ID, assigns both problem-level and experience-level grades, and keeps mandatory
original-post/reply links, answer status and collection-completeness markers. Chinese and English posts are both
summarized Chinese-first, with canonical `中文（English, ABBR）` terminology. Browse the generated
[Chinese engineering-problem handbook](content/social-engineering-candidates.md). See the
[Chinese collection runbook](docs/social-collection.md) and
[visible-browser execution contract](docs/social-browser-automation.md). Cross-run query
yield, canonical-URL deduplication, post/comment-driven topic evolution, and resumable
large GitHub Issues backfills are specified in the
[social discovery evolution runbook](docs/social-discovery-evolution.md).
The complete topic catalogue, minimal all-candidate index, three-grade rules and
pending appendix are specified in the
[social credibility and inventory standard](docs/social-credibility-and-inventory.md).
The paid official X API remains an explicit opt-in mode; its pagination, retry,
incremental-state and failure-recovery details are in the [X API automation runbook](docs/x-api-automation.md).

Inspect paper-topic coverage and run a bounded, on-demand discovery pass:

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status
PYTHONPATH=src python3 -m wbc_handbook papers-discover \
  --max-per-topic 8 --out var/paper-candidates.json
```

Paper discovery never runs on a schedule and never auto-accepts candidates. When the
user asks for an update, follow the [on-demand paper update runbook](docs/on-demand-paper-update.md),
which uses only the single-paper analysis part of `paper-daily` and has no push/digest workflow.

## Repository map

| Path | Purpose |
|---|---|
| `src/wbc_handbook/` | Original models, validation, import, paper coverage, on-demand social collection, index, answer, and CLI code |
| `config/social-queries.json` | Open WBC engineering-problem scopes shared by X, Zhihu, and Xiaohongshu; optional domain hints are not collection boundaries |
| `content/papers/` | Coverage catalog, quality-gated deep-read registry, generated topic indexes, Chinese interpretations, and key-figure manifests |
| `content/problems/` | Generated Chinese engineering-problem pages plus matching English pages under `content/problems/en/` |
| `data/` | 286 canonical source records, a minimal all-candidate social/Issue index, and 14 bounded, human-reviewed Engineering Claims |
| `data/locales/en/problems/` | Reviewed, versioned English problem translations with stale-source fingerprints |
| `docs/` | Architecture, safety, source policy, clean-room record, and workflows |
| `site/` | Dependency-free bilingual GitHub Pages search UI, vendored FlexSearch, SVG background, and generated schema-v2 index |
| `templates/` | Authoring templates, including full-paper interpretation |
| `tests/` | Offline deterministic acceptance tests |
| `var/` | Ignored generated indexes and test artifacts |

Start with the [paper corpus](content/papers/README.md), [on-demand paper update workflow](docs/on-demand-paper-update.md), [paper interpretation standard](docs/paper-interpretation.md), [architecture](docs/architecture.md), [data contract](docs/data-contract.md), [source gate](docs/source-feasibility/README.md), [safety policy](docs/safety.md), [Git commit conventions](docs/git-conventions.md), and [clean-room study](docs/clean-room-study.md).

Every deep-read registry paper has a version-pinned paper record, a commit-pinned official implementation or explicit public-code status, at least one bounded claim, a full-paper interpretation, and three source-traceable key figures. The larger catalog records classic anchors, verified official-code papers, hardware evidence, and current topic gaps without pretending every queued item has already been deeply interpreted.

## Scope boundary

Core reproducibility uses GitHub, arXiv, official documentation/project pages, and manual imports. Social sources are optional and user-triggered: X defaults to bounded signed-in browser extraction with the paid official API as an opt-in; Zhihu uses official discovery plus bounded signed-in browser enrichment; Xiaohongshu uses bounded signed-in browser extraction with a manual queue fallback. Browser results describe only the visible bounded subset and never claim complete reply coverage. All remain outside offline builds and are never unattended dependencies. The project contains no cookie/profile reader, hidden API client, CAPTCHA/paywall bypass, background scheduler, or autonomous gated-platform daemon.

## Development

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
python3 scripts/check_corpus.py
python3 scripts/check_paper_quality.py
python3 scripts/render_paper_topics.py --check
```

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a source or claim. All current work is local; no remote repository is configured or pushed by this build process. Public repository identity and contact details remain explicit items in the [release checklist](docs/release-checklist.md).

## License and safety

Original code and documentation are Apache-2.0 licensed. Imported source material keeps its own copyright and license and should normally be represented by metadata, original summaries, short necessary excerpts, and links—not vendored full text.

This project is not a real-time controller. Hardware execution requires qualified human review, manufacturer limits, physical safeguards, and the complete safety case in [docs/safety.md](docs/safety.md).
