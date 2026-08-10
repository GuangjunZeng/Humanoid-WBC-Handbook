# Humanoid WBC Engineering Handbook

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

Import one manually reviewed source record:

```bash
PYTHONPATH=src python3 -m wbc_handbook import-source examples/manual-source.json --data-dir data
```

The importer performs no network access. Review the resulting JSON and add claims separately.

Create no-network plans for each social acquisition level:

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x --dry-run
PYTHONPATH=src python3 -m wbc_handbook social-collect-zhihu --dry-run
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu
```

When the user asks for a social-source update, X uses official X API v2, Zhihu uses
the official invited-preview search API, and Xiaohongshu uses a no-network human
review queue unless written platform permission is available. All candidates and
incremental state stay under ignored `var/`. Reviewed captures are normalized with
`import-social-captures`; `social-report` renders engineering problems and candidate
answers with mandatory original-post/reply links. See the
[Chinese collection runbook](docs/social-collection.md).

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
| `data/` | 28 canonical source records and 14 bounded, human-reviewed Engineering Claims |
| `docs/` | Architecture, safety, source policy, clean-room record, and workflows |
| `templates/` | Authoring templates, including full-paper interpretation |
| `tests/` | Offline deterministic acceptance tests |
| `var/` | Ignored generated indexes and test artifacts |

Start with the [paper corpus](content/papers/README.md), [on-demand paper update workflow](docs/on-demand-paper-update.md), [paper interpretation standard](docs/paper-interpretation.md), [architecture](docs/architecture.md), [data contract](docs/data-contract.md), [source gate](docs/source-feasibility/README.md), [safety policy](docs/safety.md), [Git commit conventions](docs/git-conventions.md), and [clean-room study](docs/clean-room-study.md).

Every deep-read registry paper has a version-pinned paper record, a commit-pinned official implementation or explicit public-code status, at least one bounded claim, a full-paper interpretation, and three source-traceable key figures. The larger catalog records classic anchors, verified official-code papers, hardware evidence, and current topic gaps without pretending every queued item has already been deeply interpreted.

## Scope boundary

Core reproducibility uses GitHub, arXiv, official documentation/project pages, and manual imports. Social sources are optional and user-triggered: X is collected through its official paid API, Zhihu discovery uses its official invited-preview API, and Xiaohongshu remains a human-review link queue until written permission exists. All remain outside offline builds and are never unattended dependencies. The project contains no cookie reader, hidden API client, CAPTCHA bypass, background scheduler, or gated-platform crawler.

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
