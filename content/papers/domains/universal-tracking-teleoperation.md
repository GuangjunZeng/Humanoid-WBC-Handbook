# 通用跟踪与遥操作

本板块关注从稠密或稀疏人体命令到全身关节目标的在线控制。下面两篇深读锚点共同采用教师—学生蒸馏与历史状态，但一个强调头手稀疏遥操作，另一个强调运行时多种控制模式；扩展目录则补齐经典基线和官方开源工作。

- [OmniH2O](../omnih2o-2406.08858v1.md)：头/手目标、历史观测、DAgger 和实机遥操作证据。
- [HOVER](../hover-2410.21229v2.md)：统一命令向量、模式/稀疏掩码与多模式全身控制。

建议联读问题：何时历史能替代显式全局线速度？运行时模式切换怎样设置 ODD、延迟与失败回退？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：11 篇，其中深度解读 3 篇，有可核验官方代码 9 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、稀疏命令（sparse command）、多模式（multi-mode）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](../hover-2410.21229v2.md) | 2024 | 多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/NVlabs/HOVER) | 用统一命令向量、模式掩码与稀疏掩码训练一个多模式全身控制器。 |
| 深度解读 | [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../omnih2o-2406.08858v1.md) | 2024 | 稀疏命令（sparse command）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/human2humanoid) | 用头手稀疏命令、历史观测和教师蒸馏实现全身遥操与任务学习。 |
| 深度解读 | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](../humi-2602.06643v2.md) | 2026 | 机器人数据质量（robot data quality）、稀疏命令（sparse command） | [公开计划，待核验](https://humanoid-manipulation-interface.github.io/) | 代表无机器人示教、人在环可行性反馈与分层全身跟踪的数据路线。 |
| 待深读 | [ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196) | 2024 | 多模式（multi-mode）、领域锚点（field anchor） | 未发现官方公开代码 | 将关键点跟踪与根速度控制解耦，并在两种真实人形平台上验证表达性动作。 |
| 待深读 | [HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454) | 2024 | 领域锚点（field anchor）、开源实现（open source）、稀疏命令（sparse command） | [官方代码](https://github.com/MarkFzp/humanplus) | 把真人影子模仿、全身数据采集与自主视觉模仿连成完整系统。 |
| 待深读 | [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](https://arxiv.org/abs/2403.04436) | 2024 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/human2humanoid) | 早期真实全尺寸人形学习式实时全身遥操锚点，建立 sim-to-data 筛选管线。 |
| 待深读 | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](https://arxiv.org/abs/2409.14393) | 2024 | 潜技能（latent skill）、开源实现（open source）、多模式（multi-mode） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 把关键帧、文本、场景和稀疏目标统一为掩码动作补全问题。 |
| 待深读 | [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013) | 2025 | 学习控制（learning）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/InternRobotics/OpenHomie) | 同构外骨骼驾驶舱与移动操作策略联合设计，并完整开源硬件和训练资源。 |
| 待深读 | [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820) | 2025 | 多模式（multi-mode）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/NVlabs/GR00T-WholeBodyControl) | 系统扩展模型、数据和计算，用统一 token 接口连接遥操、视频与 VLA。 |
| 待深读 | [TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832) | 2025 | 稀疏命令（sparse command）、开源实现（open source）、机器人数据质量（robot data quality） | [官方代码](https://github.com/amazon-far/TWIST2) | 用便携 VR 和低成本机器人颈部取代昂贵 MoCap，面向可规模化数据采集。 |
| 待深读 | [TWIST: Teleoperated Whole-Body Imitation System](https://arxiv.org/abs/2505.02833) | 2025 | 稀疏命令（sparse command）、开源实现（open source） | [官方代码](https://github.com/YanjieZe/TWIST) | 以 RL+BC、特权未来帧和真实 MoCap 提高单一网络的响应性全身遥操。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
