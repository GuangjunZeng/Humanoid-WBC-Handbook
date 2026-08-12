# 论文库按需自主更新

这是一个由用户明确请求触发的一次性流程。它不创建定时任务，不订阅 Scholar Inbox，不向飞书/邮件/消息平台推送，也不在后台自动运行。

## 何时执行

当用户说“更新论文库”、“更新某个 topic”、“补齐经典/开源论文”或含义等价的请求时，执行本流程。如果用户只指定一个 topic，只扩展该板块；如果未指定，按覆盖缺口从七个板块中自主排序。

## 阶段 A：离线覆盖审计

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status \
  --catalog content/papers/catalog.json \
  --registry content/papers/registry.json
```

1. 核对 `catalog.json` 是否无重复 arXiv 作品，已核验官方代码是否有 URL，深度解读与 `registry.json` 是否一致。
2. 按 topic 查看必要角色缺口。优先级从高到低为：缺失的经典基线、缺失的开源实现、实机/负面证据、新方法。
3. “已收录”不等于“已深读”。队列中的论文用来表达板块地图，只有通过全文质量门才能升级。

## 阶段 B：有界网络发现

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-discover \
  --topic locomotion_terrain \
  --catalog content/papers/catalog.json \
  --max-per-topic 8 \
  --out var/paper-candidates-YYYY-MM-DD.json
```

`--topic` 可重复使用；省略时才扫描全部七个板块。当用户只点名一个板块时，命令也必须给出对应 `--topic`，不应用全库扫描代替。

发现命令只查询 arXiv 主记录，自动去除已知版本，根据 topic 关键词排序，并写入忽略的 `var/`。输出固定为 `mode=manual_on_demand` 和 `auto_accepted=false`：发现结果不能仅凭关键词自动进入正式目录。

执行更新的 agent 随后自主完成有限候选的主来源核验：

- 使用 arXiv/出版方记录确认论文身份与版本；
- 使用作者项目页或作者/实验室 GitHub 确认官方代码、许可证和开源范围；
- 查看引用谱系与后续方法对它的定位，判断是否属于经典锚点；
- 只收录与 Humanoid WBC 控制链有明确关系的工作，不因标题含“humanoid”就纳入。

## 阶段 C：更新目录

对通过核验的论文，将主记录加入 `content/papers/catalog.json`：

- `paper_id` 使用可去重的主键，arXiv 版本不作为新作品重复收录；
- 至少写入一个 topic、覆盖角色、主论文 URL、代码状态与中文收录理由；
- 尚未做完全文解读时标记 `queued`，不建立空白 brief 冒充完成；
- 更新 `updated_at`，运行 `papers-status` 与 `python3 scripts/render_paper_topics.py`。

## 阶段 D：升级为深度解读

根据板块缺口和用户范围，选择有限数量的高优先级论文。对每篇执行 [`paper-interpretation.md`](paper-interpretation.md)：完整 PDF、官方代码映射、3–5 张关键图、中文为主的 3000+ 汉字解读、最强实验、作者/独立局限与安全边界。

只有以下检查全部通过才能更新 `registry.json`、深度 source 和 claim：

```bash
python3 scripts/extract_key_figures.py --check
python3 scripts/check_paper_quality.py
PYTHONPATH=src python3 scripts/render_paper_translations.py --check
python3 scripts/render_paper_topics.py --check
python3 scripts/check_corpus.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

若新深读被选为 README 技术路线的代表作，必须先在 `data/locales/en/papers/` 补齐已审阅英文记录并生成 `content/papers/en/`；缺失或 stale 时不能更新 README 路线。普通队列论文不要建空白英文页冒充解读。

## 更新完成的报告

交付时报告：新发现数、因重复/非官方代码/与 WBC 无关而排除的数量、每个 topic 新增条目、新增深度解读、仍存在的覆盖缺口和所有质量检查结果。一次更新结束后不保留后台任务。
