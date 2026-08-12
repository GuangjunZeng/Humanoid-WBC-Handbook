# 人形机器人 WBC 工程手册

**[English](README.md) | 中文**

[![人形机器人 WBC 工程手册中英文快速搜索预览](site/assets/search-preview.svg)](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/?lang=zh)

**[打开中英文快速搜索](https://guangjunzeng.github.io/Humanoid-WBC-Handbook/?lang=zh)**：无论当前界面语言如何，都可以用中文、英文或中英混合关键词搜索全部工程问题；可信度、解决状态和证据边界只在详情页展示。

<!-- BEGIN GENERATED PAPER ROUTES -->
## 论文地图：七个 WBC 工程板块

这里按技术路线进入，而不是堆一长串论文。每条路线只保留一篇领域经典或工程代表作；详情页解释机制、关键证据、实现位置和适用边界。

| 板块 | 技术路线 | 代表作深度解读 |
|---|---|---|
| 训练数据与动作重定向 | 统一人体动作语料 | [AMASS: Archive of Motion Capture as Surface Shapes](content/papers/amass-1904.03278v1.md) |
|  | 机器人动作重定向 | [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](content/papers/retargeting-matters-2510.02252v1.md) |
|  | 无机器人示教与在线可行性反馈 | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](content/papers/humi-2602.06643v2.md) |
| 通用跟踪与全身遥操 | 稠密实时全身遥操 | [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](content/papers/h2o-2403.04436v1.md) |
|  | 头手稀疏指令 | [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](content/papers/omnih2o-2406.08858v1.md) |
|  | 掩码式多模式控制 | [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](content/papers/hover-2410.21229v2.md) |
| 行走与复杂地形 | ZMP 预览控制 | [Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point](content/papers/zmp-preview-kajita-2003.md) |
|  | 周期奖励的仿真到现实强化学习 | [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](content/papers/periodic-gaits-2011.01387v2.md) |
|  | 开源零样本迁移 | [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](content/papers/humanoid-gym-2404.05695v2.md) |
|  | 轨迹预训练与地形微调 | [Learning Humanoid Locomotion over Challenging Terrain](content/papers/challenging-terrain-2410.03654v1.md) |
| 移动操作与末端 WBC | 层级操作空间全身控制 | [A Whole-Body Control Framework for Humanoids](content/papers/sentis-wbc-2006.md) |
|  | 优化式任务空间逆动力学 | [Implementing Torque Control with High-Ratio Gear Boxes and without Joint-Torque Sensors](content/papers/hrp2-torque-control-hal-01136936.md) |
|  | 受力感知双策略学习 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](content/papers/falcon-2505.06776v2.md) |
|  | 统一策略课程学习 | [ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation](content/papers/ulc-2507.06905v2.md) |
| 体育与高动态技能 | 示例引导的高动态技能 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](content/papers/deepmimic-1804.02717v3.md) |
|  | 行走、恢复与策略一体化 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](content/papers/agile-soccer-2304.13653v2.md) |
|  | 真实物理残差对齐 | [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](content/papers/asap-2502.01143v3.md) |
|  | 多阶段任务交互 | [Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning](content/papers/humanoid-badminton-2511.11218v3.md) |
| 动作生成与可命令行为 | 示例引导动作控制 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](content/papers/deepmimic-1804.02717v3.md) |
|  | 对抗运动先验 | [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](content/papers/amp-2104.02180v2.md) |
|  | 掩码动作补全 | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](content/papers/maskedmimic-2409.14393v1.md) |
|  | 测试时引导扩散 | [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](content/papers/beyondmimic-2508.08241v4.md) |
| 起身恢复、跌倒与受力安全 | 倒地恢复与起身统一控制 | [FRASA: An End-to-End Reinforcement Learning Agent for Fall Recovery and Stand Up of Humanoid Robots](content/papers/frasa-2410.08655v3.md) |
|  | 多样姿态起身 | [Learning Humanoid Standing-up Control across Diverse Postures](content/papers/host-2502.08378v2.md) |
|  | 保护性跌倒 | [SafeFall: Learning Protective Control for Humanoid Robots](content/papers/safefall-2511.18509v1.md) |
|  | 力矩约束的受力交互 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](content/papers/falcon-2505.06776v2.md) |

这是一张有意克制的入口地图；包含待深读经典论文与已核验官方代码论文的完整目录见 [`content/papers/`](content/papers/README.md)。
<!-- END GENERATED PAPER ROUTES -->
---
这是一个原创、离线优先的工具集，把论文、源码、Issue、Release、官方文档和经授权的工程记录，转化为可审计的人形机器人全身控制（Whole-Body Control, WBC）问题解答。

当前状态：alpha。论文覆盖目录横跨七个 WBC 工程板块，并用质量门维护深度解读集合。当前快照收录 46 篇互不重复的论文，其中 25 篇已完成中文全文深读，21 篇经典或开源工作仍在深读队列。README 路线图以 26 条技术路线组织 24 篇互不重复的代表作，并为每篇提供已审阅英文页。任何内容用于实机前，仍须由具备资质的人员完成技术与安全复核。

## 什么样的答案可以发布

正式答案来自已审核的 `EngineeringClaim` 记录。每条结论都必须包含：

- 一个原子的工程陈述，以及它回答的具体问题；
- 支持、冲突、替代和背景证据链接；
- 精确的证据定位与规范化原始 URL；
- 机器人、仿真器、控制器和环境的适用条件；
- 置信度、书面理由与复核日期；
- 对实机关键建议强制要求的“先仿真”安全论证。

本工具不会把点赞、浏览量或 Star 当成技术可信度。没有已审核结论时，它会明确返回“没有已审核结论”，而不是编造答案。

## 快速上手

只需要 Python 3.9+；运行时刻意保持零第三方依赖。

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
wbc-handbook validate --data-dir data
wbc-handbook build-index --data-dir data --index var/handbook.sqlite
wbc-handbook query "全身遥操作需要全局线速度吗？" --index var/handbook.sqlite
```

不安装也可以运行：

```bash
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
```

生成版本化的中英文问题详情页，再构建共用的离线搜索索引：

```bash
PYTHONPATH=src python3 -m wbc_handbook render-problems \
  --data-dir data --translations-dir data/locales/en/problems \
  --output-dir content/problems
PYTHONPATH=src python3 -m wbc_handbook build-web-index \
  --data-dir data --translations-dir data/locales/en/problems \
  --problems-dir content/problems --output site/search-index.json
```

中文详情页继续使用 `content/problems/<id>.md`，对应英文页生成到 `content/problems/en/<id>.md`。两种界面语言检索同一个双语语料库，但搜索结果会跳转到当前界面的语言版本。源指纹会让 CI 拒绝缺失或已过期的英文记录。

代表论文页使用同样的审阅式本地化契约。中文分析是事实主记录；英文记录位于 `data/locales/en/papers/`，通过 SHA-256 绑定完整中文源。不使用在线翻译服务即可生成与检查：

```bash
PYTHONPATH=src python3 scripts/render_paper_translations.py
PYTHONPATH=src python3 scripts/render_paper_translations.py --check
python3 scripts/render_paper_topics.py --check
PYTHONPATH=src python3 scripts/check_paper_quality.py
```

中文事实发生任何变化，英文记录都会立即过期，直到人工复核更新。生成器还会拒绝代表作缺失、孤立译文、中文证据页中不存在的新外链、核心章节缺失或语言互链断裂。

导入一条已人工审核的来源记录：

```bash
PYTHONPATH=src python3 -m wbc_handbook import-source examples/manual-source.json --data-dir data
```

导入器不访问网络。生成的 JSON 必须人工复核，工程结论需要另行建立。

为不同社交信息获取层级生成计划：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform x --max-posts-per-run 15
PYTHONPATH=src python3 -m wbc_handbook social-collect-zhihu --dry-run
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu
PYTHONPATH=src python3 -m wbc_handbook github-issue-plan
# GITHUB_TOKEN 只用于免费提高速率限制，可选：
PYTHONPATH=src python3 -m wbc_handbook github-issue-collect
# 付费 X API 是可选模式：PYTHONPATH=src python3 -m wbc_handbook social-collect-x --dry-run
```

当用户要求更新社交来源时，X 默认使用无需 API 费用的有界可见浏览器搜索、详情与回复提取；知乎使用官方邀测搜索 API 发现并通过有界可见浏览器补充；小红书使用有界可见浏览器搜索和详情提取，离线人工队列作为降级方案。用户只处理登录失效、验证码、风控、付费墙或内容不可访问，不需要逐帖导航。原始候选和增量状态保存在忽略的 `var/` 下，最小 URL 级清单提交到 `data/`。经审核的捕获由 `import-social-captures` 规范化；`social-report` 按稳定问题 ID 汇总经验，保留问题级与经验级分级、原帖/回复链接、答案状态和采集完整度。中英文帖子都以中文为主提炼，并采用 `中文（English, ABBR）` 术语格式。入口见[中文工程问题手册](content/social-engineering-candidates.md)、[采集手册](docs/social-collection.md)、[可见浏览器执行约定](docs/social-browser-automation.md)、[跨轮次发现演进机制](docs/social-discovery-evolution.md)与[可信度和全候选清单标准](docs/social-credibility-and-inventory.md)。付费 X API 只在用户明确选择时启用，见 [X API 自动化说明](docs/x-api-automation.md)。

查看论文板块覆盖，并按需执行有界发现：

```bash
PYTHONPATH=src python3 -m wbc_handbook papers-status
PYTHONPATH=src python3 -m wbc_handbook papers-discover \
  --max-per-topic 8 --out var/paper-candidates.json
```

论文发现不定时运行，也不会自动接受候选。只有用户提出更新要求时，才执行[论文库按需更新流程](docs/on-demand-paper-update.md)；该流程只复用 `paper-daily` 的单篇论文分析方法，不包含推送、日报或订阅。

## 仓库地图

| 路径 | 用途 |
|---|---|
| `src/wbc_handbook/` | 原创的数据模型、校验、导入、论文覆盖、按需社交采集、索引、回答与 CLI 代码 |
| `config/social-queries.json` | X、知乎和小红书共享的开放 WBC 工程问题范围；domain hint 不是采集边界 |
| `content/papers/` | 论文覆盖目录、质量门深读注册表、生成的 topic 索引、中文解读和关键图清单 |
| `content/problems/` | 生成的中文工程问题页，以及 `content/problems/en/` 下对应英文页 |
| `data/` | 规范化来源、最小全候选社交/Issue 索引和经人工审核的 `EngineeringClaim` |
| `data/locales/en/problems/` | 已审核、可版本控制并带源指纹过期检查的英文问题译文 |
| `docs/` | 架构、安全、来源政策、clean-room 记录与工作流 |
| `site/` | 无运行时依赖的双语 GitHub Pages 搜索界面、vendored FlexSearch、SVG 背景和生成索引 |
| `templates/` | 内容模板，包括完整单篇论文解读模板 |
| `tests/` | 离线、确定性的验收测试 |
| `var/` | 被忽略的生成索引、原始缓存和测试产物 |

建议从[论文语料库](content/papers/README.md)、[论文库按需更新流程](docs/on-demand-paper-update.md)、[单篇论文解读标准](docs/paper-interpretation.md)、[架构](docs/architecture.md)、[数据契约](docs/data-contract.md)、[来源门禁](docs/source-feasibility/README.md)、[安全政策](docs/safety.md)、[Git 提交约定](docs/git-conventions.md)和 [clean-room 调研](docs/clean-room-study.md)开始。

每篇进入深读注册表的论文，都必须有锁定版本的论文记录、锁定提交的官方实现或明确的未公开代码结论、至少一条有边界的工程结论、完整论文解读和三张可追溯关键图。更大的 catalog 用来记录经典锚点、已核验官方代码、实机证据和板块缺口，不会把排队论文伪装成已完成深读。

## 范围边界

核心可复现来源是 GitHub、arXiv、官方文档/项目页和手工导入。社交来源是可选且由用户触发的：X 默认使用有界登录浏览器，付费官方 API 仅为显式选择项；知乎使用官方发现加有界登录浏览器补充；小红书使用有界登录浏览器并提供人工队列降级。浏览器结果只描述当前可见的有限子集，不声称覆盖全部回复。它们都不属于离线构建的强依赖，也不会成为无人值守后台任务。本项目不读取 Cookie/浏览器 profile，不调用隐藏接口，不绕过验证码或付费墙，也不提供后台调度器或自主运行的受限平台爬虫。

## 开发与校验

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m wbc_handbook validate --data-dir data
python3 scripts/check_corpus.py
python3 scripts/check_paper_quality.py
python3 scripts/render_paper_topics.py --check
```

提交来源或结论前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。公开仓库身份、联系信息和发布项见[发布检查清单](docs/release-checklist.md)。

## 许可证与安全

原创代码与文档采用 Apache-2.0。导入材料保留各自版权和许可证；通常只保存元数据、原创摘要、必要短引文和链接，不复制完整原文。

本项目不是实时控制器。任何实机执行都必须经过具备资质的人工复核、厂商限值检查、物理防护，以及 [docs/safety.md](docs/safety.md) 规定的完整安全论证。
