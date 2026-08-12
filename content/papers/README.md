# Humanoid WBC 论文库

本目录分成两层：[`catalog.json`](catalog.json) 是经典论文、官方开源工作和板块缺口的覆盖目录；[`registry.json`](registry.json) 只包含已通过全文解读质量门的论文。当前快照收录 46 篇唯一作品，其中 25 篇深度解读、21 篇待深读。

这个目录是可按需更新的领域地图，不声称永久穷尽所有论文。更新只在用户明确要求时执行，不定时、不订阅、不推送。

## 当前板块覆盖

| 板块 | 收录 | 深度解读 | 待深读 | 可核验官方代码 |
|---|---:|---:|---:|---:|
| [训练数据与动作重定向](domains/training-data-retargeting.md) | 7 | 4 | 3 | 6 |
| [通用跟踪与全身遥操](domains/universal-tracking-teleoperation.md) | 11 | 5 | 6 | 9 |
| [行走与复杂地形](domains/locomotion-terrain.md) | 9 | 4 | 5 | 6 |
| [移动操作与末端 WBC](domains/loco-manipulation-wbc.md) | 6 | 4 | 2 | 4 |
| [体育与高动态技能](domains/sports-athletic-skills.md) | 7 | 4 | 3 | 3 |
| [动作生成与可命令行为](domains/motion-generation.md) | 11 | 5 | 6 | 11 |
| [起身恢复、跌倒与受力安全](domains/recovery-safety-force.md) | 9 | 5 | 4 | 5 |

同一篇论文可以属于多个 topic，所以板块行数之和大于 46；目录本身仍按 `paper_id` 与去版本的 arXiv 主键去重。

## 深度解读完成门

- 阅读锁定版本的完整论文与相关附录，不以摘要代替全文；
- 中文为主，关键术语使用“中文（English）”；长度服从证据，不为字数、段落、类比或“金句”配额补写空话；
- 说清工程痛点、输入 → 处理 → 输出机制、最强实验、可执行但有边界的结论；
- 嵌入至少 3 张从锁定 PDF 渲染的关键图/表，解释它们能与不能支持的结论；
- 每张图有源 PDF、页码、定位、中文图注和 SHA-256 清单，只用于分析原论文；
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

## 离线检查

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status
python3 scripts/extract_key_figures.py --check
python3 scripts/check_paper_quality.py
PYTHONPATH=src python3 scripts/render_paper_translations.py --check
python3 scripts/render_paper_topics.py --check
python3 scripts/check_corpus.py
```

以上检查分别验证目录去重/角色覆盖、关键图完整性、中文全文解读、英文译文覆盖与指纹、topic 页同步，以及 deep-read source/claim 闭环。
