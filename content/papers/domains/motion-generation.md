# 动作生成与可命令行为

本板块位于高层命令与低层跟踪器之间。BeyondMimic 用可微测试时代价引导扩散采样，TextOp 用文本与历史动作块自回归生成；两者的生成质量、响应时间和跟踪稳定性必须分层度量。

- [BeyondMimic](../beyondmimic-2508.08241v4.md)：状态潜变量扩散、测试时代价、自动梯度引导和可组合约束。
- [TextOp](../textop-2602.07439v1.md)：CLIP 条件、机器人骨架动作块、6.25 Hz 生成与 50 Hz G1 跟踪。

建议联读问题：采样时引导何时破坏动作转场？模块计算延迟与人感知的命令响应为何必须分别报告？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：11 篇，其中深度解读 2 篇，有可核验官方代码 11 篇。
- 必要覆盖角色：领域锚点（field anchor）、潜技能（latent skill）、开源实现（open source）、机器人部署（robot deployment）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](../beyondmimic-2508.08241v4.md) | 2025 | 潜技能（latent skill）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/HybridRobotics/whole_body_tracking) | 用状态潜变量扩散与可微测试时代价将跟踪技能组合为新任务。 |
| 深度解读 | [TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control](../textop-2602.07439v1.md) | 2026 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/TeleHuman/TextOp) | 用流式文本、自回归短动作块和独立跟踪器实现可随时改写的真机运动。 |
| 待深读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 待深读 | [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](https://arxiv.org/abs/2104.02180) | 2021 | 领域锚点（field anchor）、开源实现（open source）、潜技能（latent skill） | [官方代码](https://github.com/isaac-sim/IsaacGymEnvs) | 用对抗运动先验取代繁重的逐项风格奖励，是后续动作先验控制的关键基线。 |
| 待深读 | [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](https://arxiv.org/abs/2205.01906) | 2022 | 潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/nv-tlabs/ASE) | 将大规模动作数据压入可重用技能嵌入，为下游分层任务提供动作基元。 |
| 待深读 | [CALM: Conditional Adversarial Latent Models for Directable Virtual Characters](https://arxiv.org/abs/2305.02195) | 2023 | 潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 联合学习控制策略和动作编码器，使潜空间同时支持重建、风格和高层任务控制。 |
| 待深读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](https://arxiv.org/abs/2305.06456) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 待深读 | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](https://arxiv.org/abs/2409.14393) | 2024 | 潜技能（latent skill）、开源实现（open source）、多模式（multi-mode） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 把关键帧、文本、场景和稀疏目标统一为掩码动作补全问题。 |
| 待深读 | [Universal Humanoid Motion Representations for Physics-Based Control](https://openreview.net/forum?id=OrOd8PxOO2) | 2024 | 潜技能（latent skill）、领域锚点（field anchor） | [官方代码](https://github.com/ZhengyiLuo/PHC) | PULSE 将大规模通用跟踪器蒸馏为带本体条件先验的通用运动表示。 |
| 待深读 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://arxiv.org/abs/2506.12851) | 2025 | 开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction） | [官方代码](https://github.com/TeleHuman/PBHC) | 面向武术类高动态动作的多阶段运动处理、自适应跟踪与真机开源基线。 |
| 待深读 | [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820) | 2025 | 多模式（multi-mode）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/NVlabs/GR00T-WholeBodyControl) | 系统扩展模型、数据和计算，用统一 token 接口连接遥操、视频与 VLA。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
