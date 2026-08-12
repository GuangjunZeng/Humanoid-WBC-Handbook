# 动作生成与可命令行为

本板块位于高层命令与低层跟踪器之间。BeyondMimic 用可微测试时代价引导扩散采样，TextOp 用文本与历史动作块自回归生成；两者的生成质量、响应时间和跟踪稳定性必须分层度量。

- [BeyondMimic](../beyondmimic-2508.08241v4.md)：状态潜变量扩散、测试时代价、自动梯度引导和可组合约束。
- [TextOp](../textop-2602.07439v1.md)：CLIP 条件、机器人骨架动作块、6.25 Hz 生成与 50 Hz G1 跟踪。

建议联读问题：采样时引导何时破坏动作转场？模块计算延迟与人感知的命令响应为何必须分别报告？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：19 篇，其中深度解读 10 篇，有可核验官方代码 19 篇。
- 必要覆盖角色：领域锚点（field anchor）、潜技能（latent skill）、开源实现（open source）、机器人部署（robot deployment）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../deepmimic-1804.02717v3.md) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 深度解读 | [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](../amp-2104.02180v2.md) | 2021 | 领域锚点（field anchor）、开源实现（open source）、潜技能（latent skill） | [官方代码](https://github.com/isaac-sim/IsaacGymEnvs) | 用对抗运动先验取代繁重的逐项风格奖励，是后续动作先验控制的关键基线。 |
| 深度解读 | [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](../ase-2205.01906.md) | 2022 | 潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/nv-tlabs/ASE) | 将大规模动作数据压入可重用技能嵌入，为下游分层任务提供动作基元。 |
| 深度解读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](../phc-2305.06456.md) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 深度解读 | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](../maskedmimic-2409.14393v1.md) | 2024 | 潜技能（latent skill）、开源实现（open source）、多模式（multi-mode） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 把关键帧、文本、场景和稀疏目标统一为掩码动作补全问题。 |
| 深度解读 | [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](../beyondmimic-2508.08241v4.md) | 2025 | 潜技能（latent skill）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/HybridRobotics/whole_body_tracking) | 用状态潜变量扩散与可微测试时代价将跟踪技能组合为新任务。 |
| 深度解读 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](../kungfubot-2506.12851.md) | 2025 | 开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction） | [官方代码](https://github.com/TeleHuman/PBHC) | 面向武术类高动态动作的多阶段运动处理、自适应跟踪与真机开源基线。 |
| 深度解读 | [Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models](../meta-motivo-2504.11054.md) | 2025 | 潜技能（latent skill）、领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/facebookresearch/metamotivo) | Meta Motivo 用行为基础模型展示零样本全身控制，是高 Star 无独立页面项目转为论文—代码联合解读的关键案例。 |
| 深度解读 | [M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](../m3imic-2606.04829v1.md) | 2026 | 多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/Renforce-Dynamics/MultiModalWBC) | 统一处理多种动作条件与模态输入，是 Renforce Dynamics 开源全身控制路线中最直接的论文锚点。 |
| 深度解读 | [TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control](../textop-2602.07439v1.md) | 2026 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/TeleHuman/TextOp) | 用流式文本、自回归短动作块和独立跟踪器实现可随时改写的真机运动。 |
| 待深读 | [CALM: Conditional Adversarial Latent Models for Directable Virtual Characters](https://arxiv.org/abs/2305.02195) | 2023 | 潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 联合学习控制策略和动作编码器，使潜空间同时支持重建、风格和高层任务控制。 |
| 待深读 | [Universal Humanoid Motion Representations for Physics-Based Control](https://arxiv.org/abs/2310.04582) | 2023 | 领域锚点（field anchor）、潜技能（latent skill）、多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/ZhengyiLuo/PULSE) | PULSE 从大规模非结构化动作学习通用潜在表示，并用于跟踪、地形穿越和下游任务，是动作先验路线的代表作。 |
| 待深读 | [BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning](https://arxiv.org/abs/2511.04131) | 2025 | 潜技能（latent skill）、多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/BFM-Zero) | 无监督预训练可提示行为模型，代表从单任务跟踪走向可组合、可查询动作空间的开放实现。 |
| 待深读 | [MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains](https://arxiv.org/abs/2506.08840) | 2025 | 地形（terrain）、多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/MoRE) | 用残差专家混合在复杂地形上保持类人步态，连接动作风格、多模式策略与地形适应。 |
| 待深读 | [Physics-Based Motion Imitation with Adversarial Differential Discriminators](https://arxiv.org/abs/2505.04961) | 2025 | 学习控制（learning）、开源实现（open source） | [官方代码](https://github.com/xbpeng/MimicKit) | 差分判别器比较动作变化而非只看绝对姿态，为物理动作模仿提供对风格和动态更敏感的目标。 |
| 待深读 | [SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending](https://arxiv.org/abs/2506.09366) | 2025 | 任务交互（task interaction）、潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/Humanoid-SkillBlender/SkillBlender) | 通过技能混合组合全身移动操作行为，体现可复用技能比单一端到端策略更易扩展的技术路线。 |
| 待深读 | [SMP: Reusable Score-Matching Motion Priors for Physics-Based Character Control](https://arxiv.org/abs/2512.03028) | 2025 | 潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/xbpeng/MimicKit) | 把 score matching 动作先验做成可复用控制组件，便于比较生成先验与任务策略如何解耦。 |
| 待深读 | [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820) | 2025 | 多模式（multi-mode）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/NVlabs/GR00T-WholeBodyControl) | 系统扩展模型、数据和计算，用统一 token 接口连接遥操、视频与 VLA。 |
| 待深读 | [HoloMotion-1 Technical Report](https://arxiv.org/abs/2605.15336) | 2026 | 多模式（multi-mode）、实机证据（hardware evidence）、机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/HorizonRobotics/HoloMotion) | 以统一数据与控制栈连接动作资产、全身跟踪和可部署技能，适合作为大型开源系统的架构案例。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
