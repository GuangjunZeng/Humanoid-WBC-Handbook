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
6. For papers, follow `docs/paper-interpretation.md` and `docs/on-demand-paper-update.md` before marking a paper-backed claim reviewed.
7. For hardware-critical material, complete every safety field and obtain qualified human review.

## Social engineering experience

- Social discovery uses open engineering `scope_id` values; the seven paper/claim domains are optional hints and must not limit collection coverage.
- Extract the reported environment, observable symptom, diagnostics, attempted changes, outcome, limitations, and safety context when present. Never fill absent details by inference.
- Every extracted engineering question and candidate answer must include the stable original-post URL and a precise body/comment locator.
- If the post does not provide an answer, keep `answer_status=unresolved`; do not invent a solution.
- Community answers stay candidates until independently checked against stronger sources. Likes, saves, and comments are ranking signals only.

## Local checks

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
PYTHONPATH=src python3 -m wbc_handbook build-index --data-dir data --index var/handbook.sqlite
PYTHONPATH=src python3 -m wbc_handbook papers-status
python3 scripts/check_paper_quality.py
python3 scripts/extract_key_figures.py --check
python3 scripts/render_paper_topics.py --check
python3 scripts/check_corpus.py
```

论文发现只在维护者明确要求时运行 `papers-discover`。项目不为论文分析配置定时任务、推送或摘要分发。

## Git commits

所有提交必须遵守 [Git 提交规范](docs/git-conventions.md)：使用有限的 Conventional Commits 类型、稳定 scope、可回滚的原子改动和明确验证记录。
