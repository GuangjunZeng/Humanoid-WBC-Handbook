# Humanoid WBC 论文库

本目录分成三层：[`catalog.json`](catalog.json) 是经典论文、官方开源工作和板块缺口的覆盖目录；[`registry.json`](registry.json) 只包含已通过全文解读质量门的论文；[`project-catalog.json`](project-catalog.json) 单独记录高质量开源项目。当前论文快照收录 76 篇唯一作品，其中 14 篇已有完整中英文深度解读、62 篇经主来源核验后待深读；项目快照收录 43 个仓库，其中 11 个已有固定 commit 的完整中英文代码解读页。

这个目录是可按需更新的领域地图，不声称永久穷尽所有论文。更新只在用户明确要求时执行，不定时、不订阅、不推送。

## 当前板块覆盖

| 板块 | 收录 | 深度解读 | 待深读 | 可核验官方代码 |
|---|---:|---:|---:|---:|
| [训练数据与动作重定向](domains/training-data-retargeting.md) | 16 | 2 | 14 | 15 |
| [通用跟踪与全身遥操](domains/universal-tracking-teleoperation.md) | 22 | 3 | 19 | 20 |
| [行走与复杂地形](domains/locomotion-terrain.md) | 20 | 2 | 18 | 17 |
| [移动操作与末端 WBC](domains/loco-manipulation-wbc.md) | 15 | 2 | 13 | 12 |
| [体育与高动态技能](domains/sports-athletic-skills.md) | 11 | 2 | 9 | 7 |
| [动作生成与可命令行为](domains/motion-generation.md) | 20 | 2 | 18 | 20 |
| [起身恢复、跌倒与受力安全](domains/recovery-safety-force.md) | 16 | 3 | 13 | 11 |

同一篇论文或项目可以属于多个 topic，所以板块行数之和大于全局去重数量；论文目录仍按 `paper_id` 与去版本的 arXiv 主键去重，项目目录按 GitHub `owner/repo` 去重。

## 深度解读完成门

- 阅读锁定版本的完整论文与相关附录，不以摘要代替全文；
- 中文为主，不少于 3000 个汉字、15 个正文段落和 6 组“中文（English）”关键术语；
- 说清工程痛点、输入 → 处理 → 输出机制、最强实验、可执行但有边界的结论；
- 嵌入至少 3 张从锁定 PDF 渲染的关键图/表，解释它们能与不能支持的结论；
- 每张图有源 PDF、页码、定位、中文图注和 SHA-256 清单，只用于分析原论文；
- 中文页保留原 URL，英文伴随页放在 [`en/`](en/)；两页必须互链、复用同一组锁定 PDF 图证，并分别通过深度、结构、实验和安全边界门禁；
- 官方实现映射到至少两个文件/函数/类，或明确写代码未公开或无法核验；
- 作者明确局限与独立工程判断分开，实机结论包含 ODD、缺失保护与 sim-to-real 不确定性；
- 版本化 paper source、一条有边界的 `EngineeringClaim` 和所有离线检查通过。

完整标准见 [`docs/paper-interpretation.md`](../../docs/paper-interpretation.md)。本项目只使用 `paper-daily` 的论文分析步骤，不使用其推送或日报功能。

## 按需更新

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status
PYTHONPATH=src python3 -m wbc_handbook papers-discover \
  --max-per-topic 8 --out var/paper-candidates.json
```

候选集明确标记 `auto_accepted=false`。执行更新的 agent 使用主来源核对经典性、官方代码、许可证、与 WBC 的直接关系和 topic 缺口，再将通过者加为 `queued`。端到端流程见 [`docs/on-demand-paper-update.md`](../../docs/on-demand-paper-update.md)。

聚合清单（包括 [`humanoid-motion-intelligence`](https://github.com/RealXiaoze/humanoid-motion-intelligence)）只用来发现候选，不能成为论文编号、标题、代码关系或技术结论的最终依据。本轮发现的三条错误 arXiv 映射及其主来源纠正记录在 [`discovery-audit.json`](discovery-audit.json)，测试会阻止被拒绝的编号重新进入论文或项目目录。

高 Star、没有论文或仓库能力明显超出论文快照的项目使用独立证据链：

```bash
PYTHONPATH=src python3 -m wbc_handbook projects-status
PYTHONPATH=src python3 -m wbc_handbook projects-discover \
  --query "humanoid whole-body control" --out var/project-candidates.json
```

默认门槛为 80 stars；60–79 只有官方归属、topic 缺口和论文支撑同时成立时才可书面例外，低于 60 不收。每个 `deep_review` 项目都必须固定 40 位 commit、定位至少两个源码符号，并提供中文页与英文页。完整规范见 [`docs/project-interpretation.md`](../../docs/project-interpretation.md)。stars 只用于发现，不代表技术可信度。

## 离线检查

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status
python3 scripts/extract_key_figures.py --check
python3 scripts/check_paper_quality.py
python3 scripts/render_paper_topics.py --check
python3 scripts/check_corpus.py
```

以上检查分别验证目录去重/角色覆盖、关键图完整性、中英文全文解读、topic 页同步与 deep-read source/claim 闭环。
