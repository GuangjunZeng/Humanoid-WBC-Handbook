# Humanoid WBC Engineering Handbook

[![Humanoid WBC Engineering Handbook 中英文快速搜索预览](site/assets/search-preview.svg)](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/)

**[打开中英文快速搜索](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/)**：所有工程问题均可搜索；可信度、状态和证据边界在独立详情页查看。

---

An original, offline-first toolkit for turning papers, code, issues, releases, official documentation, and authorized field notes into auditable answers to concrete humanoid whole-body-control questions.

Status: alpha implementation with a coverage catalog spanning seven WBC engineering domains and a quality-gated deep-read corpus. The current snapshot contains 46 unique papers (14 complete Chinese deep reads and 32 queued classics/open-source works). Content still requires qualified human technical and safety review before hardware use.

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

Render every Chinese-first problem page and build the static bilingual index:

```bash
PYTHONPATH=src python3 -m wbc_handbook render-problems \
  --data-dir data --output-dir content/problems
PYTHONPATH=src python3 -m wbc_handbook build-web-index \
  --data-dir data --problems-dir content/problems --output site/search-index.json
```

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
| `content/problems/` | One Chinese-first, bilingual-terminology Markdown detail page per Engineering Claim or engineering QA |
| `data/` | 174 canonical source records, a minimal all-candidate social/Issue index, and 14 bounded, human-reviewed Engineering Claims |
| `docs/` | Architecture, safety, source policy, clean-room record, and workflows |
| `site/` | Dependency-free GitHub Pages search UI, vendored FlexSearch, SVG background, and generated static index |
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

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a source or claim. Public repository identity and contact details remain explicit items in the [release checklist](docs/release-checklist.md).

## License and safety

Original code and documentation are Apache-2.0 licensed. Imported source material keeps its own copyright and license and should normally be represented by metadata, original summaries, short necessary excerpts, and links—not vendored full text.

This project is not a real-time controller. Hardware execution requires qualified human review, manufacturer limits, physical safeguards, and the complete safety case in [docs/safety.md](docs/safety.md).
