# Contributing

## Before opening a change

- Use an issue/design discussion for new schemas, collectors, domains, or safety behavior.
- Keep changes independently written; follow `docs/clean-room-study.md`.
- Do not commit secrets, cookies, tokens, private community content, restricted full text, generated indexes, or robot logs containing personal/sensitive data.
- Confirm that you have the right to contribute every original or imported artifact.

## Source and claim review

1. Record canonical URL, access mode, capture time, version, license when known, and integrity hash.
2. Write an original concise summary and use only a short necessary excerpt.
3. Attach evidence to one atomic claim with a precise locator.
4. Record conflicts and negative results; do not silently select only favorable evidence.
5. Keep attention signals separate from evidence strength.
6. For papers, follow `docs/paper-interpretation.md` before marking a paper-backed claim reviewed.
7. For hardware-critical material, complete every safety field and obtain qualified human review.

## Local checks

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
PYTHONPATH=src python3 -m wbc_handbook build-index --data-dir data --index var/handbook.sqlite
```

Use focused commits. Explain the engineering problem, evidence, applicability, safety impact, and tests in the change description.
