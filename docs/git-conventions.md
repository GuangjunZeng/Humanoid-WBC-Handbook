# Git 提交规范

本项目使用 Conventional Commits 的有限子集，目标是让每个提交都能回答“改了什么、为什么改、怎样验证”。规范适用于人工与 agent 生成的所有提交。

## 标题格式

```text
<type>(<scope>): <summary>
```

- `type` 和 `scope` 使用小写英文；标题不超过 72 个字符，末尾不加句号。
- `summary` 使用祈使语气，描述可观察的改动，不使用 `update`、`changes`、`misc` 等无信息词。
- `scope` 必须能定位主要影响面；确实跨多个组件时可省略。

## 允许的 type

| Type | 用途 |
|---|---|
| `feat` | 新增用户可见能力、CLI 或工作流 |
| `fix` | 修复错误、数据不一致或安全边界 |
| `content` | 新增或实质修订论文解读与 topic 内容 |
| `data` | 修订 source、claim、catalog 或其他可审计数据 |
| `docs` | 只改文档、规范或示例 |
| `test` | 只改测试或测试数据 |
| `refactor` | 不改变外部行为的代码重构 |
| `chore` | 构建、CI、依赖或维护性工作 |

推荐 scope：`papers`、`social`、`cli`、`evidence`、`safety`、`tooling`、`docs`。需要新 scope 时应优先使用稳定的产品边界，不使用个人名、任务号或临时目录名。

## 提交正文

下列情况必须有正文：跨组件变更、证据/安全边界变更、数据迁移、兼容性变更、或者不能从 diff 直接推断动机的变更。正文用简短段落说明：

1. 问题与动机；
2. 关键实现和明确不在范围内的事项；
3. 证据、适用边界或安全影响；
4. 已运行的测试与结果。

破坏性变更在 type/scope 后加 `!`，并在 footer 写 `BREAKING CHANGE: ...`。关联 issue 时使用 `Refs: #123` 或 `Closes: #123`。

## 原子性与分组

- 一个提交只表达一个可回滚的工程意图；文档、测试和生成资产可与它们直接支持的实现同提交。
- 论文全文解读、关键图、manifest 与 catalog/registry 状态应作为一个不可分的证据单元。
- 不得提交 `var/`、下载的完整 PDF、cookie、token、私密内容、生成索引或机器人敏感日志。
- 工作区含有无关改动时，必须显式按路径暂存，不得盲目执行 `git add -A`。

## 提交前门禁

```bash
git diff --check
sh scripts/acceptance.sh
python3 scripts/check_paper_quality.py
python3 scripts/extract_key_figures.py --check
python3 scripts/render_paper_topics.py --check
```

只暂存目标文件，然后用 `git diff --cached` 复核最终提交。禁止用 `--no-verify` 跳过现有 hook；禁止对已共享提交做 force-push。

## 示例

```text
feat(social): add bounded X API candidate collection
content(papers): add figure-grounded Chinese deep reads
data(evidence): correct BeyondMimic code coverage boundary
docs(git): define commit and verification conventions
fix(safety): require hardware validation envelope
```
