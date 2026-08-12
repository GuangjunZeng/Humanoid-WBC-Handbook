# 单篇论文深度解读流程

本流程只复用本地 `paper-daily` 中的“单篇论文分析”方法。Scholar Inbox、定时任务、飞书、消息、推送、订阅状态和日报功能都不属于本项目。

## 阅读与核验

1. 下载并阅读锁定版本的完整 PDF，包括对实现、消融、参数和限制有用的附录；不以摘要或项目页代替全文。
2. 说清工程痛点、先前方法为什么不足，以及论文实际声称的贡献；不把后来仓库能力倒写成论文贡献。
3. 用“输入 → 处理 → 输出 → 为什么可能有效”追踪主机制，解释决定性公式而不堆砌符号。
4. 先建立“结论 → Figure/Table → PDF 物理页 → 原始 caption → 支持/不支持什么”的证据表，再选 3–5 张最能支持分析的原论文图/表。优先系统图、机制消融、最强实验、失败例和与代码接口有关的表；不得先猜页码再生成截图。
5. 使用锁定 PDF 的 SHA-256 和 `research/key-figures.json` schema v2。每个 region 必须记录物理页、规范化 crop 和 caption anchor；图号、表号和完整 caption 文本块都必须落在裁剪区内。
6. 关键图只能是“具体 Figure/Table 本体 + 该图表原始完整 caption”的紧裁剪。严禁整页论文截图、仅包含正文引用却没有图表的页、项目页截图、caption 被截断、相邻图表残片或无关正文。跨页/多图组合只能拼接分别核验的 region，中间不夹正文。
7. 生成全分辨率 contact sheet 并逐张人工查看。审阅者确认图号、内容、caption 和详情页解释一致后，才运行 `extract_key_figures.py --record-visual-review <reviewer>`；crop、PDF、locator、支持边界或图注一变，review fingerprint 自动过期。CI 不得自动批准。
8. 对每张图说明“看什么”、“它支持哪个结论”和“不能支持什么”；不把图当装饰，不把最佳轨迹当平均表现。图里没有的分母或数值必须明确定位到正文/Table，不能把正文事实冒充图上可见内容。
9. 选出最有说服力的实验，写清基线、自变量、指标、分母、环境和结论边界；优先保留负面结果和失败模式。
10. 有公开代码时，只使用官方仓库并固定 commit，将至少两个论文组件映射到具体文件、函数或类；无公开代码时明确写“未公开/无法核验”，不用第三方实现填空。
11. 分开“作者明确局限”与“独立工程判断”。记录机器人、模拟器、传感器、控制频率、动作空间、数据、计算和部署假设中已报告与未报告的部分。
12. 涉及实机时，明确安全条件、缺失的保护、sim-to-real 不确定性与 ODD；论文参数不得被表述为其他机器人可直接下发的安全限值。

## 写作标准

- 正文以中文为主，关键术语首次出现使用“中文（English）”；不使用大段英文转述，也不为了满足篇幅重复摘要、堆砌“重要/先进/显著”等空泛判断。
- 每篇至少 3000 个汉字、15 个正文段落、6 组中英术语、3 张来自锁定 PDF 的关键图，并保留图的页码、来源 URL 和完整性哈希。
- 结构至少包含：一句话总结、术语导航、工程痛点、核心洞察、方法主线、关键图解、最强实验、论文—代码/实现状态、局限、有边界结论和“复现与验收清单”。
- 每段必须至少完成一项工程工作：解释机制、给出事实/定位、划清外推边界、映射实现接口、提炼失败模式或定义复现验收；删掉不承担这些作用的段落。
- 量化陈述附带 Figure/Table/Equation 定位；不确定信息保持未知，不从 README 或视频补写论文未报告的分母。
- 依次运行 `python3 scripts/extract_key_figures.py --check` 和 `python3 scripts/check_paper_quality.py`，只有图表审阅与全文质量门都通过才能把 `analysis_status` 改为 `deep_read`。

## 关键图作者工作流

```bash
# 1. 锁定 PDF 后生成/更新精确裁剪与 manifest
python3 scripts/extract_key_figures.py --force --paper <slug> \
  --audit-sheet var/<slug>-key-figure-audit.jpg

# 2. 人工逐张查看全分辨率 audit sheet 后，显式记录审阅
python3 scripts/extract_key_figures.py --paper <slug> \
  --record-visual-review <reviewer>

# 3. 重新生成 manifest 中的 review 元数据并执行只读门禁
python3 scripts/extract_key_figures.py --paper <slug>
python3 scripts/extract_key_figures.py --check --paper <slug>
```

`--record-visual-review` 是人工审阅的留痕命令，不是自动验图器；不得在 CI、批量迁移或未打开 audit sheet 时调用。`var/` 中的 PDF 和联系表不提交，仓库只保留紧裁剪、manifest 和审阅指纹。

完整解读只是证据输入，不会自动成为已评审 `EngineeringClaim`。

## 代表作双语页

README 技术路线选中的代表作必须同时有中英文页。中文深读是事实主记录；英文内容是已审阅的紧凑解读，保留工程问题、方法、三张关键图、决定性证据、代码/公开状态、边界、结论和复现清单，不运行时机翻。

- 已审阅英文记录位于 `data/locales/en/papers/`，完整中文页的 SHA-256 存入 `source_fingerprint`。
- 中文事实、图表或代码边界修改后，旧英文记录必须过期，不允许 CI 继续发布。
- 英文页只能复用中文证据页已核验的外链；不得在翻译时新增未核验代码或项目链接。
- 运行 `PYTHONPATH=src python3 scripts/render_paper_translations.py --check`，验证 24 篇当前代表作的覆盖、指纹、章节、图片和双向语言链接。
