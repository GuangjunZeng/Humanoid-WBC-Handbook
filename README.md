# Humanoid WBC Engineering Handbook

An original, offline-first toolkit for turning papers, code, issues, releases, official documentation, and authorized field notes into auditable answers to concrete humanoid whole-body-control questions.

Status: alpha implementation with a complete frozen seed corpus: 14 original paper interpretations across seven WBC engineering domains. Content still requires qualified human technical and safety review before hardware use.

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

## Repository map

| Path | Purpose |
|---|---|
| `src/wbc_handbook/` | Original models, validation, import, index, answer, and CLI code |
| `content/papers/` | Frozen 14-paper registry, seven domain indexes, and original Chinese engineering interpretations |
| `data/` | 28 canonical source records and 14 bounded, human-reviewed Engineering Claims |
| `docs/` | Architecture, safety, source policy, clean-room record, and workflows |
| `templates/` | Authoring templates, including full-paper interpretation |
| `tests/` | Offline deterministic acceptance tests |
| `var/` | Ignored generated indexes and test artifacts |

Start with the [paper corpus](content/papers/README.md), [architecture](docs/architecture.md), [data contract](docs/data-contract.md), [source gate](docs/source-feasibility/README.md), [safety policy](docs/safety.md), and [clean-room study](docs/clean-room-study.md).

Every registered paper has a version-pinned paper record, a commit-pinned official implementation or explicit public-code status, at least one bounded claim, and a full-paper interpretation. The corpus is deliberately bounded and does not claim to exhaust the field.

## Scope boundary

Core reproducibility uses GitHub, arXiv, official documentation/project pages, and manual imports. Xiaohongshu, Zhihu, Discord, restricted comments, and other session-bound sources are not automated dependencies. The project contains no cookie reader, hidden API client, CAPTCHA bypass, or unattended gated-platform crawler.

## Development

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
python3 scripts/check_corpus.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a source or claim. All current work is local; no remote repository is configured or pushed by this build process. Public repository identity and contact details remain explicit items in the [release checklist](docs/release-checklist.md).

## License and safety

Original code and documentation are Apache-2.0 licensed. Imported source material keeps its own copyright and license and should normally be represented by metadata, original summaries, short necessary excerpts, and links—not vendored full text.

This project is not a real-time controller. Hardware execution requires qualified human review, manufacturer limits, physical safeguards, and the complete safety case in [docs/safety.md](docs/safety.md).
