# Meta Motivo：面向虚拟人形的零样本行为基础模型代码

[English version](en/meta-motivo.md)

审阅快照：[facebookresearch/metamotivo@`ff8dcc55cf58f766d365ab0be23a021a7e34d53d`](https://github.com/facebookresearch/metamotivo/tree/ff8dcc55cf58f766d365ab0be23a021a7e34d53d) · 778 stars（2026-08-12 快照）· CC-BY-NC-4.0。对应论文：[Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models, arXiv:2504.11054](https://arxiv.org/abs/2504.11054)。star 只用于发现，不是科学置信度或真机安全等级。

## 为什么收录

Meta Motivo 最初被归为“纯项目”，但官方仓库 citation 与 arXiv 已明确给出论文，因此修正为官方论文代码。它代表运动生成 topic 中不同于逐动作 tracker 的路线：在 HumEnv 的 SMPL 虚拟人形上学习 forward-backward representation，并通过奖励、目标或跟踪上下文零样本提示同一策略。

独立项目页很必要，因为仓库公开预训练模型、buffer、HumEnv benchmark wrapper 和后续 FB-CPR 训练代码，读者需要区分“论文方法”“当前 release 能运行的推理”“后来补充的训练实现”。它不是 Unitree 等硬件 WBC，不应因使用 humanoid 一词被写成真机基线。

## 它解决什么问题

任务专用 RL 每换一个奖励或动作目标就要重新训练。无监督零样本 RL 希望预训练一个条件策略，通过 latent context 适配奖励、目标状态或示范轨迹。普通覆盖型预训练可能探索很多状态，却不保证行为像人体动作；Meta Motivo 用 observation-only 动作数据正则化策略覆盖，使潜空间更贴近可用行为。

工程上，用户先从 buffer 与任务定义推断 latent `z`，再调用 `model.act(observation, z)`。奖励推断、目标推断与 tracking inference 是不同上下文构造过程；把它们都叫“prompt”不能忽略其所需数据量、计算成本和 evaluation protocol。

## 架构与数据流

主要路径是 `HumEnv observation-only buffer → forward/backward encoders + conditional policy → FB-CPR agent training → checkpoint → reward/goal/tracking context inference → model.act → HumEnv`。`fb` 与 `fb_cpr` 目录区分基础 forward-backward 与条件策略正则化版本，Hugging Face helper 加载发布模型。

benchmark wrapper 把模型适配到 HumEnv 的 reward、goal 与 tracking evaluation，并可用大量 buffer 样本推断 reward context。tracking wrapper 则从参考下一状态序列生成逐时刻 context。它们衡量虚拟角色状态控制，不包括机器人关节限制、执行器或 sim-to-real。

## 代码定位

- [`metamotivo/fb_cpr/agent.py`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/agent.py) 组织 FB-CPR 更新、context 与策略训练。
- [`metamotivo/fb_cpr/model.py`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/model.py) 定义部署侧模型组件与 action 接口。
- [`RewardWrapper`、`GoalWrapper` 与 `TrackingWrapper`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/wrappers/humenvbench.py) 把 latent inference 映射到 HumEnv benchmark。
- [`ZBuffer`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/misc/zbuffer.py) 管理 latent/context 样本，影响上下文搜索与复用。
- [`FBcprModel.from_pretrained`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/huggingface.py) 是固定发布模型与代码兼容性的加载边界。

## 最小复现路径

固定 HumEnv、模型 release、buffer、仓库 commit 与随机种子，先在 CPU 加载 `facebook/metamotivo-S-1`，对一个标准任务运行固定 observation 和 latent，保存 action 输出作为 smoke test。然后分别复现 reward、goal 与 tracking wrapper，禁止在同一数字里混合三种 protocol。

完整报告应记录 context inference 使用的样本数、并行 worker、时间、任务列表、初始状态分布和 episode 数；报告均值与方差、失败任务和 inference cost。训练复现还需区分当前 FB-CPR 代码与论文最初发布快照，并保存数据许可和 checkpoint 哈希。

## 能力边界

结果面向 HumEnv/SMPL 虚拟人形，不包含真实机器人形态重定向、接触传感、状态估计、关节力矩或通信延迟。零样本表示下游不再梯度训练，不表示不需要 buffer、任务定义或上下文推断计算。

许可证为非商业 CC-BY-NC-4.0，不能按宽松代码许可证使用。预训练模型、数据和依赖还可能有单独条款。论文 benchmark 的任务分布不能外推到真实地形、操作或高动态体育动作。

## 工程判断与风险

Meta Motivo 适合作为通用行为表征研究锚点，也可作为上层运动建议器；若接入机器人 WBC，必须加入显式重定向、动力学可行性、碰撞、接触和低层安全过滤，并重新验证延迟与频率。其 latent 可控性不等于每个中间 context 都语义稳定。

不要把 HumEnv render 直接当作硬件部署证据。任何真实机器人实验都需要独立 tracker/WBC、限位、低增益、支撑/吊装、急停和逐动作审核。高 star 和“foundation model”名称都不能代替安全 case；本页不提供上机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/facebookresearch/metamotivo/tree/ff8dcc55cf58f766d365ab0be23a021a7e34d53d)
- [arXiv:2504.11054](https://arxiv.org/abs/2504.11054)
- [CC-BY-NC-4.0 许可证](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/LICENSE)
